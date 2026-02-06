s="A"
print(s.isupper())          # True

s="ABC"
print(s.isupper())        # True

s="ABC123"
print(s.isupper())     # True

s="ABC!"
print(s.isupper())       # True

s="abc"
print(s.isupper())        # False

s="ABC#@$"
print(s.isupper())        # True

s="ABC0123"
print(s.isupper())        # True

s="ABc"
print(s.isupper())        # False

s="123"
print(s.isupper())        # False (no letters)

s="!@#"
print(s.isupper())        # False

s="   "
print(s.isupper())        # False

s="\u2003"
print(s.isupper())          # False

s="€"
print(s.isupper())          # False

s="hello🙂"
print(s.isupper())        #False

s="🙂"
print(s.isupper())        #False