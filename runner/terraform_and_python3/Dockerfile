FROM alpine:3.14 AS BUILDER
LABEL maintainer="ionut.pirva@gmail.com"
LABEL name="Terraform and Python3 Runner"
# https://pkgs.alpinelinux.org/packages?name=python3&branch=v3.14
# https://hub.docker.com/_/python

ENV TZ Etc/UTC
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

ENV TERRAFORM_VERSION 1.0.6

WORKDIR /tmp

COPY requirements.txt .

RUN wget https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \
wget -c https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_SHA256SUMS && \
cat terraform_${TERRAFORM_VERSION}_SHA256SUMS | grep terraform_${TERRAFORM_VERSION}_linux_amd64.zip > TMP_SHA_FILE && \
if [ $(sha256sum -c TMP_SHA_FILE  2>&1 | grep OK | wc -l) != 1 ]; then echo "Message diget check failed for Terraform" >&2; exit 1; fi && \
unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip && mv terraform /usr/bin/terraform && rm -rf terraform_${TERRAFORM_VERSION}_linux_amd64.zip
RUN apk add --update --no-cache python3=~3.9 python3-dev=~3.9 && \
apk add --update --no-cache build-base gcc && \
apk add --update --no-cache py3-pip && \
apk add --update --no-cache bash

RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip3 install -r requirements.txt

FROM python:3.9.7-alpine3.13

ENV PATH="/opt/venv/bin:/bin:$PATH"
RUN ln -s /usr/local/bin/python3 /usr/bin/python3
RUN apk add --update --no-cache bash curl jq
COPY --from=BUILDER /usr/bin/terraform /usr/bin/terraform
COPY --from=BUILDER /opt/venv /opt/venv

