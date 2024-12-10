document.getElementById('repairForm').addEventListener('submit', async (e) => {
    e.preventDefault();  // Hindrer siden fra å laste på nytt når skjemaet sendes.

    // Hent verdiene fra skjemaet
    const mechanicId = document.getElementById('mechanic').value;  // Henter verdien fra inputfeltet for mekaniker-ID.
    const description = document.getElementById('description').value;  // Henter verdien fra inputfeltet for beskrivelse.
    const totalPrice = document.getElementById('totalPrice').value;  // Henter verdien fra inputfeltet for totalpris.

    // Send en POST-forespørsel til backend for å lagre reparasjonen
    const response = await fetch('/add_repair', {  // Sender forespørsel til backend-endepunktet '/add_repair'.
        method: 'POST',  // Setter HTTP-metoden til POST.
        headers: { 'Content-Type': 'application/json' },  // Angir at dataene sendes som JSON.
        body: JSON.stringify({  // Konverterer dataene til JSON-format.
            mechanic_id: mechanicId,  // Sender mekaniker-ID.
            description: description,  // Sender beskrivelsen.
            total_price: totalPrice  // Sender totalprisen.
        })
    });

    const result = await response.json();  // Henter svar fra serveren og konverterer til JSON.
    alert(result.message);  // Vis en melding til brukeren (f.eks. suksess eller feil).
    loadRepairs();  // Oppdater reparasjonslisten på siden.
});

// Funksjon for å hente alle reparasjoner og vise dem på siden
async function loadRepairs() {
    const response = await fetch('/repairs');  // Sender forespørsel til '/repairs' for å hente alle reparasjoner.
    const repairs = await response.json();  // Konverterer svaret til JSON-format.

    const repairDiv = document.getElementById('repairs');  // Henter HTML-elementet der reparasjoner skal vises.
    repairDiv.innerHTML = '<h2>Liste over reparasjoner</h2>';  // Tømmer innholdet og legger til en overskrift.

    repairs.forEach(repair => {  // Itererer gjennom listen av reparasjoner.
        const repairElement = document.createElement('p');  // Oppretter et nytt <p>-element for hver reparasjon.
        repairElement.innerText = `ID: ${repair.id}, Mekaniker ID: ${repair.mechanic_id}, Beskrivelse: ${repair.description}, Pris: ${repair.total_price}`;  // Legger til reparasjonsdetaljer.
        repairDiv.appendChild(repairElement);  // Legger til <p>-elementet i repairDiv.
    });
}

// Last inn reparasjoner når siden lastes
window.onload = loadRepairs;  // Kaller loadRepairs-funksjonen automatisk når siden er ferdig lastet.

async function searchDatabase(search) {
    const resultatContainer = document.getElementById("search-resultat");  // Henter elementet der søkeresultater skal vises.

    // Send en POST-forespørsel til backend for å sende søketeksten
    const response = await fetch('/search_query', {  // Sender forespørsel til '/search_query'.
        method: 'POST',  // Setter HTTP-metoden til POST.
        headers: { 'Content-Type': 'application/json' },  // Angir at dataene sendes som JSON.
        body: JSON.stringify({  // Konverterer dataene til JSON-format.
            search : search  // Sender søketeksten til serveren.
        })
    });

    const result = await response.json();  // Konverterer svaret til JSON.
    alert(result.message);  // Vis en melding til brukeren med resultatet.
}

async function deleteRepair(repairId) {
    const response = await fetch('/delete_repair', {  // Sender forespørsel til '/delete_repair' for å slette en reparasjon.
        method: 'POST',  // Bruker POST-metoden for slettingen.
        headers: { 'Content-Type': 'application/json' },  // Angir JSON som innholdstype.
        body: JSON.stringify({ repairId: repairId })  // Sender reparasjons-ID-en som skal slettes.
    });
    
    if (response.ok) {  // Sjekker om forespørselen var vellykket.
        const result = await response.json();  // Henter svar fra serveren og konverterer til JSON.
        alert(result.message); // Vis en melding om suksess.
        loadRepairs(); // Oppdater reparasjonslisten.
    } else {
        console.error('Error deleting repair:', response.status);  // Logger feilmeldingen hvis noe går galt.
        alert('Error: Could not delete repair.');  // Viser en feilmelding til brukeren.
    }
}

// Modifiser loadRepairs-funksjonen for å legge til slett-knapp
async function loadRepairs() {
    const response = await fetch('/repairs');  // Henter listen over reparasjoner fra backend.
    const repairs = await response.json();  // Konverterer svaret til JSON-format.

    const repairDiv = document.getElementById('repairs');  // Henter HTML-elementet for å vise reparasjoner.
    repairDiv.innerHTML = '<h2>Liste over reparasjoner</h2>';  // Tømmer innholdet og legger til en overskrift.

    repairs.forEach(repair => {  // Itererer gjennom reparasjonene.
        const repairElement = document.createElement('div');  // Oppretter en <div> for hver reparasjon.
        repairElement.innerHTML = `
            ID: ${repair.id}, Mekaniker ID: ${repair.mechanic_id}, Beskrivelse: ${repair.description}, Pris: ${repair.total_price}
            <button onclick="deleteRepair(${repair.id})">Slett</button> `;  // Legger til en knapp for å slette reparasjonen.
        repairDiv.appendChild(repairElement);  // Legger til reparasjonselementet i repairDiv.
    });
}
