USE coffee_machine_manager;

-- insert data to machine

INSERT INTO machine(name, max_water_ml, max_milk_ml, max_coffee_gr, current_water_ml, current_milk_ml, current_coffee_gr)
VALUES('Lazy coffee', 2000, 500, 1000, 2000, 500, 1000);

-- insert data to receipt

INSERT INTO receipt(name, water_ml, milk_ml, coffee_gr)
VALUES
	('Americano', 50, 0, 20),
    ('Americano with milk', 50, 10, 20),
    ('Latte', 30, 30, 10);
    
-- added receipts to machine

INSERT INTO machine_receipt
VALUES
	(1, 1), (1, 2), (1, 3);
    
