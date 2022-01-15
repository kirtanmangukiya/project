# 20ce051
# KIRTAN MANGUKIYA
# https://github.com/kirtanmangukiya/project



#write a Python script to check whether a given key already exists in a dictionary.

dic = {'A': 'apple', 'B': 'ball', 'C': 'cat', 'D': 'dall', 'E': 'eye'}
def is_key_present(key):
  if key in dic:
      print('Key is exist')
  else:
      print('Key is not exist')
is_key_present('A')
is_key_present('ball')
is_key_present('c')
print('')

#Write a Python script to merge two Python dictionaries.
dic_A={ 'apple':1, 'ball':2 }
dic_B={'cat':3, 'dall':4 }
dicMerge=dic_A.copy()
dicMerge.update(dic_B)
print(dicMerge)
print('')


#Write a Python program to sum all the items in a dictionary.

dic = {'a': 10, 'b': 20}
print("Total Sum of values in the dictionary is:", sum(dic.values()))
print('')


#Write a Python script to add a key to a dictionary.

dic = {'a': 25, 'b': 30}
dic.update({'C': 10})
print(dic)
print('')


#Write a Python script to concatenate dictionaries to create a new one.

dic_1={1:'aman', 2:'kirtan'}
dic_2={3:'vivek', 4: 'anirudh'}
dic_3={5: 'milan', 6:'dev'}
dic_4={}
dic_4.update(dic_1)
dic_4.update(dic_2)
dic_4.update(dic_3)
print(dic_4)
print('')