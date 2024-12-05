# Redwine Prediction Model end-to-end

Full end-to-end code for releasing machine learning models into production with CI/CD capabilties using circleCI. This repo was inspired by the Udemy course [Deployment of Machine Learning Model](https://www.udemy.com/course/deployment-of-machine-learning-models/)


## Project Directory

This project is broken down into 3 sections:
1. Research Environment 
    - Exploratory Data Analysis and Feature Engineering
    - Hyperparameter Tuning, Evaluation and Model Selection
2. Production Environment
    - Model packaging and deployment to Pypi
3. App Environemnt
    - FastAPIs endpoints for model prediction 
    - Deployable as a docker container for both Railway and AWS ECS

More information for each particular section can be found in their respective READMEs.


## Deploying with CircleCI

Some environment variables need to be set in the circleci project for CI/CD to work. These are:

If you plan to use railway, 
`RAILWAY_SERVICE_NAME`: the name of your railway service

`RAILWAY_TOKEN`: the token of your railway project 

`TWINE_USERNAME`: Twine username 

`TWINE_PASSWORD`: Twine password

`AWS_ACCESS_KEY_ID`: The access key id in your security credentials 

`AWS_SECRET_ACCESS_KEY`: the access key secret

`AWS_REGION`: your aws region

`AWS_ACC_NUMBER`: your account number id 



