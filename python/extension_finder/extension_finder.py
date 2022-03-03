import glob, os

def extension_finder():
    '''
    Extension finder function
    '''
    os.chdir("my_directory")
    
    for file in glob.glob("*.txt"):
        print(file)
        
extension_finder(my_directory)
