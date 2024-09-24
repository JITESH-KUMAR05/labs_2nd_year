import pandas as pd

data = {
    "Name":["JK","Kamal","Varshith"],
    "Age" : [19,20,21],
    "Section":["C","B","A"]
}
df = pd.DataFrame(data)
print(df)