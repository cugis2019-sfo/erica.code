import plotly
import pandas

studentlist = [["steve",32,"male"], ["Lia", 28, "female"], ["Vin", 45, "male"], ["Katie", 38, "female"]]
print(studentlist)

studentlistdf= pandas.DataFrame(studentlist, columns= ["name","age","gender"])
print(studentlistdf)



studentlistdf= pandas.DataFrame(studentlist, columns=["name","age","gender"],index=[1,2,3,4])
print(studentlistdf)



#graph our data
from plotly.offline import plot
import plotly.graph_objs as go

agename= go.Bar(x=studentlistdf["name"], y=studentlistdf["age"])

#plot([agename])

import pandas as pd
import plotly
from plotly.offline import plot


#we read the data into a dataset or dataframe called df
df= pd.read_excel("GISdata.xlsx", sheet_name= "womenOccupation")

#we use the Bar graph option of the graph_objs function from the plotly library
womenoccupation= go.Bar(x=df["occupation"], y=df["women"],

                #we add color to the graph using the jet scale
                marker= {"color": df["women"], "colorscale": "Jet"})



#we use the layout option of the graph_objs from the plotly library
titles= go.Layout(
        #define title of the graph
        title= "Percentage of Women Employed by Occupation",
        
        
        #define title for x-axis
        xaxis=go.layout.XAxis(
                title=go.layout.xaxis.Title(
                        text="Occupation",
                        )
                ),
                
                #define title for y-axis
                yaxis=go.layout.YAxis(
                        title=go.layout.yaxis.Title(
                                text="Percentage",
                                )
                        )
                )


#we use figure option of the graph_objs function from the plotly libraby
fig= go.Figure(data=[womenoccupation], layout= titles)
#fig= go.figure (data[womenOccupation])
plot(fig)    

#we call the plot function




