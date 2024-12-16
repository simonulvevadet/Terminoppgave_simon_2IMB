
# Praktiske oppgaver - Fagsamtalen

## Server og nettverk

- **Vis hvor du kan endre datamaskinnavnet (Windows og Linux)**  
  Svar: Datamaskinnavnet kan endres i Windows via **Innstillinger > System > Om**. På Linux kan dette gjøres med kommandoen:  
  ```bash  
  sudo hostnamectl set-hostname nyttnavn  
  ```

- **Sett statisk IP 10.100.104.211 (Windows og Linux)**  
  Svar: I Windows: **Innstillinger > Nettverk og Internett > Rediger adapterinnstillinger**, høyreklikk nettverk og velg **Egenskaper** for IPv4.  
  På Linux:  
  ```bash  
  sudo ip addr add 10.100.104.211/24 dev eth0  
  ```

- **Sjekk om datamaskinen din har alle de nyeste oppdateringene (Windows og Linux)**  
  Svar:  
  - Windows: **Innstillinger > Windows Update**  
  - Linux:  
  ```bash  
  sudo apt update && sudo apt upgrade  
  ```

- **Sjekk om databasen er startet (Windows og Linux)**  
  Svar:  
  - Windows: **Services.msc** og søk etter databasen.  
  - Linux:  
  ```bash  
  sudo systemctl status mysql  
  ```

- **Stopp, start og restart databasen**  
  Svar:  
  - Stoppe:  
    ```bash  
    sudo systemctl stop mysql  
    ```  
  - Starte:  
    ```bash  
    sudo systemctl start mysql  
    ```  
  - Restart:  
    ```bash  
    sudo systemctl restart mysql  
    ```

- **Vis hvor du kan endre porten til databasen**  
  Svar: Konfigurasjonsfil for MariaDB:  
  ```bash  
  sudo nano /etc/mysql/mariadb.conf.d/50-server.cnf  
  ```

- **Åpne for port 3306 fra 10.200.12.4 i brannmuren**  
  Svar:  
  - Windows: **Brannmurinnstillinger > Inngående regler**, legg til ny regel for port 3306.  
  - Linux:  
  ```bash  
  sudo ufw allow from 10.200.12.4 to any port 3306  
  ```

- **Bruk terminalen til å navigere frem til rotkatalogen for webserveren**  
  Svar:  
  ```bash  
  cd /var/www/html  
  ```

- **Lag en ny katalog/mappe som heter ‘fancymappe’**  
  Svar:  
  ```bash  
  mkdir fancymappe  
  ```

- **Vis IP-adressen(e) til maskinen din**  
  Svar:  
  ```bash  
  ip a  
  ```

## MariaDB

- **Logg inn i databasen med en bruker med administratorrettigheter (f.eks root)**  
  Svar:  
  ```bash  
  mysql -u root -p  
  ```

- **Vis rettighetene til brukeren**  
  Svar:  
  ```bash  
  SHOW GRANTS FOR 'brukernavn';  
  ```

- **Lag en ny bruker og gi denne rett til lesing i alle databaser og tabeller**  
  Svar:  
  ```bash  
  CREATE USER 'ny_bruker'@'localhost' IDENTIFIED BY 'passord';  
  GRANT SELECT ON *.* TO 'ny_bruker'@'localhost';  
  ```

- **Lag en ny database**  
  Svar:  
  ```bash  
  CREATE DATABASE ny_database;  
  ```

- **Lag en ny tabell med tre kolonner med ulike datatyper**  
  Svar:  
  ```sql  
  CREATE TABLE ny_tabell (id INT AUTO_INCREMENT PRIMARY KEY, navn VARCHAR(50), dato DATE);  
  ```

- **Sett inn data i tabellene**  
  Svar:  
  ```sql  
  INSERT INTO ny_tabell (navn, dato) VALUES ('Navn', '2024-12-16');  
  ```

