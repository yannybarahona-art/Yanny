# with open("source/sample.txt", "r") as file:
#    content = file.read()
#    lines=file.readlines()
#    print(f"Lines: {lines}")
#    first_line=file.readline()
#    print(f"First Line: {first_line}")
# print(content)
with open("source/sample.txt", "a") as file:
    file.write("This is a new line added to the file.\n")
