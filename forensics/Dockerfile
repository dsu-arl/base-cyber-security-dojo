FROM ubuntu

USER root
RUN apt update
RUN apt install python3.12 -y
RUN apt update && apt install -y \
    steghide

RUN apt install -y zip

RUN apt install -y exiftool binwalk

# Add exec-suid to the image (important for Python challenges to be able to read the flag):
ADD --chown=0:0 http://github.com/pwncollege/exec-suid/releases/latest/download/exec-suid /usr/bin/exec-suid
RUN chmod 6755 /usr/bin/exec-suid

COPY hidden-treasures-in-the-picture/treasure.jpg /home/ubuntu/Hidden-Treasure-in-Picture/

COPY secret-message-in-photo/suspicious_doggo.jpg /home/ubuntu/Secret-Message-in-Photo/

COPY secret-message-in-photo/secret.txt /home/ubuntu/Secret-Message-in-Photo/

COPY chatty-server/server.log /home/ubuntu/Chatty-Server/

COPY code-cracker/secret.bin /home/ubuntu/Code-Cracker/

COPY the-artists-clue/art.jpg /home/ubuntu/Artists-Clue/

COPY chatty-server/server.log /home/ubuntu
RUN chown ubuntu: /home/ubuntu/server.log

USER hacker