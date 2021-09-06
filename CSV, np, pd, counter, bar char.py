import csv  #csv file je jednostavan  oblik fajla koji sadarzi podatke koji se koriste za baze podataka i citaju se kao sa tabele
import numpy as np
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

 #with open("data.csv") as csv_file: 
  #  csv_reader = csv.DictReader(csv_file) u sledecem redu je alternaiva za citanje fajlova -->

data = pd.read_csv("data.csv")  # pandas komanda za citanje csv fajla
ids = data["Responder_ID"]     #  odvajanje po koloni koja se ovako zove (broj korisnika(popularnost)) ovo ne koristimo
lang_responses = data ["LanguagesWorkedWith"]  # takodje odvajanje po koloni (programming languages)

language_counter = Counter()
    
   # row = next(csv_reader) #citanje jednog reda iz csv file
    # print(row["LanguagesWorkedWith"].split[";"]) #izbacivanje odredjenje reci preodjenje organizacije podataka u listu
for response in lang_responses:
    language_counter.update(response["LanguagesWorkedWith"].split[";"]) # iz row smo promenili u response
# petlja radi identicnu stvar kao i sa row-om ali ovog puta smo koristili pandas
        
languages = []       # kreiramo praznu list za x koordinatu i y
popularity = []
        
        
for item in language_counter.most_common(15):     #odavde, posto se podaci printuju u torkama izvlacimo posebno podatke
    languages.append(item[0])   # x koordinata (progaramski jezici)
    popularity.append(item[1])  # y koordinata (brojevi)
    # append-pridruziti

languages.reverse()    # menja redosled podataka od najpopularnijih do najmanje popularnih
popularity.reverse()
plt.barh(languages, popularity)  # horizontal bar char- must switch x and y labels

plt.title("Popularity of programming languages")
plt.xlabel("Popularity")
# plt.ylabe("LAnguages") - not necessary
plt.tight_layout() #prikaz
plt.show()
    
    
# from collections import Counter
# c = Counter(["Python", "JavaScript", "HTML", "C#"])
# c.update(["C++", "Python"])
# ako printujemo c -->
# Counter ({"Python": 2, "JavaScript": 1....}) --> Python:2-->broj pojavljivanja
# Counter sluzi za prebrojavanje ucestalosti bilo slova, reci, brojeva itd...
