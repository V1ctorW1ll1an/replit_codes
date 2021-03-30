
import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    results = [0,0]
    for i in range(len(a)):
      if a[i] > b[i]:
        results[0] += 1
      elif b[i] > a[i]:
        results[1] += 1
    return results


    

if __name__ == '__main__':

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    print(' '.join(map(str, result)))
   