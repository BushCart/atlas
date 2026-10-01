import os
import csv
import docx


PATH = 'data/'
file = []

for i in os.listdir(PATH):
    s = os.path.getsize(PATH+i)
    file.append({'name':i,'size':s})
print(file)


def readfile(path : list):
    for i in path:
        if i['name'].split('.')[-1] == 'docx':          #библиотека textract, мб черех XML
            file_docx = docx.Document(PATH+i['name'])
            print(PATH+i['name'], ' - ', file_docx.paragraphs[0].text)
        elif i['name'].split('.')[-1] == 'csv':
            with open(PATH+i['name'], newline='') as file_csv:
                head_csv = list(csv.reader(file_csv))
                print(PATH+i['name'], ' - ', head_csv[0])
        elif i['name'].split('.')[-1] == 'txt':
            with open(PATH+i['name'], 'r') as file_txt:
                print(PATH+i['name'], ' - ', file_txt.readline())
        else:
            print('it is pdf')
    return 0

readfile(file)