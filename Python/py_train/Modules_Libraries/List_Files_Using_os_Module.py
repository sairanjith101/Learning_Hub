import os

def list_files(path: str) -> list[str]:
    return sorted(
        [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    )
