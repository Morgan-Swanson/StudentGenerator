import numpy as np
import pandas as pd
import random
import csv
import string
import sys
import json
from scipy import stats

name_intro_normie = ["The Cal Poly student, ", "This student, ", "This student's name is ", "The student ",
                     "A scholar named "]
name_intro_normie_2 = ["ethnic orgin is ","is a","ethnicity is"]

genders = ['male', 'female']
religions = ['chirstian','noe','jewish','catholic','athiest', 'muslim','none']

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
personalities = ["normie", "stoner", "brogrammer", "tryhard", "nerd", "alternative"]


class Student:
    def __init__(self, county, race, gender):
        self.gender = gender
        self.race = race
        self.county = county
        self.name = self.get_name()
        self.personality = self.get_personality()
        self.highschool, self.hometown = self.get_highschool_and_hometown()
        self.phone = self.get_phone()
        self.email = self.get_email()
        self.activities = self.get_activities() 
        self.religion = self.get_religion()
        self.clubs = self.get_clubs()

       
        
    def get_personality(self):
        return personalities[random.randint(0, len(personalities) - 1)]

    def get_name(self):
        return self.get_first_name() + ' ' + self.get_last_name()

    def get_last_name(self):
        last_names = pd.read_csv('lastnames.csv')
        col = last_names.columns
        names = [n.lower().capitalize() for n in last_names[col[0]].tolist()]
        counts = [int(s.replace(",", "")) for s in last_names[col[1]].tolist()]
        s = sum(counts)
        counts = [c / s for c in counts]
        return names[stats.rv_discrete(values=(np.arange(len(counts)), counts)).rvs(1)]
        
    def get_first_name(self):
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

    def get_email(self):
        first, last = self.name.split()
        return (first[0] + last[:random.randint(4, 8)] + "@calpoly.edu").lower()

    def get_activities(self):
        data = pd.read_csv('activities.csv')
        col = data.columns
        active = ['normie','brogrammer','alternative']
        if self.personality in active:
            num_activities = random.randint(2,5)
        else:
            num_activities = random.randint(2,3)
        preference = 'masculine' if self.gender is 'male' else 'feminine'
        data = data[data[col[1]].str.match(self.personality)]
        activities = data[col[0]].tolist()
        # print(activities)
        preferences = data[col[2]].tolist()
        # print(preferences)
        counts = []
        for p in preferences:
            if preference == p:
                counts.append(3)
            elif preference == 'neutral':
                counts.append(2)
            else:
                counts.append(1)
        s = sum(counts)


        counts = [c / s for c in counts] 
        samples = stats.rv_discrete(values=(np.arange(len(counts)), counts)).rvs(size=num_activities)
        return list(set([activities[s] for s in samples]))
    

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
        
    def to_dict(self):
        return {'name': self.name,
                'gender': self.gender,
                'county': self.county,
                'race': self.race,
                'personality': self.personality,
                'highschool': self.highschool,
                'hometown': self.hometown,
                'phone': self.phone,
                'email': self.email,
                'activites': self.activities,
                'clubs': self.clubs}


    def __str__(self):
        if self.personality == 'normie':
            s1 = random.choice(name_intro_normie) + self.name + random.choice(name_intro_normie_2) + string.capwords(self.race) + ". "
            s2 = (("He " if self.gender is "male" else "She ") +
                  "went to " + self.highschool + ". ")
            finalsentecne = s1 + s2
            return finalsentecne

        else:

            s1 = (self.name +
                  " is a " +
                  string.capwords(self.race) + " " +
                  self.gender +
                  " from " + string.capwords(self.hometown) + ". ")
            s2 = (("He " if self.gender is "male" else "She ") +
                  "went to " + self.highschool + ". ")
            s3 = ("He likes " if self.gender is "male" else "She likes ")
            for i, a in enumerate(self.activities):
                if i == len(self.activities) - 1:
                    if len(self.activities) == 1:
                        s3 = a + '. '
                    else:
                        s3 = s3 + 'and ' + a + '. '
                else:
                    s3 = s3 + a + ', '
            if len(self.clubs) == 0:
                s5 = ""
            else:
                s5 = ("He is a part of " if self.gender is "male" else "She is a part of ")
                for i, a in enumerate(self.clubs):
                    if i == len(self.clubs) - 1:
                        if len(self.clubs) == 1:
                            s5 = 'member of ' + a + ". "
                        else:
                            s5 = s5 + 'and ' + a + '. '
                    else:
                        s5 = s5 + a + ', '

            s4 = (" Contact them at " +
                  self.phone + " or " +
                  self.email)

            finalsentecne = s1 + s2 + s3 + s5 + s4

            return finalsentecne

    """data = pd.read_csv('activities.csv')
    col = data.columns
    active = ['normie', 'brogrammer', 'alternative']
    if self.personality in active:
        num_activities = random.randint(2, 5)
    else:
        num_activities = random.randint(2, 3)
    preference = 'masculine' if self.gender is 'male' else 'feminine'
    data = data[data[col[1]].str.match(self.personality)]
    activities = data[col[0]].tolist()
    print(activities)
    preferences = data[col[2]].tolist()
    print(preferences)
    counts = []
    for p in preferences:
        if preference == p:
            counts.append(3)
        elif preference == 'neutral':
            counts.append(2)
        else:
            counts.append(1)
    s = sum(counts)
    counts = [c / s for c in counts]
    samples = stats.rv_discrete(values=(np.arange(len(counts)), counts)).rvs(size=num_activities)
    return list(set([activities[s] for s in samples]))"""


    def get_clubs(self):
        data = pd.read_csv('clubs.csv')
        col = data.columns
        active = ['nerd', 'tryhard']
        if self.personality in active:
            num_activities = random.randint(1, 4)
        else:
            num_activities = random.randint(0, 3)
        preference = 'masculine' if self.gender is 'male' else 'feminine'
        revised_data = data[data[col[1]].str.match(self.personality)].append(data[data[col[1]].str.match('normie')])
        activities = revised_data[col[0]].tolist()
        gender_preferences = revised_data[col[4]].tolist()
        personality_preferences = revised_data[col[1]].tolist()
        counts = []

        for i in range(len(revised_data)):
            if revised_data.iloc[i]['gender'] == preference:
                counts.append(5)
            elif revised_data.iloc[i]['gender'] == 'none':
                counts.append(3)
            else:
                counts.append(1)

            if revised_data.iloc[i]['religon'] == self.religion:
                counts[-1] *= 1.5

            if revised_data.iloc[i]['race'] == self.race:
                counts[-1] *= 1.5

        s = sum(counts)
        # print(s)
        counts = [c / s for c in counts]
        samples = stats.rv_discrete(values=(np.arange(len(counts)), counts)).rvs(size=num_activities)
        clubs1 =(list(set([activities[s] for s in samples])))
        return clubs1


    def get_religion(self):
        relig = random.choice(religions)
        return relig


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
