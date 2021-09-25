FROM alpine:3.14 AS BUILDER
# https://pkgs.alpinelinux.org/packages?name=python3&branch=v3.14
# https://hub.docker.com/_/python

ENV TZ Etc/UTC
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

ENV TERRAFORM_VERSION 1.0.6
ENV SWAGGER_CODEGEN_VERSION 3.0.27

ENV PATH "/opt/venv/bin:$PATH"

WORKDIR /tmp

COPY requirements.txt .

RUN wget https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \
wget -c https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_SHA256SUMS && \
cat terraform_${TERRAFORM_VERSION}_SHA256SUMS | grep terraform_${TERRAFORM_VERSION}_linux_amd64.zip > TMP_SHA_FILE && \
if [ $(sha256sum -c TMP_SHA_FILE  2>&1 | grep OK | wc -l) != 1 ]; then echo "Message diget check failed for Terraform" >&2; exit 1; fi && \
unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip && mv terraform /usr/bin/terraform && rm -rf terraform_${TERRAFORM_VERSION}_linux_amd64.zip

RUN wget -c https://repo1.maven.org/maven2/io/swagger/codegen/v3/swagger-codegen-cli/${SWAGGER_CODEGEN_VERSION}/swagger-codegen-cli-${SWAGGER_CODEGEN_VERSION}.jar -O /usr/bin/swagger-codegen-cli.jar

RUN apk add --update --no-cache python3=~3.9 python3-dev=~3.9 && \
apk add --update --no-cache build-base gcc && \
apk add --update --no-cache py3-pip && \
apk add --update --no-cache bash

RUN python3 -m venv /opt/venv
RUN pip3 install -r requirements.txt

FROM python:3.9.7-alpine3.13
LABEL maintainer="ionut.pirva@gmail.com"
LABEL name="Terraform and Python3 Runner"
LABEL terraform_version="1.0.6"
LABEL python_version="3.9.7"
LABEL swagger_cogen_version="3.0.27"

ENV PATH "/opt/venv/bin:/bin:/usr/local/bin:$PATH"
ENV JAVA_HOME "/usr/lib/jvm/java-11-openjdk"
ENV PATH "${PATH}:${JAVA_HOME}/bin"
ENV PYTHONPATH "${PYTHONPATH}:/root/.local/lib/python3.9/site-packages/"

RUN ln -s /usr/local/bin/python3 /usr/bin/python3
RUN apk add --update --no-cache bash curl jq openjdk11 openssl
COPY --from=BUILDER /usr/bin/terraform /usr/bin/terraform
COPY --from=BUILDER /usr/bin/swagger-codegen-cli.jar /usr/bin/swagger-codegen-cli.jar
COPY --from=BUILDER /opt/venv /opt/venv
RUN /opt/venv/bin/python3 -m pip install --upgrade pip

