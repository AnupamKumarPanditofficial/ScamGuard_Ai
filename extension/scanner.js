const Scanner = {
    RISK_THRESHOLD: 60,

    async scan(pageData) {
        console.log("ScamGuard: Scanning page...", pageData.domain);
        
        const result = await ScamGuardAPI.analyzePage(pageData);
        
        if (!result) {
            console.log("ScamGuard: Scan aborted due to API error.");
            return;
        }

        console.log(`ScamGuard: Risk Score = ${result.risk_score}`);
        
        if (result.risk_score > this.RISK_THRESHOLD) {
            WarningUI.inject(result.risk_score, result.reasons);
        } else {
            console.log("ScamGuard: Page appears safe.");
        }
    }
};
