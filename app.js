let rawData = [];

async function fetchData() {
    try {
        // Przypominajka: Sprawdź czy VPN wyłączony przed testem!
        const res = await fetch('data.json');
        if (!res.ok) throw new Error('Błąd pobierania pliku data.json');
        
        const jsonResponse = await res.json();
        
        // Dynamiczne wyciąganie danych: obsługuje Twój format 'deep_analysis' lub zwykłą listę
        rawData = jsonResponse.deep_analysis || (Array.isArray(jsonResponse) ? jsonResponse : [jsonResponse]);
        
        render(rawData);
        
        document.getElementById('last-update').innerText = 'SYSTEM LIVE | ' + new Date().toLocaleTimeString();
    } catch (e) {
        console.error("Szczegóły błędu:", e);
        document.getElementById('last-update').innerText = 'LINK DISRUPTED | BRAK DANYCH';
    }
}

function render(data) {
    const container = document.getElementById('dashboard');
    if (!container) return;
    container.innerHTML = '';

    data.forEach(item => {
        // Mapowanie pól pod Twój specyficzny plik JSON (widoczny na laptopie)
        const niche = item.niche_or_area || item.niche || 'Satellite Scan';
        const decision = (item.decision || 'WATCH').toUpperCase();
        const reason = item.reason_short || item.reason || 'Processing data...';
        const market = (item.domain || item.market || 'General').toUpperCase();
        const score = item.confidence ? Math.round(item.confidence * 100) : (item.score || 0);

        const card = document.createElement('div');
        // Klasy stylu
        card.className = `card ${score > 70 ? 'high-score' : 'low-score'} ${market.includes('DPE') ? 'core-project' : ''}`;
        
        card.innerHTML = `
            <div class="score-tag" style="color: ${score > 70 ? '#00ff41' : '#ff3131'}; font-weight: bold;">
                ${score}% CONFIDENCE
            </div>
            <small style="color: #8b949e; letter-spacing: 1px;">${market}</small>
            <h2 style="margin: 8px 0; font-size: 1.2rem; color: #fff;">${niche}</h2>
            
            <div class="analysis-section" style="background: rgba(255,255,255,0.05); padding: 12px; border-radius: 8px; margin-top: 10px;">
                <span style="font-size: 0.7rem; color: #00d4ff; font-weight: bold; display: block; margin-bottom: 5px;">ANALYSIS RESULT</span>
                <p style="font-size: 0.9rem; color: #d1d5db; margin: 0;">${reason}</p>
            </div>

            <button class="decision-btn" style="width: 100%; margin-top: 12px; padding: 12px; border: none; border-radius: 6px; font-weight: bold; background: ${decision === 'BUY' || decision === 'YES' ? '#28a745' : '#444'}; color: white;">
                ACTION: ${decision}
            </button>
        `;
        container.appendChild(card);
    });
}

function filter(market) {
    const btns = document.querySelectorAll('nav button');
    btns.forEach(b => b.classList.remove('active'));
    if(event && event.target) event.target.classList.add('active');

    const filtered = market === 'ALL' ? rawData : rawData.filter(i => {
        const m = (i.domain || i.market || '').toUpperCase();
        return m.includes(market.toUpperCase());
    });
    render(filtered);
}

// Start systemu
fetchData();