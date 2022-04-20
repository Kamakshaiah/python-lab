import PySimpleGUI as sg
 
# Create some elements
layout = [[sg.Text("What's your name?"), sg.InputText()],
          [sg.Button('OK'), sg.Button('Cancel')]]
 
# Create the Window
window = sg.Window('Hello PySimpleGUI', layout)
 
# Create the event loop
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        # User closed the Window or hit the Cancel button
        break
    print(f'Event: {event}')
    print(str(values))
 
window.close()
