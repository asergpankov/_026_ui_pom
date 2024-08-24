FROM python:3.12-bullseye

SHELL ["/bin/bash", "-c"]

# ARG только для фазы сборки
ARG run_env=development

# set ENV variables (для выполнения кода внутри)
ENV env $run_env
ENV PYTHONNOTBUFFERED 1

LABEL 'creator'='apan'

#RUN mkdir app
#WORKDIR /app
#RUN mkdir allure_results
# WORKDIR /app
#RUN apk update && apk upgrade && apk bash
RUN pip install --upgrade pip

COPY requirements/main.txt .
RUN pip install -r main.txt
COPY . .

#EXPOSE 8080
#открыть порт контейнера. по умолчанию закрыт

#ADD .env.docker /app/.env    # перенести переменные в контейнер если требуется
#ENV APP_NAME=D OCKER_DEMO

# RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
# RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
# RUN apt-get update && apt-get install -y google-chrome-stable
# CMD ["pytest", "test_main.py", "--alluredir=allure-results"]
#CMD ["python", "-m" , "pytest", "-v", "./tests/api/group_test.py"]
VOLUME /allure_results

CMD ["python", "-m", "pytest", "tests/elements_test.py", "--alluredir=allure_results"]

# указать марку запускаемых тестов через переменную
#CMD python -m pytest -m "$env" -v -s tests/ui/localization_test.py

# как сбилдить с аргументами --build-arg
#docker build --build-arg run_env=development -t dcoker_test .

# Как запустить образ с тестами
#docker run --rm -v C:\..\PycharmProjects\proj_name\docker_results:\allure_results {cont_name}