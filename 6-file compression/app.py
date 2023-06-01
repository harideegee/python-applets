import PySimpleGUI as gui

label1 = gui.Text("Select the files to compress:")
input1 = gui.Input()
button1 = gui.FilesBrowse("Choose")

label2 = gui.Text("Select the destination folder: ")
input2 = gui.Input()
button2 = gui.FolderBrowse("Choose")

compress = gui.Button("Compress")


window = gui.Window("File Compression Tool", 
                    layout=[[label1, input1, button1], 
                            [label2, input2, button2],
                            [compress]])

window.read()
window.close()