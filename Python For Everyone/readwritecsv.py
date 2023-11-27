import csv

def writecsv(data):
    with open('knowlege.csv','a',newline='',encoding='utf-8') as file:
        fw = csv.writer(file) #fw = file writer
        fw.writerow(data)

    # filename = 'C:\\Users\\poohn\\AppData\\Local\\Programs\\Python\\Python311\\Python For Everyone>'
    # with open(filename,'a',newline='',encoding='utf-8') as file:


def readcsv():
    with open('knowlege.csv',newline='',encoding='utf-8') as file:
        fr = csv.reader(file)
        data = list(fr)
        print(data)

readcsv()



