from datetime import timedelta


class PerformanceException(Exception):
    def __init__(self, runtime: timedelta, limit: timedelta):
        self.runtime = runtime
        self.limit = limit

    def __str__(self) -> str:
        return f"Performace test failed, runtime {self.runtime.total_seconds()}'s, limit {self.limit.total_seconds()}'s"
