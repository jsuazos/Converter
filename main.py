import PySimpleGUI as sg

layout = [
    [
        sg.Input(key = '-INPUT-'),
        sg.Spin(
            [
                'km a millas', 
                'kgs a libras', 
                'seg a minu'
            ], 
            key = '-UNITS-'), 
        sg.Button('Convertir', key = '-CONVERT-')
    ],
    [
        sg.Text('Output', key = '-OUTPUT-')
    ]
]

window = sg.Window('Converter', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == '-CONVERT-':
        input_value = values['-INPUT-']
        if input_value.isnumeric():
            match values['-UNITS-']:
                case 'km a millas':
                    output = round(float(input_value) * 0.06214, 2)
                    output_string = f'{input_value} kms son {output} en millas'
            
            window['-OUTPUT-'].update(output_string)

window.close()