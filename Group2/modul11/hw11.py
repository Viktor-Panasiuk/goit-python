
from collections import UserDict
from datetime import datetime
import re

def normalize_phone(num):

    pref = '+38'
    i = 13-len(num)
    number = pref[0:i] + num
    
    result = number if re.match(r'[+]380\d{9}', number) else False
    return result

class AddressBook(UserDict):
    lenght = 0
    pos_iter = 0
    keys_list = []
    def __iter__(self):
        return self

    def __next__(self):
        lenght = len(self.data)
        self.keys_list = list(self.data.keys())
        if self.pos_iter < lenght:
            result_keys = self.keys_list[self.pos_iter]
            result_value = self.data.get(result_keys)
            self.pos_iter += 1
            return result_keys, result_value
        self.pos_iter = 0
        raise StopIteration

    def add_record(self, record):
        self.data[record.name.value] = record


class Record:

    def __init__(self, name, birthday = None):
        self.name = name
        self.birthday = birthday
        self.phones = []

    def add_birthday(self, birthday):
        self.birthday = birthday
        return self.birthday.value == birthday.value

    def add_phone(self, phone):
        self.phones.append(phone)

    def days_to_birthday(self):
        result = ''
        if self.birthday:
            
            now  = datetime.now()
            birthday_str = self.birthday.value
            birthday = datetime.strptime(birthday_str, '%d.%m.%Y')
            if birthday.day>=now.day and birthday.month>=now.month:
                year = now.year
            else:
                year = now.year + 1

            new_birthday = datetime(day=birthday.day, month=birthday.month, year=year)
            delta = new_birthday - now
            result = delta.days
        return result

    def edit_phone(self, old_phone, new_phone):
        self.remove_phone(old_phone)
        self.phones.append(new_phone)
    
    def remove_phone(self, phone):
        for ph in self.phones:
            if ph.value == phone.value:
                self.phones.remove(ph)


class Field:
    def __init__(self, new_value=None):
        self.__value = new_value

    
    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, new_value):
        self.__value = new_value


class Name(Field):
   # def __init__(self, value):
   #     self.value = value
    pass

class Phone(Field):
    def __init__(self):
        self.__value = None
    
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        norm_phone = normalize_phone(new_value)
        if norm_phone:
            self.__value = norm_phone
        else:
            raise ValueError()    
    

class Birthday(Field):
    def __init__(self):
        self.__value = None 

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if datetime.strptime(new_value, r'%d.%m.%Y'):
            self.__value = new_value
        else:
            raise ValueError()


def add(arguments, address_book):
    
    name = Name(arguments[0])
    record = Record(name)
    for i in range(len(arguments) - 1):
        phone = Phone()
        phone.value = arguments[i+1]
        record.add_phone(phone)
    address_book.add_record(record) 

    output_line = f'Contact {arguments[0]} is added to the address book.'
    return output_line

def add_birthday(arguments, address_book):
    
    birthday = Birthday()
    birthday.value = arguments[1] 
    if address_book.data[arguments[0]].add_birthday(birthday):
        output_line = f'Birthday {arguments[1]} saved in contact {arguments[0]}'
    return output_line

def add_phone(arguments, address_book):

    phone = Phone()
    phone.value = arguments[1]
    output_line = ''
    if address_book.data[arguments[0]].add_phone(phone):
        output_line = f'Phone number {arguments[1]} saved in contact {arguments[0]}'
    return output_line


def change(arguments, address_book):

    if not address_book.data.get(arguments[0]):
        raise ValueError

    phone1 = Phone()
    phone1.value = arguments[1]
    phone2 = Phone()
    phone2.value = arguments[2]
    address_book.data[arguments[0]].edit_phone(phone1, phone2)
    output_line = f'Contact {arguments[0]} changed.'
    return output_line
 

def comand_parser(cli_string):

    comand_list = cli_string.split(' ')
    comand_list = list(filter(lambda x: x, comand_list))
    comand_list[0] = comand_list[0].casefold()
    return tuple(comand_list) 


