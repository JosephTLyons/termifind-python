from pathlib import Path


def get_list_of_parent_directories_from_path(path: Path) -> list[Path]:
    parent_directory_paths: list[Path] = [path]
    path = path.resolve()

    while path.parent != path:
        path = path.parent
        parent_directory_paths.insert(0, path)

    return parent_directory_paths
