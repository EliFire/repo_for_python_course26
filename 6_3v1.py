"""Уровень 3
Напишите функцию, get_html(link), которая принимает один аргумент - название веб страницы.
Функция должна получать текст веб страницы с помощью библиотеки requests.

def get_html(link):
  pass

Запустите 5 потоков с с данной функцией и разными именами в качестве аргументов.
Сравните время работы параллельного и последовательного запуска с помощью библиотеки time.
Это задание на самостоятельность, где понадобится установка request."""

import threading
import time
import requests

def get_html(link):
    try:
        response = requests.get(link, timeout=5)
        print(f"Загружена страница: {link}")
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при загрузке {link}")
        return None

def parallel(urls):
    threads = []
    results = []
    
    def target(url):
        result = get_html(url)
        results.append(result)
    
    for url in urls:
        thread = threading.Thread(target=target, args=(url,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    return results

def sequence(urls):
    results = []
    for url in urls:
        result = get_html(url)
        results.append(result)
    return results

urls = [
    "https://www.google.com",
    "https://www.mail.ru",
    "https://www.yandex.ru",
    "https://www.nalog.ru",
    "https://www.ozon.ru"
]

print("-" * 40)

start_parallel = time.time()
parallel_results = parallel(urls)
parallel_time = time.time() - start_parallel
print(f"\nВремя параллельного выполнения: {parallel_time:.2f}")

start_sequence = time.time()
sequence_results = sequence(urls)
sequence_time = time.time() - start_sequence
print(f"\nВремя последовательного выполнения: {sequence_time:.2f}")

print(f"Разница: {sequence_time - parallel_time:.2f} сек")