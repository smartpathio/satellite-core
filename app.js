let rawData = [];

async function fetchData() {
    try {
        const res = await fetch('data.json');
        if (!res.ok) throw new Error('Data not found');
        const jsonResponse = await res.json();
        
        // Pobieramy dane z Twojej struktury 'deep_analysis'
        rawData = jsonResponse.deep_analysis || [];
        render(rawData);
        
        document.getElementById('last-update').innerText = 'SATELLITE LIVE | ' + new Date().toLocaleTimeString();
    } catch (e) {
        document.getElementById('last-update').innerText = 'LINK DISRUPTED | WAITING FOR BOT';
    }
}

function render(data) {
    const container = document.getElementById('dashboard');
    if (!container) return;
    container.innerHTML = '';

    data.forEach(item => {
        const niche = item.niche_or_area || 'Satellite Analysis';
        const decision = (item.decision || 'WATCH').toUpperCase();
        const reason = item.reason_short || 'No details provided';
        const market = (item.domain || 'GENERAL').toUpperCase();
        const score = item.confidence ? Math.round(item.confidence * 100) : 0;

        // Logika kolorów przycisku
        let btnColor = '#444'; // Domyślny szary
        if (decision === 'BUY' || decision === 'YES') btnColor = '#28a745'; // Zielony
        if (decision === 'WATCH' || decision === 'HOLD') btnColor = '#ffc107'; // Żółty

        const card = document.createElement('div');
        card.className = `card ${score > 70 ? 'high-score' : 'low-score'}`;
        
        card.innerHTML = `
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                <span style="color: ${score > 70 ? '#00ff41' : '#ff3131'}; font-weight: bold; font-size: 0.8rem;">
                    ${score}% CONFIDENCE
                </span>
                <small style="color: #8b949e; text-transform: uppercase; font-size: 0.7rem;">${market}</small>
            </div>
            
            <h2 style="margin: 0 0 10px 0; font-size: 1.3rem; color: #fff;">${niche}</h2>
            
            <div style="background: rgba(255,255,255,0.03); padding: 12px; border-radius: 8px; border-left: 2px solid #00d4ff;">
                <p style="font-size: 0.95rem; color: #d1d5db; margin: 0; line-height: 1.4;">${reason}</p>
            </div>

            <button style="width: 100%; margin-top: 15px; padding: 14px; border: none; border-radius: 8px; font-weight: 800; background: ${btnColor}; color: ${decision === 'WATCH' ? '#000' : '#fff'}; cursor: pointer; text-transform: uppercase; letter-spacing: 1px;">
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
        const m = (i.domain || '').toUpperCase();
        return m.includes(market.toUpperCase());
    });
    render(filtered);
}

fetchData();