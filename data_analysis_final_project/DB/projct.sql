CREATE SCHEMA Bike_sharing;
go

CREATE TABLE dim_time (
    time_id INT PRIMARY KEY,
    date DATE NOT NULL,
    hour INT NOT NULL,
    day INT NOT NULL,
    day_of_week VARCHAR(20),
    month INT NOT NULL,
    year INT NOT NULL
);

CREATE TABLE dim_station (
    station_id INT PRIMARY KEY,
    station_name VARCHAR(100) NOT NULL,
    latitude DECIMAL(9,6) NOT NULL,
    longitude DECIMAL(9,6) NOT NULL
);

CREATE TABLE dim_user (
    user_id INT PRIMARY KEY,
    birth_year INT,
    age INT,
    gender VARCHAR(10),
    user_type VARCHAR(50)
);

CREATE TABLE fact_trips (
    trip_id INT PRIMARY KEY,
    start_time DATETIME NOT NULL,
    end_time DATETIME NOT NULL,
    duration_sec INT NOT NULL,
    bike_id INT NOT NULL,
    start_station_id INT NOT NULL,
    end_station_id INT NOT NULL,
    user_id INT NOT NULL,
    time_id INT NOT NULL,

    CONSTRAINT fk_start_station FOREIGN KEY (start_station_id)
        REFERENCES dim_station(station_id),

    CONSTRAINT fk_end_station FOREIGN KEY (end_station_id)
        REFERENCES dim_station(station_id),

    CONSTRAINT fk_user FOREIGN KEY (user_id)
        REFERENCES dim_user(user_id),

    CONSTRAINT fk_time FOREIGN KEY (time_id)
        REFERENCES dim_time(time_id)
);