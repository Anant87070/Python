# s="anant"
# print(s.count("a"))     #2

# s="Anant"
# print(s.count("a"))     #1

# s="Anant mishra"
# print(s.count("na"))    #1

# s="banana"
# print(s.count("a",2))   #2
  
# s="anant mishra"
# print(s.count("a",3))  #1

# s="Anant mishra"
# print(s.count("a",3))    #1

# s="Hello hello"
# print(s.count("hello"))  #1

# s="Anant mishra"               #empty case ->Empty string is found b/w every character + ends
# print(s.count(""))     #13

# s="akm python wala bnda hai"
# print(s.count("a"))             #5

# s= [1,2,3,2,2,4]
# print(s.count(2))       #3

# fruits=["apple","banana","apple"]
# print(fruits.count("apple"))            #2

# s=" akm python wala bnda hai"     
# print(s.count("a",15))                     #3   

# s="akm python wala bnda hai"     
# print(s.count("a",15))            #2

# s=" akm python wala bnda hai"
# print(s.count("a",15,20))       #1

# s="akm python wala bnda hai"     
# print(s.count("a",0,1))        #1

# s="akm python wala bnda hai"     
# print(s.count("a",1,1))            #0    

# s=" akm python wala bnda hai"     
# print(s.count("a",-2,-15))         #0  

# s="akm python wala bnda hai"     
# print(s.count("a",-2,-15))         #0  

print("akm".count("a",-1,-15))    

print("akm".count(""))