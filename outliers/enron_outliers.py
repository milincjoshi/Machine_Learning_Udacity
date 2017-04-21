#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
data_dict.pop("TOTAL",0)
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below
#print data_dict
max_salary = []
max_bonus = []

for point in data:
    salary = point[0]
    bonus = point[1]
    max_salary.append(salary)
    max_bonus.append(bonus)
    matplotlib.pyplot.scatter( salary, bonus)


max_salary = sorted(max_salary, reverse=True)
max_bonus = sorted(max_bonus, reverse=True)

print max_salary
print max_bonus
#print "max salary "+str(max_salary)
#print "max bonus "+str(max_bonus)
print max_salary[0]
print max_salary[1]
print max_salary[2]

for each_item in data_dict:
	if data_dict[each_item]['salary'] == max_salary[1]:
		print each_item


matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()
