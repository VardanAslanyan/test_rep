import os

folder = os.path.join("/Users/ingenico/Desktop/python/practice_class")

with open(os.path.join(folder, 'combine.txt'), 'w+') as endFile:

    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".txt"):
                f = open(os.path.join(root, file), "r")
                endFile.write(f.read())
                f.close()