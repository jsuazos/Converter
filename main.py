import PySimpleGUI as sg

layout = [
    [sg.Text('Text', enable_events = True, key = '-TEXT-'), sg.Spin(['Item 1', 'Item 2'])],
    [sg.Button('Button', key = '-BUTTON1-')],
    [sg.Input()],
    [sg.Text('Test'), sg.Button('Test Button', key = '-BUTTON2-')]
]

window = sg.Window('Converter', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    if event == '-BUTTON1-':
        print('button pressed')
    if event == '-BUTTON2-':
        print('something else')
    if event == '-TEXT-':
        print('text was pressed')

    print(event)

window.close()