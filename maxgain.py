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

while True:
    # Get the list of files in the folder
    files = os.listdir(folder_path)

    # Filter for CSV files
    csv_files = [file for file in files if file.endswith('.csv')]

    if not csv_files:
        print("No CSV files found in the folder.")
        # Wait for a specified duration before checking again
        time.sleep(60)  # Adjust the duration as per your requirement
        continue

    # Find the most recent CSV file
    most_recent_file = max(csv_files, key=lambda x: os.path.getmtime(os.path.join(folder_path, x)))

    # Read the most recent CSV file
    with open(os.path.join(folder_path, most_recent_file), 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        # Get user input and multiply by 1000000
        user_input = input("Enter a number (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break

        user_number = float(user_input) * 1000000

        closest_diff = float('inf')
        closest_row = None

        # Iterate through the rows and find the closest equivalent number in column 0
        for row in csv_reader:
            number_str = row[column_number].split(';')[0]  # Extract the number to the left of the semicolon
            number = float(number_str)
            diff = abs(user_number - number)
            if diff < closest_diff:
                closest_diff = diff
                closest_row = row

    # Display the numbers to the left and right of the semicolon of the closest equivalent row
    if closest_row is not None:
        left_of_semicolon = closest_row[column_number].split(';')[0]
        right_of_semicolon = closest_row[column_number].split(';')[1]
        print(f"The number to the left of the semicolon of the closest equivalent row is: {left_of_semicolon}")
        print(f"The number to the right of the semicolon of the closest equivalent row is: {right_of_semicolon}")

    # Ask the user if they want to move the CSV file to the old folder
    move_file = input("Do you want to move the CSV file to the 'old_csv' folder? (y/n): ")

    if move_file.lower() == 'y':
        # Move the most recent CSV file to the old folder
        old_file_path = os.path.join(old_folder_path, most_recent_file)
        shutil.move(os.path.join(folder_path, most_recent_file), old_file_path)
        print(f"Moved {most_recent_file} to {old_folder_name} folder.")

    # Wait for a specified duration before checking again
    time.sleep(5)  # Adjust the duration as per your requirement
