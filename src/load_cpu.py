#!/usr/bin/env python3

import time
import argparse
import multiprocessing
import sys
import math
import signal

PROGRAM_VERSION="PRG_VERSION_GIT_UID_TAG"

def generate_cpu_load(interval, utilization):
    """
    Генерация CPU-нагрузки заданного процента utilization на протяжении interval секунд.
    Использует таймслоты по 100 мс.
    """
    run_until = time.time() + interval
    busy_time = utilization / 100.0 * 0.1  # активная часть таймслота
    idle_time = 0.1 - busy_time            # пассивная часть таймслота

    while time.time() < run_until:
        start = time.time()
        while (time.time() - start) < busy_time:
            a = math.sqrt(64*64*64*64*64)
        time.sleep(idle_time)

def main():
    parser = argparse.ArgumentParser(description='Генерация заданной CPU-нагрузки для стресс-теста')
    parser.add_argument('-i', '--interval', type=int, default=30,
                        help='Продолжительность теста в секундах (по умолчанию: 30)')
    parser.add_argument('-u', '--utilization', type=int, default=50,
                        help='Целевая загрузка CPU в %% (по умолчанию: 50)')
    parser.add_argument('-c', '--cpus', type=int, default=multiprocessing.cpu_count(),
                        help='Количество CPU ядер для нагрузки (по умолчанию: все доступные)')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s PROGRAM_VERSION')
    args = parser.parse_args()

    if not (1 <= args.utilization <= 100):
        sys.exit("Ошибка: значение утилизации должно быть от 1 до 100 процентов.")
    if args.interval <= 0:
        sys.exit("Ошибка: интервал должен быть положительным числом.")
    if not (1 <= args.cpus <= multiprocessing.cpu_count()):
        sys.exit(f"Ошибка: количество CPU должно быть от 1 до {multiprocessing.cpu_count()}.")

    print(f"▶ Interval: {args.interval} сек")
    print(f"▶ Target Utilization: {args.utilization}%")
    print(f"▶ CPUs to load: {args.cpus}/{multiprocessing.cpu_count()}")

    # Обработка Ctrl+C
    def handle_sigint(sig, frame):
        print("\n⛔ Прерывание по Ctrl+C. Завершаем процессы...")
        for p in processes:
            p.terminate()
        sys.exit(0)

    signal.signal(signal.SIGINT, handle_sigint)

    # Запуск процессов нагрузки
    processes = []
    for _ in range(args.cpus):
        p = multiprocessing.Process(target=generate_cpu_load, args=(args.interval, args.utilization))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    print("✅ Нагрузочный тест завершён.")

if __name__ == '__main__':
    main()
