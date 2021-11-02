import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

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
data3 = pd.read_csv('https://public.tableau.com/s/sites/default/files/media/fifa18_clean.csv', header=0, index_col=False)

df.sort_values(by="Age")
df[['First Name', 'Last Name']] = df.Name.str.split(" ", expand=True)

covid = pd.read_csv('number-of-community-cases-by-age.csv', header=0, parse_dates=True)
covid2 = covid.pivot(index="pr_date", columns="age_group", values="count_of_case")
covid2.plot()

# Other Graphs
covid2.plot.hist(subplots=True, layout=(3, 2), figsize=(10, 10), bins=20)  # Histogram
covid2.plot.bar()  # Bar Chart
covid2.plot.area()  # Area Chart
covid2.plot.barh(stacked=True)  # Horizontal Bar

fig = plt.figure()
plt.xticks(rotation=45, ha="right", rotation_mode="anchor")
plt.subplots_adjust(bottom=0.2, top=0.9)
plt.ylabel("No of Infections")
plt.xlabel("Date")

color = ['red', 'green', 'blue', 'orange', 'purple', 'black']


def chartfunc(i=int):
    plt.legend(covid2.columns)
    p = plt.plot(covid2[:i].index, covid2[:i].values)
    for i in range(0, 6):
        p[i].set_color(color[i])


animator = ani.FuncAnimation(fig, chartfunc, interval=100)
animator.save("covid.gif")