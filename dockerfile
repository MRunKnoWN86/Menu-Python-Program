FROM centos

RUN yum install python3 -y

RUN yum install httpd -y

RUN yum install net-tools -y

RUN yum install gedit -y

RUN yum install ncurses -y

ENTRYPOINT [ "date" ] 
