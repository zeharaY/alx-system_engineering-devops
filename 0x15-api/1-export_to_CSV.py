#!/usr/bin/python3
""" Program to Gather data from an API and Export it to CSV """
import csv
import requests
from sys import argv

if __name__ == "__main__":
    """ Entry point """
    empId = argv[1]
    url_todo = 'https://jsonplaceholder.typicode.com/todos'
    url_user = 'https://jsonplaceholder.typicode.com/users'
    payload1 = {'userId': empId}
    payload2 = {'id': empId}

    req_todo = requests.get(url_todo, params=payload1)
    req_user = requests.get(url_user, params=payload2)

    # gathering the NUMBER_OF_DONE_TASKS and total tasks
    total_tasks = req_todo.json()
    
    # gathering Employee name from users
    user_data = req_user.json()
    emp_name = user_data[0].get('username')

    with open('{}.csv'.format(empId), mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',',
                                     quotechar='"', quoting=csv.QUOTE_ALL)
        for task in total_tasks:
            employee_writer.writerow(["{}".format(empId), "{}".format(
                        emp_name), "{}".format(task.get(
                                'completed')), "{}".format(task.get('title'))])
