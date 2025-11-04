
SELECT
    t1.participants_id,    -- table participants
    t1.age,
    t1.pregnancies,

    t2.participants_id,    -- table metabolic_measurements
    t2.glucose,
    t2.bloodpressure,
    t2.bmi,
    t2.outcome,

-- feature engineering: fasting duration calculation
    EXTRACT(EPOCH FROM (
        CASE
            WHEN t3.first_meal_time < t3.last_meal_time THEN (t3.first_meal_time + interval '24 hours') - t3.last_meal_time
            ELSE t3.first_meal_time - t3.last_meal_time
        END
    )) / 3600 AS fasting_duration_hours  -- fasting duration in hours

FROM
    participants t1   -- principal table
INNER JOIN
    metabolic_measurements t2 ON t1.participants_id = t2.participants_id  -- metabolic measurements table
INNER JOIN
    fasting_info t3 ON t1.participants_id = t3.participants_id;  -- fasting info table

-- Note: The fasting duration is calculated by considering the time difference between the last meal and the first meal.

