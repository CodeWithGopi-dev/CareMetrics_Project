CREATE DATABASE caremetrics;
USE caremetrics;
CREATE TABLE patients (
  patient_id INT PRIMARY KEY,
  name VARCHAR(100),
  age INT,
  gender VARCHAR(10)
);

CREATE TABLE appointments (
    appointment_id INT PRIMARY KEY,
    patient_id INT,
    department VARCHAR(50),
    doctor_id INT,
    appointment_time DATETIME
);

CREATE TABLE admissions (
    admission_id INT PRIMARY KEY,
    patient_id INT,
    admit_time DATETIME,
    discharge_time DATETIME,
    ward VARCHAR(50)
);

CREATE TABLE events (
    event_id INT PRIMARY KEY,
    patient_id INT,
    event_type VARCHAR(50),
    timestamp DATETIME
);

INSERT INTO patients VALUES
(1, 'Rahul', 25, 'Male'),
(2, 'Anita', 30, 'Female'),
(3, 'Kiran', 40, 'Male'),
(4, 'Sneha', 35, 'Female'),
(5, 'Arjun', 28, 'Male');

INSERT INTO appointments VALUES
(101, 1, 'Cardiology', 201, '2026-04-19 09:00:00'),
(102, 2, 'Neurology', 202, '2026-04-19 09:30:00'),
(103, 3, 'Orthopedics', 203, '2026-04-19 10:00:00'),
(104, 4, 'General', 204, '2026-04-19 10:30:00'),
(105, 5, 'Dermatology', 205, '2026-04-19 11:00:00');

INSERT INTO admissions VALUES
(201, 1, '2026-04-19 08:50:00', '2026-04-20 10:00:00', 'Ward A'),
(202, 2, '2026-04-19 09:20:00', '2026-04-20 11:30:00', 'Ward B'),
(203, 3, '2026-04-19 09:50:00', '2026-04-21 09:00:00', 'Ward A'),
(204, 4, '2026-04-19 10:10:00', '2026-04-20 14:00:00', 'Ward C'),
(205, 5, '2026-04-19 10:40:00', '2026-04-20 16:00:00', 'Ward B');

INSERT INTO events VALUES
-- Patient 1
(1, 1, 'registration', '2026-04-19 08:30:00'),
(2, 1, 'consultation', '2026-04-19 09:15:00'),
(3, 1, 'diagnostics', '2026-04-19 09:45:00'),
(4, 1, 'billing', '2026-04-19 10:15:00'),
(5, 1, 'discharge', '2026-04-20 10:00:00'),

-- Patient 2
(6, 2, 'registration', '2026-04-19 09:00:00'),
(7, 2, 'consultation', '2026-04-19 09:50:00'),
(8, 2, 'diagnostics', '2026-04-19 10:30:00'),
(9, 2, 'billing', '2026-04-19 11:00:00'),
(10, 2, 'discharge', '2026-04-20 11:30:00');

SELECT * FROM patients;
SELECT * FROM events;

SELECT 
    e1.patient_id,
    TIMESTAMPDIFF(MINUTE, e1.timestamp, e2.timestamp) AS wait_time_minutes
FROM events e1
JOIN events e2 
    ON e1.patient_id = e2.patient_id
WHERE e1.event_type = 'registration'
AND e2.event_type = 'consultation';


SELECT 
    AVG(TIMESTAMPDIFF(MINUTE, e1.timestamp, e2.timestamp)) AS avg_wait_time
FROM events e1
JOIN events e2 
    ON e1.patient_id = e2.patient_id
WHERE e1.event_type = 'registration'
AND e2.event_type = 'consultation';

SELECT 
    e1.patient_id,
    TIMESTAMPDIFF(MINUTE, e1.timestamp, e2.timestamp) AS consult_to_diag_delay
FROM events e1
JOIN events e2 
    ON e1.patient_id = e2.patient_id
WHERE e1.event_type = 'consultation'
AND e2.event_type = 'diagnostics';

SELECT 
    e1.patient_id,
    TIMESTAMPDIFF(MINUTE, e1.timestamp, e2.timestamp) AS diag_to_billing_delay
FROM events e1
JOIN events e2 
    ON e1.patient_id = e2.patient_id
WHERE e1.event_type = 'diagnostics'
AND e2.event_type = 'billing';

SELECT 
    e1.patient_id,
    TIMESTAMPDIFF(MINUTE, e1.timestamp, e2.timestamp) AS billing_to_discharge_delay
FROM events e1
JOIN events e2 
    ON e1.patient_id = e2.patient_id
WHERE e1.event_type = 'billing'
AND e2.event_type = 'discharge';

SELECT 
    HOUR(timestamp) AS hour,
    COUNT(*) AS patient_count
FROM events
GROUP BY hour
ORDER BY patient_count DESC;

CREATE USER 'gopi'@'localhost' IDENTIFIED BY '1234';
GRANT ALL PRIVILEGES ON caremetrics.* TO 'gopi'@'localhost';
FLUSH PRIVILEGES;

SELECT user, host FROM mysql.user;
GRANT ALL PRIVILEGES ON caremetrics.* TO 'gopi'@'localhost';
FLUSH PRIVILEGES;