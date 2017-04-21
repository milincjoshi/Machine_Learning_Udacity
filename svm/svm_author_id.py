#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn import svm
# C (say, 10.0, 100., 1000., and 10000.)
clf = svm.SVC(kernel='rbf', C=10000.0)
t0 = time() # caculating training time

# training a small dataset
#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100] 

clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s" # calculating training time
t1 = time() # caculating training time
predicted_labels = clf.predict(features_test)
print "prediction time:", round(time()-t1, 3), "s" # calculating training time
from sklearn.metrics import accuracy_score
print accuracy_score(labels_test, predicted_labels)
answers10 = predicted_labels[10]
answers26 = predicted_labels[26]
answers50 = predicted_labels[50]

print "answer10 "+str(answers10)
print "answer26 "+str(answers26)
print "answer50 "+str(answers50)
chris_emails = 0
sara_emails = 0
for each_predicted_label in predicted_labels:
	if each_predicted_label == 1:
		chris_emails+=1
	else:
		sara_emails+=1
print "chris_emails "+str(chris_emails)
print "sara_emails "+str(sara_emails)


#########################################################


