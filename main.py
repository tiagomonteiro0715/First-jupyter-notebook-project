from mpl_toolkits import mplot3d
import matplotlib.pyplot as mpl
import numpy as np
import pandas as pd

df = pd.read_csv('StudentsPerformance.csv')
#make a 3d graph

studyData = {
    'study' : len(df[df['test preparation course'] == "completed"]),
    'not_study': len(df[df['test preparation course'] == "none"]),
}
studeName = list(studyData.keys())
studeval = list(studyData.values())

grade = {
    'math': df["math score"],
    'reading': df["reading score"],
    'writing': df["writing score"],
}



def study():
    mpl.bar(studeName, studeval)
    mpl.show()


def grades():
    fig = mpl.figure()
    ax = fig.add_subplot(projection='3d')

    x = grade['math']
    y = grade['reading']
    z = grade['writing']

    ax.scatter3D(x, y, z, color="green");
    mpl.title("simple 3D scatter plot")

    mpl.show()

    mpl.show()


def main():
    grades()

if __name__ == "__main__":
    main()