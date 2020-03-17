import pandas as pd
import csv

def main_old():
    with open('schools.txt', 'r') as sfile:
        data = []
        current_city = None
        current_county = None
        for l in sfile:
            l = l.strip()
            if l.startswith('<district>'):
                l = l[len('<district>'):]
                t = l.split(',')
                if len(t) > 1:
                    current_city = t[1].strip()
            elif l.startswith('<school>'):
                l = l[len('<school>'):]
                t = l.split(',')
                if len(t) > 1:
                    current_city = t[1].strip()
                extra = t[0].find('(')
                if extra > -1:
                    l = t[0][:extra].strip()
                else:
                    l = t[0].strip()
                data.append((l, current_city, current_county))
            else:
                current_county = l
        df = pd.DataFrame(data, columns=['School', 'City', 'County'])
        df.to_csv('schools.csv')
            
def new_schools():
    with open('schools.txt', 'r') as sfile:
        data = []
        christians = ['Catholic', 'Diocesan', 'Independent', 'Protestant',
                      '7th Day Adventist', 'Non-denominational', 'Episcopal',
                      'Lutheran', 'Baptist', 'Seventh-Day Adventist', 
                      'Non-Denominational', 'Nonsectarian']
        current_city = None
        current_county = None
        religion = 'None'
        for l in sfile:
            l = l.strip()
            if 'District' in l:
                l = l[len('<school>'):] if l.startswith('<school>') else l[len('<district>'):]
                t = l.split(',')
                if len(t) > 1:
                    current_city = t[1].strip()
            elif l.startswith('<'):
                l = l[len('<school>'):] if l.startswith('<school>') else l[len('<district>'):]
                t = l.split(',')
                extra = t[0].find('(')
                if extra > -1:
                    l = t[0][:extra].strip()
                else:
                    l = t[0].strip()
                if len(t) > 1:
                    data.append((l, t[1].strip(), current_county))
                else:
                    data.append((l, current_city, current_county))
            else:
                if l = current_county = l
        df = pd.DataFrame(data, columns=['School', 'City', 'County', 'Religion'])
        df.to_csv('schools_new.csv')
        
if __name__ == '__main__':
    new_schools()
