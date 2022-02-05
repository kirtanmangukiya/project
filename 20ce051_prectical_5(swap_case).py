# 20ce051
# kirtan mangukiya
# https://github.com/kirtanmangukiya/project.git


def swap(s):

    Output = '';
    for char in s:
        if (char.islower()==True):
             Output += (char.upper());
             
        elif(char.isupper()==True):
            Output += (char.lower());
        
        else:
            Output += char;
    return Output;

if __name__ == '__main__':
    s = input()
    result = swap(s)
    print(result)