'''1.Write a Python class which has two methods get_String and print_String get_String accepts a string 
from the user and print_String print the string in upper case.''' 
class string: 
  def get_String(self,input): 
    if isinstance(input,str): 
      self.input = input 
    else: 
      return 
  def print_String(self): 
    print(self.input.upper())  
object = string() 
object.get_String("python") 
object.print_String()    


''' 2. Write a Python class named Rectangle constructed by a length and width and a method which will 
compute the area of a rectangle.''' 
class rectangle: 
    def __init__(self,length,width): 
      self.length = length 
      self.width = width 
    def area_rectangle(self): 
      return self.length * self.width 
object = rectangle(5,3) 
print(object.area_rectangle())  


''' 3. Write a Python class named Circle constructed by a radius and two methods 
which will compute the area and the perimeter of a circle.''' 
import math as mt 
class circle: 
  def __init__(self,radius): 
    self.radius = radius 
  def area_circle(self): 
    return mt.pi * (self.radius)**2 
  def perimeter_circle(self): 
    return 2 * mt.pi * self.radius  
object = circle(1) 
print(object.area_circle()) 
print(object.perimeter_circle()) 


''' 4. Write a Python class to implement function pow(x, n)''' 
class funcpow: 
  def pow(self,x,n): 
    value = 1 
    for n in range(n): 
      value *= x 
    return value 
object = funcpow() 
print(object.pow(5,3))  

''' 4. Write a python program using class to take a number convert an integer to a roman''' 
class roman: 
  def __init__(self,number): 
    self.number = number 
  def numTOroman(self): 
    result = '' 
    roman_dict = {1:'I',4:'IV', 5 : 'V' , 6 : 'VI' , 9:'IX' , 10:'X', 40:'XL',50:'L',90:'XC',100:'C'} 
    roman_dict = dict(reversed(list(roman_dict.items()))) 
    while(self.number > 0): 
      for key,values in roman_dict.items(): 
        if self.number - key >= 0: 
          self.number = self.number - key 
          result = result + values 
          break 
    return result  
object = roman(33) 
object.numTOroman()


''' 5. Write a Python class to get all possible unique subsets from a set of distinct integers''' 
class setTOsubset(): 
  def __init__(self,value): 
    self.value = set(value) 
  def subsets(self): 
     return self.subsetsRecursive([], sorted(self.value)) 
  def subsetsRecursive(self, current, set1): 
    if set1: 
      return self.subsetsRecursive(current, set1[1:]) + self.subsetsRecursive(current + [set1[0]], set1[1:]) 
    return [current] 
object = setTOsubset([1,2,3,4,5]) 
object.subsets()   

''' 6. Write a Python class to find a pair of elements (indices of the two numbers) from a given list whose 
sum equals a specific target number.''' 
class pairofelements: 
  def __init__(self,value): 
    self.value = value 
  def pairelements(self,target): 
    for i in range(len(self.value)): 
      for j in range(len(self.value)): 
        if i!=j and self.value[i] + self.value[j] == target: 
          return self.value[i] , self.value[j] 
 
object = pairofelements([1, 2, 3, 4, 5, 6, 7, 8, 9]) 
object.pairelements(8) 


''' 7. Write a Python class to find the three elements that sum to zero from a set of N real numbers.''' 
import random 
class sum_threenum_zero: 
  def threeNumbers(self): 
    N = int(input('Enter the number AS between the number you wants (N for -N to N) SEARCH:')) 
    a = random.randint(-N,0) 
    b = random.randint(0,N) 
    c = -1*(a+b) 
    return a, b ,c 
object = sum_threenum_zero() 
object.threeNumbers() 


