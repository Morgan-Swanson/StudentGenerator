import os
import numpy as np
import pandas as pd
import random
import csv
import string
import sys
import json
from scipy import stats
from student import Textgen

from student import generateSchedule
from student import formatstats
from student import resumefiller

import os
import bisect

class Student:
    genders = ['male', 'female']
    religions = ['christian','jewish','athiest', 'muslim', 'none']
    races = ['black', 'white', 'asian', 'hispanic', 'mixed', 'native american', 'other']
    personalities = ["normie", "stoner", "brogrammer", "tryhard", "nerd", "alternative"]
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
    county_mappings = {"Los Angeles" : "los angeles",
                        "San Francisco Bay Area" : "san francisco",
                        "Sacramento Area" : "sacramento",
                        "San Diego" : "san diego",
                        "San Joaquin" : "san joaquin"}

    def __init__(self, lastnames, boy_names, girl_names, schools, activities, areacodes, clubs, jobs, soft_skills, statdata, gender=None, year=None):
        if year:
            self.school_year = year
        else:
            self.school_year = statdata.getClass()
        self.personality = self.get_personality()
        self.last_names = lastnames
        self.boy_names = boy_names
        self.girl_names = girl_names
        self.schools = schools
        self.activities_data = activities
        self.areacodes = areacodes
        self.clubs = clubs
        if gender:
            self.gender = gender
        else:
            self.gender = statdata.getGender(self.school_year)
        self.race = statdata.getEthnicity()
        self.county = statdata.getGeoArea()
        if self.county == "Other CA Counties" or self.county == "Other US States":
            self.county = random.choice(self.counties)
        elif self.county == "Central Coast":
            self.county = random.choice(["santa barbara", "san luis obispo", "ventura", "monterey", "san benito", "santa cruz"])
        else:
            self.county = self.county_mappings[self.county]
        self.name = self.get_name()
        self.highschool, self.hometown, self.school_religion = self.get_highschool_and_hometown()
        self.phone = self.get_phone()
        self.email = self.get_email()
        self.religion = self.get_religion()
        self.activities = self.get_activities() 
        self.clubs = self.get_clubs(clubs)
        self.jobs = self.get_work(jobs)
        self.soft_skills = self.get_skills(soft_skills)
        self.specialization = self.get_specialization()
        self.key = str(abs(hash(str(self)) % 100000000))
        print(self.key)

    def draw_from_distribution(self, values, counts, num=1):

        s = sum(counts)
        p = [c / s for c in counts]
        return list(np.random.choice(values, num, p=p))


    def get_school_year(self):
        return str(random.randint(1,5))

    def get_work(self, j):
        cols = j.columns
        jobs = j[cols[0]].tolist()
        counts = j[cols[1]].tolist()
        chance = random.random()
        if self.school_year == 4 and chance < 0.85:
            if random.random() < 0.7:
                return self.draw_from_distribution(jobs, counts, 2)
            return self.draw_from_distribution(jobs, counts)
        elif self.school_year == 3 and chance < 70:
            return self.draw_from_distribution(jobs, counts)
        elif self.school_year == 2 and chance < 40:
            return self.draw_from_distribution(jobs, counts)
        elif chance < 10:
            return self.draw_from_distribution(jobs, counts)
        else:
            return []

    def get_personality(self):
        return self.personalities[random.randint(0, len(self.personalities) - 1)]

    def get_name(self):
        return self.get_first_name() + ' ' + self.get_last_name()

    def get_last_name(self):
        col = self.last_names.columns
        names = [n.lower().capitalize() for n in self.last_names[col[0]].tolist()]
        counts = [int(s.replace(",", "")) for s in self.last_names[col[1]].tolist()]
        return self.draw_from_distribution(names, counts)[0]

    def get_first_name(self):
        if self.gender is 'Male':
            col = self.boy_names.columns
            names = self.boy_names[col[0]].tolist()
            counts = self.boy_names[col[1]].tolist()
            race = self.boy_names[col[2]].tolist()
        else:
            col = self.girl_names.columns
            names = self.girl_names[col[0]].tolist()
            counts = self.girl_names[col[1]].tolist()
            race = self.girl_names[col[2]].tolist()
        return self.draw_from_distribution(names, counts)[0]

    def get_highschool_and_hometown(self):
        try:
            sample = self.schools[self.schools['County'] == self.county.lower()].sample()
            return tuple(sample[['School', 'City', 'Religion']].to_numpy()[0])
        except:
            print(self.county)

    def get_bio(self):
        if self.archetype is 'normie':
            return self.normie_bio()

    def get_email(self):
        first, last = self.name.split()
        return (first[0] + last[:random.randint(4, 8)] + "@calpoly.edu").lower()

    def get_activities(self):
        col = self.activities_data.columns
        active = ['normie','brogrammer','alternative']
        if self.personality in active:
            num_activities = random.randint(2,5)
        else:
            num_activities = random.randint(2,3)
        preference = 'masculine' if self.gender is 'Male' else 'feminine'
        data = self.activities_data[self.activities_data[col[1]].str.match(self.personality)]
        activities = self.activities_data[col[0]].tolist()
        preferences = self.activities_data[col[2]].tolist()
        counts = []
        for p in preferences:
            if preference == p:
                counts.append(3)
            elif preference == 'none':
                counts.append(2)
            else:
                counts.append(1)
        activities = self.draw_from_distribution(activities, counts, num_activities)
        return list(set(activities))
    
    def get_phone(self):
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        data_small = self.areacodes[self.areacodes['city'] == self.hometown]
        if data_small.empty:
            phone = "(" + str(self.areacodes.sample()['code'].to_numpy()[0])
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
        
    def get_clubs(self, clubs):
        # only one racial or religious club, make sure religion is the same
        df = clubs.copy()
        col = df.columns
        active = ['nerd', 'tryhard']
        if self.personality in active:
            num_activities = random.randint(1, 4)
        else:
            num_activities = random.randint(0, 3)
        preference = 'masculine' if self.gender is 'Male' else 'feminine'
        probs = np.ones(len(df))
        df['probabilities'] = probs
        df.loc[df.academic == True, 'probabilities'] *= 3.5
        df.loc[df.personality == self.personality, 'probabilities'] *= 2
        df.loc[df.personality == 'none', 'probabilities'] *= 1.5
        df.loc[df.gender == preference, 'probabilities'] *= 1.5
        df.loc[df.race == self.race, 'probabilities'] *= 1.5
        df.loc[(df.race != self.race) & (df.race != 'none'), 'probabilities'] = 0
        df.loc[df.religion == self.religion, 'probabilities'] *= 1.5
        df.loc[(df.religion != self.religion) & (df.religion != 'none'), 'probabilities'] = 0
        # revised_data = data[data[col[1]].str.match(self.personality)].append(data[data[col[1]].str.match('normie')])
        activities = df[col[0]].tolist()
        p = df['probabilities'].tolist()
        return list(set(self.draw_from_distribution(activities, p, num_activities)))

    def get_religion(self):        
        if self.school_religion != 'None':
            if random.random() < 0.7:
                return self.school_religion
            else:
                return 'none'
        elif self.personality == 'nerd':
            if random.random() < 0.5:
                return 'athiest'
            else:
                return 'none'
        else:
            s = random.random()
            if s < 0.7:
                return 'none'
            elif s < 0.88:
                return 'christian'
            elif s < 0.93:
                return 'jewish'
            elif s < 0.99:
                return 'athiest'
            else:
                return 'muslim'
            
    def to_dict(self):
        return {'name': self.name,
                'year' : self.school_year,
                'gender': self.gender,
                'county': self.county,
                'race': self.race,
                'personality': self.personality,
                'highschool': self.highschool,
                'hometown': self.hometown,
                'phone': self.phone,
                'email': self.email,
                'religion': self.religion,
                'activites': self.activities,
                'clubs': self.clubs,
                'work' : self.work}

    def __str__(self):
        return(('Year: ' + self.school_year + '\n' + 
                'Gender: ' + self.gender + '\n'+
                'Race: ' + self.race + '\n' +
                'County: ' + self.county + '\n' + 
                'Name: ' + self.name + '\n' + 
                'Personality: ' + self.personality + '\n' +
                'High School: ' + self.highschool + '\n' +
                'School Religion: ' + self.school_religion + '\n' +
                'Hometown: ' + self.hometown + '\n' +
                'Phone Number: ' + self.phone + '\n' +
                'Email: ' + self.email + '\n' +
                'Religion: ' + self.religion + '\n' +
                'Activities: ' + str(self.activities) + '\n' 
                'Clubs: ' + str(self.clubs) + '\n' + 
                'Jobs: ' + str(self.jobs) + '\n'))

    def get_skills(self, soft_skills):
        col = soft_skills.columns
        num_activities = random.randint(2, 6)
        preference = self.personality
        soft = soft_skills[col[0]].tolist()
        preferences = soft_skills[col[1]].tolist()
        counts = []
        for p in preferences:
            if preference == p:
                counts.append(7)
            else:
                counts.append(1)
        s = sum(counts)
        counts = [c / s for c in counts]
        samples = stats.rv_discrete(values=(np.arange(len(counts)), counts)).rvs(size=num_activities)
        return list(set([soft[s] for s in samples]))

    def get_specialization(self):
        data = WeightedTuple({'Back end': 25, 'Front end': 30, 'Graphics/Games': 5, 'Low level': 5, "Security": 10, "Machine Learning": 25})
        return random.choice(data)


