# Работа со списками

# list_str = [1567,25675,5673,456,567,676553,"Volvo"]
# print(list_str,type(list_str),len(list_str))

# for i in range(len(list)):
#     print(i, list[i], sep=':')

#list
# list_str=list("Volvo")
# print(list_str)

# срезы

# for i in range(len(list_str)):
#     print(i,list[i:])
# for i in range(len(list_str)):
#     print(i,list[:i])

#функции со спичком

# list_str2=['Vova','Pete','Sasha']
# print(list_str*2)

#методы
# integer_list=[]
# for i in range (5):
#     integer_list.append(i)
# print(integer_list)
# integer_list.append(0)
# print(integer_list)
# integer_list.remove(0)
# print(integer_list)
# el=len(integer_list)
# del integer_list[el-1]
# print(integer_list)

#reverse
# integer_list.reverse()
# print(integer_list)
# integer_list_2=[6,3,2,6,4,5,7,8]
# integer_list_2.sort()
# print(integer_list_2)
# integer_list_2.insert(5,'Volvo')
# print(integer_list_2)

# обработка списков map, filter,reduce

#map
integer_list_3=[6,3,2,5,6,7,7,8]
integer_list_3=map(str,integer_list_3)
integer_list_3=list(integer_list_3)
print(integer_list_3)


#filter
integer_list_3=[6,3,2,5,6,7,7,8]
integer_list_4=filter(lambda x: x<=5,integer_list_3)
integer_list_4=list(integer_list_4)
print(integer_list_4)

#reduse
from functools import reduce
integer_list_5 = [1,4,5,8]
sum=reduce(lambda x,y: x+y, integer_list_5)
mult=reduce(lambda x,y: x*y, integer_list_5)
print(sum,mult)


