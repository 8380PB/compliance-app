import os
import datetime

def extract_metadata(file):
    content = file.file.read()
    size_kb = round(len(content) / 1024, 2)
    file.file.seek(0)

    return {
        "filename": file.filename,
        "file_size_kb": size_kb,
        "uploaded_at": datetime.datetime.utcnow().isoformat(),
        "file_extension": os.path.splitext(file.filename)[1]
    }