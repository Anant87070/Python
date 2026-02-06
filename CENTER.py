s='anant'
print(s.center(10))     #  anant  

s='anant'
print(s.center(5))       #anant

s='anant'
print(s.center(5,"8"))      #same length unchanged ->anant

# s="Python"
# print(s.center(10,"++"))       #TypeError: The fill character must be exactly one character long  

# s="Python"
# print(s.center(10,""))          #TypeError: The fill character must be exactly one character long

# s='anant'
# print(s.center(9,"10"))        #TypeError: The fill character must be exactly one character long

s='anant'
print(s.center(7,"9"))       #9 added on both side ->9anant9

s='anant'
print(s.center(12,"1"))         #111anant1111

s='anant'
print(s.center(-7,"1"))         #anant  ->-ve value unchanged

# s='anant'
# print(s.center(1.7,"1"))         #TypeError: 'float' object cannot be interpreted as an integer

s=""
print(s.center(5,"*"))         #*****

s="あいう"
print(s.center(5,"_"))         #_あいう_

print("CODE".center(2))         #CODE  -> Width < length -> unchanged

print("C".center(1,"-"))         #C  -> Width == length -> unchanged

# s=123
# print(s.count(12,"2"))          #AttributeError: 'int' object has no attribute 'count'