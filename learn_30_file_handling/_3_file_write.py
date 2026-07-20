import os 

# Python File Write 

current_path = os.path.dirname(__file__)
file_path = os.path.join(current_path,"_1_demofile.txt")

with open(file_path,"a") as file:
    file.write("Now the file has more content")

with open(file_path) as file:
    print(file.read())

# "a" - Append - will append to the end of the file


print("***")


# Overwrite Existing Content
# To overwrite the existing content to the file, use the w parameter:
with open(file_path,"w") as file:
    file.write("Now the file was overwrite")

with open(file_path) as file:
    print(file.read())


# Create a New File
# To create a new file in Python, use the open() method, with one of the following parameters:

# "x" - Create - will create a file, returns an error if the file exists

# "a" - Append - will create a file if the specified file does not exists

# "w" - Write - will create a file if the specified file does not exists

