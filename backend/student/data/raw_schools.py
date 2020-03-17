import string
import pandas as pd
import csv

counties = ['alameda', 'alpine', 'amador', 'butte', 'calaveras', 'colusa', 
            'contra costa', 'del norte', 'el dorado', 'fresno', 'glenn',
            'humboldt', 'imperial', 'inyo', 'kern', 'kings', 'lake',
            'lassen', 'los angeles', 'madera', 'marin', 'mariposa',
            'mendocino', 'merced', 'modoc', 'mono', 'monterey', 'napa',
            'nevada', 'orange', 'placer', 'plumas', 'riverside',
            'sacramento', 'san benito', 'san bernardino', 'san diego',
            'san francisco', 'san joaquin', 'san luis obispo', 'san mateo',
            'santa barbara', 'santa clara', 'santa cruz', 'shasta', 'sierra',
            'siskiyou', 'solano', 'sonoma', 'stanislaus', 'sutter', 'tehama',
            'trinity', 'tulare', 'tuolumne', 'ventura', 'yolo', 'yuba']

christians = ['Catholic', 'Diocesan', 'Independent', 'Protestant',
              '7th Day Adventist', 'Non-denominational', 'Episcopal',
              'Lutheran', 'Baptist', 'Seventh-Day Adventist', 
              'Non-Denominational', 'Nonsectarian']


def main():
    with open('raw_schools.txt', 'r') as sfile:
        data = []
        current_county = None
        current_city = None
        current_religion = 'None'
        for i, l in enumerate(sfile):
            l = l.strip()
            if '(' in l and ')' in l:
                l = l[:l.index('(')] + l[l.index(')') + 1:]
            if '<' in l:
                l = l[len('<light>'):] if '<light>' in l else l[len('<dark>'):] 
                if 'District' in l:
                    current_city = l.split(' Un')[0]
                elif ',' in l:
                    tok = l.split(',')
                    data.append((tok[0].strip(), tok[1].strip(), current_county.strip(), current_religion))
                else:
                    data.append((l.strip(), string.capwords(current_county.strip()), current_county.strip(), current_religion))    
            else:
                done = False
                for c in counties:
                    if l == string.capwords(c) + " County": 
                        current_county = c
                        done = True
                        break
                if not done:
                    if l in christians:
                        print(i)
                        current_religion = 'Christian'
                    elif l == 'Jewish':
                        current_religion = 'Jewish'
                    elif 'Private' in l or 'Public' in l:
                        current_religion = 'None'

        df = pd.DataFrame(data, columns=['School', 'City', 'County', 'Religion'])
        df.to_csv('schools.csv')
if __name__ == '__main__':
    main()
