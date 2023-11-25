# Install the package pymysql
!pip install pymysql

# Import the required libraries

import pandas as pd
from sqlalchemy import create_engine
import pymysql

# Create engine
engine = create_engine('mysql+pymysql://User1:123@localhost/video_games')
# Specify the connection string
conn = engine.connect()
# The data from the MySQL workbench table vgsales2016 is read into the Dataframe df in Python
df = pd.read_sql("SELECT * FROM video_games.vgsales2016", conn)
# Print DataFrame and show the first 5 raws, to check if the data has been loaded correctly
df.head()
# Print DataFrame and show the last 5 raws, to check if the data has been loaded correctly
df.tail()
#Find how many records this data frame has
df.shape

(16450, 16)

# Execute the query to answer question 1

q1_df = pd.read_sql('''SELECT CASE WHEN before2005 < after2005 THEN CONCAT("After the year 2005, Avg. Sales = ", after2005)
		ELSE CONCAT("Before the year 2005, Avg. Sales = ", before2005)
        END AS Result FROM
        (SELECT AVG(CASE WHEN Year_of_Release < 2005 THEN Global_Sales END) AS before2005,
		AVG(CASE WHEN Year_of_Release > 2005 THEN Global_Sales END) AS after2005
		FROM video_games.vgsales2016) AS Averages;''', conn)

print(q1_df)

                                              Result
0  Before the year 2005, Avg. Sales = 0.650038654...


# Execute the query

q2_df = pd.read_sql('''SELECT *,
    CASE
        WHEN Year_of_Release < 2005 THEN 'pre-2005'
        WHEN Year_of_Release > 2005 THEN 'post-2005'
        ELSE 'unknown' -- Optional, handles cases where Year_of_Release is NULL or unexpected values
    END AS Year_Label
FROM video_games.vgsales2016;''', conn)

print(q2_df)

                                Name Platform  Year_of_Release         Genre  \
0                         Wii Sports      Wii             2006        Sports   
1                  Super Mario Bros.      NES             1985      Platform   
2                     Mario Kart Wii      Wii             2008        Racing   
3                  Wii Sports Resort      Wii             2009        Sports   
4           Pokemon Red/Pokemon Blue       GB             1996  Role-Playing   
...                              ...      ...              ...           ...   
16445  Samurai Warriors: Sanada Maru      PS3             2016        Action   
16446               LMA Manager 2007     X360             2006        Sports   
16447        Haitaka no Psychedelica      PSV             2016     Adventure   
16448               Spirits & Spells      GBA             2003      Platform   
16449            Winning Post 8 2016      PSV             2016    Simulation   

          Publisher  NA_Sales  EU_Sales  JP_Sales  Other_Sales  Global_Sales  \
0          Nintendo     41.36     28.96      3.77         8.45         82.53   
1          Nintendo     29.08      3.58      6.81         0.77         40.24   
2          Nintendo     15.68     12.76      3.79         3.29         35.52   
3          Nintendo     15.61     10.93      3.28         2.95         32.77   
4          Nintendo     11.27      8.89     10.22         1.00         31.37   
...             ...       ...       ...       ...          ...           ...   
16445    Tecmo Koei      0.00      0.00      0.01         0.00          0.01   
16446   Codemasters      0.00      0.01      0.00         0.00          0.01   
16447  Idea Factory      0.00      0.00      0.01         0.00          0.01   
16448       Wanadoo      0.01      0.00      0.00         0.00          0.01   
16449    Tecmo Koei      0.00      0.00      0.01         0.00          0.01   
...
16448   pre-2005  
16449  post-2005  

[16450 rows x 17 columns]
Output is truncated. View as a scrollable element or open in a text editor. Adjust cell output settings...