FROM elleflorio/svn-server

RUN apk add --no-cache python py-pip

WORKDIR /home/svn

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

RUN htpasswd -b /etc/subversion/passwd user password

RUN svnadmin create demo && chown -R apache:users demo
