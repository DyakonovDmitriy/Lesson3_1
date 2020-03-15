# инициализация словаря

dict_temp={}
print(type(dict_temp))

dict_temp={'dict1':1,'dict2':2.1,'dict3':'name','dict4':[1,2,3]}
print(type(dict_temp),dict_temp)

dict_temp=dict.fromkeys(['a','b'],[12,20])
print(type(dict_temp),dict_temp)

dict_temp=dict(brend='Volvo', volueme_engaine=1.6)
print(type(dict_temp),dict_temp)

dict_temp_2={a:a**2 for a in range(10)}
print(dict_temp_2[5])


#обращение по ключу
print(dict_temp['brend'])

#функции со словорями

print(dict_temp.values())
print(dict_temp.keys())
print(dict_temp.items())

#обращения по ключу

dict_temp['brend']=100
print(dict_temp)

# dict_temp['name']='Dima'
# print(dict_temp.items())



#Итерирование по словаю
