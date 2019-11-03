'''
You are given a string S and width  W.
Your task is to wrap the string into a paragraph of width  W.
Sample Input:
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4

Sample Output:
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
'''
import textwrap
def wrap(string, max_width):
    string=list(string)
    m=[]
    while string:
        a=string[0:max_width]
        b=''
        b=b.join(a)
        m.append(b)
        string=string[max_width:]
    j='\n'
    j=j.join(m)
    return j

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

