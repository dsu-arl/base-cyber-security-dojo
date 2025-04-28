FROM phocean/volatility

USER root

# Install steghide and system dependencies for Volatility 3
RUN apt update && apt install -y \
    steghide

RUN apt install python3 -y

# Create hacker user with no password and set up bash env
RUN useradd -s /bin/bash -m hacker && passwd -d hacker
RUN ln -s /etc/bash.bashrc /etc/bashrc

# Add exec-suid
ADD --chown=0:0 http://github.com/pwncollege/exec-suid/releases/latest/download/exec-suid /usr/bin/exec-suid
RUN chmod 6755 /usr/bin/exec-suid

USER hacker

COPY Volatility /home
