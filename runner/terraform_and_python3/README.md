# Terraform and Python Runner

This is a Docker image containing Terraform and Python.
Terraform version 1.0.6 and Python version 3.9.7

To build this container, you may use the following command:

```bash
docker build -t ipirva/runner:latest -t ipirva/runner:terraform1.0.6 -t ipirva/runner:python3.9.7 --squash --no-cache .
```

One may run this container as follows:

```bash
docker run -it --network host --env-file=vars.env -v `pwd`:/workspace -w /workspace  ipirva/runner [terraform|python]
```

## Prerequisites

The container may need only outgoing internet access to install Python modules or/and Terraform providers.
The required Python modules are to be specified in the "requirements.txt" file.
The Terraform modules are downloaded upon Terraform init phase.
