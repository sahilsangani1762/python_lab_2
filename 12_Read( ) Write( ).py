with open("example.txt", "w") as file:
    file.write("Python Language\n")
    file.write("Machine Learning\n")
    file.write("Artificial Intelligence")
with open("example.txt", "r") as file:
    content = file.read()
    print(content)