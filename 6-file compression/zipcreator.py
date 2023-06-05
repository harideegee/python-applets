import zipfile
import pathlib

def Zip(filepaths, destination):

    """ Creates an archive of the file(s) provided as arguments to 'filepaths' """

    if len(filepaths) == 1:
        destination_path = pathlib.Path(destination, "compressed_file.zip")
    else:
        destination_path = pathlib.Path(destination, "compressed_files.zip")
    
    with zipfile.ZipFile(destination_path, "w") as archive:
        for file in filepaths:
            file = pathlib.Path(file)
            archive.write(file, arcname=file.name)