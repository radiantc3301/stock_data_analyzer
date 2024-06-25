import pandas as pd
from datetime import date,timedelta
from jugaad_data.nse import stock_df
import yfinance as yf
import plotly.graph_objs as go
import plotly.io as pio
# Download bhavcopy
file_path = 'my.csv'
df = pd.read_csv(file_path)
mylist=(df["SYMBOL"])
Stock_list_Complete=[]
for i in range(len(mylist)):
    Stock_list_Complete.append(mylist[i])
def Graph_develop(Stock_list,time_scale):
    if(time_scale=="daily"):
        no_yrs=1
    if(time_scale=="weekly"):
        no_yrs=4
    if(time_scale=="monthly"):
        no_yrs=7
    my_set=[]
    for i in range(len(Stock_list)):
        stock_index=Stock_list_Complete.index(Stock_list[i])
        X_set=[]
        series=df['SERIES'][stock_index]
        my_data = yf.download(Stock_list[i]+".NS",period=str(no_yrs)+"y",interval='1d')
        y_values=find_set(my_data,time_scale)
        for j in range(len(y_values)):
            if(time_scale=="daily"):
                X_set.append("Day"+str(j+1))
            if(time_scale=="monthly"):
                X_set.append("Month"+str(j+1))
            if(time_scale=="weekly"):
                X_set.append("Week"+str(j+1))
        trace=go.Scatter(x=X_set,y=y_values,mode='lines',name=Stock_list[i])
        my_set.append(trace)
    layout = go.Layout(
            title='Variation of stock price vs time',
            xaxis=dict(title='Time scale'),
            yaxis=dict(title='Price of Stock'),
            height=750,  # Set the height (in pixels) of the graph
            width=1600    # Set the width (in pixels) of the graph
    )
    # layout = go.Layout(title='Variation of stock price vs time', xaxis=dict(title='Time scale'), yaxis=dict(title='Price of Stock'))
    fig=go.Figure(data=my_set,layout=layout)
    return fig.to_html(full_html=False)
def find_set(my_data,time_scale):
    Data_values=[]
    My_sum=0
    for i in range(len(my_data)):
        if(time_scale=="daily"):
            Data_values.append(my_data["Close"][i])
        if(time_scale=="weekly"):
            if(i%5!=4):
                My_sum=My_sum+my_data["Close"][i]
            else:
                My_sum=(My_sum+my_data["Close"][i])/5
                Data_values.append(My_sum)
                My_sum=0
        if(time_scale=="monthly"):
            if(i%22!=21):
                My_sum=My_sum+my_data["Close"][i]
            else:
                My_sum=(My_sum+my_data["Close"][i])/22
                Data_values.append(My_sum)
                My_sum=0
    return Data_values