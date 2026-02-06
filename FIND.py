# s="Anant Mishra"
# print(s.find("Mishra"))         #6

# s="hm pata nahi kya kr rahe hai"
# print(s.find("a"))                  #4

# s="Anant Mishra"
# print(s.find("python"))         #-1

# s="anant Mishra"
# print(s.find("a"))          #0  a appears multiple times, returns only the first occurance

# s="Anant Mishra"
# print(s.find("a"))          #2  

# s="anant Mishra"
# print(s.find("a",2))        #2      seaech start from index 2.

# s="anant Mishra"
# print(s.find("a",5))        #11     seaech start from index 5.

# s="anant Mishra"
# print(s.find("a",2,5))       #2     seaech between index 2 and 5,end index not included.

# s="anant Mishra"
# print(s.find("n",1,5))         #1      seaech between index 1 and 5 ,end index not included.

# s="anant Mishra"
# print(s.find("n",-1,-5))         #-1     #     seaech between index 1 and 5 ,end index not included.

s="hello"
print(s.find("e",0,-1))         #1

s="hello"
print(s.find("e",4,2))         #-1    start > end

# s="anant Mishra"
# print(s.find("n",4))            #-1

# s="hm pata nahi kya kr rahe hai"
# print(s.find(("a","t")))               #TypeError: find() argument 1 must be str, not tuple

# s="hm pata nahi kya kr rahe hai"
# print(s.find("a",0.0,8.0))              #TypeError: slice indices must be integers or None or have an __index__ method

# s="hm pata nahi kya kr rahe hai"
# print(s.find(("a",0.0,8.0)))            #TypeError: find() argument 1 must be str, not tuple

# s="anant Mishra"
# print(s.find(" "))       #5   finding spaces

# s="anant Mishra"
# print(s.find(""))       #0

# s="anant Mishra"
# print(s.find("Mishra"))   #6

s="anant Mishra"
print(s.find("akm"))     #-1  case sensitive

s="anant Mishra"
print(s.find("",3))       #3