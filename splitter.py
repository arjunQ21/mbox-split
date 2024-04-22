from os import path
file_size_limit = 190 * 1024 * 1024 # 190 MB (+ Last Email's Size) max .mbox file size in output .mbox files 
mbox_file_path = '/Users/arjunq21/Downloads/All mail Including Spam and Trash-002 (1).mbox'  # Change this to your .mbox file path
destination ="splitted"
part_no = 0
count = 0

def get_file_save_path():
    global part_no, destination
    return path.join(destination, f"new_part_{part_no}.mbox")

current_file = open(get_file_save_path(), "a")

with open(mbox_file_path, "r") as file:
    for line in file:
        if(line.startswith("From ")):
            count += 1
            print(f"Processing Email {count}")
            if(path.getsize(get_file_save_path()) > file_size_limit):
                current_file.close()
                part_no += 1
                current_file = open(get_file_save_path(), "a")
                print(f"Created New File: {get_file_save_path()}")
            
        current_file.write(line)





