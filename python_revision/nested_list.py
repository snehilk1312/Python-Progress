N=int(input())
name_list=list()
mark_list=list()
for i in range(N):
	name=input()
	marks=float(input())
	name_list.append(name)
	mark_list.append(marks)


zipped_list=list(zip( mark_list,name_list))
sorted_marks_list=sorted(mark_list)
#print(zipped_list)
#for i,v in zipped_list:
#	print(i)


zipped_list=sorted(zipped_list)
#print(zipped_list)

mark_set=set(mark_list)
mark_list1=list(mark_set)

mark_list1=sorted(mark_list1)
#print(mark_list1)
#print(type(mark_list1))
g=mark_list1[1]
answer=[]
for i,v in zipped_list:
	#print(i,v)
	#print(g)
	if i==g:
		answer.append(v)


answer=sorted(answer)
for i in answer:
	print(i)
