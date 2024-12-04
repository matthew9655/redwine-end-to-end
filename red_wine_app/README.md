# FastAPI endpoints for the Red Wine Model 

## We create two endpoints 
 - health: checks the versions of the api and the model 
 - predict: takes input parameters and passes it through the model to make a prediction

## Pushing to AWS
Create a `.env` file and create the following variables:
`AWS_ACCOUNT_NUMBER`: your AWS account number 
`AWS_REGION`: your AWS region, like `us-east-1`
run `./push_to_aws.sh`

## How to deploy
1. Login into AWS, you should see `red_wine_mm` in your ECR directory
2. Now create a cluster in the ECS directory with AWS Fargate.
3. Create a new task definition and make sure to use `Linux/ARM` as the OS and set the number of CPUS and RAM you need. 
4. Now back at the cluster, Create a new task. You should see your task definition under task families. 
5. Under networking in "Create a new task" -> "Create a new security group" -> Inbound Rules -> Set Type to HTTP and Source anywhere, this exposes our port. 
6. When the task has been created, there should be a link for the model. The api html will be available at `{link}:8001/health`

