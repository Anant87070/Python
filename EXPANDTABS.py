# s="Anant\tMishra"
# print(s.expandtabs())       #Anant   Mishra  8-5->3

# s="Anant\tMishra"
# print(s.expandtabs(4))      #Anant   Mishra  8-5->3

# s="Anant\tMishra"
# print(s.expandtabs(0))       #AnantMishra

# s="Anant\tMishra"
# print(s.expandtabs(-3))       #AnantMishra
# print(s.expandtabs(-4))       #AnantMishra
# print(s.expandtabs(-10))       #AnantMishra

# s="An\tant\tMi\tsh\tra"
# print(s.expandtabs())           #An      ant     Mi      sh      ra , 8-2->6, 8-3->5, 8-2->6, 8-2->6 

# s1 ="a\tk\tm"
# print(s1)
# print(s1.expandtabs())
# print(s1.expandtabs(8))
# print(s1.expandtabs(2))

s1 ="a\tk\tm"
print(s1.expandtabs(0))         #akm
print(s1.expandtabs(-1))        #akm
print(s1.expandtabs(18))        #a                 k                 m
print(s1.expandtabs(-18))       #akm
#print(s1.expandtabs(1.2))       #TypeError: 'float' object cannot be interpreted as an integer
#print(s1.expandtabs("1"))       #TypeError: 'str' object cannot be interpreted as an integer

s="\t\tX"
print(s.expandtabs(4))          #        X    First tab ->column 4, second tab ->column 8 