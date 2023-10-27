import os


async def check_exist(file_path: str):
    if os.path.exists(file_path):
        return True
    else:
        return False
