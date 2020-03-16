import pandas as pd
with open('areacode.txt', 'r') as infile:
    data = []
    code = None
    for line in infile:
        line = line.strip()
        if line.isnumeric():
            code = line
        else:
            data.append((code, line))
    df = pd.DataFrame(data, columns = ['code', 'city'])
    df.to_csv('areacodes.csv')
