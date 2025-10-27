def get_todos1(filepath='todos.txt'):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()  # Read all lines into a list
    return todos_local


def write_todos(todos_w, filepath='todo.txt'):
    with open('todos.txt', 'w') as file:  # Write all todos back into the file
        file.writelines(todos_w)