def delete_phone(arguments, address_book):

    if not address_book.data.get(arguments[0]):
        raise ValueError 
    phone = Phone()
    phone.value = arguments[1]
    address_book.data[arguments[0]].remove_phone(phone)
    output_line = f'Phone number {arguments[1]} removed from contact {arguments[0]}'
    return output_line   


def exit_program(*args):
    return 'exit'


def hello(*args):

    output_line = 'How can I help you?'
    return output_line


def help(*args):

    print(r'** List CLI comands **')
    print('*' * 30)
    print(r'add <name> <phone 1> ... <phone N>   -   Add new record')
    print(r'add birthday <name> <dd.mm.yyyy>   -   Add or change birthday')
    print(r'add phone <name> <phone>   -   Add phone to contact "name"')
    print(r'change <name> <old phone> <new phone>   -   Change contact phone')
    print(r'close   -   Close program')
    print(r'delete phone <name> <phone>   -   Delete contact phone')
    print(r'exit   -   Close program')
    print(r'hello   -  Show "hello" message')
    print(r'good bye   -   Close program')
    print(r'phone   -   Show all contact phone numbers ')
    print(r'show all   -   Print all records')
    print(r'show <N>   -   Print N records')
    return '*' * 30


def phone(arguments, address_book):
    record = address_book.data.get(arguments[0], None)
    if record:
        result = list(map(lambda x: x.value, record.phones))
    else:
        result = 'Wrong name!'
    return result


def show_all(arguments, address_book):

    if len(address_book.data) == 0:
        return 'The address book is empty.'
    else:
        output_list = []
        for key, value in address_book.data.items():
            phones = list(map(lambda x: x.value, value.phones))
            birthday_obj = value.birthday
            birthday = f'{birthday_obj.value} ({value.days_to_birthday()} days to birthday)'  if birthday_obj else ''
            output_list.append(f'{key} {birthday} {phones}') 
    return tuple(output_list)

def show_n(arguments, address_book):

    count = int(arguments[-1])
    output_list = []
    for key, value in address_book:
        phones = list(map(lambda x: x.value, value.phones))
        birthday_obj = value.birthday
        birthday = f'{birthday_obj.value} ({value.days_to_birthday()} days to birthday)'  if birthday_obj else ''
        output_list.append(f'{key} {birthday} {phones}') 
        count -= 1
        if count == 0:
            break
    return tuple(output_list)


OPERATIONS = {
                 
                'add': add,
                'add birthday': add_birthday,
                'add phone': add_phone,
                'change': change,
                'close': exit_program,
                'delete phone': delete_phone,
                'exit': exit_program,
                'hello': hello,
                'help': help,
                'good bye': exit_program,
                'phone': phone,
                'show': show_n,
                'show all': show_all
                
            }

def input_error(func):
    def inner(cli_parse_string, addres_book):
        try:
            return func(cli_parse_string, addres_book)
        except KeyError:
            return 'Unsuported comand or wrong data!'
        except IndexError:
            return 'Incomplated comand!'
        except ValueError:
            return 'Wrong data!'
    return inner

@input_error
def handler(cli_parse_string, address_book):
    
    if len(cli_parse_string) > 1:  
        comand = f'{cli_parse_string[0].lower()} {cli_parse_string[1].lower()}'
        if comand in OPERATIONS:
            arguments = cli_parse_string[2:]
        else:
            comand = cli_parse_string[0]
            arguments = cli_parse_string[1:]
    else:
        comand = cli_parse_string[0]
        arguments = cli_parse_string[1:]
    result = OPERATIONS[comand](arguments, address_book)
    return result


def main():
    address_book = AddressBook()
    hello()
    while True:
        cli_string = input('Enter comand or type "help" to view documentation : ')
        if len(cli_string.strip()) == 0:
            continue
        cli_parse_string = comand_parser(cli_string)
        result = handler(cli_parse_string, address_book)
    
        if result == 'exit':
            break
        else:
            if type(result) is tuple:
                for i in range(len(result)):
                    print(result[i])
            else:
                print(result)
            print('-' * 50)
    input('Bye! Bye!')


if __name__ == "__main__":
    main()