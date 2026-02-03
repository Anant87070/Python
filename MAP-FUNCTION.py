# s = ['1', '2', '3', '4']
# result = map(int, s)
# print(list(result))                 #[1, 2, 3, 4]

# s = ['1', '2', '3', '4']
# result = map(int, s)
# print(list(result))                 #[1, 2, 3, 4]     -> map() applies to each element of s. the iterator is fully consumed
# print(list(result))                 #[]               -> The iterator already exhausted
# print(list(result))                 #[]               -> The iterator already exhausted

# s = ['1', '2', '3', '4']
# result =list( map(int, s))
# print(result)                       #[1, 2, 3, 4]
# print(result)                       #[1, 2, 3, 4] 
# print(result)                       #[1, 2, 3, 4] 

# s = ['-1', '-2', '-3', '4']
# result = map(int, s)
# print(list(result))                  #[-1, -2, -3, 4]

# s = ['1.1', '2', '3', '4']
# result = map(float, s)
# print(list(result))                 #[1.1, 2.0, 3.0, 4.0]

