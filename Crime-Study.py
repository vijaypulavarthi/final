#!/usr/bin/env python
# coding: utf-8

# ### Table of Contents <a class="anchor" id="FBI_crime_toc"></a>
# 
# * [Table of Contents](#FBI_crime_toc)
#     * [Page 1 - Introduction](#FBI_crime_page_1)
#     * [Page 2 - Explanation of Data](#FBI_crime_page_2)
#     * [Page 3 - Importing Libraries and Reading in the Data](#FBI_crime_page_3)
#     * [Page 4 - A Preliminary Look at Data Types](#FBI_crime_page_4)
#     * [Page 5 - Exploratory Data Analysis](#FBI_crime_page_5)
#     * [Page 6 - Graphing Relationships](#FBI_crime_page_6)
#     * [Page 7 - Rankings with the Highest Occurrences of Human Trafficking](#FBI_crime_page_7)
#     * [Page 8 - Nevada Highlighted ](#FBI_crime_page_8)
#     * [Page 9 - Conclusions and Findings](#FBI_crime_page_9)
#     

# <hr style="height:10px;border-width:0;color:midnightblue;background-color:midnightblue">
# 
# # Page 1 - Introduction<a class="anchor" id="FBI_crime_page_1"></a>
# 
# [Back to Top](#FBI_crime_toc)
# 
# <hr style="height:10px;border-width:0;color:midnightblue;background-color:midnightblue">

# 
# #### Assignment:  For the exercise, we'd like you to download historical crime data from the FBI Crime Data Explorer for the U.S. and create a script for analyzing it using Python. Please write a brief overview explaining the methodology you used and any trends/observations you take away from the data. You are free to set the parameters for types of crime you want to analyze and the time frame.
# 
# --- 
# 

# <p style="text-align: center ">
#   <img  src="https://crime-data-explorer.fr.cloud.gov/assets/images/fbi-logo.png" width="200" height = "100" alt="FBI Logo">
# </p>
# 

#  ---
#  Human trafficking is a significant issue in this country, and the topic of sex trafficking is of great importance. In this exercise, I will be examining a human trafficking dataset compiled from various local, state, city, county, and federal agencies reporting human trafficking cases in the United States from 2013-2021. The dataset, which can be found __[at this link here](https://crime-data-explorer.fr.cloud.gov/pages/downloads#nibrs-downloads)__, includes totals by state and offense for both commercial sex acts and involuntary servitude. 
#   
#   By analyzing this data, we can better understand the prevalence of human trafficking in different regions of the country and potentially identify connections to specific groups or areas. To analyze the dataset, I will use Python and several libraries such as matplotlib, seaborn, numpy, and pandas. After cleaning and preprocessing the data, I will use visualizations and statistical techniques to identify trends and patterns in the data, such as using bar charts, scatter plots, and line graphs to visualize the number of human trafficking cases over time or by location. By using these tools, we can gain a deeper understanding of the issue of human trafficking and work towards finding solutions to prevent future tragedies.
# 
# 

# <hr style="height:10px;border-width:0;color:midnightblue;background-color:midnightblue">
# 
# # Page 2 - Explanation of Data <a class="anchor" id="FBI_crime_page_2"></a>
# 
# [Back to Top](#FBI_crime_toc)
# 
# <hr style="height:10px;border-width:0;color:midnightblue;background-color:midnightblue">

