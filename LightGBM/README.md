# Light Gradient Boost Decision Tree (GBDT) Demo 
### Goal: 
To test how decision tree model can be applied to identify the relevant / meaning repair options out of infinitely many repair instances

### Methods:
The framework of this approach is motivated by this paper, LightGBM: A Highly Efficient Gradient BoostingDecision Tree, by Microsoft Research. (Link: https://papers.nips.cc/paper/2017/file/6449f44a102fde848669bdd9eb6b76fa-Paper.pdf)

### Data: 
The original full dataset consisting of a ground truth dataset, D_t, a dirty dateset, D_d, and other repair instances, R_1, R_2…,R_20 is stored in data.csv with a clear header. 
Since LightGBM model takes a matrix for the input, I turned each data instance into a column containing tuple values in rows. 
For training and testing data, I splitted the original dataset into 25 rows and 10 rows. 

### Result: 
Once you compile demo_gridsearch.py, you'll get the result below: 

```
Loading data...
Starting training...
[1]	valid_0's l1: 19.412	valid_0's l2: 553.854
Training until validation scores don't improve for 5 rounds
[2]	valid_0's l1: 19.412	valid_0's l2: 553.854
[3]	valid_0's l1: 19.412	valid_0's l2: 553.854
[4]	valid_0's l1: 19.412	valid_0's l2: 553.854
[5]	valid_0's l1: 19.412	valid_0's l2: 553.854
[6]	valid_0's l1: 19.412	valid_0's l2: 553.854
Early stopping, best iteration is:
[1]	valid_0's l1: 19.412	valid_0's l2: 553.854
Starting predicting...
The rmse of prediction is: 23.110049761954215
Feature importances: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Starting training with custom eval function...
[1]	valid_0's l2: 553.854	valid_0's RMSLE: 0.462812
Training until validation scores don't improve for 5 rounds
[2]	valid_0's l2: 553.854	valid_0's RMSLE: 0.462812
[3]	valid_0's l2: 553.854	valid_0's RMSLE: 0.462812
[4]	valid_0's l2: 553.854	valid_0's RMSLE: 0.462812
[5]	valid_0's l2: 553.854	valid_0's RMSLE: 0.462812
[6]	valid_0's l2: 553.854	valid_0's RMSLE: 0.462812
Early stopping, best iteration is:
[1]	valid_0's l2: 553.854	valid_0's RMSLE: 0.462812
Starting training with multiple custom eval functions...
[1]	valid_0's l2: 553.854	valid_0's RMSLE: 0.462812	valid_0's RAE: 1.49784
Training until validation scores don't improve for 5 rounds
[2]	valid_0's l2: 553.854	valid_0's RMSLE: 0.462812	valid_0's RAE: 1.49784
[3]	valid_0's l2: 553.854	valid_0's RMSLE: 0.462812	valid_0's RAE: 1.49784
[4]	valid_0's l2: 553.854	valid_0's RMSLE: 0.462812	valid_0's RAE: 1.49784
[5]	valid_0's l2: 553.854	valid_0's RMSLE: 0.462812	valid_0's RAE: 1.49784
[6]	valid_0's l2: 553.854	valid_0's RMSLE: 0.462812	valid_0's RAE: 1.49784
Early stopping, best iteration is:
[1]	valid_0's l2: 553.854	valid_0's RMSLE: 0.462812	valid_0's RAE: 1.49784
Starting predicting...
The rmsle of prediction is: 0.4695717561882056
The rae of prediction is: 1.520679012345679
Best parameters found by grid search are: {'learning_rate': 0.01, 'n_estimators': 20}
```

### Next Step:
Gradient Boost Decision Tree is highly versatile as you can see in the documentation: https://lightgbm.readthedocs.io/en/latest/Parameters.html.
By specifying the object of a model in `objective` parameter, you can use it for a variety of applications such as regression, classification, and entropy calculation.

Given this property, we can experiment this model with our database repair research project to see the most relevant repair instances to focus on.
