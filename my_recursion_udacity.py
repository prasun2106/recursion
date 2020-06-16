#!/usr/bin/env python
# coding: utf-8

# # Udacity Notebook 1 - Introduction

# In[14]:


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


# In[15]:


# my implementation - almost same as Udacity
def sum_integers(n):
    if n==0:
        return (0)
    else:
        output = n + sum_integers(n-1)
        return output
        
sum_integers(3)


# In[16]:


# my implementation - almost same as Udacity
def sum_array(arr):
    if len(arr)==1:
        return(arr[0])
    else:
        pop = arr.pop()
        output = pop + sum_array(arr)
        return output
sum_array([1,2,3,4,5])


# In[17]:


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
    


# # Udacity Notebook 2 - Factorial Using Recursion

# In[19]:


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


# In[21]:


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


# In[22]:


# Test Cases

print ("Pass" if (1 == factorial(0)) else "Fail")
print ("Pass" if  (1 == factorial(1)) else "Fail")
print ("Pass" if  (120 == factorial(5)) else "Fail")


# # Udacity Notebook 3 - Reversing a string

# In[41]:


def reverse_string(my_string):
    if len(my_string)<=1:
        return my_string
    if len(my_string)>=1:
        reversed_string = my_string[-1] + reverse_string(my_string[:-1])
        return reversed_string

reverse_string('prasun')


# In[42]:


# my implementation - almost same as Udacity
def reverse_string(my_string):
    if len(my_string) <=1:
        return my_string
    else:
        output = my_string[-1] + reverse_string(my_string[:-1])
        return output
reverse_string('prasun')


# In[43]:


# Test Cases
    
print ("Pass" if  ("" == reverse_string("")) else "Fail")
print ("Pass" if  ("cba" == reverse_string("abc")) else "Fail")


# # Udacity Notebook 4 - Checking Palindrome

# In[44]:


# my implementation - different than Udacity
# my implementation doesn't use recursion, it just uses the function reverse_string
def check_palindrome(my_string):
    if reverse_string(my_string) == my_string:
        return('Yes its a palindrome')
    else:
        return('no its not a palindrome')
    return


# In[45]:


print(check_palindrome('prasarp'))
print(check_palindrome('prasarpwmdk'))


# In[49]:


# another method:
def is_palindrome(my_string):
    if len(my_string) <= 1:
        return True
    if len(my_string) == 2:
        return my_string[0] == my_string[1]
    else:
        output = (my_string[0] == my_string[-1]) & is_palindrome(my_string[1:len(my_string)-1])
        return output


# In[50]:


# Test Cases

print ("Pass" if  (is_palindrome("")) else "Fail")
print ("Pass" if  (is_palindrome("a")) else "Fail")
print ("Pass" if  (is_palindrome("madam")) else "Fail")
print ("Pass" if  (is_palindrome("abba")) else "Fail")
print ("Pass" if not (is_palindrome("Udacity")) else "Fail")


# # Udacity Notebook 5 - List Permutation

# In[77]:


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


# # Udacity Notebook 6 - String Permutations

# In[87]:


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
    


# In[82]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