# Below are explanations of what is found in each column of the Human Trafficking dataset.  <br>
# 
# * __DATA_YEAR__ – The year in which the incident occurred.  <br>
# 
# * __ORI – ORIGINATING AGENCY IDENTIFIER (ORI)__ - This identifies the agency in which the offense occurred.  <br>
# 
# * __PUB_AGENCY_NAME__ – Agency name as it appears in FBI UCR Publications.  <br>
# 
# * __PUB_AGENCY_UNIT__ – The specific unit name for which a Publication Agency report UCR data as.  <br>
# 
# * __AGENCY_TYPE_NAME__ – Type of agency that reports UCR data (city/county/federal agency, etc).  <br>
# 
# * __STATE_ABBR__ – This is the state abbreviation.  <br>
# 
# * __STATE_NAME__ – Full name of the state.  <br>
# 
# * __DIVISION_NAME__ – The geographic division in which the agency is located.  <br>
# 
# * __COUNTY_NAME__ – The name of the county within the state.  <br>
# 
# * __REGION_NAME__ – Geographic region in which the agency is located.  <br>
# 
# * __POPULATION_GROUP_CODE__ – Group 0 is possessions; 1-7 are cities; 8-9 are counties.  <br>
# 
# * __POPULATION_GROUP_DESC__ – The name of the population groups.  <br>
# 
# * __OFFENSE_SUBCAT_ID__ – A numeric code assigned to the Offense_Subcat_Name.  <br>
# 
# * __ACTUAL_COUNT__ – Total number of Human Trafficking offenses reported to the UCR Program.  <br>
# 
# * __UNFOUNDED_COUNT__ – Total number of false or baseless complaints reported to the UCR Program from law enforcement agencies.  <br>
# 
# * __CLEARED_COUNT__ – Total number of Human Trafficking offenses that were cleared or closed.  <br>
# 
# * __JUVENILE_CLEARED_COUNT__ – Total number of Human Trafficking offenses that involved a juvenile offender that were cleared or closed.  <br>
# 
# * __OFFENSE_SUBCAT_NAME__ 
#     - Commercial Sex Acts – Human trafficking commercial sex acts is defined as inducing a person by force, fraud, or coercion to participate in commercial sex acts, or in which the person induced to perform such act(s) has not attained 18 years of age.  <br>
# 
#     - Involuntary Servitude –Human trafficking involuntary servitude is defined as the obtaining of a person(s) through recruitment, harboring, transportation, or provision, and subjecting such persons by force, fraud, or coercion into involuntary servitude, peonage, debt bondage, or slavery __(not to include commercial sex acts)__.  <br>
# 

# <hr style="height:10px;border-width:0;color:midnightblue;background-color:midnightblue">
# 
# # Page 3 - Importing Libraries and Reading in the Data <a class="anchor" id="FBI_crime_page_3"></a>
# 
# [Back to Top](#FBI_crime_toc)
# 
# <hr style="height:10px;border-width:0;color:midnightblue;background-color:midnightblue">

# In[1]:


import pandas as pd
import seaborn as sns
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display, HTML
import requests, io
from zipfile import ZipFile


# #### Importing file from the FBI website, so anyone can replicate the results. 

# In[2]:


url = 'https://s3-us-gov-west-1.amazonaws.com/cg-d4b776d0-d898-4153-90c8-8336f86bdfec/HT_2013-2021.zip'
filename = 'HT_2013-2021.csv'
r = requests.get(url)
z = ZipFile(io.BytesIO(r.content))
z.extractall()


# In[3]:


df = pd.read_csv(filename, sep=',')


# In[4]:


# df = pd.read_csv(r"Data\fbi human trafficking FL.csv") #importing data with relative path 


# <hr style="height:10px;border-width:0;color:midnightblue;background-color:midnightblue">
# 
# # Page 4 - Preliminary Look at Data Types <a class="anchor" id="FBI_crime_page_4"></a>
# 
# [Back to Top](#FBI_crime_toc)
# 
# <hr style="height:10px;border-width:0;color:midnightblue;background-color:midnightblue">

# In[5]:


#looking at first five rows. Note Python starts counting at zero (is zero indexed).

df.head()


# #### We can see a mix of data types: numbers, words and NaN, which are null values. This is a cell in which no information was entered during the data entry portion of the process.

# #### Count of rows, standard deviations, percentiles, minimum and maximums for numeric values and frequency of categorical, or non-numeric values.

# In[6]:


display(HTML("<center><h1>Numeric Columns</h1></center>"))


# In[7]:


round(df.describe(),1)


# In[8]:


# frequency of non numeric values

display(
    HTML("<center><h1>Categorical Columns</h1></center>"),
    HTML("<center><h3>Descriptive Statistics</h3></center>"),
    df.describe(include = ['O']) 
)


# In[9]:


# checking data types - are dates in date format, numbers read as numeric, etc.
df.info()


# <hr style="height:10px;border-width:0;color:midnightblue;background-color:midnightblue">
# 
# # Page 5 - Exploratory Data Analysis<a class="anchor" id="FBI_crime_page_5"></a>
# 
# [Back to Top](#FBI_crime_toc)
# 
# <hr style="height:10px;border-width:0;color:midnightblue;background-color:midnightblue">

# #### Taking a look at percentage of total of data points there are for each value in a row/column for each column in the dataset. 
# 

# In[10]:


for i in df.columns:
    display(pd.DataFrame(round(df[i].value_counts(normalize=True)*100,2)))


# In[11]:


print ("\033[1mPercentage of total with null values for:\033[0m\n")
for i in df.columns:
    if df[i].isna().sum():
        print (i, round(df[i].isna().sum()/len(df),3), "%")


