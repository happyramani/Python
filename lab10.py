
# A
### 01) WAP to create Calculator module which defines functions like add, sub,mul and div. create another file that uses the Calculator module.
import calculator

calculator.add(2,3)
calculator.sub(3,2)
calculator.multi(2,3)
calculator.div(6,2)
### 02) WAP to Pick a random character from a given String.
import random
nam=random.choice('kauhsal patel')
print(nam)
### 03) WAP to Pick a random element from a given list.
import random
nam=random.choice([10,20,30])
print(nam)

### 04) WAP to demonstrate the use of the math module.

import math

print("e = ",math.e)
print("pie = ",math.pi)
print("tau = ",math.tau)
print("ceil = ",math.ceil(5.6))
print("floor = ",math.floor(5.6))
print("factorial = ",math.factorial(50))
print("GCD ",math.gcd(15,30))
print("LCM ",math.lcm(15,30))
print("ABS ",math.fabs(-9000000000000000000))
print("EXP ",math.exp(120))
print("POWER ",math.pow(2,120))
print("Log",math.log(2,4))
print("Log Base 2 ",math.log2(2))
print("Log Base 10 ",math.log10(2))
print("Radian ",math.radians(180))
print("Degrees ",math.degrees(math.pi*2))
print("Gamma ",math.gamma(6))
### 05) WAP to demonstrate the use of date time module.

import datetime

d = datetime.date(2004,7,26)
todayDate = datetime.date.today()
print("Imput Date : ",d)
print("Today Date : ",todayDate)
print(todayDate)
print(todayDate.year)
print(todayDate.month)
print(todayDate.day)
t = datetime.time(10,30,5,1)
print(t)
print(t.hour)
print(t.minute)
print(t.second)
print(t.microsecond)

dd = datetime.datetime(2004,7,25,12,12,12)
print(dd)

print(datetime.datetime.now())

n = datetime.datetime.now()
y = n+datetime.timedelta(days=2)
a = n+datetime.timedelta(weeks=-2)
print(y)
print(a)
print(n.strftime("%a"))
print(n.strftime("%A"))
print(n.strftime("%m"))
print(n.strftime("%M"))
print(n.strftime("%y"))
print(n.strftime("%Y"))
# B
### 01) WAP to Roll dice in such a way that every time you get the same number.
import random

random.seed(2)
print(random.choice([1,2,3,4,5,6]))
### 02) WAP to generate 3 random integers between 100 and 999 which is divisible by 5.
import random
count=0

while(count!=3):
    n1=random.randrange(100,999)
    if(n1%5==0):
        print(n1)
        count=count+1


        or
    
    
    for i in range(3):
    print(random.randrange(100,1000,5))
### 03) WAP to generate 100 random lottery tickets and pick two lucky tickets from it as a winner.
import random

l1 = []

for i in range(1,101):
    x = random.randrange(1,100000)
    l1.append(x)
print(l1)
print(random.sample(l1,2))
### 04) WAP to print current date and time in Python.
import datetime
print(datetime.datetime.now())
### 05) Subtract a week (7 days) from a given date in Python.
n = datetime.datetime.now()
a = n+datetime.timedelta(weeks=-1)
print(a)

or


import datetime
n = datetime.datetime.now()
a = n+datetime.timedelta(days=-7)
print(a)
### 06) WAP to Calculate number of days between two given dates.
import datetime

day1=int(input("enter 1st date day "))
month1=int(input("enter 1st date month "))
year1=int(input("enter 1st date year "))
day2=int(input("enter 2st date day "))
month2=int(input("enter 2st date month "))
year2=int(input("enter 2st date year "))

d1 = datetime.date(year1,month1,day1)
d2 = datetime.date(year2,month2,day2)

dif=d2-d1
print('Difference is {} days'.format(dif.days))
### 07) WAP to Find the day of the week of a given date.
import datetime

day1=int(input("enter 1st date day "))
month1=int(input("enter 1st date month "))
year1=int(input("enter 1st date year "))

d1 = datetime.date(year1,month1,day1)
print(d1.strftime("%A"))