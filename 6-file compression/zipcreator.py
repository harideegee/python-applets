import zipfile
import pathlib
import time

def Zip(filepaths, destination):

    """ Creates an archive of the file(s) provided as arguments to 'filepaths' """

    destination_path = pathlib.Path(destination, f"compressed-{time.strftime('%d-%b-%Y-%I-%M-%S-%p')}.zip")
    with zipfile.ZipFile(destination_path, "w") as archive:
        for file in filepaths:
            file = pathlib.Path(file)
            archive.write(file, arcname=file.name)