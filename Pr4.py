import datetime

students = {'ivanov': datetime.datetime(2022, 12, 1),
            'sidorov': datetime.datetime(2022, 12, 30),
            'petrov': datetime.datetime(2023, 1, 11),
            'bonchbruevich': datetime.datetime(2022, 11, 29)
            }


def deadline_score(pass_date, deadline_date):
    """"
    Функция для оценивания практической работы

    Функция определяет исходя из даты дедлайна и фактической сдачи,
    сколько баллов получит студент за сданную работу.
    Функция принимает на вход два параметра в формате (год, месяц, день)
    в формате модуля datetime.
    1)Дату сдачи работы
    2)Дату дэдлайна работы

    Args:
        pass_date(class 'datetime.datetime')
        deadline_date(class 'datetime.datetime')
    Returns:
        int: оценка за практическую работу
    Examples:
        input valid command:deadline_score
        pass_year:22
        pass_month:12
        pass_day:12
        year_deadline:22
        month_deadline:11
        day_deadline29
        3
    """
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
    elif 14 < data_int <= 21:
        return 2
    elif data_int > 21:
        return 0


def late_list(dict_students, deadline_date):
    """"
    Студенты просрочевшие дедлайн

    Функия определяет сколько студентов из определённого списка
    сдали работу позже намеченного срока

    Args:
        dict_students(dict)
        deadline_date(class 'datetime.datetime')
    Returns:
        list: список с фамилиями студентов, просрочевших дедлайн
    Example:
        input valid command:late_list
        ['bonchbruevich', 'ivanov', 'petrov', 'sidorov']

    """
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
                                                  int(input('pass_month:')), int(input('pass_day:')))
                    deadline_date = datetime.datetime((int(input('year_deadline:'))),
                                                      int(input('month_deadline:')), int(input('day_deadline')))
                    break
                except ValueError:
                    print('digits is required or input format is wrong')
                    continue
            print(deadline_score(pass_date, deadline_date))
        elif input_string == 'late_list':
            print(sorted(late_list(students, deadline_date)))
        elif input_string == 'exit':
            print('Bye!')
            break


if __name__ == '__main__':
    main()


# изменения для защиты