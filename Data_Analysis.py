import pandas as pd
import csv
import plotly_express as px

df = pd.read_csv(
    "C:/Users/sraav_1jk4baa/OneDrive/Desktop/WhitehatJr Python/Projects/Data Analysis By Visualization/Data.csv")

data = df.groupby(['level', 'student_id'], as_index=False).mean()

fig = px.scatter(data, x="student_id", y="level", color="attempt", size="attempt",
                 title="The Average Attempts of Each Student In Each Level")

fig.show()
