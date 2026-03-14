const WarningUI = {
    inject(riskScore, reasons) {
        // Remove existing warning if any
        const existing = document.getElementById('scam-guard-warning');
        if (existing) existing.remove();

        // Create container
        const container = document.createElement('div');
        container.id = 'scam-guard-warning';
        
        // Create content
        const reasonsHTML = reasons.map(r => `<li>${r}</li>`).join('');
        
        container.innerHTML = `
            <div class="sg-header">
                <span class="sg-icon">⚠</span>
                <span class="sg-title">Potential Scam Website Detected</span>
                <button class="sg-close" onclick="document.getElementById('scam-guard-warning').remove()">×</button>
            </div>
            <div class="sg-body">
                <div class="sg-score-container">
                    <span class="sg-score-label">Risk Score:</span>
                    <span class="sg-score-value">${riskScore}/100</span>
                </div>
                <ul class="sg-reasons">
                    ${reasonsHTML}
                </ul>
            </div>
        `;

        document.body.appendChild(container);
    }
};
