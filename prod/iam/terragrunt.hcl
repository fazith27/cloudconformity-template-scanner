# Terraform module source
terraform {
  source = "${get_terragrunt_dir()}/../../aws/iam"
}

include {
  path = find_in_parent_folders()
}

locals {
  config = {
    "name" = "prod-iam-role"
  }
}

inputs = merge("${local.config}")
