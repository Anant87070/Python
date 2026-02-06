s="a"
print(s.islower())          # True

s="abc"
print(s.islower())        # True

s="abc "
print(s.islower())        # True

s="abc123"
print(s.islower())     # True

s="abc!"
print(s.islower())       # True

s="café"
print(s.islower())      # True  unicode

s="naïve"
print(s.islower())     # True

s="ABC"
print(s.islower())        # False

s="abcDef"
print(s.islower())     # False (D is uppercase)

s="123"
print(s.islower())        # False (no letters)

s="!@#"
print(s.islower())        # False

s="   "
print(s.islower())        # False

s=""
print(s.islower())           # False (empty string)

s="\u2003"
print(s.islower())          # False

s="€"
print(s.islower())          # False

s="hello🙂"
print(s.islower())        # True

s="🙂"
print(s.islower())        #False