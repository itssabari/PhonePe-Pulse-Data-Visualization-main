# PhonePe-Pulse-Data-Visualization
Capstone Project Assigned by Guvi Institute.

 <img src="https://1000logos.net/wp-content/uploads/2022/11/PhonePe-Logo.png" width="20%" height="50%">

 The open-source platform for visualizing PhonePe pulse insights

 ## PhonePe Pulse ##

PhonePe Pulse is your window to the world of how India transacts with interesting trends, deep insights and in-depth analysis based on data put together by the PhonePe team. The goal is to extract this data and process it to obtain insights and information that can be visualized in a user-friendly manner.

### Tools and Libraries Required :
#### #️⃣ Python
Python is used for complete project processes like **extracting** the phonepe's pulse data, **transforming** to dataframe, **insert** the extracting datas into sql database and **visualizing** in streamlit.

#### 🛢 PostgreSQL
The Database used for store the extracted pulse datas and converting as structured format for merge and queries.

#### 📶 Plotly

One of the Visualization tool for viewing data's comparison and changes as charts

#### 🖥️ Streamlit 

Streamlit is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science. In just a few minutes you can build and deploy powerful data apps. So we used this for projecting insights to all users.

## Steps involved for this project :
**Data extraction**

Cloning the Github using scripting to fetching the data from the
Phonepe pulse Github repository and stored it in a suitable format such as CSV
or JSON. To clone> [GitHub](https://github.com/PhonePe/pulse).

**Data transformation**

Used a scripting language such as Python, along with
libraries such as Pandas, to manipulate and pre-process the data.

**Database insertion**

Used the "postgeresql-connector-python" library in Python to
connect to a PostgreSQL database and insert the transformed data using SQL
commands.

**Dashboard creation** 

Used the Streamlit and Plotly libraries in Python to create
an interactive and visually appealing dashboard. Plotly's built-in geo map
functions can be used to display the data on a map and Streamlit can be used
to create a user-friendly interface with multiple dropdown options for users to
select different facts and figures to display.

**Data retrieval**

Used the "pyscopg-sql-connector-python" library to connect to the
postgreSQL database and fetch the data into a Pandas dataframe. Use the data in
the dataframe to update the dashboard dynamically.

**Deployment**
Ensure the solution is secure, efficient, and user-friendly. Test
the solution thoroughly and deploy the dashboard publicly, making it
accessible to users.
