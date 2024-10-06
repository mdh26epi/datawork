# Class and method (funcion within a Python class)

# A simple example: "Calculator" class of addition and subtraction
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):       # addition method within the Calculator class
        self.result += num    # a += 1 is the same as a = a + 1, therefore self.result += num is the same as self.result = self.result + num
        return self.result

    def sub(self, num):       # subtracion method within the Calculator class
        self.result -= num    # a += 1 is the same as a = a + 1, therefore self.result -= num is the same as self.result = self.result - num
        return self.result



# A more complex example: the Expanded Calculator of addition, subtraction, multiplication, division
# Each method is built into the class like a module

class FourCal:
    #pass   // null
    # def <method_name>(variables):
    
    # "__init__" is a special method automatically called when an object is created from a class.
    # It creates an object "self" with input parameters

    # "__init__" method allows us to **initialize an object's attributes** and perform any necessary **setup** or initialization tasks.
    # With this method, we don't need to call a null clsas instance, e.g. a = FourCal() before proceeding with input values
    # Instead, we can proceed with, e.g. a = FourCal(10, 3), which will initialise FourCal() with the input values of 10 and 3.
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
    #def setdata(self, first, second):   # To take in two input values 'first' and 'second'. 
                                        # Must run setdata() to generate 'first' and 'second' input objects for each method
                                        # The variable 'self' is to designate the call for the method itself
                                        # This explicit method reference to 'self' is a unique Python feature.
    #    self.first = first              # First number
    #    self.second = second            # Second number

    def add(self): # Addition method
        result = self.first + self.second
        return result
    def sub(self): # Subtraction method
        result = self.first - self.second
        return result
    def mul(self): # Multiplication method
        result = self.first * self.second
        return result
    def div(self): # Division & Modulo method
        result_quotient = self.first / self.second
        result_remainder = self.first % self.second
        return result_quotient, result_remainder  # comma b/w two variables to return TWO values at once
                                                  # In Python, comma-separated values are treated as tuples, even without parentheses


x = FourCal(10, 3)  # Starting with __init__() method
#x = FourCal()    // starting without __init__() method: have to create an empty class instance first before setting input parameters
#x.setdata(10,3)  // starting without __init__() method
print(x.first)  # 10
print(x.second) # 3
print(x.div())  # return result_quotient, result_remainder >> (3.3333333333333335, 1)


#------------------------------------------------------------------------------------------------------------------------
# Class inheritance: class <inheriting_class>(inherited_class)
#------------------------------------------------------------------------------------------------------------------------
# 보통 상속은 기존 클래스를 변경하지 않고 기능을 추가하거나 기존 기능을 변경하려고 할 때 사용한다. 
# ‘클래스에 기능을 추가하고 싶으면 기존 클래스를 수정하면 되는데 왜 굳이 상속을 받아서 처리해야 하지?’라는 의문이 들 수도 있다. 
# 하지만 기존 클래스가 라이브러리 형태로 제공되거나 수정이 허용되지 않는 상황이라면 상속을 사용해야 한다.
#------------------------------------------------------------------------------------------------------------------------

# In the below form, MoreFourCal() inherits all methods from FourCal() without modifications
# Therefore, MoreFourCal() behaves exactly like FourCal()
class MoreFourCal(FourCal):
    pass
# For example...
a = MoreFourCal(4, 2)
print(a.add())  # returns 6
print(a.sub())  # returns 2
print(a.mul())  # returns 8
print(a.div())  # returns (2.0, 0)


##########################################################
# Expand upon FourCal class by adding in more methods
##########################################################

class MoreFourCal(FourCal):
    def pow(self):                          # pow() method: power
        result = self.first ** self.second  #   [ ** ] in Python is the same as [ ^ ] in R and Stata
        return result

# The above follows from the __init__() of the original FourCal() class:
#--------------------------------------------------------------------------
#    def __init__(self, first, second):
#        self.first = first
#        self.second = second
#---------------------------------------------------------------------------

# Therefore, 
a = MoreFourCal(4, 2)  # takes 4,2 as self.first = 4, self.first = 2
a.pow()                # result = self.first ** self.second, thus 4 ^ 2 = 16
a.add                  # result = self.first + self.second, thus 4 + 2 = 6


##########################################################
# Method Overriding
##########################################################

#----------------------------------------------------------------------------------------------------------------
# Q: What if we want to override this default output from .div() of FourCal() without changing the original method?
# A: Override the .div() method of Fourcal() class by writing a new .div() method for another inheriting class
#----------------------------------------------------------------------------------------------------------------

class SafeFourCal(FourCal):   # SafeFourCal() inherits all methods from 
    def div(self):
        if self.second == 0:  #
            return "Cannot divide by zero"
        else:
            return (self.first / self.second, self.first % self.second)

x = SafeFourCal(4,0)
print(x.div()) # returns "Cannot divide by zero"

y = SafeFourCal(4,3)
print(y.div()) # returns (1.3333333333333333, 1)

