#question1

class Circle():
    def __init__(self,radius):
        self.r=radius
    def getarea(self):
        a=3.14*(self.r)
        print(a)
    def getcircumference(self):
        b=7*3.14*(self.r)
        print(b)

c=Circle(1)
c.getarea()
c.getcircumference()

#question2

class Student():
    def __init__(self,name,rollnumber):
        self.n=name
        self.r=rollnumber
    def display(self):
        print(self.n)
        print(self.r)
c=Student('mohit',136)
c.display()

#question3

class Temperature():
    def __init__(self,cel,far):
        self.c=cel
        self.f=far
    def convertCelsius(self):
        celsius=((self.f)-32)*(5/9)
        print(celsius)
    def convertFarenheit(self):
        farenheit=9/5*(self.c)+32
        print(farenheit)
p=Temperature(0,68)
p.convertFarenheit()
p.convertCelsius()

#question4

class Moviedetails():
    def __init__(self,moviename,artistname,yearofrelease,rating):
        self.m=moviename
        self.a=artistname
        self.y=yearofrelease
        self.r=rating
    def display(self):
        print(self.m)
        print(self.a)
        print(self.y)
        print(self.r)

    def update(self, moviename, artistname, yearofrelease,rating):
        self.q=moviename
        self.w=artistname
        self.e=yearofrelease
        self.t=rating
        print(self.q)
        print(self.w)
        print(self.e)
        print(self.t)

z=Moviedetails("infinity war","hulk",2018,3)
z.display()
z.update("infinity war","iron man",2008,4)

#question5

class Expenditure():
    expenditure = 50000
    savings = 1
    gpf=4500
    def __init__(self):
        print(self.expenditure)
        print(self.savings)
    def display(self):
        print(self.expenditure)
        print(self.savings)
        salary=50001
        totalsalary=(self.expenditure)+(self.savings)+(self.gpf)
        print(salary)
        print(totalsalary)
z=Expenditure()
z.display()