import streamlit


streamlit.title('my parents new healthy dinner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥬 Kale,Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard - Boiled Free - Range Egg')
streamlit.text('🍐🍞 Avokado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝')

import pandas 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')

#let's put a pick list here so they can pick the fruit they want to include
streamlit.multiselect("pick some fruits:",list(my_fruit_list.index))
#display the table on the page
streamlit.dataframe(my_fruit_list)

#let's put a pick list here so they can pick the fruit they want to include
streamlit.multiselect("pick_some_fruit:",list(my_fruit_list.index),['Avocado','Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(my_fruit_list)
