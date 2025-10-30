# To learn recommended GLOB,
# To learn recommended CSV,

# Import custom functions from another Python file named 'Functions.py'
from Functions import get_todos1, write_todos

# Import the 'time' module to work with current time
import time

# Get the current date and time formatted as 'Month.Day.Year Hour:Minute:Second'
now = time.strftime("%b.%d.%Y %H:%M:%S")

# Print the current time to the console
print('It is now', now)

# Call the 'get_todos1()' function to fetch the existing todo list
get_todos1()

# Start an infinite loop to keep the program running until the user exits
while True:
    # Ask the user to type a command (add, show, edit, complete, or exit)
    user_action = input("Type add, show, edit or exit or complete: ")

    # Remove any leading or trailing spaces from the user’s input
    user_action = user_action.strip()

    # --- ADD a new todo ---
    # If the user starts with 'add' or uses similar words ('new', 'more')
    if user_action.startswith("add") or 'new' in user_action or 'more' in user_action:
        # Extract the todo text after the word 'add'
        todo = user_action[4:]

        # Retrieve current todos from the file
        todos = get_todos1()

        # Add the new todo item to the list (append newline for file formatting)
        todos.append(todo + '\n')

        # Save the updated todo list back to the file
        write_todos(todos)

    # --- SHOW all todos ---
    # Display all todos if the command starts with 'show'
    elif user_action.startswith("show"):
        # Get the list of todos from file
        todos = get_todos1()

        # Loop through todos and print each with numbering
        for index, item in enumerate(todos):
            # Remove newline character at the end of each todo
            item = item.strip('\n')
            # Capitalize first letters for neat display
            item = item.title()
            # Format the todo with its number
            row = f"{index + 1}. {item}"
            # Print the formatted todo
            print(row)

    # --- COMPLETE a todo ---
    elif user_action.startswith("complete"):
        try:
            # Get the todo number to mark as completed (after 'complete ')
            number = int(user_action[9:])

            # Read todos from the file
            todos = get_todos1()

            # Convert to zero-based index
            index = number - 1
            # Store the todo being removed for message display
            todo_to_remove = todos[index].strip('\n')
            # Remove the selected todo from list
            todos.pop(index)
        except IndexError:
            # Handle error if the number doesn't exist in the list
            print("There is no item with that number please try again::")
            continue

        # Write the updated list back to file
        write_todos(todos)
        # Print confirmation message
        messege = f'Todo {todo_to_remove} was removed from the list. '
        print(messege)

    # --- EDIT an existing todo ---
    elif user_action.startswith("edit"):
        try:
            # Get todo number from the command
            number = int(user_action[5:])
            # Adjust to zero-based index
            number = number - 1

            # Read existing todos
            todos = get_todos1()

            # Ask user for the new todo text
            new_todo = input("Enter new todo: ")
            # Replace old todo with the new one
            todos[number] = new_todo + '\n'
        except ValueError:
            # Handle invalid input (not a number)
            print("Your command is not valid:")
            continue

        # Save the updated list
        write_todos(todos)

    # --- EXIT the program ---
    elif user_action.startswith("exit"):
        # Break the loop to end the program
        break

    # --- INVALID COMMAND ---
    else:
        # Handle unknown commands
        print("Command is not vailid:")

# Print goodbye message after exiting loop
print("Have a good day:")
