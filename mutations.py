def mutate_string(s, position, character):
    k=[i for i in s]
    del k[position]
    k.insert(position,character)
    k=''.join(k)
    return k

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
