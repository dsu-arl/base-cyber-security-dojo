FROM ubuntu:latest

USER root
RUN apt update && apt install -y steghide autopsy

RUN <<EOF
  if id ubuntu; then userdel -f -r ubuntu; fi
  useradd -s /bin/bash -m hacker
  passwd -d hacker

  ln -s /etc/bash.bashrc /etc/bashrc
EOF

USER hacker
