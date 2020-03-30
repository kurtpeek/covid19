import argparse
import requests
import pandas as pd
import matplotlib.pyplot as plt


def getdata():
    response = requests.get("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv")
    with open('data.csv', 'wb') as fp:
        fp.write(response.content)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--logarithmic", action='store_true')
    args = parser.parse_args()

    getdata()
    df = pd.read_csv('data.csv')
    dfg = df.groupby(by='Country/Region').sum()
    dfg.sort_values(by=dfg.columns[-1], ascending=False, inplace=True)
    dfg.drop(labels=['Lat', 'Long'], axis=1, inplace=True)
    dfg.columns = pd.to_datetime(dfg.columns)
    dfplot = dfg.iloc[:10].T.plot(logy=args.logarithmic, title="Covid-19 deaths", grid=True)
    plt.minorticks_on()
    plt.show()

