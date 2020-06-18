#!/usr/bin/env python
# coding: utf-8

# # Recursion

# ## Problem 1 - Introduction

# In[1]:


# my implementation accounts for both positive and negative exponents
def power_function(n, e):
    if n ==0 and e == 0:
        raise ValueErrorueError("0 raised to 0 is not defined")
    if e == 0:
        return(1)
    if e > 0:
        result = n * power_function(n, e-1)
    if e < 0:
        result = n**-1 * power_function(n, e + 1)
    return result

power_function(2,-1)


# In[2]:


# my implementation - almost same as Udacity
def sum_integers(n):
    if n==0:
        return (0)
    else:
        output = n + sum_integers(n-1)
        return output
        
sum_integers(3)


# In[3]:


# my implementation - almost same as Udacity
def sum_array(arr):
    if len(arr)==1:
        return(arr[0])
    else:
        pop = arr.pop()
        output = pop + sum_array(arr)
        return output
sum_array([1,2,3,4,5])


# In[4]:


# my implementation - in slightly different way
def sum_array(arr):
    
    if len(arr) == 0:
        raise ValueError('size of array is 0')
    
    if len(arr)==1:
        return(arr[0])
     
    if len(arr)>1:
        result = arr[0] + sum_array(arr[1:len(arr)])
    return result
sum_array([1,2,3,4,5])
    


# ## Problem 2 - Factorial Using Recursion

# In[5]:


# factorial using recursion
def fact(n):
    if n == 0:
        return(1)
    if n> 0:
        result = n*fact(n-1)
        return result
    if n<0:
        raise ValueError("Factorial Not Defined")

fact(5)


# In[6]:


# my implementation - almost same as Udacity
def factorial(n):
    if n<0:
        raise ValueError('Factorial of Negative numbers are not defined')
    if n==0:
        return(1)
    else:
        output = n*factorial(n-1)
        return output
factorial(5)


# In[7]:


# Test Cases

print ("Pass" if (1 == factorial(0)) else "Fail")
print ("Pass" if  (1 == factorial(1)) else "Fail")
print ("Pass" if  (120 == factorial(5)) else "Fail")


# ## Problem 3 - Reversing a string

# In[8]:


def reverse_string(my_string):
    if len(my_string)<=1:
        return my_string
    if len(my_string)>=1:
        reversed_string = my_string[-1] + reverse_string(my_string[:-1])
        return reversed_string

reverse_string('prasun')


# In[9]:


# my implementation - almost same as Udacity
def reverse_string(my_string):
    if len(my_string) <=1:
        return my_string
    else:
        output = my_string[-1] + reverse_string(my_string[:-1])
        return output
reverse_string('prasun')


# In[10]:


# Test Cases
    
print ("Pass" if  ("" == reverse_string("")) else "Fail")
print ("Pass" if  ("cba" == reverse_string("abc")) else "Fail")


# ## Problem 4 - Checking Palindrome

# In[11]:


# my implementation - different than Udacity
# my implementation doesn't use recursion, it just uses the function reverse_string
def check_palindrome(my_string):
    if reverse_string(my_string) == my_string:
        return('Yes its a palindrome')
    else:
        return('no its not a palindrome')
    return


# In[12]:


print(check_palindrome('prasarp'))
print(check_palindrome('prasarpwmdk'))


# In[13]:


# another method:
def is_palindrome(my_string):
    if len(my_string) <= 1:
        return True
    if len(my_string) == 2:
        return my_string[0] == my_string[1]
    else:
        output = (my_string[0] == my_string[-1]) & is_palindrome(my_string[1:len(my_string)-1])
        return output


# In[14]:


# Test Cases

print ("Pass" if  (is_palindrome("")) else "Fail")
print ("Pass" if  (is_palindrome("a")) else "Fail")
print ("Pass" if  (is_palindrome("madam")) else "Fail")
print ("Pass" if  (is_palindrome("abba")) else "Fail")
print ("Pass" if not (is_palindrome("Udacity")) else "Fail")


# ## Problem 5 - List Permutation

# In[15]:


