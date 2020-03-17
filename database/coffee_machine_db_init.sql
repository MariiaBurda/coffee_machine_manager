CREATE DATABASE coffee_machine_manager;
USE coffee_machine_manager;

CREATE TABLE receipt(
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(20),
water_ml INT, 
milk_ml INT,
coffee_gr INT
);

CREATE TABLE machine(
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(20),
max_water_ml INT, 
max_milk_ml INT,
max_coffee_gr INT,
current_water_ml INT, 
current_milk_ml INT,
current_coffee_gr INT
);

CREATE TABLE machine_receipt(
machine_id INT,
receipt_id INT,
PRIMARY KEY(machine_id,receipt_id),
   FOREIGN KEY(machine_id) 
       REFERENCES machine(id),
   FOREIGN KEY(receipt_id) 
       REFERENCES receipt(id)
); 

CREATE TABLE history(
id INT AUTO_INCREMENT PRIMARY KEY,
machine_id INT,
receipt_id INT,
date DATETIME,
   FOREIGN KEY(machine_id) 
       REFERENCES machine(id),
   FOREIGN KEY(receipt_id) 
       REFERENCES receipt(id)
);

SHOW TABLES;
DESCRIBE receipt;
DESCRIBE machine;
DESCRIBE machine_receipt;
DESCRIBE history;