# #### Unfounded Count has 1,969 blank values accounting for 63.6% of the dataset, and Public Agency Unit has 2,867 null values for 92.5% of the dataset. There are three apiece for Population Group Code and Population Group Desc. accounting for just .1% of the dataset (minimal).  It seems that Unfounded_Count null values likely can be interpreted as zero; that who did data entry just left that blank if there were none. 
# 
# ### Also taking note of the fact there are 1,684 entries where zero cases were cleared, or resolved in a year, is really disturbing to me. What percentage of the data is this occurrence, again? That warrants a closer look:

# In[12]:


#finding Top 10 percentages of unsolved cases  
display (pd.DataFrame (df['CLEARED_COUNT'].value_counts(normalize = True)*100).head(10))


# ### Just over half of the cases in this entire 8-year dataset remain unsolved? Is this possible? This would warrant a deeper examination. 
# 
# Next I'll look at which agencies are reporting, or investigating, trafficking-related crimes. 

# In[13]:


#finding percentages of reporting agencies, rounded to three decimal places.   
display (pd.DataFrame(round(df['AGENCY_TYPE_NAME'].value_counts(normalize = True)*100,3)))


# In[14]:


df.DATA_YEAR.value_counts(ascending = True)
# There has been increasing participation since the inception of data collection. It's possible that data was only partially reported in 2013. 


# In[15]:


df.AGENCY_TYPE_NAME.value_counts()


# In[16]:


df.AGENCY_TYPE_NAME.value_counts()


# In[17]:


#checking number of rows and columns in the dataset
df.shape


# #### There are 3098 rows with 19 columns
# 
# Next I'd like to look at just tribal agencies who filed criminal trafficking reports. 

# In[18]:


df.query("AGENCY_TYPE_NAME.str.contains ('Tribal')")


# #### Note that county name is not specified on tribal lands, nor in federal cases. Next I'll look at Florida cases.

# In[19]:


df.query("STATE_ABBR.str.contains ('FL')")


# #### Now to look at the county in Florida where I live.
# 

# In[20]:


df.query("COUNTY_NAME.str.contains ('SEMINOLE')")


# #### Seminole County, Florida has reported four of the eight years. They are reporting a 100% success rate for solving cases in every year reported. 

# #### Next uneder the magnifying glass is departments reporting juvenile cases that have been solved: 

# In[21]:


df.query("JUVENILE_CLEARED_COUNT > 0")


# #### Listed above are jurisdictions with juvenile cases that were cleared, or solved. There are 103 rows of information submitted from different agencies. Here we see that several counties can be listed in one cell, making this an unreliable cell to classify. 

# ### Based on graphs found on the next page, I'm going to focus on Nevada state information for a moment, along with my home state of Florida.  I'll sort data based on number of cases in Nevada and Florida, returning top 15 number of cases in a given year.

# In[22]:


df_sorted_state = df.loc[(df.STATE_NAME.isin(['Nevada', 'Florida'])) & (df.OFFENSE_SUBCAT_NAME == 'Commercial Sex Acts'), ['DATA_YEAR', 'STATE_NAME','ACTUAL_COUNT']].sort_values(by='ACTUAL_COUNT', ascending = False)
df_sorted_state.head(15)


# #### Nevada has held the top 6 spots statewide before Florida makes its first appearance in this list in 2020 with 5,888 cases. 

# In[23]:


# # group state cases by year for involuntary servitude

# df_group_year = df[df.OFFENSE_SUBCAT_NAME.isin(['Involuntary Servitude'])].agg('sum').reset_index().groupby('DATA_YEAR').sort_values(by='ACTUAL_COUNT', ascending=False)



# <hr style="height:10px;border-width:0;color:midnightblue;background-color:midnightblue">
# 
# # Page 6 - Graphing Relationships <a class="anchor" id="FBI_crime_page_6"></a>
# 
# [Back to Top](#FBI_crime_toc)
# 
# <hr style="height:10px;border-width:0;color:midnightblue;background-color:midnightblue">

# ## Visualizing some of the relationships

# #### Sorting number of reported cases in descending order and assigned to a new variable name, then using matplotlib to design a graph showing cases reported by state. 
# 

# In[24]:


df_sorted = df.sort_values('ACTUAL_COUNT', ascending = False)


# In[25]:


plt.style.use("fivethirtyeight")
plt.subplots (figsize = (20,8))
plt.xticks(rotation = 90)
plt.title("Reported Cases by State")
plt.bar(df_sorted["STATE_NAME"], df_sorted["ACTUAL_COUNT"])


