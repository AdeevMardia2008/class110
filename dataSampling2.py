import plotly.figure_factory as ff
import statistics
import pandas as pd
import csv
import random

df=pd.read_csv("temperature.csv")
data=df["temp"].tolist()

def random_set(Counter):
    data_set=[]
    for i in range(0,Counter):
        random_index=random.randint(0,len(data))
        value=data[random_index]
        data_set.append(value)
        
    mean=statistics.mean(data_set)
    return mean


def showfig(mean_list):
    df=mean_list
    fig=ff.create_distplot([df],["Temperature"],show_hist=False)
    fig.show()


def setup():
    mean_list=[]
    for i in range(0,1000):
        setOfMeans=random_set(100)
        mean_list.append(setOfMeans)
        
    showfig(mean_list)
    
setup()