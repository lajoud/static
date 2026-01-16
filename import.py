import shutil


def export_data(origin, destination):
    
    shutil.copytree(
        "/source",
        "/dest",
        dirs_exist_ok=True,
        copy_function=shutil.copy2  # preserves metadata like cp -a
    )
        