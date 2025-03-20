from datetime import date

from application.db.people import get_employee
from application.salary import calculate_salary

if __name__ == '__main__':
    print(f'Сегодня: {date.today()}')
    calculate_salary('Виктор')
    get_employee('Alex', 26, 8999665441)