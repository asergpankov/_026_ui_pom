Подготовка подключения allure

- установить Java 8 SE Runtime Environment 8u361
[скачать с офф. ресурса oracle.com](https://www.oracle.com/cis/java/technologies/downloads/)

- создать директорию

`sudo mkdir /usr/lib/jvm`

- распаковать архив (указать коректный адрес и имя)

`sudo tar -zxf /home/username/Загрузки/tarname -C /usr/lib/jvm`

- установить в систему

`sudo update-alternatives --install "/usr/bin/java" "java" "/usr/lib/jvm/foldername/bin/java" 1500`
`sudo update-alternatives --install "/usr/bin/javaws" "javaws" "/usr/lib/jvm/foldername/bin/javaws" 1500`

Редактируем environment
# sudo nano /etc/environment

-добавляем в /etc/environment следующее:

JAVA_HOME="/usr/lib/jvm/foldername"

-применение изменений без перезагрузки
# source /etc/environment
======

Скачать allure из repository
# https://github.com/allure-framework/allure2/tags

-распаковать архив allur в папку проекта
-добавить alias в .bashrc
# nano .bashrc
# alias allure='allure-2.21.0/bin/allure'

-перегрузить терминал
======

Проставить теги в тестовом модуле: suite, feature, title

-структура вложенности:
@allure.suite('Elements')
    @allure.feature('TextBox')
        @allure.title('Check data in TextBox')


Как запустить генерацию репортов allure
# pytest --alluredir=tests/allure_results tests/elements_test.py

Обработать результаты репортов
# allure serve tests/allure_results/
======

Проставить теги в page модуле: step
@allure.step('fill all text boxes _step')
    with allure.step('generate data _step'):

Запустить выборочную генерацию отчета
# pytest --alluredir=tests/allure_results tests/elements_test.py::TestElements::TestTextBox::test_all_data_in_text_boxes
