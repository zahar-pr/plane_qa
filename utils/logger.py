import datetime
import os


class Logger:
    def __init__(self, file_path="logs/test.log"):
        self.file_path = file_path
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

    def _write(self, level, message):
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_line = f"[{time}] [{level}] {message}"

        print(log_line)

        with open(self.file_path, "a", encoding="utf-8") as f:
            f.write(log_line + "\n")

    def info(self, msg):
        self._write("INFO", msg)

    def step(self, msg):
        self._write("STEP", msg)

    def assert_log(self, msg):
        self._write("ASSERT", msg)

    def error(self, msg):
        self._write("ERROR", msg)