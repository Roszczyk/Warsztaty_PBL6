FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
        tcpdump \
        iproute2 \
        iputils-ping \
        sudo \
	curl \
        wget \
        iperf \
        nano \
        nload \
        openssh-server \
        cowsay

COPY zespol.txt /root/
RUN mkdir /run/sshd
RUN echo 'root:root' | chpasswd
EXPOSE 22

RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN echo "### PAM kontener ###" | /usr/games/cowsay -f tux > /etc/ssh/banner && \
    sed -i 's/#Banner none/Banner \/etc\/ssh\/banner/' /etc/ssh/sshd_config

HEALTHCHECK --interval=10s --timeout=3s \
	CMD /etc/init.d/ssh status

CMD ["/usr/sbin/sshd", "-ddd"]
