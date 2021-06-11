from datetime import datetime, timedelta


def find_users(users, day):
    result_list = []
    for user in users:
        if user['birthday'].date() == day.date():
            result_list.append(user['name'])

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
    for day, list_user in congratulate_list.items():
        print(f'{week_days[day]}: ' + ", ".join(list_user))

###########################################################################################

if __name__ == '__main__':
    users = [{'name':'Bill', 'birthday':datetime(2021, 6, 1)}, 
            {'name':'Jill', 'birthday': datetime(2021, 6, 5)},
            {'name':'Kim', 'birthday': datetime(2021, 6, 2)},
            {'name':'Jan', 'birthday': datetime(2021, 6, 3)},
            {'name':'Ostap', 'birthday': datetime(2021, 6, 4)},
            {'name':'Ivan', 'birthday': datetime(2021, 6, 5)},
            {'name':'Viktor', 'birthday': datetime(2021, 6, 3)},
            {'name':'Olga', 'birthday': datetime(2021, 6, 6)},
            {'name':'Kate', 'birthday': datetime(2021, 6, 2)},
            {'name':'Olena', 'birthday': datetime(2021, 6, 7)},
            {'name':'Michel', 'birthday': datetime(2021, 6, 8),}]

congratulate(users)
