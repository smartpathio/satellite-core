async function loadData() {
    try {
        const response = await fetch('data.json');
        const data = await response.json();
        const dashboard = document.getElementById('dashboard');
        dashboard.innerHTML = ''; // Czyścimy "Syncing..."

        data.forEach(item => {
            const card = document.createElement('div');
            // Jeśli score > 70 dajemy zieloną ramkę, inaczej czerwoną
            card.className = `card ${item.score > 70 ? 'high-score' : 'low-score'}`;
            
            card.innerHTML = `
                <span class="score-tag">${item.score}%</span>
                <h3>${item.market || 'PROJECT'}</h3>
                <p>${item.title || 'No Title'}</p>
                <button class="decision-btn ${item.decision.toLowerCase()}">${item.decision}</button>
            `;
            dashboard.appendChild(card);
        });
        
        document.getElementById('last-update').innerText = 'Live Data: ' + new Date().toLocaleTimeString();
    } catch (error) {
        console.error('Błąd ładowania danych:', error);
        document.getElementById('last-update').innerText = 'Data Error';
    }
}

// Funkcja obsługująca przyciski w menu
function filter(type) {
    console.log('Filtrowanie:', type);
    // Na razie przeładowujemy dane, żeby sprawdzić czy przycisk w ogóle "klika"
    loadData();
}

// Odpalamy przy starcie strony
loadData();