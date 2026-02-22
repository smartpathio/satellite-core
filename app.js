let satelliteData = [];

// 1. Pobieranie danych
async function fetchSystemData() {
    try {
        const response = await fetch('data.json?cache=' + Date.now());
        const json = await response.json();
        
        // Wyciągamy dane z deep_analysis
        satelliteData = json.deep_analysis || [];
        
        renderCards(satelliteData);
        document.getElementById('last-update').innerText = 'SATELLITE LIVE | ' + new Date().toLocaleTimeString();
    } catch (err) {
        console.error("Błąd systemu:", err);
        document.getElementById('dashboard').innerHTML = "Błąd synchronizacji. Sprawdź VPN.";
    }
}

// 2. Renderowanie kart
function renderCards(data) {
    const container = document.getElementById('dashboard');
    container.innerHTML = '';

    if (data.length === 0) {
        container.innerHTML = '<div class="card">Brak danych w raporcie.</div>';
        return;
    }

    data.forEach(item => {
        const score = item.confidence ? Math.round(item.confidence * 100) : 0;
        const decision = (item.decision || 'WATCH').toUpperCase();
        const color = score > 70 ? '#3fb950' : '#f85149';

        const card = document.createElement('div');
        card.className = 'card';
        card.innerHTML = `
            <div class="status-tag" style="color: ${color}">${score}% CONFIDENCE</div>
            <h2>${item.niche_or_area || 'Analiza'}</h2>
            <p>${item.reason_short || 'Przetwarzanie danych rynkowych...'}</p>
            <button class="action-btn" style="background: ${decision === 'YES' || decision === 'BUY' ? '#238636' : '#30363d'}">
                ACTION: ${decision}
            </button>
        `;
        container.appendChild(card);
    });
}

// 3. Obsługa filtrów (BEZPIECZNA - omija Kaspersky)
document.addEventListener('click', function(e) {
    // Sprawdzamy czy kliknięty element to przycisk filtra
    if (e.target.classList.contains('filter-btn')) {
        const market = e.target.getAttribute('data-market');

        // Zmiana aktywnego przycisku
        document.querySelectorAll('.filter-btn').forEach(btn => btn.classList.remove('active'));
        e.target.classList.add('active');

        // Filtrowanie danych
        if (market === 'ALL') {
            renderCards(satelliteData);
        } else {
            const filtered = satelliteData.filter(i => 
                (i.domain || i.market || '').toUpperCase().includes(market)
            );
            renderCards(filtered);
        }
    }
});

// Start
fetchSystemData();