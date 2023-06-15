import PySimpleGUI as sg
from zip_creator import make_archive

def compress_files():
    label_files = sg.Text("Choose files to compress")
    input_files = sg.Input(key="files_text")
    button_files = sg.FilesBrowse("Choose", key="files")
    label_folder = sg.Text("Choose folder to contain files")
    input_folder = sg.Input(key="folder_text")
    button_folder = sg.FolderBrowse("Choose", key="folder")
    button_home = sg.B("<", key="Back", font=12, size=(3, 0))
    button_compress = sg.Button("Compress")
    output = sg.Text(key="output_compress")

    layout = [[button_home], [label_files], [input_files, button_files],
              [label_folder], [input_folder, button_folder],
              [button_compress, output]]
    return sg.Window("File Compressor", layout, size=(500, 300), resizable=True, finalize=True)


sg.theme("black")
text_select = sg.T("Choose compression type:", font=14, pad=(0, 10))
button_files = sg.Button("Files", key="Files", size=(15, 2), pad=(0, 5))
button_folder = sg.Button("Folders", key="Folder", size=(15, 2), pad=(0, 5))
button_files_folder = sg.Button("Both", key="Both", size=(15, 2), pad=(0, 5))
layout = [
    [sg.VPush()],
    [sg.Push(), text_select, sg.Push()],
    [sg.Push(), button_files, sg.Push()],
    [sg.Push(), button_folder, sg.Push()],
    [sg.Push(), button_files_folder, sg.Push()],
    [sg.VPush(), sg.Sizegrip()]
]

window = sg.Window("File Compressor", layout, size=(500, 300), resizable=True)

while True:
    event, values = window.read()

    if event is None or event == sg.WINDOW_CLOSED:
        break

    if event == "Files":
        window.hide()
        window2 = compress_files()
        back_to_main_window = False
        while True:
            event2, values2 = window2.read()
            if event2 == "Back":
                back_to_main_window = True
                break
            if event2 is None or event2 == sg.WINDOW_CLOSED:
                window.close()
                break
            window2['files_text'].update("")
            window2['folder_text'].update("")
            window2['output_compress'].update("Succesfully!!!")
            file_path = values2['files'].split(";")
            folder_path = values2['folder']
            make_archive(file_path, folder_path)
        window2.close()

    if back_to_main_window:
        back_to_main_window = False
        window.un_hide()

window.close()
