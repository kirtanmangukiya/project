# 20ce051
# kirtan mangukiya
# https://github.com/kirtanmangukiya/project.git

import collections;

n = int(input())
data = collections.OrderedDict()

for i in range(n):
    word = input()
    if word not in data:
        data[word] =1
    else:
        data[word] += 1

print(len(data));

for k,v in data.items():
    print(v,end = " ");
