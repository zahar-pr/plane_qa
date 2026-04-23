import datetime


class Logger:

    def _time(self):
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def info(self, msg):
        print(f"[{self._time()}] [INFO] {msg}")

    def step(self, msg):
        print(f"[{self._time()}] [STEP] {msg}")

    def assert_log(self, msg):
        print(f"[{self._time()}] [ASSERT] {msg}")

    def error(self, msg):
        print(f"[{self._time()}] [ERROR] {msg}")