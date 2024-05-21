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
    user_id = sys.argv[1]
    url = f'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + f'users/{user_id}')

    if (user.status_code == 200):
        user_name = user.json()['username']
        todo = requests.get(url + f'todos?userId={user_id}')

        if todo.status_code == 200:
            todo = todo.json()

            mytodo = []
            for i in range(len(todo)):
                mytodo.append(
                    {
                        "task": todo[i]['title'],
                        "completed": todo[i]['completed'],
                        "username": user_name
                    }
                )

            mydic = {user_id: mytodo}
            with open(f'{user_id}.json', 'w') as file:
                json.dump(mydic, file)