# #### This graph is what led me to look more closely at Nevada, and a closer look at more specific granular data follows on page 2. 
# 
# Note that this style graph could be used to further answer a question of "safest states," or something similar. 

# #### As shown below, the average actual count of human trafficking offenses have increased over the years, or reporting of them has increased. It's important to take into account that 2013 may have only had partial reporting and should not be included in any summary statistics. 
# 

# In[26]:


df.groupby('DATA_YEAR')
plt.plot(df.groupby('DATA_YEAR').sum().ACTUAL_COUNT.index, df.groupby('DATA_YEAR').sum().ACTUAL_COUNT.values)
plt.title ("Aggregated Reported Cases by Year")         
plt.show()


# #### Creating a line plot of the number of solved cases each year, showing a general trend down. 
# 

# In[27]:


sns.lineplot(x="DATA_YEAR", y="CLEARED_COUNT", data=df)


# In[28]:


sns.catplot(x="ACTUAL_COUNT", y="REGION_NAME", data=df)


# In[29]:


max_REGION_NAME = df['REGION_NAME'].value_counts().index[0]
print('Region with highest occurrence:', max_REGION_NAME)


# #### Above, note the number of reported cases each year by region - with the west showing the highest data points recorded but a larger number of cases, or data points overall in the South. 

# In[30]:


sns.catplot(x="ACTUAL_COUNT", y="STATE_NAME", data=df, height = (10)).set(title = "All Reported Cases of Trafficking by State")


# #### In the graph above, we see reports of trafficking for each state. Each dot is a reporting agency and Nevada far and away has greater numbers of cases reported by some six departments. Texas is second, with Kentucky showing a high case count for one of its reporting agencies. 

# #### Actual count is actually a binary either/or category of crimes that are sex acts or are not sex acts.  What's the breakdown of each?
# 

# In[31]:


plt.figure(figsize=(10,10))
plt.title("Breakdown of Reported Offenses involving Sex Acts or Not")
sns.stripplot(x="OFFENSE_SUBCAT_NAME", y="ACTUAL_COUNT", data=df, hue= "OFFENSE_SUBCAT_NAME", linewidth=2,size=10)
plt.show()


# #### We can see in the graph above the instances of reported agency cases occurring in greater amounts in the blue Commercial Sex Acts. 
# 
# 
# #### Below, the number of times each subcategory offense is listed, or mentioned, in the dataset and the overall percentage of total for each.
# 

# In[32]:


df["OFFENSE_SUBCAT_NAME"].value_counts(),df["OFFENSE_SUBCAT_NAME"].value_counts(normalize = True)*100


# #### Breakdown of each crime reported by year 
# 

# In[33]:


sns.lmplot(x="DATA_YEAR", y="ACTUAL_COUNT", hue="OFFENSE_SUBCAT_NAME", data=df)


# #### Sex trafficking-related crimes are in blue, and we can see more instances of them being reported at higher aggregate numbers. Involuntary servitude is in red, and is reported in low quantities, with a few outlying instances. 

# <hr style="height:10px;border-width:0;color:midnightblue;background-color:midnightblue">
# 
# # Page 7- Rankings With Highest Occurrences of Human Trafficking <a class="anchor" id="FBI_crime_page_7"></a>
# 
# [Back to Top](#FBI_crime_toc)
# 
# <hr style="height:10px;border-width:0;color:midnightblue;background-color:midnightblue">

# #### Ranking of top 30 states with overall highest occurrences for all of the past 8 years

# In[34]:


df[['STATE_NAME','ACTUAL_COUNT']].groupby('STATE_NAME').sum().sort_values(by=['ACTUAL_COUNT'], ascending = False).head(30)


# In[ ]:





# In[35]:


print (" ")

max_county_name = df['COUNTY_NAME'].value_counts().index[1] #first occurrence was "Unspecified"
max_state_crime = df['STATE_NAME'].value_counts().index[0]
max_POPULATION_GROUP_DESC = df['POPULATION_GROUP_DESC'].value_counts().index[0]
max_REGION_NAME = df['REGION_NAME'].value_counts().index[0]
print('County with highest occurrence of human trafficking', max_county_name)
print('State with highest occurrence of human trafficking:', max_state_crime)
print('Metropolitan size with highest occurrence:', max_POPULATION_GROUP_DESC)
print('Region with highest occurrence:', max_REGION_NAME)


