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
            'lassen',  'los angeles', 'madera', 'marin', 'mariposa',
            'mendocino', 'merced', 'modoc', 'mono', 'monterey', 'napa',
            'nevada', 'orange', 'placer', 'plumas', 'riverside',
            'sacramento', 'san benito', 'san bernardino', 'san diego',
            'san francisco', 'san joaquin', 'san luis obispo', 'san mateo',
            'santa barbara', 'santa clara', 'santa cruz', 'shasta', 'sierra',
            'siskiyou', 'solano', 'sonoma', 'stanislaus', 'sutter', 'tehama',
            'trinity', 'tulare', 'tuolumne', 'ventura', 'yolo', 'yuba']
archetypes = ["normie", "stoner", "brogrammer", "tryhard", "geek", "alternative"]


class Student:
    def __init__(self, county, race, gender):
        self.gender = gender
        self.race = race
        self.county = county
        self.name = self.get_name()
        self.archetype = self.get_archetype()
        self.highschool, self.hometown = self.get_highschool_and_hometown()
        self.phone = self.get_phone()
        print(self.phone)
        
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

    def get_highschool_and_hometown(self):
        data = pd.read_csv('schools.csv')
        try:
            sample = data[data['County'] == self.county].sample()
            return tuple(sample[['School', 'City']].to_numpy()[0])
        except:
            print(self.county)

    def get_bio(self):
        if self.archetype is 'normie':
            return self.normie_bio()

    def get_phone(self):
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        data = pd.read_csv('areacodes.csv')
        data_small = data[data['city'] == self.hometown]
        if data_small.empty:
            phone = "(" + str(data.sample()['code'].to_numpy()[0])
        else:
            phone = "(" + str(data_small.sample()['code'].to_numpy()[0])
        index = random.randint(1, 8)
        phone = phone + ')-' + digits[index]
        index2 = random.randint(0, 8)
        index3 = random.randint(0, 8)
        while (index == index2):
            index2 = random.randint(0, 8)
        phone = phone + digits[index2] + digits[index3] + '-'
        for i in range(3):
            phone = phone + digits[random.randint(0, 8)]
        return phone 
        
    def __str__(self):
        return((self.name + " is a " + 
                string.capwords(self.race) + " " + 
                self.gender + " from " + 
                string.capwords(self.hometown) + ". " + 
                ("He is a " if self.gender is "male" else "She is a ") +
                self.archetype + " that went to " + self.highschool + "."))

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

def read_students(data):
    l = json.loads(data)
    return [read_student(d) for d in l]
        

def read_student(d):
    s = Student(d['county'], d['race'], d['gender'])
    s.name = d['name']
    s.archetype = d['archetype']
    return s

def build_students(n=100):
    index, pop = populate_table()
    total = sum(pop)
    pop = [p / total for p in pop]
    students = stats.rv_discrete(values=(np.arange(len(pop)), pop)).rvs(size=n)
    return [Student(*index[s]) for s in students]

def get_students(n=100):
    S = build_students(n)
    D = [s.to_dict() for s in S]
    return json.dumps(D)

if __name__ == '__main__':
    for s in build_students(int(sys.argv[1])):
        print(s)
    sys.stdout.flush()
