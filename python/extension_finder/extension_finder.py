import glob, os

os.chdir("my_directory")

for file in glob.glob("*.txt"):
    print(file)
