#!/usr/bin/python3
'''
Python script that, using (https://jsonplaceholder.typicode.com) REST API,
for a given employee ID, returns information about his/her TODO list progress.
'''
import json
import requests
import sys

if __name__ == "__main__":
    ''' main program '''
    arg = sys.argv[1]
    users_url = f'https://jsonplaceholder.typicode.com/users/{arg}'
    response_user = requests.get(users_url)

    if (response_user.status_code == 200):
        user_name = json.loads(response_user.text)['name']
        todo_url = f'https://jsonplaceholder.typicode.com/todos?userId={arg}'
        response_todo = requests.get(todo_url)

        if response_todo.status_code == 200:
            response_todo = json.loads(response_todo.text)
            num_total_tasks = len(response_todo)
            num_done_tasks = 0
            list_done_tasks = []

            for i in range(num_total_tasks):
                if response_todo[i]['completed'] is True:
                    num_done_tasks += 1
                    list_done_tasks.append(response_todo[i]['title'])
            print(f"Employee {user_name} is done with tasks"
                  + f"({num_done_tasks}/{num_total_tasks}):")
            for task in list_done_tasks:
                print(f"\t {task}")
