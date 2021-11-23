import os
import time

os.system("tput setaf 3")
print("\t\t ***********************************")
os.system("tput bold")
os.system("tput setaf 2")
print("\t\t\tWelcome to Main menu")
os.system("tput setaf 3")
print("\t\t ***********************************")

os.system("tput sgr0")
while True:
    os.system("tput setaf 6")
    print(""" 
             \t 1. Explore Zenity
             \t 2. Explore Linux Funny Commands
             \t 3. Date
             \t 4. Calendar
             \t 5. Open Firefox
             \t 6. Fun With Docker
             \t 7. Create your own directory
             \t 8. List of Directory and Launch Jupyter notebook
             \t 9. Exit
              
              
              
              """)
    lw = int(input("Enter your Choice:"))
    if lw == 1:
        os.system("python3 zenity.py")
        time.sleep(2)
        continue
    elif lw == 2:
        os.system("python3 funny.py")
        time.sleep(2)
        continue
    elif lw == 3:
        os.system("date")
        time.sleep(2)
        continue
    elif lw == 4:
        os.system("cal")
        time.sleep(2)
        continue
    elif lw == 5:
        os.system("firefox")
        time.sleep(2)
        continue
    elif lw == 6:
        os.system("python3 docker.py")
        time.sleep(2)
        continue
    elif lw == 7:
        f_name = input("Enter the Directory name:")
        os.system("mkdir {}".format(f_name))
        time.sleep(2)
        continue
    elif lw == 8:
        os.system("ls")
        print("Want to get in the Directory(y/n):")
        lr = input()
        if lr == 'y':
            dir_name = input("Enter Directory name:")
            os.system("cd {}".format(dir_name))
            os.system("ls")
            print("Want to launch Jupyter Notebook(y/n):")
            lx = input()
            if lx == 'y':
                print("""1.Install and Run Jupyter Notebook
2. Run Jupyter Notebook""")
                lz = int(input("Enter your Choice"))
                if lz ==1:
                         os.system("pip3 install jupyter")
                         os.system("jupyter notebook --allow-root")
                elif lz ==2:
                         os.system("jupyter notebook --allow-root")
            if lx == 'n':
                continue
                         
    elif lw == 9:
        break
        
        
os.system("tput bold")
os.system("tput setaf 3")
print("\t\t ***********************************")
os.system("tput bold")
os.system("tput setaf 4")
print("\t\t\t\tThank You")
os.system("tput setaf 3")
print("\t\t ***********************************")
os.system("tput sgr0")
        
        

    


    
    
