str_1="очень хорошая машина \'Volvo\'"
str_2="Mersedec"
print(str_1[::], len(str_1))
print(str_1*2)
print(str_1+str_2)
brand='Volvo'
price=1.6
# cars=f'Марка авто {brand}, цена {price}'
# print(cars)
print(str_1.split())
cars='Volvo, Lada, Mersedes'
print(cars.split(','))

# Методы форматирования строк

print(str_1.upper())
print(str_1.lower())
print(str_1.title())

#замена подстроки

email_adress='eMail: _mail_'
email='my_email@gmail.com'
print(email_adress.replace('_mail_',email))