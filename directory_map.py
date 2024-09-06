import os


def generate_directory_map(root_dir, indent_level=0, exclude_dirs=None, exclude_files=None):
    """
    Recursively generates a map of the directory structure starting from root_dir,
    excluding specified directories and files.

    Args:
        root_dir (str): The root directory to start mapping from.
        indent_level (int): The current indentation level (used for recursion).
        exclude_dirs (list): List of directories to exclude.
        exclude_files (list): List of files to exclude.

    Returns:
        None
    """
    if exclude_dirs is None:
        # Exclude common directories that should not appear in the structure
        exclude_dirs = ['.venv', '.idea', '__pycache__', '.git', 'logs', 'refs', 'hooks', 'branches']
    if exclude_files is None:
        # Exclude common file types that should not appear in the structure
        exclude_files = ['.pyc', '.iml', 'COMMIT_EDITMSG', 'config', 'index', 'packed-refs']

    try:
        # List all items in the directory
        items = os.listdir(root_dir)

        # Loop through each item in the directory
        for item in items:
            item_path = os.path.join(root_dir, item)

            # Skip excluded directories
            if os.path.isdir(item_path) and item in exclude_dirs:
                continue

            # Skip excluded files
            if any(item.endswith(ext) for ext in exclude_files):
                continue

            # Print the item with indentation
            print("    " * indent_level + "|-- " + item)

            # If the item is a directory, recurse into it
            if os.path.isdir(item_path):
                generate_directory_map(item_path, indent_level + 1, exclude_dirs, exclude_files)

    except Exception as e:
        print(f"Error reading directory {root_dir}: {e}")


if __name__ == "__main__":
    # Specify the root directory to start mapping from
    root_directory = "/home/blacktooth/Projects/Warehouse Info Screens/Old"  # Replace with your directory
    print(f"Directory structure of '{root_directory}':\n")
    generate_directory_map(root_directory)