import FreeSimpleGUI as sg
from ZIP import make_archive
label1 = sg.Text('Select where to compress:')
input1 = sg.Input()
button1 = sg.FileBrowse('Browse', key='files' )


label2 = sg.Text('Select where to save file:')
input2 = sg.Input()
button2 = sg.FolderBrowse('Browse', key='folder')

button3 = sg.Button('Compress')

window = sg.Window('File Compressor ',
                   layout=[[label1, input1, button1],
                          [label2, input2, button2,
                           button3]])


while True:

    event, values = window.read()
    print(event, values)
    filepaths = values['files'].split(';')
    folder = values['folder']
    make_archive(filepaths, folder)

windows.close()
