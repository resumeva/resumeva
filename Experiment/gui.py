import Functions
import FreeSimpleGUI as sg


label = sg.Text('Type in new To do')
inout_box = sg.InputText(tooltip='Enter New To do', key='-IN-')
add_button = sg.Button('Add')

window = sg.Window('My App',
                   layout = [[label], [inout_box, add_button]],
                   font = ('Helvetica', 20))
while True:
    event, values = window.read()
    print(event, values)
    window.read()
    window.close()
    match event:
        case 'Add':
            tolist = Functions.get_todos1()
            new_todo = values['-IN-'] + '\n'
            tolist.append(new_todo + '\n')
            Functions.write_todos(tolist)
        case sg.WIN_CLOSED:
            break




window.close()
