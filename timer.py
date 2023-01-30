class Timer:
    def __init__( self, hours, minutes, seconds ):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        if self.hours == 24:
            self.hours = 0
        if self.hours >= 10 and self.minutes >= 10 and self.seconds >= 10:
            format = "{}:{}:{}".format(self.hours, self.minutes, self.seconds)
        if self.hours < 10:
            format = "0{}:{}:{}".format(self.hours, self.minutes, self.seconds)
        if self.minutes < 10:
            format = "{}:0{}:{}".format(self.hours, self.minutes, self.seconds)
        if self.seconds < 10:
           format = "{}:{}:0{}".format(self.hours, self.minutes, self.seconds)
        return format

    def next_second(self):
        if self.seconds != 59:
            self.seconds += 1
        else:
            if self.minutes != 59:
                self.seconds = 0
                self.minutes += 1
            else:
                self.seconds = 0
                self.minutes = 0
                self.hours += 1

    def prev_second(self):
        if self.seconds > 0:
            self.seconds -= 1
        else:
            if self.minutes > 0:
                self.seconds = 59
                self.minutes -= 1
            else:
                if self.hours > 0:
                    self.seconds = 59
                    self.minutes = 59
                    self.hours -= 1
                else:
                    self.seconds = 59
                    self.minutes = 59
                    self.hours = 23


timer = Timer(12, 9, 9)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
