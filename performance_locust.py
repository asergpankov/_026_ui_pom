from src.service import Service
from locust import task, constant_pacing, HttpUser, LoadTestShape, between
import random
import assertion

import configurations as config


# from configurations import logger


class NetworkSet(HttpUser):
    """Виртуальный пользователь"""
    # wait_time = between(1, 5)
    wait_time = constant_pacing(0.1)  # задержка между отправкой запросов
    host = config.URL_API
    admin_headers = str()

    def on_start(self):
        self.admin_headers = Service.auth_user('admin')
        config.logger.debug(f"user authed")

    @task  # метод, который будет получать нагрузку
    def get_network_set(self) -> None:
        func_name = self.get_network_set.name

        with self.client.post("/Network/GetNetworkSet", headers=self.admin_headers, catch_response=True,
                              name=func_name) as request:
            assert request.status_code == 202
            assert request.json().get('networks', f"{func_name} doesn't work correctly")

    @task
    def get_notification(self) -> None:
        func_name = self.get_notification.name

        notification_id = 240
        with self.client.post(f"/Notifications/Notification?id={notification_id}&withRecepients=true",
                              headers=self.admin_headers,
                              catch_response=True,
                              name=func_name) as request:
            assert request.status_code == 202
            assert request.json().get("id", f"{func_name} doesn't work correctly") == notification_id

    def on_stop(self):
        status = Service.logout_user(self.admin_headers)
        assert status == 204
        config.logger.debug(f"user logged out")


class StagesShape(LoadTestShape):
    """Модель ramp up теста с пошаговым повышением нагрузки"""  # todo реализовать тест с пиковой нагрузкой
    stages = [
        {"duration": 20, "users": 1, "spawn_rate": 1},
        {"duration": 40, "users": 2, "spawn_rate": 1},
        {"duration": 60, "users": 4, "spawn_rate": 1},
        {"duration": 80, "users": 8, "spawn_rate": 1},
        {"duration": 100, "users": 10, "spawn_rate": 1},
    ]

    def tick(self):  # служебный метод
        run_time = self.get_run_time()
        for stage in self.stages:
            if run_time < stage["duration"]:
                tick_data = (stage["users"], stage["spawn_rate"])
                return tick_data
        return None

# ===============
# Как запустить процесс нагрузки
# Терминал: locust -f http_max_perf.py
# Терминал: locust --headless --users 10 --spawn-rate 1 -H http://your-server.com


# ===============
# Задачи:
# 1. Провести тест на поиск максимума с профилем "Получение данных запросов" (система должна обрабатывать 100 RPS) []
# -Отправить http запрос на сервер []
# -Выполнить проверку приходящего ответа на наличие ожидаемых данных []
# -Сохранить информацию о времени необходимом для отправки сообщений в статистику []