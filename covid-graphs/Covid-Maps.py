#get altair library for data vis
#"as alt" import altair with the alias alt
import altair as alt
#get pandas - data maniputlation and tables
import pandas as pd
import requests

ny_data_url = 'https://api.covidtracking.com/v1/states/ny/daily.json'

#request to url
r = requests.get(ny_data_url)
#decode response to json
ny_data = r.json()
data = alt.Data(values = ny_data)

chart1 = alt.Chart(data).mark_line().encode(
    x = alt.X('date:N', axis = alt.Axis(title = 'March 03, 2020 - December 03, 2020', labels = False)),
    y = alt.Y('positiveIncrease:Q', axis = alt.Axis(title = '')),
    color = alt.Color('state:N', legend=alt.Legend(title="State"))

    ).properties(
        width = 700
    )

url_CA_Data = 'https://api.covidtracking.com/v1/states/ca/daily.json'

r = requests.get(url_CA_Data)

CAData = r.json()

#altair Data object

data2 = alt.Data(values=CAData)

chart2 = alt.Chart(data2).mark_line().encode(
    x = alt.X('date:N', axis = alt.Axis(title = 'March 03, 2020 - December 03, 2020', labels = False)),
    y = alt.Y('positiveIncrease:Q', axis = alt.Axis(title = '')),
    color = alt.Color('state:N', legend=alt.Legend(title="State"))

    ).properties(
        width = 700
    )

url_NH_Data = 'https://api.covidtracking.com/v1/states/nh/daily.json'
r = requests.get(url_NH_Data)
NHData = r.json()
#altair Data object
data3 = alt.Data(values=NHData)

chart3 = alt.Chart(data3).mark_line().encode(
    x = alt.X('date:N', axis = alt.Axis(title = 'March 03, 2020 - December 03, 2020', labels = False)),
    y = alt.Y('positiveIncrease:Q', axis = alt.Axis(title = '')),
    color = alt.Color('state:N', legend=alt.Legend(title="State"))

    ).properties(
        width = 700
    )

chartTotal = chart1 + chart2 + chart3
chartTotal.save('chart.html')