# Terraform

## Usage

```bash
docker run -it --network host -v `pwd`:/workspace -w /workspace/terraform ipirva/runner:terraform1.0.6 terraform init -force-copy -get=true -no-color
docker run -it --network host --env-file=terraform/tf_vars.env -v `pwd`:/workspace -w /workspace/terraform ipirva/runner:terraform1.0.6 terraform plan -detailed-exitcode -no-color
docker run -it --network host --env-file=terraform/tf_vars.env -v `pwd`:/workspace -w /workspace/terraform ipirva/runner:terraform1.0.6 terraform apply -auto-approve -no-color
docker run -it --network host --env-file=terraform/tf_vars.env -v `pwd`:/workspace -w /workspace/terraform ipirva/runner:terraform1.0.6 terraform destroy -auto-approve -no-color
```
