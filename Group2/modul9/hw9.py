
contacts = {}

def add(cli_parse_string, contacts):
    
    contacts[cli_parse_string[1]] = int(cli_parse_string[2])
    output_line = f'Contact {cli_parse_string[1]} is added to the address book.'
    return output_line


def change(cli_parse_string, contacts):

    if not contacts.get(cli_parse_string[1]):
        raise ValueError
    contacts[cli_parse_string[1]] = int(cli_parse_string[2])
    output_line = f'Contact {cli_parse_string[1]} changed.'
    return output_line


def comand_parser(cli_string):

    comand_list = cli_string.split(' ')
    comand_list = list(filter(lambda x: x, comand_list))
    comand_list[0] = comand_list[0].casefold()
    return tuple(comand_list) 


def exit_program(*args):
    return 'exit'


def hello(*args):

    output_line = 'How can I help you?'
    return output_line


def phone(cli_parse_string, contacts):
    return contacts.get(cli_parse_string[1], 'Wrong name!')


def show_all(cli_parse_string, contacts):

    output_line = ''
    for key, value in contacts.items():
        output_line += f'/{key} {value}/   '
    if len(contacts) == 0:
        output_line = 'The address book is empty.'
    return output_line


OPERATIONS = {
                 
                'add': add,
                'change': change,
                'good bye': exit_program,
                'close': exit_program,
                'exit': exit_program,
                'hello': hello,
                'phone': phone,
                'show all': show_all
            }

def input_error(func):
    def inner(cli_parse_string, contacts):
        try:
            return func(cli_parse_string, contacts)
        except KeyError:
            return 'Unsuported comand!'
        except IndexError:
            return 'Incomplated comand!'
        except ValueError:
            return 'Wrong data!'
    return inner

@input_error
def handler(cli_parse_string, contacts):
    
    if cli_parse_string[0] == 'good' and cli_parse_string[1] == 'bye':
        result = OPERATIONS['good bye'](cli_parse_string, contacts)
    elif cli_parse_string[0] == 'show' and cli_parse_string[1] == 'all':
        result = OPERATIONS['show all'](cli_parse_string, contacts)
    else:
        result = OPERATIONS[cli_parse_string[0]](cli_parse_string, contacts)
    return result


def main():
    while True:
        cli_string = input('Enter comand: ')
        if len(cli_string.strip()) == 0:
            continue
        cli_parse_string = comand_parser(cli_string)
        result = handler(cli_parse_string, contacts)
    
        if result == 'exit':
            break
        else:
            print(result)
            print('-' * 50)
    input('Bye! Bye!')


if __name__ == "__main__":
    main()