# Introduksjon til prosjektet mitt



Jeg vil gjerne introdusere dere for mitt prosjekt, som har sitt utspring fra en tidligere jobb jeg hadde som mekaniker på et sykkelverksted i byen. Etter hver reparasjon måtte vi dokumentere hva som ble gjort, hvem som jobbet på oppdraget, og hva det kostet. Dessverre var systemet vi brukte både tungvint og lite brukervennlig, noe som førte til frustrasjon i hverdagen.

For terminoppgaven min bestemte jeg meg derfor for å utvikle et mer brukervennlig system. Selv om prosjektet langt fra er ferdig, har jeg kommet i gang og lagt grunnlaget for noe jeg ønsker å jobbe videre med fremover. Ambisjonene mine har kanskje vært litt høye, men dette er en start, og jeg ser frem til å dele det jeg har gjort så langt med dere.


```markdown
# Prosess fra å legge til reparasjon til visning i listen

Denne prosessen beskriver hvordan en reparasjon blir lagt til i systemet og deretter vises i listen over reparasjoner.

---

## 1. **Brukerinteraksjon: index.html**

### Fil: `index.html` (linjenumre fra originalfilen)

```html
30  <form id="repairForm">
31      <label for="mechanic">Mekaniker-ID:</label>
32      <input type="text" id="mechanic" name="mechanic_id" required>
33
34      <label for="description">Beskrivelse:</label>
35      <input type="text" id="description" name="description" required>
36
37      <label for="totalPrice">Totalpris:</label>
38      <input type="number" id="totalPrice" name="total_price" required>
39      <button type="submit" class="button-89">Legg til Reparasjon</button>
40  </form>
```

> **Notater:**  
> - Inputfeltene har `required`-attributtet for å sikre at brukeren fyller ut alle felter.  
> - Skjemaet har `id="repairForm"`, som brukes til å legge til en event listener i `script.js`.

---

## 2. **Frontend-prosess: script.js**

### Fil: `script.js` (linjenumre fra originalfilen)

```javascript
78  document.getElementById('repairForm').addEventListener('submit', async (e) => {
79      e.preventDefault(); // Forhindrer sideoppdatering
80
81      const mechanicId = document.getElementById('mechanic').value;
82      const description = document.getElementById('description').value;
83      const totalPrice = document.getElementById('totalPrice').value;
84
85      // Send dataene til backend
86      const response = await fetch('/add_repair', {
87          method: 'POST',
88          headers: { 'Content-Type': 'application/json' },
89          body: JSON.stringify({
90              mechanic_id: mechanicId,
91              description: description,
92              total_price: totalPrice
93          })
94      });
95
96      const result = await response.json();
97      alert(result.message);
98
99      // Oppdater listen over reparasjoner
100     loadRepairs();
101 });
```

> **Notater:**  
> - `fetch` sender dataene som en JSON-struktur til `/add_repair`-ruten i backend.  
> - Funksjonen `loadRepairs()` kalles etter at reparasjonen er lagt til, for å oppdatere visningen.

---

## 3. **Backend-prosess: app.py**

### Fil: `app.py` (linjenumre fra originalfilen)

```python
45  @app.route('/add_repair', methods=['POST'])
46  def add_repair():
47      data = request.get_json()  # Hent JSON-data fra forespørselen
48      mechanic_id = data['mechanic_id']
49      description = data['description']
50      total_price = data['total_price']
51
52      # Legg til reparasjonen i databasen
53      repair = Repair(
54          mechanic_id=mechanic_id,
55          description=description,
56          total_price=total_price
57      )
58      db.session.add(repair)
59      db.session.commit()
60
61      return jsonify({"message": "Reparasjonen er lagt til"})
```

> **Notater:**  
> - `request.get_json()` henter data sendt fra frontend.  
> - En ny reparasjon blir lagt til i databasen ved å bruke SQLAlchemy.  

---

## 4. **Oppdatering av reparasjonslisten**

- Når funksjonen `loadRepairs()` i `script.js` kalles, sendes en GET-forespørsel til `/repairs`-ruten for å hente oppdaterte data.

### Fil: `script.js` (linjenumre fra originalfilen)

```javascript
103 async function loadRepairs() {
104     const response = await fetch('/repairs');
105     const repairs = await response.json();
106
107     const repairList = document.getElementById('repairList');
108     repairList.innerHTML = ''; // Tøm listen før oppdatering
109
110     repairs.forEach(repair => {
111         const listItem = document.createElement('li');
112         listItem.textContent = `${repair.description} - Kr ${repair.total_price} (Mekaniker: ${repair.mechanic_id})`;
113         repairList.appendChild(listItem);
114     });
115 }
```

> **Notater:**  
> - Funksjonen oppdaterer en HTML-liste med reparasjonene hentet fra serveren.  
> - Hver reparasjon vises med beskrivelse, pris og mekaniker-ID.  

---

## Overordnet flyt

1. Brukeren fyller ut skjemaet i `index.html` og sender inn data.
2. `script.js` sender data til backend via en POST-forespørsel.
3. Backend legger til reparasjonen i databasen og returnerer en bekreftelse.
4. Reparasjonslisten oppdateres ved å hente data fra serveren og vise dem i frontend.
```

