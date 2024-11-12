-- Opprett databasen
CREATE DATABASE IF NOT EXISTS bike_workshop;

-- Bruk databasen
USE bike_workshop;

-- Opprett tabellen for mekanikere
CREATE TABLE IF NOT EXISTS Mechanics (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone_number VARCHAR(20)
);

-- Opprett tabellen for produkter
CREATE TABLE IF NOT EXISTS Products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2)
);

-- Opprett tabellen for reparasjoner
CREATE TABLE IF NOT EXISTS Repairs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    mechanic_id INT,
    description TEXT,
    total_price DECIMAL(10, 2),
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (mechanic_id) REFERENCES Mechanics(id) ON DELETE SET NULL
);

-- Opprett tabellen for reparasjonsdetaljer (hvilke produkter som ble brukt)
CREATE TABLE IF NOT EXISTS RepairDetails (
    repair_id INT,
    product_id INT,
    work TEXT,
    FOREIGN KEY (repair_id) REFERENCES Repairs(id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES Products(id) ON DELETE CASCADE
);
