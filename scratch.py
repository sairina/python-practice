import json
import requests

''' All from realpython.com/python-json/'''

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)
# json.loads turns the response into a dictionary

todos == response.json()

''' MANIPULATE JSON DATA AS NORMAL PYTHON OBJECT '''

# map of userId to number of complete TODOs for that user
todos_by_user = {}

# get a list of completed todos for each user
for todo in todos:
    if todo['completed']:
        try:
            todos_by_user[todo['userId']] += 1
        except KeyError:
            todos_by_user[todo['userId']] = 1

# create a SORTED list of pairs with .items() for (userId, num_complete)
top_users = sorted(todos_by_user.items(),
                   key=lambda x: x[1], reverse=True)

# get the maximum number of completed todos
max_complete = top_users[0][1]

# create a list of all users who have completed the maximum number
# of todos

users = []
for user, num_complete in top_users:
    if num_complete < max_complete:
        break
    users.append(str(user))

max_users = " and ".join(users)

s = "s" if len(users) > 1 else ""
print(f"user{s} {max_users} completed {max_complete} TODOS")
# users 5 and 10 completed 12 TODOs

'''CREATE A JSON FILE THAT CONTAINS THE COMPLETED TODOS for 
each of the users who completed the maximum number of TODOs'''

# define a function to filter out completed TODOs
# of users with max completed TODOs


def keep(todo):
    is_complete = todo['completed']
    has_max_count = str(todo['userId']) in users
    return is_complete and has_max_count


# write filtered todos to file
with open('filtered_data_file', 'w') as data_file:
    filtered_todos = list(filter(keep, todos))
    json.dump(filtered_todos, data_file, indent=2)
