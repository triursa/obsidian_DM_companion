# Obsidian DM Companion

A Python script to help organize and convert image files in your Obsidian vault's "Attachments" folder. This script renames files to ensure they follow a specific naming convention, converts image files to `.webp` format, and updates a JSON file to maintain a list of valid types and their mappings.

## Features

- **File Renaming**: Ensures files follow the `(type)_(name).extension` naming convention.
- **Type Validation**: Prompts for action when an invalid type is detected.
- **Image Conversion**: Converts `.png`, `.jpeg`, and `.jpg` files to `.webp` format.
- **Conflict Resolution**: Automatically handles file name conflicts by appending unique identifiers.
- **Persistent Type Management**: Saves new types and mappings to a JSON file for future use.

## Setup Instructions

### Prerequisites

- Python 3.x
- pip (Python package installer)
- Pillow (Python Imaging Library)

### Installation

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/triursa/obsidian_dm_companion.git
   cd obsidian_dm_companion
2. **Install Required Libraries**
   ```sh 
   sudo apt update
   sudo apt install python3-pip python3-distutils
   python3 -m pip install Pillow
3. Create the Attachments Folder (if not existing):
   ```sh 
   mkdir -p Attachments

### Usage

1. Place Your Images:
- Ensure all your images are in the Attachments folder.
2. Run the Script:
   ```sh
   python3 obsidian_dm_companion.py

##### Follow the Prompts:

If an invalid type is detected, follow the on-screen prompts to either add a new type, align with an existing type, or create a new type.

### How It Works

Loading Valid Types:

- The script loads valid types and mappings from valid_types.json. If the file doesn't exist, it creates it with default types.

Renaming Files:

- Files are renamed to follow the format (type)_(name).extension. Spaces are replaced with underscores.

Handling Invalid Types:

- If a file has an invalid type, the script prompts the user to decide how to handle it. The user's choice is saved to `valid_types.json`.

Converting to .webp:
- The script converts `.png`, `.jpeg`, and `.jpg` files to `.webp` format and deletes the original files.

Conflict Resolution:
- If a file with the new name already exists, the script appends a unique identifier to the file name to avoid conflicts.

### Example

#### Initial Folder Structure

Attachments/
|── character_John.png
|── item_Sword.png
|── misc_Lake.jpeg

#### After Running the Script

Attachments/
|── character_John.webp
|── item_Sword.webp
|── miscellaneous_Lake.webp