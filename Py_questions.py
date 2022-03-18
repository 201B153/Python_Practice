'''1. Calculate simple interest. 
3. Calculate compound interest.''' 
def simple_interest(p,t,r): 
    print('The principal is', p) 
    print('The time period is', t) 
    print('The rate of interest is',r)     
    SI = (p * t * r)/100      
    print('The Simple Interest is', SI) 
    return SI 
def compound_interest(p,r,t): 
  A = p * (pow((1 + r / 100), t)) 
  CI = A - p 
  print("Compound interest is", CI) 
print('Enter SI for simple interest AND CI for compound interest') 
Choice = input('Enter choice:') 
if Choice == 'SI':  
  p = float(input('initial principal balance:')) 
  r = float(input('interest rate:')) 
  t = float(input('number of time periods elapsed'))  
  simple_interest(p,r,t) 
elif Choice == 'CI': 
  p = float(input('initial principal balance:')) 
  r = float(input('interest rate:')) 
  t = float(input('number of time periods elapsed')) 
  compound_interest(p,r,t) 
else: 
  print('Enter correct choice') 

'''
2. Find the area of a triangle. 
7. Compute the area of the circle, when its diameter is given. 
8. Compute the area of a cylinder, when its height and diameter is given. 
9. Compute the volume of a cylinder, when its height and diameter is given 
10. Compute the area of a rectangular prism, when its all sides are given. 
11. Compute the volume of a rectangular prism, when its all sides are give '''
import math 
def Area_triangle(a,b,c): 
  print('sides of Triangle are:',a,b,c) 
  s = (a+b+c)/2 
  print('Sum of all sides:',s) 
  A = s*((s-a)*(s-b)*(s-c)) 
  AREA = print(math.sqrt(A)) 
  return AREA 
def Area_circle(d): 
  print('diameter of circle is:',d) 
  pie = 3.14 
  A = pie*d*d*0.25 
  print(A) 
  return A 
def Area_cylinder(h,d): 
  print('hieght and diameter of cylinder are:',h,d)   
  pie = 3.14 
  A = pie*d*(h+d/2) 
  print(A) 
  return A 
def Volume_cylinder(h,d):  
  print('hieght and diameter of cylinder are:',h,d)  
  pie = 3.14 
  V = pie*d*h 
  print(V) 
  return V 
def Area_rectangular_prism(w,l,h): 
  print('sides of rectangular prism are:',w,l,h) 
  A = 2*(w*l+h*l+h*w) 
  print(A) 
  return A 
def Volume_rectangular_prism(w,l,h):  
  print('sides of rectangular prism are:',w,l,h) 
  V = w*l*h 
  print(V) 
  return V    
print('Enter\n', 
      '1 for Area of triangle\n', 
      '2 for Area of circle\n', 
      '3 for Area of cylinder\n', 
      '4 for volume of cylinder\n', 
      '5 for Area of rectangular prism\n', 
      '6 for volume of rectangular prism\n') 
inp = int(input('enter your choice:')) 
if inp == 1: 
  a = float(input('Enter first side a :')) 
  b = float(input('Enter second side b :')) 
  c = float(input('Enter third side c :')) 
  Area_triangle(a,b,c) 
elif inp == 2: 
  d = float(input('enter diameter of circle:')) 
  Area_circle(d) 
elif inp == 3:   
  d = float(input('enter diameter of cylinder:')) 
  h = float(input('enter hieght of cylinder:')) 
  Area_cylinder(h,d)   
elif inp == 4:   
  d = float(input('enter diameter of cylinder:')) 
  h = float(input('enter hieght of cylinder:')) 
  Volume_cylinder(h,d) 
elif inp == 5: 
  w = float(input('Enter first side w :')) 
  l = float(input('Enter second side l :')) 
  h = float(input('Enter third side h:')) 
  Area_rectangular_prism(w,l,h) 
elif inp == 6: 
  w = float(input('Enter first side w :')) 
  l = float(input('Enter second side l :')) 
  h = float(input('Enter third side h:')) 
  Volume_rectangular_prism(w,l,h) 
 
else: 
  print('Enter correct choice')


''''5. Calculate the factorial of the given number '''
def fact(n): 
  if n ==0: 
    return 1 
  if n ==1:   
    return 1 
  return  n * fact(n-1) 
num = int(input('num: ')) 
print('factorial of entered num is:',fact(num))  

'''5. Convert a temperature from Celsius to Fahrenheit. 
6. Convert a temperature from Fahrenheit to Celsius. '''
def Cel_TO_Farhnt_conversion(c):   
  farhnt = (1.8 * c) + 32 
  print('temp. in fahrenhit:',farhnt) 
  return farhnt 
def Farhnt_TO_Cel_conversion(farhnt):   
  c = (farhnt - 32) * 0.5556 
  print('temp. in celsius:',c) 
  return c   
print('To convert celsius to fahrenhit enter C', 
      'To convert fahrenhit to celsius enter F') 
Inp = input('enter your choice:') 
if Inp == 'C': 
  c = float(input('Enter temp. in celsius:')) 
  Cel_TO_Farhnt_conversion(c) 
elif Inp == 'F': 
  farhnt = float(input('Enter temp. in Fahrenheit:')) 
  Farhnt_TO_Cel_conversion(farhnt) 
else: 
  print('enter correct choice') 

'''12. Write a python function to print following shapes  
13. Write a python function to print following shape 
14. Repeat above Python script to print shapes other than square (Optional)'''
##square of '+' and '-' 
n = int(input('Enter the no. of rows u want to print')) 
for i in range(6): 
   for j in range(6): 
     if(i==0 or i==5) and (j==0 or j==5): 
       print('+',end=' ')         
     elif(i==0 or i==5) and (j!=0 or j!=5): 
       print('-', end=' ') 
     elif (i != 0 or i != 5) and (j == 0 or j == 5): 
       print('|', end=' ') 
     else: 
       print(' ',end=' ') 
   print()                             
##matrix of above problem 
for i in range(n+1): 
    for j in range(n+1): 
       if(i%5==0 or i/5==1) and (j%5==0 or j/5==1): 
           print('+',end=' ') 
       elif(i%5==0 or i/5==1) and (j/5!=1 or j%5!=0): 
           print('-', end=' ') 
       elif (i%5!= 0 or i/5 !=1) and (j%5 == 0 or j/5 == 1): 
           print('|', end=' ') 
       else: 
           print(' ',end=' ') 
    print() 
##another shape with following code 
for i in range(n+1): 
    for j in range(1,n*2): 
       if(i%5==0) and (j%5==0): 
           print('+',end=' ') 
       elif(i%5==0) and (j%5!=0): 
           print('-', end=' ') 
       elif (i%5!= 0 ) and (j%5 == 0): 
           print('|', end=' ') 
       else: 
           print(' ',end=' ') 
    print()  

'''15.Write a function named rightjustify that takes a string named s as 
a parameter and prints the string with enough leading spaces. '''
def rightjustify(s): 
  print(' ' * (70-len(s))+s) 
rightjustify('python')    

'''16.Write a function to print number 1 to 10 in ascending or descending
 order, based on user choice. '''
def asc(): 
  for i in range(1,11): 
    print(i) 
def desc(): 
  for i in range(10,0,-1): 
    print(i) 
print('Enter 1 for ascending order and 2 for descending order') 
choice = int(input('Your choice is :')) 
if choice ==1: 
  asc() 
elif choice ==2: 
  desc() 
else: 
  print('Enter correct choice')

  