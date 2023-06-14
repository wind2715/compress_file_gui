import PySimpleGUI as gui
from zip_creator import make_archive

label_files = gui.Text("Choose files to compress")
input_files = gui.Input(key="files_text")
button_files = gui.FilesBrowse("Choose", key="files")

label_folder = gui.Text("Choose folder to contain files")
input_folder = gui.Input(key="folder_text")
button_folder = gui.FolderBrowse("Choose", key="folder")

button_compress = gui.Button("Compress")

output = gui.Text(key="output_compress")

window = gui.Window("File Compressor",
                    layout=[[label_files], [input_files, button_files],
                            [label_folder], [input_folder, button_folder],
                            [button_compress, output]])

while True:
    event, values = window.read()
    print(event)
    print(values)

    if event is None:
        break

    window['files_text'].update(value="")
    window['folder_text'].update(value="")
    window['output_compress'].update(value="Succesfull")

    file_path = values['files'].split(";")
    folder_path = values['folder']
    make_archive(file_path, folder_path)
window.close()
