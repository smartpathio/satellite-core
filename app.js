let globalData = [];

async function loadData() {
    console.log("Próba pobrania danych...");
    try {
        const response = await fetch('data.json?t=' + Date.now());
        const data = await response.json();
        
        // Wyciągamy dane z Twojej struktury
        globalData = data.deep_analysis || [];
        
        console.log("Dane pobrane:", globalData);
        displayData(globalData);
        
        document.getElementById('last-update').innerText = 'LIVE | ' + new Date().toLocaleTimeString();
    } catch (error) {
        console.error("BŁĄD:", error);
        document.getElementById('dashboard').innerHTML = "Błąd ładowania danych. Sprawdź plik data.json";
        document.getElementById('last-update').innerText = 'LINK DISRUPTED';
    }
}

function displayData(items) {
    const container = document.getElementById('dashboard');
    container.innerHTML = '';

    if (items.length === 0) {
        container.innerHTML = "Brak danych do wyświetlenia.";
        return;
    }

    items.forEach(item => {
        const card = document.createElement('div');
        card.className = 'card';
        const score = item.confidence ? Math.round(item.confidence * 100) : 0;
        const decision = (item.decision || 'WATCH').toUpperCase();

        card.innerHTML = `
            <div style="font-weight: bold; color: ${score > 70 ? '#00ff41' : '#ff3131'}">${score}% CONFIDENCE</div>
            <h3>${item.niche_or_area || 'Analiza'}</h3>
            <p>${item.reason_short || 'Brak opisu'}</p>
            <button style="width: 100%; padding: 10px; background: ${decision === 'YES' || decision === 'BUY' ? '#28a745' : '#444'}; border: none; color: white; font-weight: bold;">
                ACTION: ${decision}
            </button>
        `;
        container.appendChild(card);
    });
}

// Nowa funkcja filtrowania (bez konfliktów nazw)
function handleFilter(category) {
    console.log("Filtrowanie:", category);
    
    // Wizualna zmiana przycisków
    document.querySelectorAll('nav button').forEach(btn => btn.classList.remove('active'));
    document.getElementById('btn-' + category).classList.add('active');

    if (category === 'ALL') {
        displayData(globalData);
    } else {
        const filtered = globalData.filter(i => 
            (i.domain || i.market || '').toUpperCase().includes(category)
        );
        displayData(filtered);
    }
}

// Start
loadData();