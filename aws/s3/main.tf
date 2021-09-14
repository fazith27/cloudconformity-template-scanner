resource "aws_s3_bucket" "this" {
  bucket = var.name
}

variable "name" {
    description = "Name of the bucket"
}

terraform {
  backend "local" {}
}
