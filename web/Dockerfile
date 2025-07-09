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


RUN mkdir /etc/firefox-esr; mkdir /etc/firefox-esr/defaults; mkdir /etc/firefox-esr/defaults/pref
RUN printf 'pref("general.config.filename", "firefox.cfg");\npref("general.config.obscure_value", 0);' > /etc/firefox-esr/defaults/pref/autoconfig.js
RUN printf '// IMPORTANT: Start your code on the 2nd line\npref("network.http.referer.disallowCrossSiteRelaxingDefault.top_navigation", true);\npref("network.proxy.backup.ssl", "");\npref("network.proxy.backup.ssl_port", 0);\npref("network.proxy.http", "127.0.0.1");\npref("network.proxy.http_port", 8080);\npref("network.proxy.share_proxy_settings", true);\npref("network.proxy.ssl", "127.0.0.1");\npref("network.proxy.ssl_port", 8080);\npref("network.proxy.type", 1);\npref("network.trr.mode", 5);' > /etc/firefox-esr/firefox.cfg


USER hacker
