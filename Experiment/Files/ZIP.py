import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir)
    with zipfile.ZipFile(dest_path, mode='w') as archive:
        filepaths = [str(pathlib.Path(filepath).resolve()) for filepath in filepaths]
        for filepath in filepaths:archive
            archive.write(filepath, arcname=filepath)

if __name__ == '__main__':
    make_archive(filepaths=['main.py', 'gui.py'], dest_dir='dest')
