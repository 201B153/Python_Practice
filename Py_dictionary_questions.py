'''1.Write a python script to create a dictionary week. The key to be int
eger and values should be name of the days of the week?? 
CODE: '''
import math as mt
import numpy as np
import pandas as pd
from pandas import *
week = {1: 'monday', 2: 'tuesday', 3: 'wednesday', 4: 'thursday',
        5: 'friday', 6: 'saturday', 7: 'sunday', }
print("\nDictionary with the use of Integer Keys: ")
print(week)

'''2. Write a python script to create a dictionary D1. Enter details of the s in the form of Enrolment No. and Name (from the file “Std Record.pdf” ). 
3. Write a python script to create a dictionary D2. Enter details of t
he student 
in the form of Enrolment No. and City (hometown) he/she belongs to. 
4. Write a python script to create a dictionary D3. Enter details of t
he s 
in the form of Enrolment No. and Mobile. 
5. Write a python script to create a dictionary D4. Enter details of t
he s 
in the form of Enrolment No. and State he/she belongs to. 
6. Write a python script to create a dictionary D5. Enter details of t
he s 
in the form of Enrolment No. and Marks in Phy, Chem, and Maths. 
7. Write a python script to create a dictionary D6. Enter details of t
he s 
in the form of Enrolment No. and email-id. 
CODE: '''
df = read_csv('Std_Record.csv')
df.tail(4)
df.head(4)
df
D1 = df.loc[:, ['key', 'name']]
D1 = D1.to_dict()
D2 = df.loc[:, ['key', ['city']]]
D2 = D2.to_dict()
D3 = df.loc[:, ['key', 'mobile_no.']]
D3 = D3.to_dict()
D4 = df.loc[:, ['key', 'state']]
D4 = D4.to_dict()
D5 = df.loc[:, ['key', 'marks']]
D5 = D5.to_dict()
D6 = df.loc[:, ['key', 'email']]
D6 = D6.to_dict()

'''8. Write a python script to display students name and email by receiv
ingeenrolment number at run time. 
CODE:'''
x = int(input("En.roll No. : "))
flag = 0
for i in range(17):
    if(df.key[i] == x):
        print("Name : ", df.name[i])
        print("Email : ", df.email[i])
        flag = 1
if(flag == 0):
    print("Data not found!!")


'''9. Write a python script to print name and enrolment number of the student 
receiving email id at run time. 
CODE: '''
x = str(input("email : "))
flag = 0
for i in range(17):
    if(df.email[i] == x):
        print("key : ", df.key[i])
        print("Name : ", df.name[i])
        flag = 1
if(flag == 0):
    print("Data not found!!")


''' 11.Write a python script to display students details who are from the hometown. 
CODE: '''
x = str(input("city : "))
flag = 0
for i in range(17):
    if(df.city[i] == x):
        print("key : ", df.key[i])
        print("Name : ", df.name[i])
        print("email : ", df.email[i])
        print("marks : ", df.marks[i])
        flag = 1
if(flag == 0):
    print("Data not found!!")

    ''''10.Write a python script to print the name and city of the student by mobi number at run time. 
CODE: '''
x = str(input("mobile_no. : "))
flag = 0
for i in range(17):
    if df.mobile_no[i] == x:
        print("city : ", df.city[i])
        print("Name : ", df.name[i])
        flag = 1
if(flag == 0):
    print("Data not found!!")

    '''12.Write a python script to display students details who are from the sam State. 
CODE: '''
x = str(input("state: "))
flag = 0
for i in range(17):
    if(df.state[i] == x):
        print("key : ", df.key[i])
        print("Name : ", df.name[i])
        print("email : ", df.email[i])
        print("marks : ", df.marks[i])
        flag = 1
if(flag == 0):
    print("Data not found!!")

    # conversion


def dictionaryconversion(pandas_dataframe):
    if isinstance(pandas_dataframe, pd.DataFrame):
        new_dict = {}
        df = pandas_dataframe
        for i in range(df.shape[0]):
            new_dict[df.iloc[i, 0]] = [df.iloc[i, 1], df.iloc[i, 3],
                                       df.iloc[i, 4], df.iloc[i, 6], df.iloc[i, 7], df.iloc[i, 8]]
        return new_dict
    else:
        return none


new_dict = dictionaryconversion(df)
print(new_dict)


'''13.Write a python script to display students details who have email i
d on 
same host. (i.e. gmail.com, yahoo.com, rediffmail.com etc ) 
CODE: '''


