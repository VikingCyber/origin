import datetime

students = {'ivanov': datetime.datetime(2022, 12, 1),
            'sidorov': datetime.datetime(2022, 12, 30),
            'petrov': datetime.datetime(2023, 1, 11),
            'bonchbruevich': datetime.datetime(2022, 11, 29)
            }


def deadline_score(pass_date, deadline_date):
    data = str(pass_date - deadline_date)
    try:
        data_int = int(data[0] + data[1])
    except ValueError:
        data_int = 0
    if pass_date <= deadline_date:
        return 5
    elif 1 <= data_int <= 7:
        return 4
    elif 8 <= data_int <= 14:
        return 3
    elif 14 < data_int < 21:
        return 2
    elif data_int > 21:
        return 0


def late_list(dict_students, deadline_date):
    result_list = []
    for k, v in dict_students.items():
        if v > deadline_date:
            result_list.append(k)
    return result_list


def main():
    while True:
        input_string = input('input valid command:')
        if input_string == 'deadline_score':
            while True:
                try:
                    pass_date = datetime.datetime(int(input('pass_year:')),
                                                  int(input('pass_month:')),int(input('pass_day:')))
                    deadline_date = datetime.datetime((int(input('year_deadline:'))),
                                                      int(input('month_deadline:')), int(input('day_deadline')))
                    break
                except ValueError:
                    print('digits is required')
                    continue
            print(deadline_score(pass_date, deadline_date))
        elif input_string == 'late_list':
            print(sorted(late_list(students, deadline_date)))
        elif input_string == 'exit':
            print('Bye!')
            break


if __name__ == '__main__':
    main()

# changes for fork and commit by origin_m8
