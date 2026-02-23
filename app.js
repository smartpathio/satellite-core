async function fetchIntelligence() {
    try {
        const response = await fetch('satellite_report.json?v=' + Date.now());
        const data = await response.json();
        
        document.getElementById('last-update').innerText = `UPDATED: ${data.last_update}`;
        const grid = document.getElementById('intelligence-grid');
        grid.innerHTML = '';

        data.deep_analysis.forEach(item => {
            const card = document.createElement('div');
            card.className = 'glass-card';
            
            const shareText = `MARKET ALERT: ${item.niche_or_area}\n\nDetails: ${item.reason_short}\n\nSignal: ${item.intuition_signal}`;
            
            card.innerHTML = `
                <span class="card-tag">${item.market}</span>
                <h3 style="margin: 20px 0 10px 0; font-weight: 800;">${item.niche_or_area}</h3>
                <p style="font-size: 13px; color: #64748b; line-height: 1.6; flex-grow: 1;">${item.reason_short}</p>
                <div style="border-top: 1px solid #f1f5f9; padding-top: 15px; margin-top: 15px;">
                    <p style="font-size: 11px; font-weight: 700; color: #475569 italic;">"${item.intuition_signal}"</p>
                </div>
                <button class="share-btn" onclick="dispatchSignal('${encodeURIComponent(shareText)}')">SEND TO MAIL / MSG</button>
            `;
            grid.appendChild(card);
        });
    } catch (error) {
        console.error("Fetch Error:", error);
    }
}

function dispatchSignal(encodedMsg) {
    const text = decodeURIComponent(encodedMsg);
    if (navigator.share) {
        navigator.share({ title: 'Satellite Signal', text: text });
    } else {
        window.location.href = `mailto:?subject=Market Intelligence Alert&body=${encodedMsg}`;
    }
}

window.addEventListener('DOMContentLoaded', fetchIntelligence);