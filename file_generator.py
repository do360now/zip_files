import yaml
from io import BytesIO
import zipfile
from typing import List

def generate_yaml_data() -> List[dict]:
    data = [
        {"name": "file1", "value": 1},
        {"name": "file2", "value": 2},
        {"name": "file3", "value": 3},
        {"name": "file4", "value": 4}
    ]
    return data

def generate_txt_data() -> str:
    return "This is a sample text file."

def create_files() -> List[tuple]:
    yaml_files = []
    yaml_data = generate_yaml_data()
    
    for i, data in enumerate(yaml_data, start=1):
        yaml_str = yaml.dump(data)
        yaml_buffer = BytesIO(yaml_str.encode('utf-8'))
        yaml_files.append((f"file{i}.yaml", yaml_buffer))

    txt_buffer = BytesIO(generate_txt_data().encode('utf-8'))
    yaml_files.append(("file5.txt", txt_buffer))

    return yaml_files

def create_zip_with_files() -> BytesIO:
    files = create_files()
    zip_buffer = BytesIO()
    
    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zf:
        for filename, file_buffer in files:
            zf.writestr(filename, file_buffer.getvalue())

    zip_buffer.seek(0)
    return zip_buffer
