import os

def batch_rename(directory, prefix):
    """ Rename all files in the given directory by adding a prefix. """
    for filename in os.listdir(directory):
        old_file = os.path.join(directory, filename)
        new_file = os.path.join(directory, prefix + filename)
        os.rename(old_file, new_file)
        print(f"Renamed {old_file} to {new_file}")

directory = input("Enter the directory path: ")
prefix = input("Enter the prefix to add: ")
batch_rename(directory, prefix)