# <hr style="height:10px;border-width:0;color:midnightblue;background-color:midnightblue">
# 
# # Page 8 - Nevada Highlighted <a class="anchor" id="FBI_crime_page_8"></a>
# 
# [Back to Top](#FBI_crime_toc)
# 
# <hr style="height:10px;border-width:0;color:midnightblue;background-color:midnightblue">

# #### By far, Nevada has the most reported cases of human trafficking. Let's take a closer look at just Nevada for now. 

# In[36]:


df_nevada = df.loc[df["STATE_NAME"] == "Nevada", :]


# In[37]:


# Make a copy of the DataFrame
df_nevada_copy = df_nevada.copy()


# In[38]:


# Group the data by COUNTY_NAME and compute the rank of ACTUAL_COUNT within each group
df_nevada_copy.loc[:, "ACTUAL_COUNT_RANK"] = df_nevada_copy.groupby("COUNTY_NAME")["ACTUAL_COUNT"].rank(method="dense")


# In[41]:


# Create a catplot to display the ACTUAL_COUNT_RANK column
sns.catplot(x="COUNTY_NAME", y="ACTUAL_COUNT", data=df_nevada, height = (10))


# In[42]:


# Create a barplot to display the ACTUAL_COUNT_RANK column
sns.barplot(x="COUNTY_NAME", y="ACTUAL_COUNT_RANK", data=df_nevada_copy)


# In[43]:


sns.barplot(y="PUB_AGENCY_NAME", x="ACTUAL_COUNT", data=df_nevada_copy)


# #### Las Vegas Metro PD has by far, the most cases with over 200 casinos in Las Vegas alone. Reno, a smaller casino town, trails in second place. Is there a correlation with casinos? Or just with Sin City?
# To test that theory, I'll check with __[CasinoUSA](https://www.casinousa.com/map)'s__ lineup of casino locations.
# 
# * Atlantic City, NJ - Atlantic County
#     - New Jersey ranks 45 of 50 states. 
#   <br>  
#   <br>
# * Tulsa Oklahoma (primarily Native American tribal casinos, so federal/tribal jurisdiction only).
# * Seattle - Washington State is not a location that many people associate with gambling, but this state has the biggest density of land-based casinos in America, with most located in the state’s biggest city. Located in King County. 
# * The state of Pennsylvania is relatively new on the gambling landscape since the laws legalizing casino gaming have been passed only in the last decade or so. 
#     - PA ranks 35 on the list. 
# 
# ####  From this precursory glance, there seems to be no correlation initially, at least, with the presence of casinos. If I were to continue beyond the scope of this analysis, I would look more closely at potential relationships. 
# 

# In[44]:


from IPython.display import IFrame
IFrame("https://www.casinousa.com/map", 1100,500)


# <hr style="height:10px;border-width:0;color:midnightblue;background-color:midnightblue">
# 
# # Page 9 - Conclusions and Findings <a class="anchor" id="FBI_crime_page_9"></a>
# 
# [Back to Top](#FBI_crime_toc)
# 
# <hr style="height:10px;border-width:0;color:midnightblue;background-color:midnightblue">

# Based on the analysis, I have observed that Nevada had the highest overall occurrences of human trafficking, with cases focused in the Las Vegas Metropolitan Police Department reporting area. Hennepin County, Minnesota had the highest number of cases among for all counties in the United States. The western region is showing the highest individual data points recorded but a larger overall number of cases regionally in the South.
# 
# Data reporting has steadily increased each year since reporting began in 2013. It’s important to note that reporting may be incomplete or partial in 2013 and should be taken into account when comparing to other years in the dataset. 
# In this 8-year dataset, there were a total of 13056 reported cases of human trafficking, 3264 of which were deemed unfounded and 6976 cases were solved, or cleared. 
# 
# Over 64% of city police departments are reporting human trafficking cases.  County law enforcement departments make up 25% of reporting, with state police bringing in 8% of reported cases and Tribal police departments reporting just .3% of cases overall. While Seminole County, Florida has reported four of eight years, they are reporting a 100% success rate for solving cases in every year reported.
# 
# 
# That’s not the case for other departments. 
# 
# Just like getting to know people, the more we interact with something, the more we get to know it and are sometimes surprised by what we learn. For purposes of practicing curiosity, if I were to continue studying this data, I would immediately dig deeper into the fact that some __54.35%__  of the human trafficking cases reported to the FBI are going unsolved each year. That seems a grave number to admit and warrants more investigation. Assuming one person equals one case, that’s 6080 people who continue to be victimized, subjected into slavery, sexual or otherwise in this country, since 2013. This is a huge concern and has eclipsed my initial questions. 
# 

# In[ ]:





# In[ ]:




