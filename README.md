# Assignment_stride

____________________________________________________Task 1__________________________________________________________________

INTENT CLASSIFICATION

Problem Statement:

Intent detection on Enron email set. We define “intent” here to correspond primarily to the categories “request” and “propose”.
In some cases, we also apply the positive label to some sentences from the “commit” category if they contain datetime, which makes them useful. Detecting the presence of intent in email is useful in many applications, e.g., machine mediation between human and email. The dataset contains parsed sentences from the email along with their intent (either ‘yes’ or ‘no’).

Approach for the solution:


Took a neural network approach to build a binary classifier to tackle the problem statement
Data Analysis and previous appproaches:
  Good work had been done in SVM, but as it has been done, continued with neural network approach cause context
Data cleaning and Preprocessing:
  Stopwards removal, lowercasing, removing junk
Embeddings:
  Pre-trained Glove Embeddings
  character embedding cause intent had to be taken out( very confusing),so granular level
  
 Model structure:
  Model: "model_1"
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to                     
==================================================================================================
input_2 (InputLayer)            (None, 300, 10)      0                                            
__________________________________________________________________________________________________
input_1 (InputLayer)            (None, 300)          0                                            
__________________________________________________________________________________________________
time_distributed_1 (TimeDistrib (None, 300, 10, 10)  280         input_2[0][0]                    
__________________________________________________________________________________________________
embedding_1 (Embedding)         (None, 300, 300)     1897800     input_1[0][0]                    
__________________________________________________________________________________________________
time_distributed_2 (TimeDistrib (None, 300, 64)      19200       time_distributed_1[0][0]         
__________________________________________________________________________________________________
concatenate_1 (Concatenate)     (None, 300, 364)     0           embedding_1[0][0]                
                                                                 time_distributed_2[0][0]         
__________________________________________________________________________________________________
spatial_dropout1d_1 (SpatialDro (None, 300, 364)     0           concatenate_1[0][0]              
__________________________________________________________________________________________________
bidirectional_1 (Bidirectional) (None, 256)          504832      spatial_dropout1d_1[0][0]        
__________________________________________________________________________________________________
dense_1 (Dense)                 (None, 2)            514         bidirectional_1[0][0]            
==================================================================================================
Total params: 2,422,626
Trainable params: 524,826
Non-trainable params: 1,897,800
__________________________________________________________________________________________________


Accuracy on training model: 


              precision    recall  f1-score   support

           0       0.85      1.00      0.92       197
           1       1.00      0.80      0.89       169

    accuracy                           0.91       366
   macro avg       0.93      0.90      0.90       366
weighted avg       0.92      0.91      0.91       366


Accuracy on test.csv :
78.5

Reason: The data is not very clear














___________________________________________________    Task 2  ___________________________________________


Problem Statement:

extract the following:

- Currency

- Amount

- Rounding (up / down/ nearest) If not mentioned, take it as 'nearest' by default.

for 'Delivery Amount' and 'Return Amount'.
 

We have included the textual data in isda_data.json. Refer sample_isda.py for the basic implementation framework.

Input: "Rounding. The Delivery Amount and the Return Amount will be rounded to the nearest integral multiple o f EUR 100,000; provided that if an amount corresponds to the exact half o f such multiple, then it will be rounded up; and provided further that, for the purpose o f the calculation of the Return Amount where a party's Credit Support Amount is, or is deemed to be, zero, the Return Amount shall not be rounded."

Output:

{

"delivery_currency": "EUR",

"delivery_amount": "100,000",

"delivery_rounding": "nearest",

"return_currency": "EUR",

"return_amount": "100,000",

"return_rounding": "nearest"

}






 
