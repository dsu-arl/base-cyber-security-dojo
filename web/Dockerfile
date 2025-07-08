FROM debian

RUN apt update; apt install firefox-esr python3 python3-pip python3-flask wget -y
RUN apt install wget lsb-release -y
RUN wget https://packages.microsoft.com/config/debian/$(lsb_release -rs)/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
RUN dpkg -i packages-microsoft-prod.deb

RUN apt update; apt install msopenjdk-21 -y



RUN wget -O burp.jar 'http://portswigger.net/burp/releases/download?product=community&type=Jar' 



RUN <<EOF
    useradd -s /bin/bash -m hacker
    passwd -d hacker
    ln -s /etc/bash.bashrc /etc/bashrc
EOF

ADD --chown=0:0 --chmod=6755 http://github.com/pwncollege/exec-suid/releases/latest/download/exec-suid /usr/bin/exec-suid
RUN chmod 6755 /usr/bin/exec-suid

USER hacker
