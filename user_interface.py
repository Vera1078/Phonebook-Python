import find_contact
import logger

def choice():
    print('Телефонный справочник')
    result = int(input('Меню выбора: \n\
            1 - Добавить абонента\n\
            2 - Поиск абонента\n\
            3 - Показать всех абонентов\n\
            4 - Выход\n\
            Выберите пункт: '))
    return result
    
