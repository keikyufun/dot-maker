# dot-maker
A simple tool that generates PNG images from CSV numeric data, a color list, and a configuration file.

## File Structure
To use this tool, place the following three files in a folder:

### 1. config.txt
Specifies the size of one cell in pixels.
- Example: 10 (Each number becomes a 10x10 pixel square)

### 2. colors.txt
Lists color codes (Hex) line by line. Each line corresponds to the number in the CSV.
- 1st line: Color for "1"
- 2nd line: Color for "2"
- ...and so on.
- **Note:** "0" is always reserved for transparency.

### 3. data.csv
The "blueprint" of your image using comma-separated numbers.
- Example:
  0,1,0
  1,2,1
  0,1,0

## Requirements
Python 3.x and Pillow (PIL)
Install via: `pip install Pillow`

## Usage
Run the script by passing the folder name as an argument:

python convert.py [your_folder_name]

The tool will generate an output.png inside the specified folder.