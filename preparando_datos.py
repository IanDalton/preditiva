import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder

from sklearn.model_selection import train_test_split
from concurrent.futures import ThreadPoolExecutor


import pandas as pd
import matplotlib.pyplot as plt




df_train=pd.read_csv('dataset/origen.csv')

def director_avg_rating(db):
    directors_score = dict()
    db_dict = db.groupby('directors')['averageRating'].mean().to_dict()


    for key in db_dict.keys():
        for director in key.split(','):
            if director in directors_score.keys():
                directors_score[director][0] += db_dict[key]
                directors_score[director][1] += 1 
            else:
                directors_score[director] = [db_dict[key],1]
    for director in directors_score.keys():
        directors_score[director] = directors_score[director][0] / directors_score[director][1]
    return directors_score


score = director_avg_rating(df_train)
