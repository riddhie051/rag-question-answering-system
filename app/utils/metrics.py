import time

class LatencyTracker:
    def __init__(self):
        self.start_time = None

    def start(self):
        self.start_time = time.time()

    def stop(self):
        if self.start_time is None:
            return None
        return round(time.time() - self.start_time, 3)
