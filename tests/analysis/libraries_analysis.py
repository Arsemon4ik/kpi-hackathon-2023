import re
import sys

import numpy as np
from scipy.stats import zscore

from utils import get_logs_text


def parse_test_logs(logs: list[str]):
    """
    Парсить логи для отримання часу виконання тестів та їх статусів.
    """
    time_pattern = re.compile(r"(\d+\.\d+)s (setup|teardown|call)\s+([\w/:\.]+)")
    status_pattern = re.compile(r"(=\s+)(\d+ failed, \d+ passed)")

    test_times = []
    statuses = []

    for line in logs:
        # parse time exec
        time_match = re.search(time_pattern, line)
        if time_match:
            time = float(time_match.group(1))
            phase = time_match.group(2)
            test_name = time_match.group(3)
            test_times.append((test_name, phase, time))

        # parse statuses
        status_match = re.search(status_pattern, line)
        if status_match:
            statuses.append(status_match.group(2))

    return test_times, statuses


def analyze_execution_times(test_times):
    """
    Аналізує час виконання для кожної фази тестів.
    """
    phase_times = {"setup": [], "teardown": [], "call": []}
    for _, phase, time in test_times:
        phase_times[phase].append(time)
    return phase_times


def detect_anomalies(test_times):
    """
    Виявляє аномалії у часах виконання фаз тестів.
    """
    times = [time for _, _, time in test_times]
    z_scores = zscore(times)
    anomalies = [(test, phase, time) for (test, phase, time), z in zip(test_times, z_scores) if abs(z) > 2]

    print("\nАномалії:")
    if anomalies:
        for test, phase, time in anomalies:
            print(f"  Тест: {test}, Фаза: {phase}, Час: {time}s")
    else:
        print("  Аномалій не знайдено.")


def summarize_results(statuses):
    """
    Резюмує результати тестів (успішні/провалені).
    """
    if statuses:
        last_status = statuses[-1]
        print("\nРезультати тестів:")
        print(f"  {last_status}")
    else:
        print("\nРезультати тестів не знайдені.")


def main():
    if len(sys.argv) != 2:
        print(sys.argv)
        print("Usage: python3 libraries.analysis.py <log_file_path>")
        sys.exit(1)

    log_file_path = sys.argv[1]

    logs = get_logs_text(log_file_path)
    test_times, statuses = parse_test_logs(logs)

    print("Аналіз часу виконання:")
    phase_times = analyze_execution_times(test_times)
    for phase, times in phase_times.items():
        print(f"\nФаза: {phase}")
        print(f"  Кількість виконань: {len(times)}")
        print(f"  Середній час: {np.mean(times):.2f}s")
        print(f"  Максимальний час: {np.max(times):.2f}s")
        print(f"  Мінімальний час: {np.min(times):.2f}s")

    detect_anomalies(test_times)

    summarize_results(statuses)


if __name__ == "__main__":
    main()
