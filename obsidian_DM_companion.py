import os
import json
from PIL import Image

# Define paths
obsidian_vault_path = '.'
attachments_folder = os.path.join(obsidian_vault_path, 'Attachments')
json_path = os.path.join(obsidian_vault_path, 'valid_types.json')

# Define initial valid types
initial_valid_types = ['character', 'item', 'scene', 'banner', 'miscellaneous']

# Load valid types and invalid type mapping from JSON file or create it if it doesn't exist
if not os.path.exists(json_path):
    data = {
        "valid_types": initial_valid_types,
        "type_mapping": {}
    }
    with open(json_path, 'w') as json_file:
        json.dump(data, json_file)
else:
    with open(json_path, 'r') as json_file:
        data = json.load(json_file)

valid_types = data["valid_types"]
type_mapping = data.get("type_mapping", {})

def get_user_choice(invalid_type):
    print(f"Invalid type detected: '{invalid_type}'")
    print("Choose an option:")
    print("1. Add this type to valid types")
    print("2. Create a new type to add valid types")
    print("----------------")
    print("Align to existing types:")
    for i, t in enumerate(valid_types, 3):
        print(f"{i}. Align with '{t}'")

    choice = input("Enter the number of your choice: ")
    return int(choice)

def handle_invalid_type(file_name):
    parts = file_name.split('_')
    if len(parts) < 2:
        return None

    invalid_type = parts[0]
    if invalid_type in type_mapping:
        return type_mapping[invalid_type]

    choice = get_user_choice(invalid_type)

    if choice == 1:
        valid_types.append(invalid_type)
        with open(json_path, 'w') as json_file:
            json.dump({"valid_types": valid_types, "type_mapping": type_mapping}, json_file)
        return invalid_type
    elif choice == 2:
        print("Enter the new type:")
        new_type = input("New type: ").strip().replace(' ', '_')
        valid_types.append(new_type)
        type_mapping[invalid_type] = new_type
        with open(json_path, 'w') as json_file:
            json.dump({"valid_types": valid_types, "type_mapping": type_mapping}, json_file)
        return new_type
    elif 3 <= choice < 3 + len(valid_types):
        aligned_type = valid_types[choice - 3]
        type_mapping[invalid_type] = aligned_type
        with open(json_path, 'w') as json_file:
            json.dump({"valid_types": valid_types, "type_mapping": type_mapping}, json_file)
        return aligned_type
    else:
        print("Invalid choice. Skipping this file.")
        return None

def rename_file(file_name):
    parts = file_name.split('_')
    if len(parts) < 2:
        return None

    file_type = parts[0]
    if file_type not in valid_types:
        file_type = handle_invalid_type(file_name)
        if not file_type:
            return None

    name_parts = parts[1:]
    name_parts = [part.replace(' ', '_') for part in name_parts]
    new_name = '_'.join([file_type] + name_parts)
    if 'token' in new_name:
        new_name = new_name.replace('.png', '_token.png')
    return new_name

def get_unique_file_name(file_path):
    base, ext = os.path.splitext(file_path)
    counter = 1
    new_file_path = file_path
    while os.path.exists(new_file_path):
        new_file_path = f"{base}_{counter}{ext}"
        counter += 1
    return new_file_path

def convert_to_webp(file_path):
    webp_path = os.path.splitext(file_path)[0] + '.webp'
    with Image.open(file_path) as img:
        img.save(webp_path, 'webp')
    return webp_path

def organize_files():
    for file_name in os.listdir(attachments_folder):
        file_path = os.path.join(attachments_folder, file_name)
        if os.path.isfile(file_path):
            # Rename files
            new_name = rename_file(file_name)
            if new_name:
                new_path = os.path.join(attachments_folder, new_name)
                if file_path != new_path:  # Check if renaming is actually needed
                    if os.path.exists(new_path):
                        new_path = get_unique_file_name(new_path)
                    os.rename(file_path, new_path)
                    file_path = new_path
            
            # Convert to .webp
            if file_path.endswith(('.png', '.jpeg', '.jpg')):
                webp_path = convert_to_webp(file_path)
                os.remove(file_path)  # Remove original file after conversion

if __name__ == "__main__":
    organize_files()
