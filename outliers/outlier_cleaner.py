#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here

    for i in range(0,len(predictions),1):
        age = ages[i]
        prediction = predictions[i]
        net_worth = net_worths[i]
        diff = prediction - net_worth
        arr = [age, net_worth, diff]
        cleaned_data.append(arr)

  
    from operator import itemgetter
    cleaned_data = sorted(cleaned_data, key=itemgetter(2), reverse=True)


    size_10_percent = 0.1 * len(cleaned_data)
    new_cleaned_data=[]

    for each_item in cleaned_data:
        if cleaned_data.index(each_item)>size_10_percent:
            new_cleaned_data.append(each_item) 

    return new_cleaned_data

