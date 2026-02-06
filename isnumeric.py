s="anantMishra"
print(s.isnumeric())       #False

s="123"
print(s.isnumeric())        #True

s="@#$"
print(s.isnumeric())        #False

s="ANANTMISHRA"
print(s.isnumeric())       #False

s="ANANTMISHRA123"
print(s.isnumeric())       #False

s="+-*"
print(s.isnumeric())        #False

s=" "
print(s.isnumeric())        #False

s=""
print(s.isnumeric())        #False

s="1+2"
print(s.isnumeric())        #False

s="½"
print(s.isnumeric())        # True

s="²"
print(s.isnumeric())        # True
s="Ⅻ"
print(s.isnumeric())        # True
s="四"
print(s.isnumeric())            # False
s="3.14"
print(s.isnumeric())         # False
s="+123"
print(s.isnumeric())        # False
s=" 123"
print(s.isnumeric())     # False
s="1,000"
print(s.isnumeric())         # False

s="12³"
print(s.isnumeric())     # True
s="½2"
print(s.isnumeric())           # False
s="€"
print(s.isnumeric())            # True
s="²"
print(s.isnumeric())        # False
s="½"
print(s.isnumeric())          #  True
s="½"
print(s.isnumeric())     #  True

s="12.3"
print(s.isnumeric())  #  False
s="-123"
print(s.isnumeric())  #  False

# s="a"
# print(s.isnumeric())          #False

# s="straße"
# print(s.isnumeric()) False

# s="❤"
# print(s.isnumeric())          # False

# s="€"
# print(s.isnumeric())          # False
# s="αβγ"
# print(s.isnumeric() )       # False (Greek)

# s="Жук"
# print(s.isnumeric())        #False (Cyrillic)

# s="中文"
# print(s.isnumeric())        # False (Chinese)

# s="あいう"
# print(s.isnumeric())     # False (Japanese Hiragana

# s="café"
# print(s.isnumeric())      #False

# s="naïve"
# print(s.isnumeric())     #False

# s="straße"
# print(s.isnumeric())     #False

# s="\n"
# print(s.isnumeric())         # False

# s="\t"
# print(s.isnumeric())         # False

# text = "Price is ₹500"
# print(text.isnumeric())        # False