create database accident_analysis;
use accident_analysis;

#accidents table
CREATE TABLE accidents (
    accident_id INT PRIMARY KEY,
    date DATE,
    time TIME,
    time_of_day VARCHAR(20),
    location VARCHAR(100),
    state VARCHAR(100),
    severity VARCHAR(20),
    weather VARCHAR(50),
    traffic VARCHAR(20)
);

select count(*) from accidents;

# casualties table
CREATE TABLE casualties (
    casualty_id VARCHAR(10) PRIMARY KEY,
    accident_id INT,
    injury_type VARCHAR(20),
    age INT,
    
    FOREIGN KEY (accident_id) REFERENCES accidents(accident_id)
);

select count(*) from casualties;

#vehicals table
CREATE TABLE vehicles (
    vehicle_id VARCHAR(10) PRIMARY KEY,
    accident_id INT,
    vehicle_type VARCHAR(50),
    vehicle_condition VARCHAR(20),
    driver_behavior VARCHAR(50),
    driver_age INT,
    passenger_count INT,
    
    FOREIGN KEY (accident_id) REFERENCES accidents(accident_id)
);

select count(*) from vehicles;

#road conditions table
CREATE TABLE road_conditions (
    road_id VARCHAR(10) PRIMARY KEY,
    accident_id INT,
    road_type VARCHAR(50),
    lighting VARCHAR(30),
    road_condition VARCHAR(50),
    response_time VARCHAR(20),
    
    FOREIGN KEY (accident_id) REFERENCES accidents(accident_id)
);

select count(*) from road_conditions;
