s="123"
print(s.isdecimal())     # True

s="007"
print(s.isdecimal())        # True

s="0"
print(s.isdecimal())    # True

s="123"
print(s.isdecimal())        # False

s="\u2003"
print(s.isdecimal())          # False

s="€"
print(s.isdecimal())          # False

s="hello🙂"
print(s.isdecimal())        # False

s="007"
print(s.isdecimal())        # True

s="0"
print(s.isdecimal())    # True

s=""
print(s.isdecimal())    # False

s="123 "
print(s.isdecimal())    # False

s=" 123"
print(s.isdecimal())        # False

s="12 3"
print(s.isdecimal())        # False

s="+123"
print(s.isdecimal())        # False

s="-123"
print(s.isdecimal() )         # False

s="12.3"
print(s.isdecimal())          # False

s="1,000"
print(s.isdecimal() )        # False

s="123a"
print(s.isdecimal())        # False

s="a123"
print(s.isdecimal())        # False

s="12a3"
print(s.isdecimal())        # False

s="١٢٣"
print(s.isdecimal())     # Arabic-Indic digits  # True

s="१२३"
print(s.isdecimal())     # Devanagari digits    # True

s="৪৫৬"
print(s.isdecimal())     # Bengali digits   # True

s="²³"
print(s.isdecimal())         # False

s="Ⅻ"
print(s.isdecimal())        # Roman numeral  # False

s="123\n"
print(s.isdecimal())        # False

s="123\t"
print(s.isdecimal())       # False