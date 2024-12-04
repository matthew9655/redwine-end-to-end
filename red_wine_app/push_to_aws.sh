#!/bin/bash

source .env
AWS_URL=$AWS_ACC_NUMBER.dkr.ecr.$AWS_REGION.amazonaws.com

docker build -t red-wine-mm:latest .
docker tag red-wine-mm:latest $AWS_URL/red-wine-mm:latest

#login to aws

aws ecr get-login-password \
    --region $AWS_REGION \
| docker login \
    --username AWS \
    --password-stdin $AWS_URL

docker push $AWS_URL/red-wine-mm:latest