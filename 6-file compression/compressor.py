import PySimpleGUI as gui
import zipcreator

gui.theme("Black")

label1 = gui.Text("Select the files to compress:")
input1 = gui.Input()
button1 = gui.FilesBrowse("Choose", key="files")

label2 = gui.Text("Select the destination folder: ")
input2 = gui.Input()
button2 = gui.FolderBrowse("Choose", key="folder")

compress = gui.Button("Compress")
label3 = gui.Text(key="message", text_color="green")


window = gui.Window("File Compression Tool", 
                    layout=[[label1, input1, button1], 
                            [label2, input2, button2],
                            [compress, label3]])

while True:
    action, value = window.read()
    if action == gui.WIN_CLOSED:
        break
    else:
        filepaths = value["files"].split(";")
        folder = value["folder"]
        zipcreator.Zip(filepaths, folder)
        window["message"].update(value="Compression was successful!")
window.close()