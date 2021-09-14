# Terragrunt with Cloudconformity Template Scanner

## Prerequisite
- AWS access key (AWS_ACCESS_KEY_ID) and secret key (AWS_SECRET_ACCESS_KEY) save as env variables if not using roles
- Cloudconformity API key save as env variable API_KEY

### Terragrunt run-all plan to save the plan output
`terragrunt run-all plan --terragrunt-non-interactive -out plan.out`

### Terragrunt run-all show to save the plan output as json
`terragrunt run-all show --terragrunt-non-interactive -json plan.out > plan.json`

### Python command for scanning the plan json
`python template-scanner.py`
