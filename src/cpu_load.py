#!/usr/bin/env python3
import time
import argparse
import multiprocessing as mp
import sys
import math
import signal

PROGRAM_VERSION = "%(prog)s PRG_VERSION_GIT_UID_TAG"

def generate_cpu_load(interval, utilization, timeslice):
    """
    Генерация CPU-нагрузки заданного процента utilization на протяжении interval секунд.
    Работает тайм-слотами длиной timeslice секунд.
    """
    # Бесконечный режим
    if interval == -1:
        run_until = float("inf")
    else:
        run_until = time.perf_counter() + float(interval)

    busy_time = (utilization / 100.0) * timeslice
    idle_time = max(0.0, timeslice - busy_time)

    # Небольшая «работа», не оптимизируемая в ноль
    acc = 0.0
    while time.perf_counter() < run_until:
        start = time.perf_counter()
        # активная фаза
        while (time.perf_counter() - start) < busy_time:
            acc += math.sqrt(acc * acc + 123.456) if acc else math.sqrt(123.456)
            if acc > 1e6:
                acc = 0.0
        # пассивная фаза
        if idle_time > 0:
            time.sleep(idle_time)

def main():
    cpu_total = mp.cpu_count() or 1

    parser = argparse.ArgumentParser(
        description="Генерация заданной CPU-нагрузки для стресс-теста"
    )
    parser.add_argument(
        "-i", "--interval", type=int, default=30,
        help='Продолжительность теста в секундах (по умолчанию: 30), "-1" — бесконечно'
    )
    parser.add_argument(
        "-u", "--utilization", type=int, default=50,
        help="Целевая загрузка CPU в %% (по умолчанию: 50)"
    )
    parser.add_argument(
        "-c", "--cpus", type=int, default=cpu_total,
        help=f"Количество CPU ядер для нагрузки (по умолчанию: все доступные = {cpu_total})"
    )
    parser.add_argument(
        "-t", "--timeslice", type=float, default=0.1,
        help="Длительность тайм-слота в секундах (по умолчанию: 0.1)"
    )
    parser.add_argument("-v", "--version", action="version", version=PROGRAM_VERSION)
    args = parser.parse_args()

    # Валидации
    if not (1 <= args.utilization <= 100):
        sys.exit("Ошибка: утилизация должна быть от 1 до 100 процентов.")
    if not (args.interval == -1 or args.interval > 0):
        sys.exit('Ошибка: интервал должен быть положительным числом или равен "-1".')
    if not (1 <= args.cpus <= cpu_total):
        sys.exit(f"Ошибка: количество CPU должно быть от 1 до {cpu_total}.")
    if args.timeslice <= 0:
        sys.exit("Ошибка: timeslice должен быть положительным числом.")

    print(f"▶ Interval: {'∞' if args.interval == -1 else args.interval} сек")
    print(f"▶ Target Utilization: {args.utilization}%")
    print(f"▶ CPUs to load: {args.cpus}/{cpu_total}")
    print(f"▶ Timeslice: {args.timeslice:.3f} с")

    processes = []  # объявляем до установки обработчиков

    def handle_stop(sig, frame):
        print(f"\n⛔ Получен сигнал {signal.Signals(sig).name}. Завершаем процессы...")
        for p in processes:
            if p.is_alive():
                p.terminate()
        for p in processes:
            p.join(timeout=2)
        sys.exit(0)

    # Обработка Ctrl+C и SIGTERM
    signal.signal(signal.SIGINT, handle_stop)
    try:
        signal.signal(signal.SIGTERM, handle_stop)
    except Exception:
        # На некоторых платформах (Windows) SIGTERM может быть недоступен
        pass

    # Запуск процессов нагрузки
    for _ in range(args.cpus):
        p = mp.Process(target=generate_cpu_load,
                       args=(args.interval, args.utilization, args.timeslice))
        p.start()
        processes.append(p)

    # Ожидание завершения
    for p in processes:
        p.join()

    print("✅ Нагрузочный тест завершён.")

if __name__ == "__main__":
    main()
