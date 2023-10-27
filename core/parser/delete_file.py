import os


async def delete_file(file_path: str):
    if os.path.exists(file_path):
        os.remove(file_path)
        return True
    else:
        return False
