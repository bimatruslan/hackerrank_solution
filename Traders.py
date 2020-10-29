#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'mostActive' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY customers as parameter.
#

def mostActive(customers):
    customer_count = len(customers)
    last_value = "kosong"
    min_value = 0.05
    final_list = []
    
    for i in customers :
        if i != last_value:
            last_value  = i
            count_value = customers.count(i)
            if count_value / customer_count >= min_value :
                if i not in final_list :
                    final_list.append(i)
    
    final_list.sort()
    return final_list

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    customers_count = int(input().strip())

    customers = []

    for _ in range(customers_count):
        customers_item = input()
        customers.append(customers_item)

    result = mostActive(customers)
    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