def samedomain(new_dict):
    tmp = list(new_dict.values())
    tmp1 = set()
    lengthi = len(tmp)
    for i in range(lengthi):
        flag = 0
        lengthj = len(tmp)
        for i in range(i+1, lengthj):
            if(list(tmp[i][7].split('@'))[1] == list(tmp[j][7].split('@'))[1]):
                tmp1.add(tuple(tmp[j]))
                flag = 1
            if flag == 1:
                tmp1.add(tuple(tmp[i]))
    return tmp1
    same_domain = samedomain(new_dict)
    print(same_domain)


'''14.Write a python script to display students’ details whose mobile ser
vice provider is same( first two bits 94: BSNL, 98: Airtel, 89:Idea, 77:Reliance, 97:Idea, 99:Vodafone, 79:Docomo) 
CODE: '''


def getprovider(number):
    number = int(number//10**8)
    num_dict = {94: 'BSNL', 98: 'airtel', 89: 'idea', 77: 'reliance'}
    return num_dict[number]


def getprovider(new_dict):
    airtel = {}
    BSNL = {}
    idea = {}
    reliance = {}
    for key, values in new_dict.items():
        if getprovider(values[2]) == 'airtel':
            airtel[key] = values
        elif getprovider(values[2]) == 'reliance':
            reliance[key] = values
        elif getprovider(values[2]) == 'idea':
            idea[key] = values
        elif getprovider(values[2]) == 'BSNL':
            BSNL[key] = values
        else:
            pass
    return airtel, reliance, BSNL, idea


operator = list(getprovider(new_dict))
for item in operator:
    if len(item) >= 2:
        print(item)


'''15.Write a python script to display students details who scored highest marks in Phy among all. 
CODE: '''


def maxPhy(new_dict):
    max_marks = 0
    max_scorer = None
    for key, values in new_dict.items():
        marks = list(map(int, values[4].split(',')))
        if marks[0] > max_marks:
            max_marks = marks[0]
            max_scorer = key
    return max_scorer


max_scorer = maxPhy(new_dict)
print(max_scorer, new_dict[max_scorer])


'''16.Write a python script to display students’ details who scored highest marks in Chem among all. 
CODE: '''


def maxchem(new_dict):
    max_marks = 0
    max_scorer = None
    for key, values in new_dict.items():
        marks = list(map(int, values[3].split(',')))
        if marks[1] > max_marks:
            max_marks = marks[1]
            max_scorer = key
    return max_scorer


max_scorer = maxPhy(new_dict)
print(max_scorer, new_dict[max_scorer])


'''18.Write a python script to display students’ details who scored highest average marks in Phy, Chem, and Maths among all. 
CODE: '''


def maxAll(new_dict):
    max_marks = 0
    max_scorer = 0
    for key, values in new_dict.items():
        marks = list(map(int, values[3].split(',')))
        avg_marks = sum(marks)/3
        if avg_marks > max_marks:
            max_marks = avg_marks
            max_scorer = key
    return max_scorer


max_scorer = maxAll(new_dict)
print(max_scorer, new_dict[max_scorer])


'''19.Write a python script to create a dictionary square to store 10 integers and their square. 
CODE: '''
squared_dict = {x: x**2 for x in range(10)}
print(squared_dict)


'''20.Write a python script to create any data structure named sroot to store10 integers between 20 to 30 and their square root. 
CODE: '''
sroot = {x: x**(1/2) for x in range(20, 30)}
print(sroot)

'''21.Write a python script to create a dictionary, named Odd to store the first 50 odd numbers and their log2. 
CODE: '''
Odd = {x: np.log2(x) for x in range(100) if x % 2 != 0}
print(Odd)

''''22.Write a python script to store prime numbers between 50 and100 along with their digit-sum. 
CODE'''


def isPrime(num):
    count = 0
    for i in range(2, int(mt.sqrt(num))):
        if num % i == 0:
            count += 1
        if count > 0:
            return False
    return True


prime_digit_sum = {x: sum(list(map(int, [char for char in str(x)]))) for
                   x in range(50, 100) if isPrime(x)}
print(prime_digit_sum)

'''26.Write a Python program to generate the next 15 leap years starting 
from a given year. Populate the leap years into a list and display the list. 
CODE: '''


def check_leap(year):
    count = 0
    leap_years_list = []
    while(count < 15):
        if(year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
            leap_years_list.append(year)
            count = count+1
        year = year+1
    return leap_years_list


year = int(input())
leap_year_list1 = check_leap(year)
print(leap_year_list1)
