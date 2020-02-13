import os

os.chdir('/home/lola/python/last')

print(os.getcwd())


for f in os.listdir():
        #print(f)
        f_title, f_num = f.split('_')
        f_num = f_num.strip().zfill(2)
        #print(f'{f_num}-{f_title}')
        new_name = f'{f_num}-{f_title}'
        os.rename(f, new_name)
