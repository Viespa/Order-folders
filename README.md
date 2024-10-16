
# Automatic File Organizer

This project is a Python script that automatically organizes files in a specified folder, categorizing them by type (images, documents, videos, etc.) and moving them to corresponding subfolders. It's ideal for keeping your Downloads or Desktop folder clean and organized.



## Features

- Categorizes files into folders such as Images, Documents, Videos, Compressed, and Others.
- Automatically creates the necessary folders if they don't exist.
- Easy to customize to support new file types.
- Option to automate the organization at regular intervals using schedule (optional).

## Requirements

- Python 3.x
- Standard Python libraries:
  - os
  - shutil
  - pathlib

If you want to automate the script to run periodically, install the schedule library:


```bash
  pip install schedule
```


## Installation

- Clone this repository or download the files.
- Open a terminal in the folder where the organizer_files.py script is located.
- Make sure you have Python 3 installed by running python --version or python3 --version - in your terminal.
## Usage
1. Run the script with the following command:

```bash
python organizer_files.py
```

2. Enter the path of the folder you want to organize when prompted. Examples:

- On Windows: C:/Users/YourUser/Downloads
- On Linux/macOS: /home/user/Downloads

3. The script will automatically classify the files into the following subfolders:

- Images (.jpg, .png, .gif)
- Documents (.pdf, .docx, .txt)
- Videos (.mp4, .avi)
- Compressed (.zip, .rar)
- Others (for files that don't match the above categories)