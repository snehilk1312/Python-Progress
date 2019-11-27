'''
soln to hackerrank ques:
https://www.hackerrank.com/challenges/find-a-string/problem

'''

def count_substring(string, sub_string):
    time_s=0
    m=len(sub_string)
    for i in range(len(string)):
        s=string[i:i+m]
        if s == sub_string:
            time_s+=1
    return time_s



if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
