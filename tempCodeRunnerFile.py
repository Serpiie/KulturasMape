import csv
import pandas as pd
input_file = csv.DictReader(open("Muzeji_2020.csv", encoding="utf8"))

pd.DataFrame.from_dict(input_file, orient='index')