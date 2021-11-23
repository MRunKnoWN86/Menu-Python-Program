import os
import time 

os.system("tput setab 3")
os.system("tput bold")
print("\t\t\tDOCKER\t\t\t")   #title
os.system("tput sgr0")
os.system("tput setaf 4")
os.system("espeak-ng 'Answer the Question given below'")
while True:
    doc=input("Do you have docker installed in your Linux (y/n):")
    def menu() :
        while True :
            print("""1. Explore the commands in Docker 
2. Do you want to get back to main menu""")         
            io = int(input("Enter your Choice:"))
            while True : 
                if io==1:
                    print("""1. Docker INFO
2. Docker status
3. Pull Image for Your Container 
4. See Docker Images
5. See Docker Containers
6. Remove Docker images
7. Remove All Container
8. Back to menu""")
                if io ==2:
                    break
                io1 = int(input("Enter your Choice:"))
                 
                if io1 == 1:
                    os.system("docker info")
                    continue
                elif io1 == 2:
                    os.system("systemctl status docker")
                    continue
                elif io1 == 3:
                    print("""1. Normal Image
2. Custom Image""")
                    io2 = int(input("Enter your Choice:"))
                    if io2 == 1:
                        print("""1. Centos
2. Ubuntu
3. fedora
4. Debian
5. Alpine""")
                        io3 = int(input("Enter your Choice:"))
                        if io3 == 1:
                            os.system("docker pull centos:latest")
                        elif io3 == 2:
                            os.system("docker pull ubuntu:latest")
                        elif io3 == 3:
                            os.system("docker pull fedora")
                        elif io3 == 4:
                            os.system("docker pull debian")
                        elif io3 == 5:
                            os.system("docker pull alpine")
                    elif io2 == 2:
                        print("""1. Centos
2. Ubuntu""")
                        print("""Note: The Custom image have inbuilt Python, HTTPD server, Gedit Text editor, Ncurse etc""")
                        time.sleep(4)
                        io4 = int(input("Enter your Choice:"))
                        if io4 == 1:
                            os.system("docker build -t myos1:v1 /project")
                            os.system("docker run -it myos1:v1")
                            time.sleep(4)
                        if io4 == 2:
                            os.system("docker build -t rock:v1 /project/df2")
                            os.system("docker run -it myos2:v2")
                            time.sleep(4)
                elif io1 == 4 :
                    os.system("docker images")
                elif io1 == 5 :
                    os.system("docker ps -a")
                elif io1 == 6 :
                    os.system("docker rmi -f $(docker images)")
                elif io1 == 7 :
                    os.system("docker rm -f $(docker images)")
                elif io1 == 8 :
                    break
            break                
        return 
                
                


    if doc =='n':
        os.system("tput bold")
        print("Installing Docker")
        os.system("yum-config-manager --add-repo https://download.docker.com/linux/centos/7/x86_64/stable/docker-ce.repo")
        os.system("yum install docker-ce --nobest -y")
        time.sleep(3)
        menu()
    if doc=='y':
        menu()
    p = input("Exit (y/n):")
    if p=='y':
        break
    elif p=='n':
        continue

    
    
 

                                  

              

    