class WeightedTuple(object):
    def __init__(self, items):
        self.indexes = []
        self.items = []
        next_index = 0
        for key in sorted(items.keys()):
            val = items[key]
            self.indexes.append(next_index)
            self.items.append(key)
            next_index += val

        self.len = next_index

    def __getitem__(self, n):
        if n < 0:
            n = self.len + n
        if n < 0 or n >= self.len:
            raise IndexError

        idx = bisect.bisect_right(self.indexes, n)
        return self.items[idx - 1]

    def __len__(self):
        return self.len


def populate_table():
    index = []
    pop = []
    sum = 0
    for c in Student.counties:
        for r in Student.races:
            for g in Student.genders:
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

def build_students(n=100, gender=None, year=None):
    index, pop = populate_table()
    total = sum(pop)
    pop = [p / total for p in pop]
    students = stats.rv_discrete(values=(np.arange(len(pop)), pop)).rvs(size=n)
    location = os.path.dirname(os.path.realpath(__file__))
    lastnames = pd.read_csv(os.path.join(location, 'data', 'lastnames.csv'))
    boy_names, girl_names = np.split(pd.read_csv(os.path.join(location, 'data', 'names.csv'), index_col=False), np.arange(3, 6, 3), axis=1)
    schools = pd.read_csv(os.path.join(location, 'data', 'schools.csv'))
    activities = pd.read_csv(os.path.join(location, 'data', 'activities.csv'))
    areacodes = pd.read_csv(os.path.join(location, 'data', 'areacodes.csv'))
    clubs = pd.read_csv(os.path.join(location, 'data', 'clubs.csv'))
    soft = pd.read_csv(os.path.join(location, 'data', 'soft_skills.csv'))
    jobs = pd.read_csv(os.path.join(location, 'data', 'jobs.csv'))
    statdata = formatstats.StatData()
    return [Student(lastnames, boy_names, girl_names, schools, activities, areacodes, clubs, jobs, soft, statdata, gender=gender, year=year) for s in students]
 
def get_students(n=100, gender=None, year=None):
    schedulegenerator = generateSchedule.ScheduleGenerator()
    S = build_students(n, gender, year)
    D = [s.to_dict() for s in S]
    schedules = [schedulegenerator.getSchedule(s.school_year, s.specialization) for s in S]
    resumefiller.generateStudentResume(S[0].name, S[0].email, S[0].phone, S[0].key, schedules[0])
    resumefiller.generateStudentBio(S[0].name, S[0].key, Textgen.getbio(S[0]))
    return D

if __name__ == '__main__':
    for s in build_students(int(sys.argv[1])):
        print(s)
    D = get_students(int(sys.argv[1]))
    sys.stdout.flush()
