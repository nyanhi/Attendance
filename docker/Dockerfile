FROM node:12
LABEL maintainer="Nyanhi"

RUN cd /opt \
    && curl -q "https://www.python.org/ftp/python/3.7.6/Python-3.7.6.tgz" -o Python-3.7.6.tgz \
    && tar -xzf Python-3.7.6.tgz \
    && cd Python-3.7.6 \
    && ./configure --enable-optimizations \
    && make install

RUN cd /opt \
    && curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip \
    && ./aws/install

RUN npm install -g aws-cdk@1.30

RUN cd /root \
    && git clone https://github.com/nyanhi/Attendance.git

# Make command line prettier...
RUN echo "alias ls='ls --color=auto'" >> /root/.bashrc
RUN echo "PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@syukin\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '" >> /root/.bashrc

RUN mkdir -p /root/.ssh
WORKDIR /root
CMD ["/bin/bash"]
