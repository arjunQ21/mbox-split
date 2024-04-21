from os import path

file_size_limit = 220 * 1024 * 1024 # 1 MB max .mbox file size
mbox_file_path = '/Users/arjunq21/Downloads/Takeout-acc/Mail/All mail Including Spam and Trash.mbox'  # Change this to your .mbox file path
destination ="splitted"

part_no = 0
count = 0
current_file_content = ""
len_current_file_content = 0 
current_email_content = ""
len_current_email_content = 0
to_save = ""

def save():
    global part_no, current_file_content, len_current_file_content
    with open( path.join(destination,  f"part_{part_no}.mbox"), "w") as file:
        file.write(current_file_content)
        file.close()
    print(f"Saved part {part_no}")
    part_no += 1
    current_file_content = ""
    len_current_file_content = 0

with open(mbox_file_path, "r") as file:
    for line in file:
        if(line.startswith("From ")):
            count += 1
            print(f"Processing Email {count}")
            if(len_current_email_content > 0):
                if(len_current_email_content + len_current_file_content > file_size_limit):
                    save()
                else:
                    current_file_content += "\n" + current_email_content
                    len_current_file_content += len("\n" + current_email_content)
                    current_email_content = ""
                    len_current_email_content = 0


        current_email_content += line
        len_current_email_content += len(line)

current_file_content += "\n" + current_email_content
current_email_content = ""
save()


