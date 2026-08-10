import csv
import random
from datetime import datetime
from pathlib import Path


def get_device_data(device_id):
    temperature = round(random.uniform(20, 80), 2)
    status = "alarm" if temperature > 60 else "normal"

    return {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "device_id": device_id,
        "temperature": temperature,
        "status": status,
    }


def save_data(data):
    file_path = Path("data/device_data.csv")
    file_path.parent.mkdir(parents=True, exist_ok=True)

    file_exists = file_path.exists()

    with file_path.open("a", newline="", encoding="utf-8") as file:
        fieldnames = ["time", "device_id", "temperature", "status"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow(data)


def main():
    for _ in range(10):
        data = get_device_data("device-001")
        print(data)
        save_data(data)


if __name__ == "__main__":
    main()