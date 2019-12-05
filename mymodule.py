exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
             'score': [12.5, 9, 16.5, 3, 9, 20, 20, 7, 8, 19],
             'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
             'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
             '
import pandas as pd 
import numpy as np 

a = pd.DataFrame (exam_data, columns = ['name' , 'score', 'attempts', 'qualify'])

print()
print(a)
