import pandas as pd

data = [["JK",19,"Hyd"],
        ["Kam",20,"Pat"]]
df = pd.DataFrame(data,columns=["Name","Age","City"])
print(df)