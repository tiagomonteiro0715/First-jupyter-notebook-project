import matplotlib.pyplot as mpl
import numpy as np
import pandas as pd

df = pd.read_csv('StudentsPerformance.csv')
#make a 3d graph

Data = {
    'study' : len(df[df['test preparation course'] == "completed"]),
    'not_study': len(df[df['test preparation course'] == "none"]),
}
studeName = list(Data.keys())
studeval = list(Data.values())

def study():
    mpl.bar(studeName, studeval)
    mpl.show()












def main():
    study()

if __name__ == "__main__":
    main()