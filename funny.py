
import os
import time

os.system("tput bold")
os.system("tput setaf 5")
print("\t\t\tFunny Commands")
os.system("tput setaf 4")

while True:
    print("""1. Steam locomotive
2. Figlet
3. Cowsay
4. Factor
5. E-Speak
6. Back to Main Menu""")


    mh = int(input("Enter your Choice:"))
    if mh==1:
        os.system("yum install sl -y")
        time.sleep(1)
        os.system("sl")
        time.sleep(2)
        os.system("sl -f")
        continue
    elif mh==2:
        f_te = input("Enter the Text for Figlet:")
        os.system("figlet -f bubble {}".format(f_te))
        time.sleep(2)
        os.system("figlet -f block {}".format(f_te))
        time.sleep(2)
        os.system("figlet -f digital {}".format(f_te))
        time.sleep(2)
        os.system("figlet -f big {}".format(f_te))
        time.sleep(2)
        os.system("figlet -f lean {}".format(f_te))
        time.sleep(2)
        os.system("figlet -f shadow {}".format(f_te))
        time.sleep(2)
        continue
    elif mh==3:
        cw_text = input("Enter the Cowsay Text:")
        os.system("cowsay {}".format(cw_text))
        time.sleep(2)
        os.system("cowsay -f meow {}".format(cw_text))
        time.sleep(2)
        os.system("cowsay -f surgery {}".format(cw_text))
        time.sleep(2)
        os.system("cowsay -f blowfish {}".format(cw_text))
        time.sleep(2)
        os.system("cowsay -f turkey {}".format(cw_text))
        time.sleep(2)
        os.system("cowsay -f turtle {}".format(cw_text))
        time.sleep(2)
        os.system("cowsay -f cheese {}".format(cw_text))
        time.sleep(2)
        os.system("cowsay -f eyes {}".format(cw_text))
        time.sleep(2)
        continue
    elif mh==4:
        fac_text = input("Enter the Number to get the Factor:")
        os.system("factor {}".format(fac_text))
        time.sleep(2)
        continue
    elif mh==5:
        esp_text = input("Enter the text to Listen:")
        os.system("espeak-ng {}".format(esp_text))
        time.sleep(2)
        continue
    elif mh==6:
        time.sleep(1)
        break
    
