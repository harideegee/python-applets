import PySimpleGUI as gui
import zipextractor

gui.theme("Black")

label1 = gui.Text("Select the archive to extract:")
input1 = gui.Input()
button1 = gui.FileBrowse("Choose", key="archive")

label2 = gui.Text("Select the destination folder: ")
input2 = gui.Input()
button2 = gui.FolderBrowse("Choose", key="folder")

compress = gui.Button("Extract")
label3 = gui.Text(key="message", text_color="green")

window = gui.Window("Archive Extractor Tool", 
                    layout=[[label1, input1, button1], 
                            [label2, input2, button2],
                            [compress, label3]])

while True:
    action, value = window.read()
    if action == gui.WIN_CLOSED:
        break
    else:
        archive_path = value["archive"]
        folder = value["folder"]
        zipextractor.Unzip(archive_path, folder)
        window["message"].update(value="Extraction was successful!")
window.close()