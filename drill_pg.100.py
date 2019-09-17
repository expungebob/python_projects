



import os


for file in os.listdir("C:\python_projects"):
    if file.endswith(".txt"):
        prop = os.path.getmtime(file)
        join = os.path.join("C:\python_projects", file)
        print(join,prop)












