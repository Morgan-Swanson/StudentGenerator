import os
import pandas as pd
import numpy as np
from scipy import stats 

class StatData:
    def __init__(self):
        self.genderrace_frosh_new, self.genderrace_soph_new, \
            self.genderrace_jun_new, self.genderrace_sen_new, \
            self.genderrace_jun_trans, self.genderrace_sen_trans = self.getStatData("statdata/genderrace.csv")

        self.genderrace_frosh_new = self.genderrace_frosh_new[self.genderrace_frosh_new['Gender'] != "Other"]

        self.geogender_frosh_new, self.geogender_soph_new, \
            self.geogender_jun_new, self.geogender_sen_new, \
            self.geogender_jun_trans, self.geogender_sen_trans = self.getStatData("statdata/geogender.csv")

        self.geogender_frosh_new = self.geogender_frosh_new[self.geogender_frosh_new['Gender'] != "Other"]

        self.georace = pd.read_csv(os.path.join(os.path.dirname(os.path.realpath(__file__)), "statdata/georace.csv"))

        self.total_students = self.getTotalStudents()
        self.class_probs = self.getClassProbs()
        self.frosh_gender_probs, self.soph_gender_probs, \
            self.jun_gender_probs, self.sen_gender_probs = self.getGenderProbs()
        self.ethnicities = ["Asian", "Hispanic Latino", "Multi", "White", "Non-Resident", "Pacific Islander", "African American"]
        self.race_probs = self.getRaceProbs()
        self.geo_areas = ["Central Coast", "Los Angeles", "Other CA Counties", "Other US States", "Sacramento Area", 
                            "San Diego", "San Francisco Bay Area", "San Joaquin"]
        self.geo_probs = self.getGeoProbs()

    def getStatData(self, filename):
        path = (os.path.realpath(__file__))
        print(path)
        df = pd.read_csv(os.path.join(os.path.dirname(os.path.realpath(__file__)),  filename))
        frosh = df[df['Cohort'] == "First-Time Freshmen Fall 2019"]
        soph = df[df['Cohort'] == "First-Time Freshmen Fall 2018"]
        jun = df[df['Cohort'] == "First-Time Freshmen Fall 2017"]
        sen = df[df['Cohort'] == "First-Time Freshmen Fall 2016"]
        jun_trans = df[df['Cohort'] == "New Transfers Fall 2019"]
        sen_trans = df[df['Cohort'] == "New Transfers Fall 2018"]

        return frosh, soph, jun, sen, jun_trans, sen_trans

    def getRaceProbs(self):
        asian = self.georace[self.georace["Federal Ethnicity"] == "Asian"]["N"].sum()
        hl = self.georace[self.georace["Federal Ethnicity"] == "Hispanic Latino"]["N"].sum()
        mult = self.georace[self.georace["Federal Ethnicity"] == "Multi"]["N"].sum()
        white = self.georace[self.georace["Federal Ethnicity"] == "White"]["N"].sum()
        nr = self.georace[self.georace["Federal Ethnicity"] == "Non-Resident"]["N"].sum()
        pi = self.georace[self.georace["Federal Ethnicity"] == "Pacific Islander"]["N"].sum()
        afam = self.georace[self.georace["Federal Ethnicity"] == "African American"]["N"].sum()
        total = asian + hl + mult + white + nr + pi + afam

        return [asian / total, hl / total, mult / total, white / total, nr / total,
                    pi / total, afam / total]

    def getGeoProbs(self):
        cc = self.georace[self.georace["Geographic Area"] == "Central Coast"]["N"].sum()
        la = self.georace[self.georace["Geographic Area"] == "Los Angeles"]["N"].sum()
        other = self.georace[self.georace["Geographic Area"] == "Other CA Counties"]["N"].sum()
        oth_states = self.georace[self.georace["Geographic Area"] == "Other US States"]["N"].sum()
        sac = self.georace[self.georace["Geographic Area"] == "Sacramento Area"]["N"].sum()
        sd = self.georace[self.georace["Geographic Area"] == "San Diego"]["N"].sum()
        sf = self.georace[self.georace["Geographic Area"] == "San Francisco Bay Area"]["N"].sum()
        sj = self.georace[self.georace["Geographic Area"] == "San Joaquin"]["N"].sum()
        total = self.georace["N"].sum() - self.georace[self.georace["Geographic Area"] == "Foreign Countries"]["N"].sum()

        return [cc / total, la / total, other / total, oth_states / total, sac / total,
                sd / total, sf / total, sj / total]

    def getTotalStudents(self):
        return self.genderrace_frosh_new.iloc[0]['Cohort Total Count'] + self.genderrace_soph_new.iloc[0]['Cohort Total Count'] + \
                self.genderrace_jun_new.iloc[0]['Cohort Total Count'] + self.genderrace_sen_new.iloc[0]['Cohort Total Count'] + \
                self.genderrace_jun_trans.iloc[0]['Cohort Total Count'] + self.genderrace_sen_trans.iloc[0]['Cohort Total Count']

    def getClassProbs(self):
        frosh = self.genderrace_frosh_new.iloc[0]['Cohort Total Count']
        soph = self.genderrace_soph_new.iloc[0]['Cohort Total Count']
        jun = self.genderrace_jun_new.iloc[0]['Cohort Total Count'] + self.genderrace_jun_trans.iloc[0]['Cohort Total Count']
        sen = self.genderrace_sen_new.iloc[0]['Cohort Total Count'] + self.genderrace_sen_trans.iloc[0]['Cohort Total Count']
        return [frosh / self.total_students, soph / self.total_students, jun / self.total_students, sen / self.total_students]

    def getGenderProbs(self):
        all_f = self.genderrace_frosh_new['N'].sum()
        f_male = self.genderrace_frosh_new[self.genderrace_frosh_new['Gender'] == 'Male']['N'].sum() / all_f
        f_female = self.genderrace_frosh_new[self.genderrace_frosh_new['Gender'] == 'Female']['N'].sum() / all_f

        all_so = self.genderrace_soph_new['N'].sum()
        so_male = self.genderrace_soph_new[self.genderrace_soph_new['Gender'] == 'Male']['N'].sum() / all_so
        so_female = self.genderrace_soph_new[self.genderrace_soph_new['Gender'] == 'Female']['N'].sum() / all_so

        all_j = self.genderrace_jun_new['N'].sum() + self.genderrace_jun_trans['N'].sum()
        j_male = (self.genderrace_jun_new[self.genderrace_jun_new['Gender'] == 'Male']['N'].sum() + \
                    self.genderrace_jun_trans[self.genderrace_jun_trans['Gender'] == 'Male']['N'].sum()) / all_j
        j_female = (self.genderrace_jun_new[self.genderrace_jun_new['Gender'] == 'Female']['N'].sum() + \
                        self.genderrace_jun_trans[self.genderrace_jun_trans['Gender'] == 'Female']['N'].sum()) / all_j

        all_sn = self.genderrace_sen_new['N'].sum() + self.genderrace_sen_trans['N'].sum()
        sn_male = (self.genderrace_sen_new[self.genderrace_sen_new['Gender'] == 'Male']['N'].sum() + \
                    self.genderrace_sen_trans[self.genderrace_sen_trans['Gender'] == 'Male']['N'].sum()) / all_sn
        sn_female = (self.genderrace_sen_new[self.genderrace_sen_new['Gender'] == 'Female']['N'].sum() + \
                        self.genderrace_sen_trans[self.genderrace_sen_trans['Gender'] == 'Female']['N'].sum()) / all_sn

        return [f_male, f_female], [so_male, so_female], [j_male, j_female], [sn_male, sn_female]

    def getClass(self):
        classes = ["first", "second", "third", "fourth"]
        index = stats.rv_discrete(values=(np.arange(len(classes)), self.class_probs)).rvs(size=1)
        
        return classes[index[0]]

    def getGender(self, year):
        gender = ["male", "female"]
        if year == "first":
            index = stats.rv_discrete(values=([0, 1], self.frosh_gender_probs)).rvs(size=1)
        elif year == "second":
            index = stats.rv_discrete(values=([0, 1], self.soph_gender_probs)).rvs(size=1)
        elif year == "third":
            index = stats.rv_discrete(values=([0, 1], self.jun_gender_probs)).rvs(size=1)
        elif year == "fourth":
            index = stats.rv_discrete(values=([0, 1], self.sen_gender_probs)).rvs(size=1)
        
        return gender[index[0]]

    def getEthnicity(self):
        index = stats.rv_discrete(values=(np.arange(len(self.ethnicities)), self.race_probs)).rvs(size=1)
        return self.ethnicities[index[0]]

    def getGeoArea(self):
        index = stats.rv_discrete(values=(np.arange(len(self.geo_areas)), self.geo_probs)).rvs(size=1)
        return self.geo_areas[index[0]]
