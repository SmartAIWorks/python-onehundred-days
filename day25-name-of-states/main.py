

import csv
import pandas as p

def main():
    with open('weather_data.csv') as f:
        #contents = f.readlines()
        #print(contents)

        # data = csv.reader(f)

        # for row in data:
        #     print(row)

     #read_using_pandas()

     convert_delimited_to_csv('804241.txt')
     convert_csv_to_delimited('output.csv')

def convert_delimited_to_csv(file, delimiter: str = '|'):
   df = p.read_csv(file, sep=delimiter, dtype='str')
   df.to_csv("output.csv", index=False)

def convert_csv_to_delimited(file, delimiter: str = '|'):
   df = p.read_csv(file, sep=',', dtype='str')
   #df = df.map(lambda x: x.strip('"') if isinstance(x, str) else x)
   df.to_csv('input.csv', sep=delimiter,quoting=0)
   

def read_using_pandas():
    contents = p.read_csv('weather_data.csv')
    print(contents)

    print(contents['temp'].to_list())
    

if __name__ == '__main__':
    main()