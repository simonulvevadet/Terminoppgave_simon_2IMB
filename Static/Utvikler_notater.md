

```markdown
# Spørsmål og Svar: Programmeringsoppgaver

## Utvikling med Flask/PHP (Backend)

### 1. Lag en form med et input-felt, og send dataene til en annen php-side

**Svar:**  
For å lage en form med et input-felt og sende dataene til en annen PHP-side, kan du bruke følgende eksempel:

```php
<form action="mottak.php" method="post">
    <label for="inputData">Skriv inn data:</label>
    <input type="text" id="inputData" name="inputData">
    <button type="submit">Send</button>
</form>
```

Mottaksfilen (`mottak.php`) kan være slik:

```php
<?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $data = $_POST['inputData'];
        // Lagrer data i en database eller videre prosessering
    }
?>
```

### 2. Lagre informasjonen fra form-en i en database

**Svar:**  
Her er et eksempel på hvordan du kan lagre informasjon i en database:

```php
<?php
    $conn = new mysqli('server', 'brukernavn', 'passord', 'database');

    if ($conn->connect_error) {
        die("Kobling feilet: " . $conn->connect_error);
    }

    $data = $_POST['inputData'];
    $sql = "INSERT INTO tabell (kolonne) VALUES ('$data')";

    if ($conn->query($sql) === TRUE) {
        echo "Ny post lagt til.";
    } else {
        echo "Feil: " . $conn->error;
    }

    $conn->close();
?>
```

### 3. Utfør en spørring mot databasen og skriv ut resultatet i en tabell

**Svar:**  
Et eksempel på spørring og utlisting i tabellformat:

```php
<?php
    $conn = new mysqli('server', 'brukernavn', 'passord', 'database');

    if ($conn->connect_error) {
        die("Kobling feilet: " . $conn->connect_error);
    }

    $sql = "SELECT * FROM tabell";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        echo "<table><tr><th>ID</th><th>Data</th></tr>";
        while($row = $result->fetch_assoc()) {
            echo "<tr><td>" . $row["id"]. "</td><td>" . $row["kolonne"]. "</td></tr>";
        }
        echo "</table>";
    } else {
        echo "Ingen resultater";
    }

    $conn->close();
?>
```

---

## DOM-manipulering med JavaScript

### 1. Lag en knapp i HTML og referer til den i en variabel med ‘getElementById’

**Svar:**

```html
<button id="myButton">Klikk meg</button>
<script>
    var button = document.getElementById("myButton");
</script>
```

### 2. Lag en funksjon som skriver «Hei verden» i konsollet

**Svar:**

```javascript
function heiVerden() {
    console.log("Hei verden");
}
```

### 3. Koble funksjonen til knappen med addEventListener

**Svar:**

```javascript
var button = document.getElementById("myButton");
button.addEventListener("click", heiVerden);
```

---

## Utvikling/Generelt

### Funksjoner

1. **Lag en funksjon som skriver ut teksten «hei»**

**Svar:**

```javascript
function skrivHei() {
    console.log("hei");
}
```

2. **Lag en funksjon som tar imot et navn som parameter, og skriver ut dette**

**Svar:**

```javascript
function skrivNavn(navnet) {
    console.log(navnet);
}
```

3. **Lag en funksjon som returnerer en tekst**

**Svar:**

```javascript
function getTekst() {
    return "noe tekst";
}
```

4. **Lag en funksjon som tar imot et navn som parameter, og returnerer «hei [navn]»**

**Svar:**

```javascript
function heiNavn(navnet) {
    return "hei " + navnet;
}
```

### Løkker

1. **Skriv ut alle tallene fra 0 til 10 med en løkke**

**Svar:**

```javascript
for (let i = 0; i <= 10; i++) {
    console.log(i);
}
```

2. **Skriv ut alle tallene fra 30 til 15 med en løkke**

**Svar:**

```javascript
for (let i = 30; i >= 15; i--) {
    console.log(i);
}
```

3. **Skriv ut annethvert tall fra 1 til 45 med en løkke**

**Svar:**

```javascript
for (let i = 1; i <= 45; i += 2) {
    console.log(i);
}
```

### If-statements

**Svar:**

```javascript
let tall = 10;
if (tall < 0) {
    console.log("Vinter");
} else if (tall <= 20) {
    console.log("Vår eller høst");
} else {
    console.log("Sommer");
}
```

### Variabler (Datatyper)

1. **Lag en variabel som inneholder tekst**

**Svar:**

```javascript
let tekst = "Dette er en tekst";
```

2. **Lag en variabel som inneholder et heltall**

**Svar:**

```javascript
let heltall = 42;
```

3. **Lag en variabel som inneholder et desimaltall**

**Svar:**

```javascript
let desimaltall = 3.14;
```

4. **Lag en variabel som inneholder True eller False**

**Svar:**

```javascript
let boolsk = true;
```

### Arrays/Lister

1. **Lag en liste/array med fem elementer og skriv ut det 3. elementet**

**Svar:**

```javascript
let array = [1, 2, 3, 4, 5];
console.log(array[2]);  // 3
```

2. **Bytt ut verdien av det 2. elementet**

**Svar:**

```javascript
array[1] = 99;
```

3. **Lagre verdien i det 5. elementet i en egen variabel**

**Svar:**

```javascript
let femteElement = array[4];
```

4. **Skriv ut alle elementene i arrayet ved hjelp av en løkke**

**Svar:**

```javascript
for (let i = 0; i < array.length; i++) {
    console.log(array[i]);
}
```
```
