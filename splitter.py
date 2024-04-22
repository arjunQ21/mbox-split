from os import path
file_size_limit = 220 * 1024 * 1024 # 220 MB max .mbox file size
mbox_file_path = '/Users/arjunq21/Downloads/All mail Including Spam and Trash-002.mbox'  # Change this to your .mbox file path
destination ="splitted-rajendra"

part_no = 0
count = 0
current_email_content = ""
to_save = ""

def append():
    global part_no, count, current_email_content, file_size_limit
    file_save_path = path.join(destination,  f"part_{part_no}.mbox")
    file_size = 0
    if(path.exists(file_save_path)):
        file_size = path.getsize(file_save_path)
    if(file_size + len(current_email_content) > file_size_limit):
        part_no += 1
        append()
        return 
    with open( file_save_path, "a") as file:
        file.write(current_email_content)
        file.close()
    print(f"Appended email #{count} in part:{part_no}")
    current_email_content = ""

with open(mbox_file_path, "r") as file:
    for line in file:
        if(line.startswith("From ")):
            count += 1
            print(f"Processing Email {count}")
            if(len(current_email_content) > 0):
                append()


        current_email_content += line


