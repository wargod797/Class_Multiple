
# coding: utf-8
# In[ ]:
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 15:24:34 2019

@author: sridhar
"""


# In[69]:


#
a=0
def add(a):
    #global a
    a+=1
    print(a)
    if a>500:
        return
    else:
        add(a)
add(a)
print(a)


# In[13]:


import sys
#num = int(input("Enter a number: "))
def nextpri(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                num+=1
                nextpri(num)
                break
            #break
        else:
            print(num,"is prime number")
    else:  
        print(num,",2 is next prime number")
nextpri(int(input("Enter a number: ")))


# In[12]:


class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(shaa):
        print("Hello my name is " + shaa.name)
p1 = Person("John", 36)
p1.myfunc()

p1.myfunc2()


# In[98]:


class something:
    def __init__(idk,something3,something7,something1,**something2):
        idk.something3 = something3
        idk.something7 = something7
        idk.something1 = something1
    def something4(non):
        c = non.something3+non.something7+non.something1
        print("hahahaha'wts'=",c)
    def something5(gh):
        c = int(gh.something3)+int(gh.something7)+int(gh.something1)
        print(gh.something7)
        print(c)
S1 = something("1","2","3")
S1 = something(36,24,26)
S1.something4()
S1.something5()


# In[56]:


class robot:
    #name = "python"
    def __init__(self,name,power,work):
        self.name = name 
        self.power = power
        self.work = work
    def intro(dummy_variable):
        print("I am "+dummy_variable.name+" I powered by "+dummy_variable.power+" I "+dummy_variable.work)
        
r1 = robot('emoai','microcontroller_electronics','think') 
r2 = robot('lifter','hydraulics_motor','lift')
r1.intro()
r2.intro()


# In[57]:


class Person:
    def __init__(self,n,o):
        self.name = n
        self.owned = o
    def owned(self):
        self.is_sitting = True
    
    def owned(self):
        self.is_sitting = False


# In[58]:


p1 = Person("Alice", False)
p2 = Person("Becky", True)


# In[59]:


p1.robot_owned = r2
p2.robot_owned = r1


# In[60]:


p1.robot_owned.intro()
p2.robot_owned.intro()


# In[68]:


#Classes with Inheritance
#Reference
#code from: HackerEarth "https://www.hackerearth.com/practice/python/object-oriented-programming/classes-and-objects-ii-inheritance-and-composition/tutorial/"
class Rocket:
    def __init__(self, name, distance):
        self.name = name
        self.distance = distance

    def launch(self):
        return "%s has reached %s" % (self.name, self.distance)


class MarsRover(Rocket): # inheriting from the base class
    def __init__(self, name, distance, maker):
        Rocket.__init__(self, name, distance)
        self.maker = maker

    def get_maker(self):
        return "%s Launched by %s" % (self.name, self.maker)


if __name__ == "__main__":
    x = Rocket("simple rocket", "till stratosphere")
    y = MarsRover("mars_rover", "till Mars", "ISRO")
    print(x.launch())
    print(y.launch())
    print(y.get_maker())


# In[97]:


class calculator:
    def __init__(self,x,y):
        self.x = x
        self.y =y
    def add(ad):
        print((ad.x+ad.y))
    def sub(sb):
        print((sb.x-sb.y))
class calc(calculator):
    def __init__(self,x,y):
        calculator.__init__(self,x,y)
    def div(dv):
        print(dv.x+dv.y)
    def mul(mu):
        print((mu.x*mu.y))
        
class ca:
    def __init__(self,z):
        self.z = z
    def sq(sq):
        print(sq.z*sq.z)
        
class cal(calc, ca):
    def __init__(self,x,y,z):
        calc.__init__(self,x,y)
        ca.__init__(self,z)
    def addi(ai):
        print(ai.x+ai.y+ai.z)
        
a = int(input("Enter the Value"))
b = int(input("Enter the Value"))
c = int(input("Enter the Value"))
ca(c).sq()
calc(a,b).add()
calculator(a,b).add()
calc(a,b).sub()
calculator(a,b).sub()
calc(a,b).mul()
calc(a,b).div()
cal(a,b,c).addi()

