import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Loading dataset
df= sns.load_dataset("iris")

#Details
print ("Shape: ")
print (df.shape)
print ("\nColumn Names: ")
print (df.columns.tolist())
print ("\n Columns Details")
print (df.head())
print ("\nStatistical details")
print (df.describe())
print("\nColumn Datatypes and Null Entries Count")
print (df.info())

#Plot
sns.set_style("whitegrid")
plt.figure(figsize = (8, 6))
sns.scatterplot( data= df, x= "sepal_length", y= "sepal_width", hue= "species")
plt.title("Scatterplot: Sepal Lenght vs Sepal Width", fontsize= 16)
plt.show()
print ("Scatter Plot✔")
plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x="petal_length", y="petal_width", hue= "species")
plt.show

#histogram
print("Histogram of all Features✔")
df.hist(figsize=(12,8), bins=15, edgecolor= "black")
plt.suptitle("Histogram of all features", fontsize= 16)
plt.show()

# boxplots to identfiy outliers:
print("Boxplot by species✔")
plt.figure(figsize=(14,8))

plt.subplot (2,2,1)
sns.boxplot(data=df, x="species", y="sepal_length")
plt.title("Sepal Length")

plt.subplot(2,2,2)
sns.boxplot(data=df, x="species", y="sepal_width")
plt.title("Sepal Width")

plt.subplot(2,2,3)
sns.boxplot(data=df, x= "species", y="petal_length")
plt.title("Petal Length")

plt.subplot(2,2,4)
sns.boxplot(data=df, x= "species", y= "petal_width")
plt.title("Petal Width")

plt.tight_layout()
plt.show()




