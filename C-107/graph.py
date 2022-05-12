import pandas as pd
import plotly.graph_objects as go 

file=pd.read_csv("DATA.CSV")
sd=file.loc[file["student_id"]=="TRL_987"]
a=sd.groupby("level")["attempt"].mean()
print (a)

bar1=go.Figure(go.Bar(x=a,y=["LEVEL 1","LEVEL 2","LEVEL 3","LEVEL 4"],orientation="h"))
        
bar1.show()