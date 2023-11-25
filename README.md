# python
Here we used a dataset 

**Getting Started**
Our goal here is to introduce fundamental data manipulation techniques using Python and a library like pandas.This project provides with tasks such as loading data, exploring its structure, cleaning inconsistencies, and performing basic analysis.

**Prerequisites**
-MySQL Workbench
-Anaconda Navigator
-DataSet

The dataset was selected from kaggle website.
MySql and Anaconda Navigator are used to analyze it.

**Running the tests**
Firstly, the dataset Video Games Sales
2016 was uploaded into SQL Workbench. Then the program was created using Python script
in the Jupyter notebook, steps are detailed in the Report and summarized below:
1. Upload the dataset to MySQL workbench: The dataset ‘vgsales2016’ was uploaded to
the MySQL workbench as a table with name vgsales2016 in the database
video_games.
2. Create User in MySQL Workbench and ensure right user privileges – A user created in
the MySQL workbench; the username and password will be used to create the
connection object. The user privileges are set up as ‘DBA’ (Database Administrator,
which gives full access to the database operations).
3. Create a Python script and ensure the correct packages are installed and libraries
imported: After ensuring that “pymysql” package is installed, the necessary libraries
i.e., pandas, sqlalchemy and pymysql are imported.
4. Using “create_engine” class from the “sqlalchemy” library we created the object
“engine” and connection is established between MySQL and Python.
5. The SQL queries along with connection object are passed as parameters to the method
read.sql() from the pandas library and the desired results /outputs are obtained.
6. The project was documented, a report was prepared with the detailed steps and a log
showing the member participation summary.

**Deployment**
- I have uploaded the python file into the repository.
- Download the file and open it with Jupyter Notebook.
- The code can be copied and the comments in the code will help you guide.
- The location of dataset has to be specified.
