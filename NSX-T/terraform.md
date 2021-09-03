# Terraform

## Usage

```bash
docker run -it --network host -v `pwd`:/workspace -w /workspace hashicorp/terraform init -force-copy -get=true -no-color
docker run -it --network host --env-file=tf_vars.env -v `pwd`:/workspace -w /workspace hashicorp/terraform plan -detailed-exitcode -no-color
docker run -it --network host --env-file=tf_vars.env -v `pwd`:/workspace -w /workspace hashicorp/terraform apply -auto-approve -no-color
docker run -it --network host --env-file=tf_vars.env -v `pwd`:/workspace -w /workspace hashicorp/terraform destroy -auto-approve -no-color
```
