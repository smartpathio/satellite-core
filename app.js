let rawData = [];

async function fetchData() {
    try {
        const res = await fetch('data.json');
        rawData = await res.json();
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
        const card = document.createElement('div');
        card.className = `card ${score > 70 ? 'high-score' : 'low-score'}`;
        
        card.innerHTML = `
            <div class="score-tag" style="color: ${score > 70 ? 'var(--neon-green)' : 'var(--neon-red)'}">${item.score}</div>
            <small style="color: var(--text-dim)">${item.market}</small>
            <h2 style="margin: 5px 0 15px 0; font-size: 1.4rem;">${item.title}</h2>
            
            <div class="analysis-section">
                <span class="analysis-label">DESCRIPTIVE / DIAGNOSTIC</span>
                <p>${item.description}</p>
                
                <span class="analysis-label">PREDICTIVE ANALYTICS</span>
                <p><em>${item.prediction}</em></p>
            </div>

            <button class="decision-btn ${item.decision.toLowerCase()}">
                PRESCRIPTIVE: ${item.decision}
            </button>
        `;
        container.appendChild(card);
    });
}

function filter(market) {
    const btns = document.querySelectorAll('nav button');
    btns.forEach(b => b.classList.remove('active'));
    event.target.classList.add('active');

    const filtered = market === 'ALL' ? rawData : rawData.filter(i => i.market === market);
    render(filtered);
}

fetchData();