# 20ce051
# KIRTAN MANGUKIYA
#https://github.com/kirtanmangukiya/project


#Write a Python program to add member(s) in a set and clear a set

Set_1 = {0, 2, 4, 6, 8}
print("set before adding :",Set_1)
Set_1.add(10)
print("Set before clear:", Set_1)
print("Set after clear:", Set_1.clear())
print('')


#Write a Python program to remove an item from a set if it is present in the set.

Set = {'Apple', 'Ball', 'Cat', 'Dall', 'Eye'}
Set.discard('Ball')
print(Set)
print('')

#Write a Python program to create an intersection, Union, difference of sets.

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print("Union of A and B:", set_a.union(set_b))
print("Intersection of A and B:", set_a.intersection(set_b))
print("Difference of A and B:", set_a.difference(set_b))
print('')


#Write a Python program to find maximum and the minimum value in a set.
Set_c={350,200,2050,550,457,750,80,990,1050}
print("maxium of set :",max(Set_c))
print("minium of set :",min(Set_c))

#Write a Python program to find the most common elements and their counts from list, tuple, dictionary.

list1 = [12,8,1.2,5.96,210]
tuple1 = (12,210,10,1.2,2)
dictionary1 = {210,1,1.2,5.96}
print("List =", list1)
print("Tuple =", tuple1)
print("Dictionary =",dictionary1)
set1 =set(list1).intersection(set(tuple1))
result_set = set1.intersection(set(dictionary1))
final_list = list(result_set)
print("Common of members of list, tuple and dictionary:", final_list)

    
    