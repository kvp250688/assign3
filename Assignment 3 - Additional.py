
# coding: utf-8

# In[13]:


########################## 1)
import math
class cone:
    def __init__ (self, radius, height):
        self.radius = radius
        self.height = height
        
    def calculated_area (self):
        return (3.14*self.radius*(self.radius + math.sqrt(math.pow(self.height, 2) + math.pow(self.radius,2))))

    def __str__(self):
        return "Area of cone with radius: %d and height: %d is %d."%(self.radius, self.height, self.calculated_area())

c = cone(4,5)
print(c)


# In[26]:


########################### 2)
class MathOperations:
    def pow(a,b): 
        if(b==0): 
            return 1

        answer=a 
        increment=a 

        for i in range(1,b): 
            for j in range (1,a): 
                answer+=increment 
            increment=answer 
        return answer 

MathOperations.pow(2,3)


# In[29]:


########################### 3)
class Base(object): 
    pass   
# Empty Class 
  
class Derived(Base): 
    pass   
# Empty Class 
  
# To check if Base class is subclass of derived
print(issubclass(Derived, Base)) 
print(issubclass(Base, Derived)) 

d = Derived() 
b = Base() 
  
# b is not an instance of Derived 
print(isinstance(b, Derived)) 
  
# But d is an instance of Base 
print(isinstance(d, Base)) 

