#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "no. of persons : "+str(len(enron_data))
print "no. of features for each person : "+str(len(enron_data["SKILLING JEFFREY K"]))

poi_count = 0
for each_item in enron_data:
	if enron_data[each_item]["poi"] == True:
		poi_count+=1

print "poi count : "+str(poi_count)
print "poi names in final_project/poi_names.txt file 35"

print enron_data["COLWELL WESLEY"]
def printFeatureValue(name, feature):
	return enron_data[name][feature]

print "James Prentice total stock value : "+str(printFeatureValue("PRENTICE JAMES","total_stock_value"))
print "Wesley Colwell from_this_person_to_poi : "+str(printFeatureValue("COLWELL WESLEY","from_this_person_to_poi"))
print "Jeffrey K Skilling exercised_stock_options : "+str(printFeatureValue("SKILLING JEFFREY K","exercised_stock_options"))

salary_count = 0
email_count = 0
for each_item in enron_data:
	if enron_data[each_item]["salary"] != "NaN":
		salary_count+=1
for each_item in enron_data:
	if enron_data[each_item]["email_address"] != "NaN":
		email_count+=1
print "salary_count : "+str(salary_count) 
print "email_count : "+str(email_count) 

nan_total_payments_count  = 0
for each_item in enron_data:
	if enron_data[each_item]["total_payments"] == "NaN":
		nan_total_payments_count+=1
print "nan_total_payments_count : "+str(nan_total_payments_count) 
print "len(enron_data) : "+str(len(enron_data)) 
print "% nan_total_payments_count : "+str((nan_total_payments_count*100)/len(enron_data))

poi_nan_total_payments_count  = 0
for each_item in enron_data:
	if enron_data[each_item]["total_payments"] == "NaN" and enron_data[each_item]["poi"]==True:
		poi_nan_total_payments_count+=1
print "% poi_nan_total_payments_count "+str((poi_nan_total_payments_count*100)/len(enron_data))
print "poi_nan_total_payments_count : "+str(poi_nan_total_payments_count+10)
print "% poi_nan_total_payments_count "+str(((poi_nan_total_payments_count+10)*100)/len(enron_data))
'''
for each_item in enron_data:
	if "PRENTICE" in each_item and "JAMES" in each_item:
		print enron_data[each_item]["total_stock_value"]
		for each_sub_item in enron_data[each_item]:
			print each_sub_item
for each_item in enron_data:
	if "COLWELL" in each_item and "WESLEY" in each_item:
		print enron_data[each_item]["total_stock_value"]
		for each_sub_item in enron_data[each_item]:
			print each_sub_item
'''
