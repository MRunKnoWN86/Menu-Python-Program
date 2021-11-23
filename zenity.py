import os
import time

os.system("tput bold")
os.system("tput setaf 5")
print("\t\t\tZenity Commands")
os.system("tput setaf 4")

while True:
    print("""1. Zenity-calendar
2. Zenity-entry
3. Zenity-error
4. Zenity-list
5. Zenity-question
6. Zenity-warning
7. Zenity-password
8. Back to main menu""")


    cmd = int(input("Enter your Choice:"))
    if cmd==1:
        day = input("Enter the Day:")
        month = input("Enter the Month:")
        year = int(input("Enter the Year:"))
        os.system("zenity --calendar --day={} --month={} --year={}".format(day,month,year))
        time.sleep(1)
        continue
    elif cmd==2:
        title = input("Enter the Title for Entry:")
        e_text = input("Enter the Text for Entry:")
        os.system("zenity --entry --title={} --text={}".format(title,e_text))
        time.sleep(1)
        continue
    elif cmd==3:
        er_text = input("Enter the Error Text:")
        os.system("zenity --error --text={}|espeak-ng 'ERROR' ".format(er_text))
        time.sleep(1)
        continue
    elif cmd==4:
        os.system("zenity --list --column Serial_number --column Names")
        time.sleep(1)
        continue
    elif cmd==5:
        os.system("zenity --question --text='Is Jalebi is the National sweet of India? --ok-label='Yes' --cancel-label='No'")
        time.sleep(1)
        continue
    elif cmd==6:
        warn_text = input("Enter Warn Text:")
        os.system("zenity --warning --text={} --tittle 'Danger'".format(warn_text))
        time.sleep(1)
        continue
    elif cmd==7:
        os.system("zenity --password --text 'RHEL Root' ")
        time.sleep(1)
        continue
    elif cmd==8:
        time.sleep(1)
        break
