#!/usr/bin/env python
# coding: utf-8

# Q1. An escape character that are otherwise impossible to put into a string.  We use them by adding a backslash()followed by the character you want to add to the string. 

# Q2. The escape characters n and t stand for a newline and tab. \t:Tab \n: Newline (line break).

# Q3. To put a backslash into a string, we need to code two backsheets \: Backslash()

# Q4. Since the string begins with a double quote, Python knows that single quote is a part of string and not marking the end of the string.

# Q5. Python print statement prints all the statements by default in a new line. We can also triple-quote the string.

# In[ ]:


#Q6. 
    'Hello,world!'[1]    : 'e'
    'Hello,world!'[0:5]  : 'Hello'
    'Hello,world!'[:5]   : 'Hello'
    'Hello,world!'[3:]   : 'lo,world!' 


# In[ ]:


#Q7. 
    "Hello".upper()              :'HELLO'
    "Hello".upper().isupper()    : True
    "Hello".upper().lower()      :'hello'


# In[ ]:


#Q8.
"Remember , remenber the fifth of July.".split() : ['Remeber,' , 'remember,'the','fifth','of','July.']
'-'.join('There can only one.'.split())          : 'There-can-only-one.'


# In[ ]:


#Q9. 
The methods for right-justifying, left-justifying , and centering a string rjust(),ljust(), center().
str.ljust(s, width[, fillchar])
str.rjust(s, width[,fillchar])
str.center(s,width['fillchar'])


# Q10. Use lstrip to remove whitespace from the beginning of the string, and rstrip to remove whitespace from the end of the string.
