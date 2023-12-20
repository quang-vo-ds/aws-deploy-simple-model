# aws_deploy_simple_model
Demo how to deploy a simple model on AWS

## Build Dockerfile and push to ECR
`! pip install sagemaker-studio-image-build --quiet`

`! sm-docker build . --repository sklearn-on-aws:1.0 --role quangvv9_sagemaker_role`

## Deploy on Cloudshell
`! npm install serverless`

`! cat > serverless.yml`

`npm install --prefix ./ serverless`

`node_modules/serverless/bin/serverless.js deploy`