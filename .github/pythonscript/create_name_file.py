# create_name_file.py

name = "Sumit Kumar"

with open("name-file.txt", "w") as f:
    f.write(f"Your name is {name}\n")
