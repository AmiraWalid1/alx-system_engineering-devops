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
    usr_id = sys.argv[1]
    url = f'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + f'users/{usr_id}')

    if (user.status_code == 200):
        user_name = user.json()['name']
        todo = requests.get(url + f'todos?userId={usr_id}')

        if todo.status_code == 200:
            todo = todo.json()
            done_tasks = 0
            list_done_tasks = []

            for i in range(len(todo)):
                if todo[i]['completed'] is True:
                    done_tasks += 1
                    list_done_tasks.append(todo[i]['title'])
            print(f"Employee {user_name} is done with tasks"
                  + f"({done_tasks}/{len(todo)}):")
            for task in list_done_tasks:
                print(f"\t {task}")