- **Utfør en spørring mot tabellene**  
  Svar:  
  ```sql  
  SELECT * FROM ny_tabell;  
  ```

- **Slette data**  
  Svar:  
  ```sql  
  DELETE FROM ny_tabell WHERE id = 1;  
  ```

- **Endre data**  
  Svar:  
  ```sql  
  UPDATE ny_tabell SET navn = 'Ny Verdi' WHERE id = 1;  
  ```

- **Ta en sikkerhetskopi av dataene**  
  Svar:  
  ```bash  
  mysqldump -u root -p ny_database > backup.sql  
  ```

## Flask/PHP (Backend)

- **Lag en form med et input-felt, og send dataene til en annen php-side**  
  Svar:  
  ```html  
  <form action="mottak.php" method="post">  
    <input type="text" name="inputnavn">  
    <button type="submit">Send</button>  
  </form>  
  ```

- **Lagre informasjonen fra form-en i en database**  
  Svar:  
  ```php  
  $conn = new mysqli($servername, $username, $password, $dbname);  
  $sql = "INSERT INTO tabell (felt) VALUES ('data')";  
  $conn->query($sql);  
  ```

## DOM-manipulering med JavaScript

- **Lag en knapp i html og referer til den i en variabel med ‘getElementById’**  
  Svar:  
  ```html  
  <button id="knapp1">Klikk meg</button>  
  <script>  
  let knapp = document.getElementById('knapp1');  
  </script>  
  ```

- **Lag en funksjon som skriver «Hei verden» i konsollet**  
  Svar:  
  ```javascript  
  function heiVerden() {  
    console.log('Hei verden');  
  }  
  ```

- **Koble funksjonen til knappen med addEventListener**  
  Svar:  
  ```javascript  
  knapp.addEventListener('click', heiVerden);  
  ```

## Generelt utvikling

- **Funksjoner**  
  - Lag en funksjon som skriver ut teksten «hei»  
  - Lag en funksjon som tar imot et navn som parameter, og skriver ut dette  
  - Lag en funksjon som returnerer en tekst  
  - Lag en funksjon som tar imot et navn som parameter, og returnerer «hei [navn]»

- **Løkker**  
  - Skriv ut alle tallene fra 0 til 10  
  - Skriv ut alle tallene fra 30 til 15  
  - Skriv ut annethvert tall fra 1 til 45  

- **If-statements**  
  Sjekk verdien av et tall og skriv ut vær basert på verdien.

- **Variabler (Datatyper)**  
  Lag variabler for tekst, heltall, desimaltall, og boolean.

- **Arrays/Lister**  
  Lag en liste med fem elementer og manipulér elementene.

- **Prosess og samarbeid**  
  Klon et prosjekt fra GitHub, push endringer og planlegg med GitHub Projects.

## Drift

- **Lage bruker med PowerShell**  
  ```powershell  
  New-ADUser -Name "Brukernavn" -SamAccountName "brukernavn" -AccountPassword (ConvertTo-SecureString -AsPlainText 'Passord' -Force) -Enabled $true  
  ```

- **Hvordan administrerer vi AD DS**  
  Gjennom Active Directory Administrasjonssenter eller PowerShell.

- **Hvordan setter vi opp en mapped drive**  
  Svar: **Net Use X: \\Server\Del**.

- **Hva er virtualisering**  
  Prosessen med å kjøre virtuelle maskiner på en fysisk maskin.

- **Hvordan konfigurerer du nettverket**  
  Oppsett via IP-adresser, nettverksmasker og ruting.

- **Tjenester for internett tilgang**  
  DNS, DHCP, og Internett Gateway.

- **Brannmuren/gateway**  
  Administrering av trafikk, sikkerhet og logging.

- **Testing av systemet**  
  Utføre tester som belastningstester og systemkontroller.

- **Bruk av flere AD-servere**  
  Øker tilgjengelighet og stabilitet ved feil.

```

