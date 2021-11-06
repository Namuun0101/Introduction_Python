# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 01:48:13 2021

@author: tumur
"""

#TASK 1: Matplotlib


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
gdp =pd.read_csv('data.csv', header =0)
print(gdp)

# Line graph
plt.plot(gdp.Year, gdp.Australia, label='Australia')
plt.plot(gdp.Year, gdp.Brazil, label='Brazil')
plt.title('GDP growth annual %')
plt.legend()
plt.xlabel('- Year-')
plt.ylabel('GDP growth percentage')
plt.grid(True)
plt.savefig('line.png')


# Scatter
plt.scatter(gdp.Australia, gdp.Brazil, s=10, cmap='RdBu')
plt.xlabel('Brazil')
plt.ylabel('Australia')
plt.savefig('scatter.png')


# Bar chart 
fig = plt.figure()
plt.title('Annual GDP growth of Australia and Brazil 1961-2020')
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
ax1.bar(gdp.Year, gdp.Australia)
ax2.bar(gdp.Year, gdp.Brazil)
plt.xlabel('Year')
plt.ylabel('GDP growth %')
plt.savefig('bar.png')

# Nothing /Bar chart.g ooroor hiih gej oroldson bolowch butelguitev :)
gdp.T.plot()
gdp.loc['Brazil'].plot()
years = gdp.columns
gdp_australia = gdp.loc['Australia']    
plt.style.use('ggplot')
gdp.T.plot(kind='bar')
plt.ylabel('GDP growth')


# Histogram
fig = plt.figure()
gdp_growth1 = np.array(gdp['Australia'])
gdp_growth2 = np.array(gdp['Brazil'])
print(gdp_growth1)
print(gdp_growth2)
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
ax1.hist(gdp_growth1, color='skyblue')
ax2.hist(gdp_growth2, color='red')
plt.title('GDP growth distribution of Australia and Brazil', fontsize=10, pad=20)
plt.savefig('hist.png')



# Area plot
plt.plot([],[],color='c', label='Australia', linewidth=5)
plt.plot([],[],color='g', label='Brazil', linewidth=5)
plt.stackplot(gdp.Year,gdp.Australia, gdp.Brazil, colors=['c','g'])
plt.xlabel('Years')
plt.ylabel('GDP growth')
plt.title('GDP growth rate shown by Area Plot')
plt.savefig('area.png')


# Violin plot
import matplotlib.pyplot as plt
import numpy as np
gdp =pd.read_csv('data.csv', header =0)

data_to_plot = [gdp.Australia, gdp.Brazil]
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
bp = ax.violinplot(data_to_plot)
plt.title('Violin plot of GDP growth rate of Australia and Brazil')
plt.savefig('violin.png')





# Pie chart /Songoson data deer pie chart hiihed oilgomjgui baisan uchir oor jisheeg turshij uzev/
import numpy as np
import matplotlib.pyplot as plt
  
# Creating dataset
cars = ['AUDI', 'BMW', 'FORD', 'TESLA', 'JAGUAR', 'MERCEDES'] 
data = [23, 17, 35, 29, 12, 41]

# Creating explode data
explode = (0.1, 0.0, 0.2, 0.3, 0.0, 0.0)

# Creating color parameters
colors = ( "orange", "cyan", "brown",   "grey", "indigo", "beige")
  
# Wedge properties
wp = { 'linewidth' : 1, 'edgecolor' : "green" }
  
# Creating autocpt arguments
def func(pct, allvalues):
    absolute = int(pct / 100.*np.sum(allvalues))
    return "{:.1f}%\n({:d} g)".format(pct, absolute)
  
# Creating plot
fig, ax = plt.subplots(figsize =(10, 7))
wedges, texts, autotexts = ax.pie(data, 
                                  autopct = lambda pct: func(pct, data),
                                  explode = explode, 
                                  labels = cars,
                                  shadow = True,
                                  colors = colors,
                                  startangle = 90,
                                  wedgeprops = wp,
                                  textprops = dict(color ="magenta"))
  
# Adding legend
ax.legend(wedges, cars,
          title ="Cars",
          loc ="center left",
          bbox_to_anchor =(1, 0, 0.5, 1))
  
plt.setp(autotexts, size = 8, weight ="bold")
ax.set_title("Comsimption of Top 6 cars")
  
# show plot
plt.savefig('pie.png')



#task 2: the world map

# Belen jishee code.g ashiglaad toon utguudiig ooroo garaar oruulj hiiv
import pygal as pg
from pygal.style import Style
custom_style = Style(color = '#00FFFF')
worldmap = pg.maps.world.World(style=custom_style)

print(worldmap)
worldmap.title = 'GDP of Top 15 Countries in 2020'
worldmap.add('The highest GDP', {
        'jp' : 4.91,
        'cn' : 14.86,
        'de' : 3.78,
        'gb' : 2.64,
        'in' : 2.59,
        'fr' : 2.55,
        'it' : 1.85,
        'ca' : 1.60,
        'kp' : 1.59,
        'ru' : 1.46,
        'br' : 1.36,
        'at' : 1.33,
        'es' : 1.25,
        'id' : 1.09,
        'us' : 20.81})

worldmap.render_to_file('abe.svg')
  
print("Success")


import pygal as pg #Belen jisheen deer bsan code, SupranationalWorld module.g ashiglan tiveer ni yalgaj haruulah
worldmap =  pg.maps.world.SupranationalWorld()
worldmap.title = 'Continents'
worldmap.add('Africa', [('africa')])
worldmap.add('North america', [('north_america')])
worldmap.add('Oceania', [('oceania')])
worldmap.add('South america', [('south_america')])
worldmap.add('Asia', [('asia')])
worldmap.add('Europe', [('europe')])
worldmap.add('Antartica', [('antartica')])
worldmap.render_to_file('abd.svg')

print("Success")

