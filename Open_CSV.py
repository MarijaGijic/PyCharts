import csv
import pandas as pd

with open("data.csv") as csv_file: 
  csv_reader = csv.DictReader(csv_file) #---> u sledecem redu je alternativa
  
data = pd.read_csv("data.csv")      # pandas komanda za citanje csv fajla
ids = data["Responder_ID"]          # odvajanje po koloni koja se ovako zove (broj korisnika(popularnost)) ovo ne koristimo
lang_responses = data ["LanguagesWorkedWith"]  # takodje odvajanje po koloni (programming languages)
