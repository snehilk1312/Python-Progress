'''
Split a string into subsegments of length k,
then print each subsegment with any duplicate characters stripped out.
'''

def merge_the_tools(string, k):
    i=0
    l=[]
    o=[]
    while (i+k)<=len(string):
        m=string[i:i+k]
        l.append(m)
        i=i+k
    for i in l:
        h=[]
        for j in i:
            if j not in h:
                h.append(j)
        s=''
        s=s.join(h)
        o.append(s)
    for i in o:
        print(i)



if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
