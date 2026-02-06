#s="hi Anant Mishra"
# print(s.endswith("Mishra"))         #True
# print(s.endswith("hra"))            ##True
# print(s.endswith("mishra"))         #False
# print(s.endswith("MISHRA"))         #False

# s="hi Anant Mishra"
# print(s.endswith(("Misra","shra","Mishra")))
# print(s.endswith("Misra","shra","Mishra"))   #TypeError: slice indices must be integers or None or have an __index__ method

# s="Anant Mishra"
# print(s.endswith("Anant", 0,5))         #True
# print(s.endswith("Mishra", 6,12))       #True

# s="Anant Mishra"
# print(s.endswith("Mishra",-6))      #True
# print(s.endswith("Mishra",-5))       #False

# s="Anant"
# print(s.endswith(""))        #True
# print("".endswith(""))       #True

# s="12345"
# print(s.endswith(["5"]))       #True
# #print(s.endswith("5"))        #TypeError: endswith first arg must be str or a tuple of str, not list
# #print(s.endswith["5"])        #TypeError: endswith first arg must be str or a tuple of str, not list

# s1='akm is a python developer'
# print(s1.endswith(("akm","is","a")))        #False

s1='akm is a python developer'
print(s1.endswith((("akm","is","a","developer"))))          #True  Becuase Tuple of strings

#s1='akm is a python developer'
#print(s1.endswith(["akm","is","a","developer"]))       #TypeError: endswith first arg must be str or a tuple of str, not list    Becuase List of strings

s1='akm is a python developer'
list=["akm","is","a","developer"]
print(s1.endswith(tuple(list)))             #True  Becuase Tuple of strings