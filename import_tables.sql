-- Create the tables

CREATE TABLE participants ( 
    Participants_ID INTEGER PRIMARY KEY, 
    Age INTEGER,
    Pregnancies INTEGER
    );

CREATE TABLE metabolic_measurements (
    Participants_ID INTEGER REFERENCES participants(Participants_ID),
    Glucose INTEGER,
    BloodPressure INTEGER,
    BMI INTEGER,
    Outcome INTEGER
    );

CREATE TABLE fasting_info (
    Participants_ID INTEGER REFERENCES participants(Participants_ID),
    Last_Meal_Time TIME,
    First_Meal_Time TIME
    );



-- Insert data into the tables

\copy participants FROM 'C:/IF_Dataset/participants_info.csv' DELIMITER ',' CSV HEADER;

\copy metabolic_measurements FROM 'C:/IF_Dataset/metabolic_measurements.csv' DELIMITER ',' CSV HEADER;

\copy fasting_info FROM 'C:/IF_Dataset/fasting_info.csv' DELIMITER ',' CSV HEADER;


