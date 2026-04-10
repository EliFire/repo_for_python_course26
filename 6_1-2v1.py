import threading
import time

"""Уровень 1
Напишите функцию get_thread(thread_name), которая принимает один аргумент - название потока.
Функция должна ждать одну секунду, затем выводить в стандартный вывод (print) название потока.

def get_thread(thread_name):
  pass

Ожидание в 1 секунду реализуйте с помощью библиотеки time.
Запустите 5 потоков с с данной функцией и разными именами в качестве аргументов."""

def get_thread(name):
    time.sleep(1)
    print(name)

threads = []
names = ["Поток 1", "Поток 2", "Поток 3", "Поток 4", "Поток 5"]

for name in names:
    thread = threading.Thread(target=get_thread, args=(name,))
    threads.append(thread)
    thread.start()
    thread.join()



"""Уровень 2
Сравните время работы параллельного и последовательного запуска с помощью библиотеки time."""

def get_thread(name):
    time.sleep(1)
    print(name)

start_parallel = time.time()

threads = []
names = ["Поток A", "Поток B", "Поток C", "Поток D", "Поток E"]

for name in names:
    thread = threading.Thread(target=get_thread, args=(name,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_parallel = time.time()
parallel_time = end_parallel - start_parallel
print(f"\nВремя параллельного выполнения: {parallel_time:.2f} секунд")


start_sequence = time.time()

for name in names:
    get_thread(name)

end_sequence = time.time()
sequence_time = end_sequence - start_sequence
print(f"\nВремя последовательного выполнения: {sequence_time:.2f} секунд")
