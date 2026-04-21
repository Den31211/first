buttons = ['Старт', 'Меню', 'Заказать', 'Помощь']
print('Нажмите на одну из кнопок:')
for b in buttons:
    print(b)
choice = input('Ваш выбор:').lower()
if choice == 'меню':
    print('Супы: Борщ, Харчо, Солянка') 
elif choice == 'заказать':
    print('Ваш номер телефона:')
elif choice == 'помощь':
    print('Если нужна помощь пишите в директ')
elif choice == 'старт':
    print('Начинаю работу')
    