#Tema6_Laba4

def personal_info(name, age, company = 'unnamed'):
    print(f'Имя: {name} Возраст: {age} Компания {company}')

tom = ('Tom', 25)
personal_info(*tom)

bob = ('Bob', 31, 'СИНХ')
personal_info(*bob)