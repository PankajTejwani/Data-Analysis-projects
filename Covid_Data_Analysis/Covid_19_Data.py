
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
Covid_19 = pd.read_csv(r"covid_19_data.csv")

# Shows not null values in dataset, Null values means missing values
Covid_19.count()

#show null values total in each column
Covid_19.isnull().sum()

#data visual of null values using heatmap
sns.heatmap(Covid_19.isnull())
plt.show()

Covid_19.head(3)
Covid_19.groupby('Region').sum()

# Region with  maximum number of confirm cases were recorded
Covid_19.groupby('Region').Confirmed.sum().sort_values(ascending= False)

# Region with  minimmum number of deaths cases were recorded
Covid_19.groupby('Region').Deaths.sum().sort_values(ascending= True).head(50)

#print(Covid_19[Covid_19.Region == 'India'])

#remove all the data where casess are less than 10
Covid_19[Covid_19.Confirmed < 10]

# for temporary delete the data 
Covid_19[~Covid_19.Confirmed < 10]

# for Permanent delete the data 
Covid_19 = Covid_19[~Covid_19.Confirmed < 10]

