# s="anantMishra"
# print(s.isalnum())           #True 

# s="anant123"
# print(s.isalnum())          #True

# s="anant123@"
# print(s.isalnum())             #False

# s=""
# print(s.isalnum())            #False

# s="anant Mishra"
# print(s.isalnum())           #False

# s="-1"
# print(s.isalnum())           #False

# s="1.2"
# print(s.isalnum())           #False

# s="hello🙂"
# print(s.isalnum())          # False

# s="❤"
# print(s.isalnum())          # False

# s="€"
# print(s.isalnum())          # False

s="αβγ"
print(s.isalnum() )       #True (Greek)

s="Жук"
print(s.isalnum())        #True (Cyrillic)

s="中文"
print(s.isalnum())        #True (Chinese)

s="あいう"
print(s.isalnum())     #True (Japanese Hiragana

s="naïve"
print(s.isalnum())     #True

s="straße"
print(s.isalnum())     #True

# s="\n"
# print(s.isalnum())         # False

# s="\t"
# print(s.isalnum())         # False

# text = "Price is ₹500"
# print(text.isalnum())        # False