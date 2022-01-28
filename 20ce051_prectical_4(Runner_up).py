# 20ce051
# kirtan mangukiya
# https://github.com/kirtanmangukiya/project.git

""" Que.

Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
You are given n scores. Store them in a list and find the score of the runner-up.
Input Format: The first line contains. The second line contains an array A[]  of n integers each separated by a space.
"""

n = int(input())

num = map(int, input().split())
num = list(set(num))
num.remove(max(num))

print(max(num))
    
