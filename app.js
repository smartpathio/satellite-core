let currentData = [];

async function loadData() {
    try {
        const response = await fetch('data.json');
        currentData = await response.json();
        renderCards('ALL');
        document.getElementById('last-update').innerText = 'Sync: ' + new Date().toLocaleTimeString();
    } catch (error) {
        console.error("Błąd ładowania:", error);
        document.getElementById('last-update').innerText = 'Offline Mode';
    }
}

function renderCards(filterType) {
    const dashboard = document.getElementById('dashboard');
    dashboard.innerHTML = '';

    const filteredItems = filterType === 'ALL' 
        ? currentData 
        : currentData.filter(item => item.market === filterType);

    filteredItems.forEach(item => {
        const card = document.createElement('div');
        const scoreNum = parseInt(item.score);
        
        card.className = `card ${scoreNum > 70 ? 'high-score' : 'low-score'}`;
        
        card.innerHTML = `
            <span class="score-tag ${scoreNum > 70 ? 'neon-green' : ''}">${item.score}</span>
            <small style="color: var(--neon-blue)">${item.market}</small>
            <h3 style="margin: 10px 0">${item.title}</h3>
            <p style="font-size: 0.9em; opacity: 0.8">${item.desc}</p>
            <button class="decision-btn ${item.decision.toLowerCase()}">${item.decision}</button>
        `;
        dashboard.appendChild(card);
    });

    // Aktualizacja wyglądu przycisków nav
    document.querySelectorAll('nav button').forEach(btn => {
        btn.classList.toggle('active', btn.getAttribute('onclick').includes(`'${filterType}'`));
    });
}

// Funkcja wywoływana przez przyciski
function filter(type) {
    renderCards(type);
}

// Start aplikacji
loadData();