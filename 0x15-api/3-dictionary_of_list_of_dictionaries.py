#!/usr/bin/python3
'''
Python script that, using (https://jsonplaceholder.typicode.com) REST API,
for all employee ID, returns information about his/her TODO list progress.
'''
import json
import requests
import sys

if __name__ == "__main__":
    ''' main program '''
    url = f'https://jsonplaceholder.typicode.com/'
    users = requests.get(url + 'users/')

    if (users.status_code == 200):
        mydic = {}
        users = users.json()
        for user in users:
            user_name = user['username']
            user_id = user['id']

            todo = requests.get(url + f'todos?userId={user_id}')

            if todo.status_code == 200:
                todo = todo.json()

                mytodo = []
                for i in range(len(todo)):
                    mytodo.append(
                        {
                            "username": user_name,
                            "task": todo[i]['title'],
                            "completed": todo[i]['completed']
                        }
                    )

                mydic[user_id] = mytodo

        with open('todo_all_employees.json', 'w') as file:
            json.dump(mydic, file)
