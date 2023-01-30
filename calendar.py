from calendar import Calendar as c

class MyCalendar():
    def __init__(self, y, w):
        self.y = y
        self.w = w
    def count_weekday_in_year(self):
        counter = 0
        for i in range(1, 13):
            for j in c.monthdays2calendar(self.y, i):
                if self.w in j:
                    counter += 1
        return counter
        
ex = MyCalendar(2019, 0)
print(ex.count_weekday_in_year())

