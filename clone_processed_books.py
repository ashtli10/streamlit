"""
Script to clone the contents of 'processed_books' into the root of this project, overwriting existing files/directories.

Usage:
    python clone_processed_books.py

Requirements:
    - Python 3.7+
    - No external dependencies (uses standard library only)

# Reason: Automates copying/overwriting processed_books for data pipeline setup.
"""
import shutil
import os
from pathlib import Path

from typing import Union

def clone_processed_books(
    source_dir: Union[str, Path], dest_dir: Union[str, Path]
) -> None:
    """
    Copy all contents from source_dir to dest_dir, overwriting existing files/directories.

    Args:
        source_dir (Union[str, Path]): Source directory to copy from.
        dest_dir (Union[str, Path]): Destination directory to copy to.

    Returns:
        None
    """
    source = Path(source_dir)
    dest = Path(dest_dir)
    if not source.exists() or not source.is_dir():
        raise FileNotFoundError(f"Source directory does not exist: {source}")

    dest.mkdir(parents=True, exist_ok=True)  # Ensure destination exists
    for item in source.iterdir():
        dest_item = dest / item.name
        if item.is_dir():
            if dest_item.exists():
                shutil.rmtree(dest_item)
            shutil.copytree(item, dest_item)
        else:
            if dest_item.exists():
                dest_item.unlink()
            shutil.copy2(item, dest_item)

if __name__ == "__main__":
    SOURCE = r"C:\Users\Ariel\Documents\GitHub\books-to-txt\processed_books"
    DEST = Path(__file__).parent.resolve() / "processed_books"
    clone_processed_books(SOURCE, DEST)
    print(f"Cloned '{SOURCE}' to '{DEST}' (overwriting existing files/directories).")
