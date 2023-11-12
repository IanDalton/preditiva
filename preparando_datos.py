import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder

from sklearn.model_selection import train_test_split
from concurrent.futures import ThreadPoolExecutor


import pandas as pd
import matplotlib.pyplot as plt

def compute_average(values):
        if values[0] == values[1]:
            return values[0]
        if values[1] != 0:
            return values[0] / values[1]
        return 0

def sum_into_column(persons,data:dict,category:str=None):
    total = 0
    personas = len(persons.split(","))
    if category != 'total':
        for person in persons.split(","):
            if person in data:
                total += data[person] if category is None else data[person][category]
    else:
        for person in persons.split(","):
            score_divider = 0
            score_persona = 0
            if person in data:
                data[person]:dict
                for cat in data[person].values():
                    score_persona += cat
                    if cat != 0:
                        score_divider += 1
            total += score_persona / score_divider if score_divider != 0 else 0
    return total/personas

def sum_relevant_exp(persons:pd.DataFrame,data:dict,group:str,target:str):
    total = 0
    personas = persons[group].split(",")
    relevant_cat = persons[target]
    for person in personas:
        total_person,total_cat = 0,0
        if type(relevant_cat)==str:   
            for cat in relevant_cat.split(","):
                if person in data:
                    total_person += data[person][cat]
                    total_cat += 1 if data[person][cat] != 0 else 0
        total += total_person / total_cat if total_cat != 0 else 0
    return total/len(personas)


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

def get_min_max_category(persons,data:dict,is_max:bool,categories:list):
    min_max = 0 if is_max else 999999999999

    for person in persons.split(','):
        for category in categories:
            try:
                if is_max:
                    if data[person][category] > min_max:
                        min_max = data[person][category]
                else:
                    if data[person][category] < min_max and data[person][category] != 0:
                        min_max = data[person][category]
            except KeyError:
                pass

    return min_max
def get_min_max(persons,data:dict,is_max:bool,category:str=None):
    min_max = 0 if is_max else 999999999999
    #print(persons)
    if persons == '' or persons is None or persons == '0':
        return 0
    if category != None and category != 'exp':
        min_max = get_min_max_category(persons,data,is_max,category)  
    else:
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

    return min_max if min_max != 999999999999 else 0



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

