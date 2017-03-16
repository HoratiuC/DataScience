import pandas as pd
import numpy as np
import seaborn

data = pd.read_csv('C:\\Users\\HoratiuC\\Documents\\diverse\\prog\\gapminder.csv')

data.incomeperperson = data.incomeperperson.convert_objects(convert_numeric = True)
data.co2emissions = data.co2emissions.convert_objects(convert_numeric = True)
data.urbanrate = data.urbanrate.convert_objects(convert_numeric = True)

#print a sample
data = data.set_index(data.country)
print (data[['incomeperperson','co2emissions','urbanrate']].head())

#frequency of hiv rate
c1 = data.hivrate.value_counts(sort = False, dropna = False)
p1 = data.hivrate.value_counts(sort = False, normalize = True, dropna = False)
hivFreq = pd.DataFrame({'frequency': c1, 'percent': p1})
print ('Frequency distribution for HIV rate:', hivFreq)

#income categories with bins
a = 0
b = 1045
c = 4125
d = 12736
e = 100000
bins = [a,b,c,d,e]
group_names = ["Low","LowerMiddle", "UpperMiddle","High"]
categories = pd.cut(data['incomeperperson'], bins, labels = group_names)
data['incomeperpersonbins'] = categories
print (data[['incomeperperson','incomeperpersonbins']].head())

c2 = categories.value_counts(sort = False, dropna = False)
p2 = categories.value_counts(sort = False, normalize = True, dropna = False)
categFreq = pd.DataFrame({'category frequency': c2, 'percent': p2})
print ('Frequency distribution for income categories:', categFreq)

#graphs
data.hivrate = data.hivrate.astype('category')
seaborn.distplot(data['hivrate'].dropna(), kde = False, bins = 21)
plt.xlabel('HIV Rate')
plt.title('Frequency distribution')
data['hivrate'].describe()