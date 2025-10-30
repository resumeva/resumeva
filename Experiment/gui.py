import Functions
import FreeSimpleGUI as sg


label = sg.Text('Type in new To do')
inout_box = sg.InputText(tooltip='Enter New To do')
add_button = sg.Button('Add')

window = sg.Window('My App', layout = [[label], [inout_box], [add_button]])
window.read()
window.close() 