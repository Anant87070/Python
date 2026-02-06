s="Anant Mishra"
print(s.index("A")) 

s="Anant Mishra"
print(s.index("Mishra")) 

s="banana"
print(s.index("a",2))       #search start index 2

s="banana"
print(s.index("a",2,5)) 

s="banana"
print(s.index("a",-2))             #5

## s="banana"
## print(s.index("a",-2,-5))             #ValueError: substring not found

## s="banana"
## print(s.index("a",-2000,-5000))    #ValueError: substring not found

## s="banana"
## print(s.index("x"))         #ValueError: substring not found

## s="hm pata nahi kya kr rahe hai"
## print(s.index(("a","t")))            #TypeError: index() argument 1 must be str, not tuple

## s="hm pata nahi kya kr rahe hai"
## print(s.index(("a",6,8)))              #TypeError: index() argument 1 must be str, not tuple

## s="hm pata nahi kya kr rahe hai"
## print(s.index("a",0.0,8.1))           #TypeError: slice indices must be integers or None or have an __index__ method

num = [10, 20, 30, 20, 40]
print(num.index(20))            #1   return first occurrence only

num = [10, 20, 30, 20, 40]
print(num.index(20, 2))             #3

## num = [10, 20, 30, 20, 40]
## print(num.index(8))                 #ValueError: list.index(x): x not in list

## s = ""
## print(s.index('😊'))             #ValueError: substring not found

## s = "Hello 😊"
## print(s.index('🔥'))             #ValueError: substring not found

s = "Hello\u00A0World"   
print(s.index('\u00A0'))                         #5

s = "Order No: ①②③"
print(s.index('②'))                         #11

s = "Price is ₹500"
print(s.index('₹'))                         #9

s = "नमस्ते दुनिया"
print(s.index("दुनिया"))                         #7

s = "😊Python😊"
print(s.index('😊'))                         #0

s = "Hello 😊"
print(s.index('😊'))                         #6