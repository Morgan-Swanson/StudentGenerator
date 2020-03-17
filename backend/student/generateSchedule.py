import os
import random
import pandas as pd
import numpy as np
from enum import IntEnum
from scipy import stats


class Specialties(IntEnum):
    SECURITY = 0
    BACKEND = 1
    FRONTEND = 2
    GRAPHICS = 3
    LOWLEVEL = 4
    ML = 5


def getEnrollmentProbabilities():
    f18 = getEnrollments(os.path.join(os.path.dirname(os.path.realpath(__file__)), "schedules/fall2018.csv"))
    w19 = getEnrollments(os.path.join(os.path.dirname(os.path.realpath(__file__)), "schedules/winter2019.csv"))
    s19 = getEnrollments(os.path.join(os.path.dirname(os.path.realpath(__file__)), "schedules/spring2019.csv"))
    f19 = getEnrollments(os.path.join(os.path.dirname(os.path.realpath(__file__)), "schedules/fall2019.csv"))
    w20 = getEnrollments(os.path.join(os.path.dirname(os.path.realpath(__file__)), "schedules/winter2020.csv"))
    s20 = getEnrollments(os.path.join(os.path.dirname(os.path.realpath(__file__)), "schedules/spring2020.csv"))

    return [f18, w19, s19, f19, w20, s20]

def getEnrollments(filename):
    df = pd.read_csv(os.path.join(os.path.dirname(os.path.realpath(__file__)), filename), usecols=["Course", "Description", "Type", "Enrl"])
    return df[df.Type != "Lab"].reset_index(drop=True).drop("Type", axis=1)


class ScheduleGenerator:
    def __init__(self):
        self.enrollments = getEnrollmentProbabilities()
        self.third_years = self.thirdYearClasses()
        self.fourth_years = self.fourthYearClasses()
        self.specializations = {Specialties.SECURITY : ["CPE 321", "CSC 424", "CSC 429"],
                                Specialties.BACKEND : ["CSC 349", "CSC 365", "CSC 366", "CSC 468", "CSC 369"],
                                Specialties.FRONTEND : ["CSC 437", "CSC 436", "CSC 484", "CSC 486"],
                                Specialties.GRAPHICS : ["CSC 471", "CSC 476", "CSC 473", "CSC 474", "CSC 478", "CSC 371", "CSC 378", "CSC 377"],
                                Specialties.LOWLEVEL : ["CSC 453", "CPE 357", "CSC 431", "CPE 315"],
                                Specialties.ML : ["CSC 480", "CSC 481", "CSC 466", "CSC 482", "CSC 487"]}
        self.spec_mappings = {"Back end" : Specialties.BACKEND,
                                "Front end" : Specialties.FRONTEND,
                                "Graphics/Games" : Specialties.GRAPHICS,
                                "Low level" : Specialties.LOWLEVEL,
                                "Security" : Specialties.SECURITY,
                                "Machine Learning" : Specialties.ML}

    def getSchedule(self, year, specialization):
        specialization = self.spec_mappings[specialization]
        if year.lower() == "fourth":
            return self.getUpperClassSchedule(self.fourth_years.copy(deep=True), specialization)
        elif year.lower() == "third":
            return self.getUpperClassSchedule(self.third_years.copy(deep=True), specialization)
        elif year.lower() == "second":
            return self.getSecondYearSchedule()
        else:
            return self.getFirstYearSchedule()

    def thirdYearClasses(self):
        modified = []
        for df in self.enrollments[:3]:
            new_df = df.copy(deep=True)
            new_df['Enrl'] = new_df['Enrl'].mask(new_df['Course'].str.match(pat="[A-Z]{3} [143]"), 0)
            modified.append(new_df)
        
        for df in self.enrollments[3:]:
            new_df = df.copy(deep=True)
            new_df['Enrl'] = new_df['Enrl'].mask(new_df['Course'].str.match(pat="[A-Z]{3} [12]"), 0)
            new_df['Enrl'] = new_df['Enrl'].mask(new_df['Course'].str.match(pat="CSC 430|CSC 431|CSC 445|CSC 453"), 0)
            new_df['Enrl'] = new_df['Enrl'].mask(new_df['Course'].str.match(pat="[A-Z]{3} 4"), round(new_df['Enrl'] * 0.3))
            modified.append(new_df)

        return pd.concat(modified).groupby(['Course', 'Description'], as_index=False)['Enrl'].sum().reset_index(drop=True)

    def fourthYearClasses(self):
        modified = []
        for df in self.enrollments[:3]:
            new_df = df.copy(deep=True)
            new_df['Enrl'] = new_df['Enrl'].mask(new_df['Course'].str.match(pat="[A-Z]{3} [12]"), 0)
            new_df['Enrl'] = new_df['Enrl'].mask(new_df['Course'].str.match(pat="[A-Z]{3} 4"), round(new_df['Enrl'] * 0.3))
            modified.append(new_df)
        
        for df in self.enrollments[3:]:
            new_df = df.copy(deep=True)
            new_df['Enrl'] = new_df['Enrl'].mask(new_df['Course'].str.match(pat="[A-Z]{3} [12]"), 0)
            new_df['Enrl'] = new_df['Enrl'].mask(new_df['Course'].str.match(pat="[A-Z]{3} 3"), round(new_df['Enrl'] * 0.5))
            modified.append(new_df)

        return pd.concat(modified).groupby(['Course', 'Description'], as_index=False)['Enrl'].sum().reset_index(drop=True)

    def getFirstYearSchedule(self):
        return ["CPE 101 Fundamentals of Computer Science", "CPE 202 - Data Structures", "CPE 123 - Introduction to Computing"]

    def getSecondYearSchedule(self):
        classes = ["CPE 202 - Data Structures", "CPE 203 - Project-Based Object-Oriented Programming and Design",
                    "CSC 225 - Introduction to Computer Organization", "CPE 101 - Fundamentals of Computer Science",
                    "CPE 123 - Introduction to Computing", "CSC 348 - Discrete Structures",
                    "CPE 315 - Computer Architecture"]
        probs = [3, 3, 3, 3, 3, 1, 1]
        total_enroll = sum(probs)
        probs = [p / total_enroll for p in probs]

        indices = list(set(stats.rv_discrete(values=(np.arange(len(probs)), probs)).rvs(size=4)))
        return [classes[i] for i in indices]

    def getUpperClassSchedule(self, df, specialization):
        spec_multipliers_regex = "|".join(self.specializations[specialization])
        df['Enrl'] = df['Enrl'].mask(df['Course'].str.match(pat=spec_multipliers_regex), round(df['Enrl'] * 12.5))
        df = self.normalize(df)
        
        choices = list(set(stats.rv_discrete(values=(np.arange(len(df)), df['Enrl'].tolist())).rvs(size=random.randint(4,9))))
        class_choices = df.iloc[list(choices), :]
        
        # choices = list(set(stats.rv_discrete(values=(np.arange(len(df)), df['Enrl'].tolist())).rvs(size=random.randint(4,9))))
        # courses = df["Course"].tolist()
        # desc = df["Description"].tolist()
        # final_choices = [courses[i] + " - " + desc[i] for i in choices]
        
        choices = []
        for index, row in class_choices.iterrows():
            choices.append(row["Course"] + " - " + row["Description"])
        
        return choices

    def normalize(self, df):
        total_enroll = df['Enrl'].sum()
        df['Enrl'] = df['Enrl'] / total_enroll
        return df
