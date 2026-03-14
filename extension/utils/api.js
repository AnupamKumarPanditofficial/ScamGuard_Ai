const API_URL = "http://localhost:8000/analyze";

const ScamGuardAPI = {
    async analyzePage(data) {
        try {
            const response = await fetch(API_URL, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(data)
            });

            if (!response.ok) {
                throw new Error(`API Error: ${response.statusText}`);
            }

            return await response.json();
        } catch (error) {
            console.error("ScamGuard API connection failed:", error);
            return null;
        }
    }
};
