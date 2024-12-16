# Utvikleroppgaver - Huskeliste for praktiske oppgaver

## Server og nettverk
- **Vis hvor du kan endre datamaskinnavnet (Windows og Linux)**  
  Svar: Endring av datamaskinnavn kan gjøres via Systeminnstillinger → System → Om, og deretter Endre datamaskinnavn.

- **Sett statisk IP 10.100.104.211 (Windows og Linux)**  
  Svar: På Windows kan statisk IP konfigureres i Nettverksinnstillinger → Egenskaper → Internet Protocol Version 4 (TCP/IPv4) → Egenskaper. På Linux konfigureres det i filen `/etc/network/interfaces`.

- **Sjekk om datamaskinen har alle de nyeste oppdateringene (Windows og Linux)**  
  Svar: På Windows kan dette gjøres i Innstillinger → Oppdatering og sikkerhet → Windows Update. På Linux kan det gjøres via `sudo apt update` eller tilsvarende kommando.

- **Sjekk om databasen er startet (Windows og Linux)**  
  Svar: For MariaDB, bruk `sudo systemctl status mariadb` på Linux eller `net start mariadb` på Windows.

- **Stopp databasen**  
  Svar: `sudo systemctl stop mariadb` på Linux eller `net stop mariadb` på Windows.

- **Start databasen**  
  Svar: `sudo systemctl start mariadb` på Linux eller `net start mariadb` på Windows.

- **Restart databasen**  
  Svar: `sudo systemctl restart mariadb` på Linux eller `net restart mariadb` på Windows.

- **Vis hvor du kan endre porten til databasen**  
  Svar: Endring av databaseport gjøres i MariaDB-konfigurasjonsfilen, ofte funnet på `/etc/my.cnf` på Linux eller i `my.ini` på Windows.

- **Åpne for port 3306 fra 10.200.12.4 i brannmuren (Windows og Linux)**  
  Svar: På Linux gjøres dette i UFW-konfigurasjonen eller direkte via `iptables`. På Windows kan dette gjøres i Brannmurinnstillinger → Avanserte innstillinger → Portåpning.

- **Bruk terminalen til å navigere frem til rotkatalogen for webserveren**  
  Svar: Naviger til `/var/www/html` på Linux eller `%SystemDrive%\inetpub\wwwroot` på Windows.

- **Lag en ny katalog/mappe som heter ‘fancymappe’**  
  Svar: Bruk kommandoen `mkdir fancymappe` i terminalen.

- **Vis IP-adressen(e) til maskinen din**  
  Svar: `ip a` på Linux eller `ipconfig` på Windows.

---

## MariaDB
- **Logg inn i databasen med en bruker med administratorrettigheter (f.eks root)**  
  Svar: `mysql -u root -p` og skriv inn passordet.

- **Vis rettighetene til brukeren**  
  Svar: Bruk `SHOW GRANTS FOR 'brukernavn'@'localhost';`.

- **Lag en ny bruker og gi denne rett til lesing i alle databaser og tabeller**  
  Svar: `CREATE USER 'nyBruker'@'localhost' IDENTIFIED BY 'passord'; GRANT SELECT ON *.* TO 'nyBruker'@'localhost';`.

- **Lag en ny database**  
  Svar: `CREATE DATABASE nyDB;`.

- **Lag en ny tabell med tre kolonner med ulike datatyper**  
  Svar: `CREATE TABLE nyTabell (id INT AUTO_INCREMENT PRIMARY KEY, navn VARCHAR(100), dato DATETIME);`.

- **Lag en tabell der en av kolonnene er fremmednøkkel til tabellen over, og lag en relasjon mellom dem**  
  Svar: `CREATE TABLE relasjonTabell (id INT AUTO_INCREMENT PRIMARY KEY, fk_id INT, FOREIGN KEY (fk_id) REFERENCES nyTabell(id));`.

- **Sett inn data i tabellene**  
  Svar: `INSERT INTO nyTabell (navn, dato) VALUES ('Eksempel', NOW());`.

- **Utfør en spørring mot tabellene**  
  Svar: `SELECT * FROM nyTabell;`.

- **Slette data**  
  Svar: `DELETE FROM nyTabell WHERE id = 1;`.

- **Endre data**  
  Svar: `UPDATE nyTabell SET navn = 'Nytt navn' WHERE id = 1;`.

- **Ta en sikkerhetskopi av dataene**  
  Svar: `mysqldump -u root -p database_name > backup.sql`.

---

## Flask/PHP (Backend)
- **Lagre informasjonen fra form-en i en database**  
  Svar: Send en POST-forespørsel til backend-endepunktet og lagre dataene i databasen.

- **Utfør en spørring mot databasen og skriv ut resultatet i en tabell**  
  Svar: Utfør en SQL-spørring og vis resultatene dynamisk i en HTML-tabell.

---

## JavaScript
- **Lag en knapp i html og referer til den i en variabel med ‘getElementById’**  
  Svar: `document.getElementById('knappID')`.

- **Lag en funksjon som skriver «Hei verden» i konsollet**  
  Svar: `function heiVerden() { console.log('Hei verden'); }`.

- **Koble funksjonen til knappen med addEventListener**  
  Svar: `knapp.addEventListener('click', heiVerden);`.

---

## Generelt
- **Funksjoner**  
  Svar: Opprett og bruk funksjoner for forskjellige operasjoner.

- **Løkker**  
  Svar: Bruk løkker for å iterere gjennom data og utføre handlinger.

- **If-statements**  
  Svar: Bruk vilkår for å håndtere ulike scenarier basert på verdier.

- **Arrays/Lister**  
  Svar: Opprett lister og bruk dem til å lagre og manipulere data.

---

## Prosess og samarbeid
- **Klone et prosjekt fra github**  
  Svar: Bruk kommandoen `git clone [repo-URL]`.

- **Vis hvordan du pusher en lokal endring til et repository**  
  Svar: `git add .`, `git commit -m "beskrivelse"`, `git push origin main`.

- **Vis hvordan du har brukt github projects til planlegging**  
  Svar: Lag oppgaver og oppgaverbrett i GitHub Projects for prosjektstyring.

---

## Drift
- **Hvordan administrerer vi AD DS**  
  Svar: Bruk Active Directory Administrative Centre for å administrere AD.

- **Hvordan setter vi opp en mapped drive**  
  Svar: `net use X: \\server\share`.

- **Hva er virtualisering**  
  Svar: Bruk av virtuelle maskiner for å kjøre flere operativsystemer på en fysisk maskin.

- **Hvordan konfigurerer du nettverket**  
  Svar: Konfigurer nettverksinnstillinger i Nettverks- og delingssenter.

- **Hvordan tester vi at systemet fungerer**  
  Svar: Utfør ulike tester som bruker systemets funksjonalitet og yteevne.

- **Hvorfor bruker vi flere AD servere**  
  Svar: For økt tilgjengelighet og feiltoleranse.