def create_permutations(my_list):
    store_permutation = []
    
    if len(my_list) <= 1:
        return [my_list]
    
    for i in range(len(my_list)):
        m = my_list[i]

        remaining_list = my_list[:i] + my_list[i+1:] 

        for p in create_permutations(remaining_list):
            store_permutation.append([m] + p)

    return store_permutation

create_permutations([1,2,4])


# ## Problem 6 - String Permutations

# In[16]:


# Return all permutations of a string in a list

def create_string_permutation(my_string):
    store_permutation = []
    if len(my_string) <= 1:
        return my_string
    
    else:
        for i in range(len(my_string)):
            m = my_string[i]
            
            remaining_string = my_string[:i] + my_string[i+1:]
            
            for p in create_string_permutation(remaining_string):
                store_permutation.append(m + p)
        return store_permutation

create_string_permutation('abcd')
    


# In[17]:


def test_function(test_case):
    string = test_case[0]
    solution = test_case[1]
    output = create_string_permutation(string)
    
    output.sort()
    solution.sort()
    
    if output == solution:
        print("Pass")
    else:
        print("Fail")


# In[18]:


string = 'ab'
solution = ['ab', 'ba']
test_case = [string, solution]
test_function(test_case)


# In[19]:


string = 'abc'
output = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
test_case = [string, output]
test_function(test_case)


# In[20]:


string = 'abcd'
output = ['abcd', 'bacd', 'bcad', 'bcda', 'acbd', 'cabd', 'cbad', 'cbda', 'acdb', 'cadb', 'cdab', 'cdba', 'abdc', 'badc', 'bdac', 'bdca', 'adbc', 'dabc', 'dbac', 'dbca', 'adcb', 'dacb', 'dcab', 'dcba']
test_case = [string, output]
test_function(test_case)


# ## Problem 7 - Keypad Combinations 

# In[21]:


# find all alphabet combinations if an integer "num" is pressed on a mobile keyboard
# solution:

def keypad_combinations(num):
    
    my_dict = {'2':['a','b','c'], '3':['d','e','f'],
              '4':['g','h','i'], '5': ['j','k','l'],
              '6':['m','n','o'], '7':['p','q','r','s'],
              '8':['t','u','v'], '9':['w','x','y','z']}
    if num == 0:
        return [""]
    elif num/10 <1:
        return my_dict[str(num)]
    else:
        tens = my_dict[str(num%10)]
        remaining = keypad_combinations(num//10)
        
        result = []
        for i in tens:
            for j in remaining:
                result.append(j + i)
        return result


# In[22]:


def test_keypad(input, expected_output):
    if sorted(keypad_combinations(input)) == expected_output:
        print("Yay. We got it right.")
    else:
        print("Oops! That was incorrect.")


# In[23]:


# Base case: list with empty string
input = 0
expected_output = [""]
test_keypad(input, expected_output)


# In[24]:


# Example case
input = 23
expected_output = sorted(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
test_keypad(input, expected_output)


# In[25]:


# Example case
input = 32
expected_output = sorted(["da", "db", "dc", "ea", "eb", "ec", "fa", "fb", "fc"])
test_keypad(input, expected_output)


# In[26]:


test_keypad(input, expected_output)


# In[27]:


# Example case
input = 8
expected_output = sorted(["t", "u", "v"])
test_keypad(input, expected_output)


# In[28]:


input = 354
expected_output = sorted(["djg", "ejg", "fjg", "dkg", "ekg", "fkg", "dlg", "elg", "flg", "djh", "ejh", "fjh", "dkh", "ekh", "fkh", "dlh", "elh", "flh", "dji", "eji", "fji", "dki", "eki", "fki", "dli", "eli", "fli"])
test_keypad(input, expected_output)


# ## Problem 7 - Keypad Combination Method 2

# In[29]:


digit_map = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}

def word_numbers(input):
    input = str(input)
    ret = ['']
    for char in input:
        letters = digit_map.get(char, '')
        ret = [prefix+letter for prefix in ret for letter in letters]
    return ret


# In[ ]:




