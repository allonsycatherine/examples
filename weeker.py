class WeekDayError(Exception):
    pass
	

class Weeker:
    def __init__(self, day):
        self.day = day
        week = {'Mon': 1, 'Tue': 2, 'Wed': 3, 'Thu': 4,  'Fri': 5, 'Sat': 6, 'Sun': 7}
        self.week = week
        if day not in week.keys():
            raise WeekDayError
        

    def __str__(self):
        return self.day

    def add_days(self, n):
        self.day = [i for i in self.week.keys() if self.week[i] == ((self.week[self.day] + n) // 7)]
        self.day = self.day[0]
        return self.day

    def subtract_days(self, n):
        self.day = [i for i in self.week.keys() if self.week[i] == ((self.week[self.day] - n) // 7) or self.week[i] == -((self.week[self.day] - n) // 7)]
        self.day = self.day[0]
        return self.day

try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
