import FreeSimpleGUI as sg

label1 = sg.Text('Select file to compress:')
input1 = sg.Input()
button1 = sg.FileBrowse('Browse')


label2 = sg.Text('Select where to save the compressed file:')
input2 = sg.Input()
button2 = sg.FolderBrowse('Browse')

button3 = sg.Button('Compress')

window = sg.Window('File Compressor ',
                   layout=[[label1, input1, button1],
                           [label2, input2, button2,
                           button3]])
window.read()
window.close()
