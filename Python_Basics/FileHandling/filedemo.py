# File I/O
# 'w' - write mode
# 'r' - read mode
# 'r+' - read and write mode
# 'a' - append mode
# 'x' - create mode (creates a new file, returns an error if the file already exists)
# 'b' - binary mode
# 't' - text mode (default)

my_list = ["Ishtar", "Nergal", "Ereshkigal", "Tiamat", "Marduk"]
my_file = open("Basics/FileHandling/my_file.txt", "w")  # Open the file in write mode

for item in my_list:
    my_file.write(str(item) + "\n")  # Write each item to the file followed by a newline
my_file.close()  # Close the file after writing

my_file = open("Basics/FileHandling/my_file.txt", "r")  # Open the file in read mode
content = my_file.read()  # Read the entire content of the file
print(content) 
my_file.close()  # Close the file after reading

my_file = open("Basics/FileHandling/my_file.txt", "r")
print(my_file.readline())  # Read the first line of the file
print(my_file.readline())  # Read the second line of the file
my_file.close()

my_file = open("Basics/FileHandling/my_file.txt", "a")  # Open the file in append mode
my_file.write("Nabu\n")  # Append a new line to the file 
my_file.close()

my_file = open("Basics/FileHandling/my_file.txt", "r+") # Open the file in read and write mode
my_file.write("Enki\n")  # Write a new line to the file at the beginning (overwriting the first line)
my_file.seek(0)  # Move the file pointer back to the beginning of the file
content = my_file.read()  # Read the entire content of the file
print(content)
my_file.close()

my_file = open("Basics/FileHandling/my_new_file.txt", "x")# Open the file in create mode (will raise an error if the file already exists)
my_file.write("This is a new file created in create mode.\n")
my_file.close()

# with / as keywords
with open("Basics/FileHandling/my_file.txt", "r") as my_file:
    content = my_file.read()
    print(content)