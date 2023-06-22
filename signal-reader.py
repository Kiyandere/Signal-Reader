import os
import csv
import time
import shutil

# Get the current working directory
folder_path = os.getcwd()

# Specify the folder name to store old CSV files
old_folder_name = 'old_csv'

# Create the folder to store old CSV files if it doesn't exist
old_folder_path = os.path.join(folder_path, old_folder_name)
os.makedirs(old_folder_path, exist_ok=True)

# Specify the column number to process (starting from 0)
column_number = 0

# Initialize the maximum number and the corresponding row
max_number = float('-inf')
max_row = None

while True:
    # Get the list of files in the folder
    files = os.listdir(folder_path)

    # Filter for CSV files
    csv_files = [file for file in files if file.endswith('.csv')]

    if csv_files:
        # Find the most recent CSV file
        most_recent_file = max(csv_files, key=lambda x: os.path.getmtime(os.path.join(folder_path, x)))

        # Read the most recent CSV file
        with open(os.path.join(folder_path, most_recent_file), 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')

            # Iterate through the rows and find the maximum number in the specified column
            for row in csv_reader:
                number_str = row[column_number].split(';')[1]  # Extract the decibel
                number = float(number_str)
                if number > max_number:
                    max_number = number
                    max_row = row

            # Display the frequency with the highest decibel and that decibel
            if max_row is not None:
                left_of_semicolon = max_row[column_number].split(';')[0]
                print(f"The frequency with the highest decibel is: {left_of_semicolon} Hz")
                print(f"The decibel is: {max_number} dB")

        # Move the most recent CSV file to the old folder
        old_file_path = os.path.join(old_folder_path, most_recent_file)
        shutil.move(os.path.join(folder_path, most_recent_file), old_file_path)
        print(f"Moved {most_recent_file} to {old_folder_name} folder.")

    # Wait for a specified duration before checking again
    time.sleep(10)  # Adjust the duration as per your requirement
