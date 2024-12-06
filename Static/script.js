document.getElementById('repairForm').addEventListener('submit', async (e) => {
    e.preventDefault();  // Hindrer siden fra å laste på nytt

    // Hent verdiene fra skjemaet
    const mechanicId = document.getElementById('mechanic').value;
    const description = document.getElementById('description').value;
    const totalPrice = document.getElementById('totalPrice').value;

    // Send en POST-forespørsel til backend for å lagre reparasjonen
    const response = await fetch('/add_repair', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            mechanic_id: mechanicId,
            description: description,
            total_price: totalPrice
        })
    });

    const result = await response.json();
    alert(result.message);  // Vis suksessmelding
    loadRepairs();  // Oppdater reparasjonslisten
});

// Funksjon for å hente alle reparasjoner og vise dem på siden
async function loadRepairs() {
    const response = await fetch('/repairs');
    const repairs = await response.json();

    const repairDiv = document.getElementById('repairs');
    repairDiv.innerHTML = '<h2>Liste over reparasjoner</h2>';  // Tømmer og legger til overskrift

    repairs.forEach(repair => {
        const repairElement = document.createElement('p');
        repairElement.innerText = `ID: ${repair.id}, Mekaniker ID: ${repair.mechanic_id}, Beskrivelse: ${repair.description}, Pris: ${repair.total_price}`;
        repairDiv.appendChild(repairElement);
    });
}

// Last inn reparasjoner når siden lastes
window.onload = loadRepairs;

async function searchDatabase(search) {
    const resultatContainer = document.getElementById("search-resultat");

    // Send en POST-forespørsel til backend for å sende search
    const response = await fetch('/search_query', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            search : search
        })
    });

    const result = await response.json();
    alert(result.message);  // Vis suksessmelding
}

async function deleteRepair(repairId) {
    const response = await fetch('/delete_repair', {  // Sørg for at URL-en er korrekt
        method: 'POST',  // Pass på at metoden er 'POST'
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ repairId: repairId })  // Send riktig data
    });
    

    if (response.ok) {
        const result = await response.json();
        alert(result.message); // Vis melding om suksess
        loadRepairs(); // Oppdater listen
    } else {
        console.error('Error deleting repair:', response.status);
        alert('Error: Could not delete repair.');
    }
}


// Modifiser loadRepairs-funksjonen for å legge til slett-knapp
async function loadRepairs() {
    const response = await fetch('/repairs');
    const repairs = await response.json();

    const repairDiv = document.getElementById('repairs');
    repairDiv.innerHTML = '<h2>Liste over reparasjoner</h2>';  // Tømmer og legger til overskrift

    repairs.forEach(repair => {
        const repairElement = document.createElement('div');
        repairElement.innerHTML = `
            ID: ${repair.id}, Mekaniker ID: ${repair.mechanic_id}, Beskrivelse: ${repair.description}, Pris: ${repair.total_price}
            <button onclick="deleteRepair(${repair.id})">Slett</button>
        `;
        repairDiv.appendChild(repairElement);
    });
}


body: JSON.stringify({})
