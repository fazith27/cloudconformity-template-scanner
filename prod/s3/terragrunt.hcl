# Terraform module source
terraform {
  source = "${get_terragrunt_dir()}/../../aws/s3"
}

include {
  path = find_in_parent_folders()
}

locals {
  config = {
    "name" = "prod-s3-bucket"
  }
}

inputs = merge("${local.config}")
