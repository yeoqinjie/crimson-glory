import pandas as pd

df = pd.DataFrame(
    {
        "Name": [
            "Steve Rogers",
            "Clint Barton",
            "Tony Stark",
            "Bruce Banner",
            "Natasha Romanoff"
        ],
        "Age": [103, 41, 51, 52, 37],
        "Sex": ["male", "male", "male", "male", "female"],
    }
)

data = pd.read_csv('hollywood.csv', header=0, index_col=False)
data2 = pd.read_csv('https://public.tableau.com/s/sites/default/files/media/HollywoodsMostProfitableStories.csv', header=0, index_col=False)
