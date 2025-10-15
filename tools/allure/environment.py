import platform
import sys

from config import settings


def create_allure_environment_file():
    # Создаем список из элементов в формате {key}={value}
    data = settings.model_dump()
    data.update({
        'os_info': f'{platform.system()}, {platform.release()}',
        'python_version': sys.version,
    })

    items = [f'{key}={value}' for key, value in data.items()]

    properties = '\n'.join(items)

    # Открываем файл ./allure-results/environment.properties на чтение
    with open(settings.allure_results_dir.joinpath('environment.properties'), 'w+') as file:
        file.write(properties)  # Записываем переменные в файл
