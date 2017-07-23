from datetime import datetime, timedelta

class TimeKeeper:
    current_time = -1
    end_time = -1
    delta = -1
    def __init__(self, start_time, end_time, delta):
        self.current_time = datetime.strptime(start_time,'%Y-%m-%d')
        self.end_time = datetime.strptime(end_time,'%Y-%m-%d')
        self.delta = delta
    def next(self):
        self.current_time += self.delta
        if (self.current_time < self.end_time):
            return self.current_time
        return -1
    def current(self):
        return self.current_time
