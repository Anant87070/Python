# s='anant'           #case insensitive
# result=s.casefold()
# print(result)          #anant

# s='Anant'
# result=s.casefold()
# print(result)          #anant

# s='ANANT'
# result=s.casefold()
# print(result)          #anant

# s='AnAnt'
# result=s.casefold()
# print(result)          #anant

# s='123anant'
# result=s.casefold()
# print(result)          #124anant

# s='123ANANT'
# result=s.casefold()
# print(result)          #123anant

s="straße"
result=s.casefold()
print(result)               #Unicode case -> strasse:  ß->ss 

s="❤Anant"
result=s.casefold()
print(result)               #❤anant

s1 = "AbC123"
s2 = "abc123"
print(s1.casefold() == s2.casefold())         #true

s1="straße"
s2 = "STRASSE"
print(s1.casefold() == s2.casefold())         #true 