# using ubuntu base image
FROM ubuntu:22.04

# set end and maintainer labels
LABEL end="dev"
LABEL maintainer="email@outlook.com"

# Set environment variables
ENV PATH="/usr/local/bin:${PATH}"

# apt-get clean is optional as Official Debian and Ubuntu images
# automatically run them.
RUN apt-get update && \
	apt-get install -y \
		curl \
		iproute2 \
		sshfs \
		unzip \
		less \
		groff \
		&& rm -rf /var/lib/apt/lists/*

# installing kubectl
RUN curl -LO "https://dl.k8s.io/release/v1.23.6/bin/linux/amd64/kubectl" && \
	chmod +x ./kubectl && \
	mv ./kubectl /usr/local/bin/kubectl && \
	kubectl version --client

# installing aws cli
RUN curl https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip -o /tmp/awscli-linux.zip && \
    cd /tmp && \
    unzip awscli-linux.zip && \
    ./aws/install && \
    rm -rf ./aws

# adding non-root user builder
RUN useradd -ms /bin/bash builder
USER builder

CMD bash
