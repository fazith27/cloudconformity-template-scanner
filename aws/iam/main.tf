resource "aws_iam_user" "this" {
  name = var.name
}

variable "name" {
    description = "Name of the iam user"
}

terraform {
  backend "local" {}
}
