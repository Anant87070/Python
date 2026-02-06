# s="anantMishra"
# print(s.isalpha())       #True

# s="123"
# print(s.isalpha())        #False

# s="@#$"
# print(s.isalpha())        #False

# s="ANANTMISHRA"
# print(s.isalpha())       #True

# s="ANANTMISHRA123"
# print(s.isalpha())       #False

# s="+-*"
# print(s.isalpha())        #False

# s=" "
# print(s.isalpha())        #False

# s=""
# print(s.isalpha())        #False

# s="1+2"
# print(s.isalpha())        #False

s="a"
print(s.isalpha())          # True

s="hello🙂"
print(s.isalpha())    # False

s="❤"
print(s.isalpha())          # False

s="€"
print(s.isalpha())          # False
s="αβγ"
print(s.isalpha() )       # True (Greek)

s="Жук"
print(s.isalpha())        # True (Cyrillic)

s="あい"        
print(s.isalpha())        # True 

s="あいう"
print(s.isalpha())     # True (Japanese Hiragana

s="café"
print(s.isalpha())      # True

s="naïve"
print(s.isalpha())     # True

s="straße"
print(s.isalpha())     # True

s="\n"
print(s.isalpha())         # False

s="\t"
print(s.isalpha())         # False

text = "Price is ₹500"
print(text.isalpha())        # False