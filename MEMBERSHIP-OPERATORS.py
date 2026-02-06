s="Anant Python"
print("ant"in s)        #True

s="Anant Python"
print(" "in s)         #True

s="Anant Python"
print("anant "in s)     #False

s="Anant Python"
print("akm"in s)     #False

s="Anant Python"
print("akm" not in s)     #True  -> Because akm is not present

s="Anant Python"
print(s in "akm" )      #False
