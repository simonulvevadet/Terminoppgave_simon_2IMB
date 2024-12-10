-- Opprett databasen
CREATE DATABASE IF NOT EXISTS bike_workshop;  -- Oppretter databasen hvis den ikke allerede eksisterer.

-- Bruk databasen
USE bike_workshop;  -- Setter 'bike_workshop' som den aktive databasen.

-- Opprett tabellen for mekanikere (Ikke i bruk enda!)
CREATE TABLE IF NOT EXISTS Mechanics (  -- Oppretter tabellen 'Mechanics' hvis den ikke allerede eksisterer.
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Primærnøkkel med automatisk inkrement for unik ID.
    name VARCHAR(100) NOT NULL,  -- Navn-kolonnen, som krever en streng på opptil 100 tegn.
    phone_number VARCHAR(20)  -- Telefonnummer-kolonnen, som kan lagre opptil 20 tegn.
);

-- Opprett tabellen for produkter (Ikke i bruk enda!)
CREATE TABLE IF NOT EXISTS Products (  -- Oppretter tabellen 'Products' hvis den ikke allerede eksisterer.
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Primærnøkkel med automatisk inkrement for unik ID.
    name VARCHAR(100) NOT NULL,  -- Produktnavn-kolonnen, som krever en streng på opptil 100 tegn.
    description TEXT,  -- Beskrivelse-kolonnen, som kan lagre lengre tekst.
    price DECIMAL(10, 2)  -- Pris-kolonnen, som lagrer desimaltall med opptil 10 sifre og 2 desimaler.
);

-- Opprett tabellen for reparasjoner
CREATE TABLE IF NOT EXISTS Repairs (  -- Oppretter tabellen 'Repairs' hvis den ikke allerede eksisterer.
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Primærnøkkel med automatisk inkrement for unik ID.
    mechanic_id INT,  -- Fremmednøkkel som refererer til en mekaniker i 'Mechanics'-tabellen.
    description TEXT,  -- Beskrivelse av reparasjonen, lagrer lengre tekst.
    total_price DECIMAL(10, 2)  -- Totalpris for reparasjonen, lagret som et desimaltall.
    -- Merk: Manglende komma på slutten her vil forårsake en SQL-syntaksfeil. Det bør fjernes.
);

-- Opprett tabellen for reparasjonsdetaljer (hvilke produkter som ble brukt)(Ikke i bruk enda!)
CREATE TABLE IF NOT EXISTS RepairDetails (  -- Oppretter tabellen 'RepairDetails' hvis den ikke allerede eksisterer.
    repair_id INT,  -- Kolonne som refererer til en reparasjon i 'Repairs'-tabellen.
    product_id INT,  -- Kolonne som refererer til et produkt i 'Products'-tabellen.
    work TEXT  -- Arbeidsbeskrivelse, som kan inneholde lengre tekst.
);
