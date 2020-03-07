import numpy as np
import pandas as pd
import random
import csv
import string
import sys
import json
from scipy import stats


genders = ['male', 'female']
races = ['black', 'white', 'asian', 'hispanic', 'mixed', 'native american', 'other']
counties = ['alameda', 'alpine', 'amador', 'butte', 'calaveras', 'colusa', 
            'contra costa', 'del norte', 'el dorado', 'fresno', 'glenn',
            'humboldt', 'imperial', 'inyo', 'kern', 'kings', 'lake',
            'lassen', 'los angeles', 'madera', 'marin', 'mariposa',
            'mendocino', 'merced', 'modoc', 'mono', 'monterey', 'napa',
            'nevada', 'orange', 'placer', 'plumas', 'riverside',
            'sacramento', 'san benito', 'san bernadino', 'san diego',
            'san francisco', 'san joaquin', 'san luis obispo', 'san mateo',
            'santa barbara', 'santa clara', 'santa cruz', 'shasta', 'sierra',
            'siskiyou', 'solano', 'sonoma', 'stanisluas', 'sutter', 'tehama',
            'trinity', 'tulaue', 'tholumne', 'ventura', 'yolo', 'yuba']
archetypes = ["normie", "stoner", "brogrammer", "tryhard", "geek", "alternative"]


class Student:
    def __init__(self, county, race, gender):
        self.gender = gender
        self.race = race
        self.county = county
        self.name = self.get_name()
        self.archetype = self.get_archetype()

    def get_archetype(self):
        return archetypes[random.randint(0, len(archetypes) - 1)]

    def get_name(self):
        boy_names, girl_names = np.split(pd.read_csv('names.csv', index_col=False), np.arange(3, 6, 3), axis=1)
        if self.gender is 'male':
            col = boy_names.columns
            names = boy_names[col[0]].tolist()
            counts = boy_names[col[1]].tolist()
            race = boy_names[col[2]].tolist()
        else:
            col = girl_names.columns
            names = girl_names[col[0]].tolist()
            counts = girl_names[col[1]].tolist()
            race = girl_names[col[2]].tolist()
        s = sum(counts)
        counts = [c / s for c in counts] 
        return names[stats.rv_discrete(values=(np.arange(len(counts)), counts)).rvs(1)]

    def __str__(self):
        return((self.name + " is a " + 
                string.capwords(self.race) + " " + 
                self.gender + " from " + 
                string.capwords(self.county) + " County. " + 
                ("He is a " if self.gender is "male" else "She is a ") +
                self.archetype + "."))

    def to_dict(self):
        return {'name': self.name,
                'gender': self.gender,
                'county': self.county,
                'race': self.race,
                'archetype': self.archetype}

def populate_table():
    index = []
    pop = []
    sum = 0
    for c in counties:
        for r in races:
            for g in genders:
                index.append((c, r, g))
                pop.append(random.randint(10,100))
    return index, pop

def get_students(n=100):
    index, pop = populate_table()
    total = sum(pop)
    pop = [p / total for p in pop]
    students = stats.rv_discrete(values=(np.arange(len(pop)), pop)).rvs(size=n)
    return [Student(*index[s]) for s in students]

if __name__ == '__main__':
    S = get_students(int(sys.argv[1]))
    D = [s.to_dict() for s in S]
    print(json.dumps(D))
    sys.stdout.flush()
