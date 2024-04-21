from os import path

file_size_limit = 1 * 1024 * 1024 # 1 MB max .mbox file size
mbox_file_path = 'All mail Including Spam and Trash.mbox'  # Change this to your .mbox file path
destination ="splitted"

count = 0
part_no = 0
current_file_content = ""
current_email_content = ""
to_save = ""

def save():
    global part_no, current_file_content
    with open( path.join(destination,  f"part_{part_no}.mbox"), "w") as file:
        file.write(current_file_content)
        file.close()
    print(f"Saved part {part_no}")
    part_no += 1
    current_file_content = ""

with open(mbox_file_path, "r") as file:
    for line in file:
        if(line.startswith("From ")):
            count += 1
            print(f"Processing Email {count}")
            if(len(current_email_content) > 0):
                if(len(current_email_content) + len(current_file_content) > file_size_limit):
                    save()
                else:
                    current_file_content += "\n" + current_email_content
                    current_email_content = ""


        current_email_content += line

current_file_content += "\n" + current_email_content
current_email_content = ""
save()


