
from collections import UserDict
from os import name
#contacts = {}


class AddressBook(UserDict):
    
    def add_record(self, record):
        self.data[record.name.value] = record


class Record:

    def __init__(self, name):
        self.name = name
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(phone)
    
    def remove_phone(self, phone):
        for ph in self.phones:
            if ph.phone == phone.phone:
                self.phones.remove(ph)

    def edit_phone(self, old_phone, new_phone):
        self.remove_phone(old_phone)
        self.phones.append(new_phone)

class Field:
    pass


class Name(Field):
    def __init__(self, value):
        self.value = value


class Phone(Field):
    def __init__(self, phone):
        self.phone = int(phone)


def add(arguments, address_book):
    
    name = Name(arguments[0])
    record = Record(name)
    for i in range(len(arguments) - 1):
        phone = Phone(int(arguments[i+1]))
        record.add_phone(phone)
    address_book.add_record(record) 

    output_line = f'Contact {arguments[0]} is added to the address book.'
    return output_line
    

def add_phone(arguments, address_book):

    address_book.data[arguments[0]].add_phone(Phone(arguments[1]))
    output_line = f'Phone number {arguments[1]} saved in contact {arguments[0]}'
    return output_line


def change(arguments, address_book):

    if not address_book.data.get(arguments[0]):
        raise ValueError
    address_book.data[arguments[0]].edit_phone(Phone(arguments[1]), Phone(arguments[2]))
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
    address_book.data[arguments[0]].remove_phone(Phone(arguments[1]))
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
    print(r'add phone <name> <phone>   -   Add phone to contact "name"')
    print(r'change <name> <old phone> <new phone>   -   Change contact phone')
    print(r'close   -   Close program')
    print(r'delete phone <name> <phone>   -   Delete contact phone')
    print(r'exit   -   Close program')
    print(r'hello   -  Show "hello" message')
    print(r'good bye   -   Close program')
    print(r'phone   -   Show all contact phone numbers ')
    print(r'show all   -   Print all records')
    return '*' * 30


def phone(arguments, address_book):
    record = address_book.data.get(arguments[0], None)
    if record:
        result = list(map(lambda x: x.phone, record.phones))
    else:
        result = 'Wrong name!'
    return result


def show_all(arguments, address_book):

    if len(address_book.data) == 0:
        output_line = 'The address book is empty.'
    else:
        output_line = ''
        for key, value in address_book.data.items():
            phones = list(map(lambda x: x.phone, value.phones))
            #phones = phones.join(' ')
            output_line += f' {key} {phones} ***' 
    return f'{output_line}'


OPERATIONS = {
                 
                'add': add,
                'add phone': add_phone,
                'change': change,
                'close': exit_program,
                'delete phone': delete_phone,
                'exit': exit_program,
                'hello': hello,
                'help': help,
                'good bye': exit_program,
                'phone': phone,
                'show all': show_all
            }

def input_error(func):
    def inner(cli_parse_string, addres_book):
        try:
            return func(cli_parse_string, addres_book)
        except KeyError:
            return 'Unsuported comand!'
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
    while True:
        cli_string = input('Enter comand or type "help" to view documentation : ')
        if len(cli_string.strip()) == 0:
            continue
        cli_parse_string = comand_parser(cli_string)
        result = handler(cli_parse_string, address_book)
    
        if result == 'exit':
            break
        else:
            print(result)
            print('-' * 50)
    input('Bye! Bye!')


if __name__ == "__main__":
    main()