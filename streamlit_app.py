import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('\N{bowl with spoon} Omega 3 & Blueberry Oatmeal')
streamlit.text('\N{green salad} Kale, Spinach & Rocket Smoothie')
streamlit.text('\N{chicken} Hard-Boiled Free-Range Egg')
streamlit.text('\N{avocado} \N{bread} Avocado Toast')

streamlit.header('\N{banana} \N{mango} Build Your Own Fruit Smoothie \N{blueberries} \N{grapes}')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])

# Display the table on the page.
streamlit.dataframe(my_fruit_list)
