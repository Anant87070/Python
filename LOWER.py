s='anant'           
result=s.lower()
print(result)          #anant

s='123ANANT'
result=s.lower()
print(result)          #123anant

s="straße"
result=s.lower()
print(result)               #Unicode case -> straße:  ß->ß unchanged

s="❤Anant"
result=s.lower()
print(result)               #❤anant

s="12An@# !"
result=s.lower()
print(result)               #12an@# !

s=" "
result=s.lower()
print(result)               #Empaty -> no error

s="Akm\nanant\tMishra"
result=s.lower()
print(result)               #anant   mishra

s1 = "AbC123"
s2 = "abc123"
print(s1.lower() == s2.lower())         #True

s1="straße"
s2 = "STRASSE"
print(s1.lower() == s2.lower())         # False