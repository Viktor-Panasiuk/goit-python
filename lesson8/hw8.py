from datetime import datetime, timedelta


def find_users(users, day):
    result_list = []
    for name, birthday in users.items():
        if birthday.date() == day.date():
            result_list.append(name)

    return result_list

def congratulate(users):
    week_days = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday'}
    congratulate_list = {i: list() for i in range(1, 6)}

    today = datetime.now()
    today_isoweekday = today.isoweekday()
    monday_date = today - timedelta(days = today_isoweekday - 1)
    congratulate_list[1] = (find_users(users, monday_date)) #Monday
    congratulate_list[1].extend(find_users(users, monday_date - timedelta(days = 1))) #Sunday
    congratulate_list[1].extend(find_users(users, monday_date - timedelta(days = 2))) #Saturday
    for d in range(2, 6):
        congratulate_list[d] = find_users(users, monday_date + timedelta(days = d - 1)) #Tuesday - Friday

    #print users birthday
    for d, list_user in congratulate_list.items():
        if len(list_user) > 0:
            print(f'{week_days[d]}: ' + ", ".join(list_user))

###########################################################################################

if __name__ == '__main__':
    users = {'Bill': datetime(2021, 2, 21), 
            'Jill': datetime(2021, 2, 20),
            'Kim': datetime(2021, 2, 22),
            'Jan': datetime(2021, 2, 23),
            'Ostap': datetime(2021, 2, 24),
            'Ivan': datetime(2021, 2, 25),
            'Viktor': datetime(2021, 2, 23),
            'Olga': datetime(2021, 2, 26),
            'Kate': datetime(2021, 2, 22),
            'Olena': datetime(2021, 2, 27),
            'Michel': datetime(2021, 2, 28),}

congratulate(users)