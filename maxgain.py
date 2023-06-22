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

# Create variables to store the closest match in current CSV file
frequency = None
decibel = None

while True:
    # Get the list of files in the folder
    files = os.listdir(folder_path)

    # Filter for CSV files
    csv_files = [file for file in files if file.endswith('.csv')]

    if not csv_files:
        print("No CSV files found in the folder, shutting down program")
        # Wait for a specified duration before checking again
        time.sleep(5)  # Adjust the duration as per your requirement
        break
        #continue

    # Find the most recent CSV file
    most_recent_file = max(csv_files, key=lambda x: os.path.getmtime(os.path.join(folder_path, x)))

    # Read the most recent CSV file
    with open(os.path.join(folder_path, most_recent_file), 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        rows = list(csv_reader)

        # Get user input and multiply by 1000000
        user_input = input("Enter frequency (in MHz) (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break

        user_number = float(user_input) * 1000000

        closest_diff = float('inf')
        closest_row = None

        # Find the closest match in the current CSV file
        for row in rows:
            number_str = row[column_number].split(';')[0]  # Extract the frequency
            number = float(number_str) #convert user input as string to float
            diff = abs(user_number - number)
            if diff < closest_diff:
                closest_diff = diff
                closest_row = row

        if closest_row is not None:
            frequency = closest_row[column_number].split(';')[0]
            decibel = closest_row[column_number].split(';')[1]
            #test code, if broke, delete this but converts hz default to mhz
            display_freq_in_MHz = float(frequency) / 1000000
            print(f"The closest frequency in the current CSV file '{most_recent_file}' is: {display_freq_in_MHz} MHz with {decibel} dB")

    high_dB = float(decibel)
    highest_file = None

    # Iterate through the old CSV files
    for old_file in os.listdir(old_folder_path):
        old_file_path = os.path.join(old_folder_path, old_file)
        with open(old_file_path, 'r') as old_csv_file:
            old_csv_reader = csv.reader(old_csv_file, delimiter=',')

            # Find the highest decibel
            for old_row in old_csv_reader:
                old_left = old_row[column_number].split(';')[0]
                old_right = old_row[column_number].split(';')[1]
                if old_left == frequency:
                    old_number = float(old_right)
                    if old_number > high_dB:
                        high_dB = old_number
                        highest_file = old_file

    if highest_file is not None:
        display_freq_in_MHz_2 = float(frequency) / 1000000
        print(f"The highest decibel value among the scanned CSV files is: {display_freq_in_MHz_2} MHz at {high_dB} dB (found in {highest_file})")

    #move file (remove this if doesnt work)
    move_file = input("Do you want to move the current CSV file to the 'old_csv' folder? (y/n): ")
    if move_file.lower() == 'y':
        shutil.move(os.path.join(folder_path, most_recent_file), os.path.join(old_folder_path, most_recent_file))
        print(f"Current CSV file '{most_recent_file}' moved to 'old_csv' folder.")

    # Wait for a specified duration before checking again
    time.sleep(2)  # Adjust the duration as per your requirement
