import streamlit as st

st.title("HI")

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset (replace 'FBI_dataset.csv' with your actual dataset file)
data = pd.read_csv('FBI_dataset.csv', usecols=['DATA_YEAR', 'OFFENSE_SUBCAT_NAME'])

# Filter data for 'Commercial Sex Acts' and 'Involuntary Servitude' offense subcategories
filtered_data = data[data['OFFENSE_SUBCAT_NAME'].isin(['Commercial Sex Acts', 'Involuntary Servitude'])]

# Group data by year and offense subcategory, count reported cases
grouped_data = filtered_data.groupby(['DATA_YEAR', 'OFFENSE_SUBCAT_NAME']).size().unstack().reset_index()

# Create the visualization (grouped bar chart)
plt.figure(figsize=(10, 6))

bar_width = 0.35
index = grouped_data.index

plt.bar(index, grouped_data['Commercial Sex Acts'], bar_width, label='Commercial Sex Acts')
plt.bar(index + bar_width, grouped_data['Involuntary Servitude'], bar_width, label='Involuntary Servitude')

plt.xlabel('Year')
plt.ylabel('Total Reported Cases')
plt.title('Reported Human Trafficking Cases by Offense Subcategory (2013-2021)')
plt.xticks(index + bar_width / 2, grouped_data['DATA_YEAR'])
plt.legend()
plt.tight_layout()

# Display the chart using Streamlit
st.pyplot(plt)

