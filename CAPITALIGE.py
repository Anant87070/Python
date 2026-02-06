#First character of a string to UPPERCASE and all remaining to LOWERCASE
# s='anant'
# result=s.capitalize()
# print(result)               #Anant

# s='AnAnT'
# result=s.capitalize()
# print(result)               #Anant

# s='anAnT'
# result=s.capitalize()
# print(result)               #Anant

# s='123anant'         
# result=s.capitalize()
# print(result)                #123anant   -> since first character isn't a letter nothing gets capitalized
       
# s='123anAnT'
# result=s.capitalize()
# print(result)               #123anant     

# s='@anant'
# result=s.capitalize()
# print(result)               #@anant

# s='@AnAnT'
# result=s.capitalize()
# print(result)               #@anant

# s='ANANT'
# result=s.capitalize()
# print(result)               #Anant

s=' ANANT'
result=s.capitalize()
print(result)                 # anant

s=' '
result=s.capitalize()
print(result)                 #Empaty