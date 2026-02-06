s=""
print(s.isspace())         # True

s="   "
print(s.isspace())        # True

s="\t"
print(s.isspace())         # True

s="\n"
print(s.isspace())         # True

s="\t \n"
print(s.isspace())      # True

s=" a "
print(s.isspace())        # False 

s="1.23"
print(s.isspace())        # False

s="$#@"
print(s.isspace())        # False

s="$#@\n"
print(s.isspace())        # False

s="!"
print(s.isspace())          # False

s="\u2003"
print(s.isspace())          # True

s="€"
print(s.isspace())          # False

s="hello🙂"
print(s.isspace())        # False