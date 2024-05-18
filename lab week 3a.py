#Surya Hardiansyah
#As always, attempt your lab without searching for solutions online unless otherwise noted

#1: This code does not run!  Try it and examine the errors, then figure out what needs to
#be changed to make it work.  Do not create any, global variables, delete any existing
#code, or cut and paste existing code to new locations.
print('Q1')
a = 10

def first_func(b=20):
    c = 30
#    value = second_func()
    value = second_func(b, c) # run second_func() with b and c as arguments
    return value

# def second_func(d=40):
def second_func(b, c, d=40): # incorporate b and c within second_func()
    e = 50
    return a + b + c + d + e

result = first_func()
print(result) # print result to make sure things work

#2: Take this code from last week's lab and write functions so that the final
#execution looks like:
#answer = {key_func(k):val_func(v) for k, v in start_dict.items()}
print('\nQ2')

import datetime
start_dict = {'noah': '2/23/1999',
              'sarah':'9/1/2001',
              'zach': '8/8/2005'}
#turn it into {'Noah': datetime.datetime(1999, 2, 23),
#              'Sarah': datetime.datetime(2001, 9, 1),
#              'Zach': datetime.datetime(2005, 8, 8)}

def key_func(k):
    return k.capitalize()

def val_func(v):
    from datetime import datetime
    return datetime.strptime(v, '%m/%d/%Y').date()
        
answer = {key_func(k):val_func(v) for k, v in start_dict.items()}
print(answer)

#3: A zscore is one term to describe data transformed to have mean zero and
#standard deviation one, given by: x - x_mean / x_std
#Write a function that takes any list-like object as a positional argument,
#then returns an object of the same dimensions with the zscores for the series.
#Use these two imported functions, and test your results on several lists of
#values
print('\nQ3')
from numpy import mean, std

my_list1 = [90, 100, 105, 110]
my_list2 = [1, 2, 3]
my_list3 = [10, 20, 30, 40]

def zscore(x):
    x_mean = mean(x)
    x_std = std(x)
    z = (x - x_mean) / x_std
    return z

print(zscore(my_list1))
print(zscore(my_list2))
print(zscore(my_list3))

#4: A modified zscore uses the "median absolute deviation" to better handle
#outliers in the data, where the MAD is calculated by:
#  1. x - the median of the series
#  2. the absolute values of the results from 1
#  3. the median of the results from 2
#and finally, replace the standard deviation in the formula for the zscore from
#question 3 with the results from this process: x - x_mean / MAD
#
#Copy the function you created in 3 and create an optional key word argument that
#lets you override the default zscore calculation to instead use the modified
#version. This function should work in both question 3 and 4 without needing to
#change how you call it in part 3, because of its default behavior
print('\nQ4')
from numpy import median, absolute

my_list1 = [90, 100, 105, 110]
my_list2 = [1, 2, 3]
my_list3 = [10, 20, 30, 40]

def moded_zscore(x):
    x_mean = mean(x)
    MAD = median(absolute(x - median(x)))
    moded_z = (x - x_mean) / MAD
    return moded_z

print(moded_zscore(my_list1))
print(moded_zscore(my_list2))
print(moded_zscore(my_list3))