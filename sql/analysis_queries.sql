# which location has most accidents

SELECT location, COUNT(*) AS total_accidents
FROM accidents
GROUP BY location
ORDER BY total_accidents DESC;

# what time do accidents occur more

;SELECT time_of_day, COUNT(*) AS total_accidents
FROM accidents
GROUP BY time_of_day
ORDER BY total_accidents DESC;

#  which vehical type is more dangerous

SELECT vehicle_type, COUNT(*) AS total_accidents
FROM vehicles
GROUP BY vehicle_type
ORDER BY total_accidents DESC;

# does wheather affect on accident sevirity

SELECT weather, severity, COUNT(*) AS total
FROM accidents
GROUP BY weather, severity
ORDER BY weather;

# Does driver behavior increase fatal accidents?

SELECT v.driver_behavior, a.severity, COUNT(*) AS total
FROM vehicles v
JOIN accidents a ON v.accident_id = a.accident_id
GROUP BY v.driver_behavior, a.severity
ORDER BY total DESC;