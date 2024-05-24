#Currently, the code gives a CSV output where it lists all the files int he root folder and it's subfolders with thier location, filename, date created, file type and file size.
#Output file example: SelfStudy_file_info.xlsx #Please check the main page for it. 

import os
import datetime
import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askdirectory

def get_file_info(root_directory):
    file_data = []
    for dirpath, dirnames, filenames in os.walk(root_directory):
        for file in filenames:
            file_path = os.path.join(dirpath, file)
            file_size = os.path.getsize(file_path)
            creation_time = os.path.getctime(file_path)
            creation_date = datetime.datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d %H:%M:%S')
            file_type = os.path.splitext(file)[1]
            file_data.append((dirpath, file, creation_date, file_type, file_size))
    return file_data

def main():
    # Create a Tkinter root window and hide it
    root = Tk()
    root.withdraw()

    # Ask the user to select the root directory
    root_directory = askdirectory(title="Select the root folder to traverse")
    
    if not root_directory:
        print("No folder selected. Exiting.")
        return

    # Collect file information for the selected root directory and its subdirectories
    file_information = get_file_info(root_directory)

    # Create a pandas DataFrame from the collected file information
    df = pd.DataFrame(file_information, columns=['File Location', 'Filename', 'Date Created', 'File Type', 'Size (Bytes)'])

    # Define the output Excel file name
    output_excel = os.path.join(root_directory, f"{os.path.basename(root_directory)}_file_info.xlsx")

    # Save the DataFrame to an Excel file
    df.to_excel(output_excel, index=False)
    print(f"File information has been saved to {output_excel}")

if __name__ == "__main__":
    main()
