# Research Environment 

## Installation

`pip install -r requirements.txt`


## Directory 

`eda.ipynb` - I perform exploratory data analysis and save the updated dataset in their respective train and test datasets.

`train.ipynb` - Hyperparameter tuning and model selection. The final model chosen is the Random Forest with 200 trees which had an accuracy on the test set of 91% and a ROC AUC of 0.91. This is the model moving forward when creating the production environment.