import shutil
import os

def backup_file(file_path, backup_dir):
    """Backs up the file to the specified backup directory."""
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)  # Create the backup directory if it doesn't exist
    
    # Define the backup file path
    backup_file_path = os.path.join(backup_dir, os.path.basename(file_path))
    
    # Copy the file to the backup directory
    shutil.copy(file_path, backup_file_path)
    print(f"File backed up to {backup_file_path}")
    return backup_file_path

def restore_file(backup_file_path, restore_dir):
    """Restores the file from the backup directory to the restore directory."""
    if not os.path.exists(restore_dir):
        os.makedirs(restore_dir)  # Create the restore directory if it doesn't exist
    
    # Define the restore file path
    restore_file_path = os.path.join(restore_dir, os.path.basename(backup_file_path))
    
    # Copy the file from the backup to the restore directory
    shutil.copy(backup_file_path, restore_file_path)
    print(f"File restored to {restore_file_path}")

def main():
    # Original file path
    original_file = 'data.txt'

    # Ensure the file exists before proceeding
    if not os.path.exists(original_file):
        with open(original_file, 'w') as file:
            file.write("This is some important data.")

    print(f"Original File: {original_file}")
    
    # Define the backup and restore directories
    backup_dir = 'backup'
    restore_dir = 'restored'
    
    # Step 1: Backing up the file
    backup_path = backup_file(original_file, backup_dir)
    
    # Step 2: Simulate file deletion (or corruption)
    os.remove(original_file)
    print(f"\nOriginal file '{original_file}' has been deleted.\n")
    
    # Step 3: Restoring the file from backup
    restore_file(backup_path, restore_dir)

# Run the main function
if __name__ == "__main__":
    main()
