__author__  = "Bungogood"

'''
Problem 19

Counting Sundays
'''

def f():
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    days = 1
    sundays = 0
    for y in range(1900, 2000):
        for m in range(12):
            if days%7==0:
                sundays += 1
            days += months[m]
            if m==2 and y%4==0:
                days += 1
    return sundays

if __name__ == "__main__":
    print(f())