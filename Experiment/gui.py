# from idlelib.configdialog import font_sample_text   # unused; safe to remove
import Functions
import FreeSimpleGUI as sg   # or: import PySimpleGUI as sg
import time

sg.theme('TealMono')

clock = sg.Text('', key='clock', font=('Helvetica', 18))
label = sg.Text('Type in new To do')
input_box = sg.InputText(tooltip='Enter New To do', key='todo')
add_button = sg.Button('Add')
list_box = sg.Listbox(values=Functions.get_todos1(),
                      key="todos", enable_events=True, size=(45, 10))
edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete')
exit_button = sg.Button('Exit')

window = sg.Window(
    'My App',
    layout=[
        [clock],
        [label],
        [input_box, add_button],
        [list_box, edit_button, complete_button],
        [exit_button]
    ],
    font=('Helvetica', 20)
)

while True:
    # keep UI responsive and update the clock
    event, values = window.read(timeout=100)
    window['clock'].update(value=time.strftime('%H:%M:%S', time.localtime()))

    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    match event:
        case 'Add':
            todos = Functions.get_todos1()
            new_todo = (values['todo'] or '').strip()
            if new_todo:
                todos.append(new_todo + '\n')  # store with ONE newline
                Functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update('')

        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = (values['todo'] or '').strip()
                if new_todo:
                    todos = Functions.get_todos1()
                    index = todos.index(todo_to_edit)
                    todos[index] = new_todo + '\n'
                    Functions.write_todos(todos)
                    window['todos'].update(values=todos)
            except IndexError:
                sg.popup_error('There is no item selected. Please try again.', font=('Helvetica', 20))

        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = Functions.get_todos1()
                todos.remove(todo_to_complete)
                Functions.write_todos(todos)
                window['todos'].update(values=todos, set_to_index=[])  # clear selection properly
                window['todo'].update('')
            except IndexError:
                sg.popup_error('There is no item selected. Please try again.', font=('Helvetica', 20))

        case 'todos':
            # fill the input with the selected item (strip newline for editing)
            if values['todos']:
                window['todo'].update(value=values['todos'][0].strip())

window.close()
