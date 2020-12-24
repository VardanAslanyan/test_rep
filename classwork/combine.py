import os

endFile = open('result.txt', 'w+')

for root, dirs, files in os.walk("/Users/Ingenico/Desktop/test/"):
    for file in files:
        if file.endswith(".txt"):
            f = open(os.path.join(root, file), "r")
            endFile.write(f.read())
            f.close()
endFile.close()