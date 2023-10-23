import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder

from sklearn.model_selection import train_test_split
from concurrent.futures import ThreadPoolExecutor


import pandas as pd
import matplotlib.pyplot as plt


def sum_into_column(persons,data:dict,category:str=None):
    total = 0
    personas = len(persons.split(","))
    for person in persons.split(","):
        if person in data:
            total += data[person] if category is None else data[person][category]
    return total/personas

def split_and_sum(data:dict):
    people = dict()
    list_of_people:str
    for list_of_people in data.keys():
        for person in list_of_people.split(","):
            if person in people:
                people[person]+=data[list_of_people]
            else:
                people[person]=data[list_of_people]
    people["0"] = 0
    return people

def get_min_max(persons,data:dict,is_max:bool):
    min_max = 0 if is_max else 999999999999
    for person in persons.split(','):
        try:
            if is_max:
                if data[person] > min_max:
                    min_max = data[person]
            else:
                if data[person] < min_max:
                    min_max = data[person]
        except KeyError:
            pass

    return min_max



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

