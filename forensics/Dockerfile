FROM phocean/volatility

USER root

# Install steghide and system dependencies for Volatility 3
RUN apt update && apt install -y \
    steghide

# Create hacker user with no password and set up bash env
RUN useradd -s /bin/bash -m hacker && passwd -d hacker
RUN ln -s /etc/bash.bashrc /etc/bashrc

USER hacker

COPY Volatility /home
