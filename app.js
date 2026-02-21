let rawData = [];

async function fetchData() {
    try {
        const res = await fetch('data.json');
        rawData = await res.json();
        
        // INTELIGENTNE SORTOWANIE: Najpierw te z najwyższym Score
        rawData.sort((a, b) => parseInt(b.score) - parseInt(a.score));
        
        render(rawData);
        document.getElementById('last-update').innerText = 'SYSTEM LIVE | ' + new Date().toLocaleTimeString();
    } catch (e) {
        document.getElementById('last-update').innerText = 'LINK DISRUPTED';
    }
}

function render(data) {
    const container = document.getElementById('dashboard');
    container.innerHTML = '';

    data.forEach(item => {
        const score = parseInt(item.score);
        // Sprawdzamy, czy to kluczowy rynek dla Twoich nowych projektów
        const isCoreProject = item.market.includes('DPE') || item.market.includes('COMMERCE');
        
        const card = document.createElement('div');
        // Dodajemy klasę 'core-project' jeśli to DPE/Commerce
        card.className = `card ${score > 70 ? 'high-score' : 'low-score'} ${isCoreProject ? 'core-project' : ''}`;
        
        card.innerHTML = `
            <div class="score-tag" style="color: ${score > 70 ? 'var(--neon-green)' : 'var(--neon-red)'}">
                ${item.score}% ${isCoreProject ? '⭐' : ''}
            </div>
            <small style="color: var(--text-dim)">${item.market.toUpperCase()}</small>
            <h2 style="margin: 5px 0 10px 0; font-size: 1.2rem; line-height: 1.2;">${item.title}</h2>
            
            <div class="analysis-section">
                <span class="analysis-label">DIGITAL BODY LANGUAGE</span>
                <p style="font-size: 0.9rem; margin-bottom: 10px;">${item.description}</p>
                
                <span class="analysis-label">PREDICTIVE / TREND</span>
                <p style="font-size: 0.85rem; color: var(--neon-blue);"><em>${item.prediction}</em></p>
            </div>

            <button class="decision-btn ${item.decision.toLowerCase()}" style="width: 100%; margin-top: 10px; padding: 12px;">
                ACTION: ${item.decision}
            </button>
        `;
        container.appendChild(card);
    });
}

function filter(market) {
    const btns = document.querySelectorAll('nav button');
    btns.forEach(b => b.classList.remove('active'));
    if(event) event.target.classList.add('active');

    const filtered = market === 'ALL' ? rawData : rawData.filter(i => i.market === market);
    render(filtered);
}

fetchData();