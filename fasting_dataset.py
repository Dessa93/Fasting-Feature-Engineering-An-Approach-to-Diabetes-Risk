
import pandas as pd
import psycopg2
from io import StringIO

# Connect to PostgreSQL database
DB_HOST = "localhost"
DB_NAME = "postgres"  
DB_USER = "postgres" 
DB_PASS = "dessa1907"

# Execute SQL query
query = """
SELECT
    t1.participants_id,    
    t1.age,
    t1.pregnancies,

    t2.participants_id,   
    t2.glucose,
    t2.bloodpressure,
    t2.bmi,
    t2.outcome,

    ABS(EXTRACT(EPOCH FROM (
    CASE
        WHEN t3.first_meal_time < t3.last_meal_time THEN (t3.first_meal_time + interval '24 hours') - t3.last_meal_time
        ELSE t3.first_meal_time - t3.last_meal_time
    END
))) / 3600 AS fasting_duration_hours

FROM
    participants t1   
INNER JOIN
    metabolic_measurements t2 ON t1.participants_id = t2.participants_id  -- metabolic measurements table
INNER JOIN
    fasting_info t3 ON t1.participants_id = t3.participants_id;
    """

conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS)
df = pd.read_sql(query, conn)
    
print("DataFrame sucessfully created!")
print(df.head())

# Close the database connection
conn.close()





