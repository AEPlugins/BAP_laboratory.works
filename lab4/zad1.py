world={'Евразия': 'Россия, Китай, Казахстан',
       'Африка': 'Судан, ЮАР, Чад',
       'Северная Америка': 'США, Канада',
       'Южная Америка': 'Бразилия, Аргенина, Чили',
       'Австралия': 'Австралия'}
for key, value in world.items():
    print("Страны {}".format(value),"находятся на материке {}.".format(key))
for key in world.keys():
    print("Материк: {}.".format(key))
for value in world.values():
    print('Страны: {}.'.format(value))