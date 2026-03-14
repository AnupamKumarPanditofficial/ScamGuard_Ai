(function() {
    function extractPageData() {
        // Extract visible text (limit to 5000 chars)
        const text = document.body.innerText.substring(0, 5000);
        
        // Extract links
        const links = Array.from(document.querySelectorAll('a'))
            .map(a => a.href)
            .filter(href => href.startsWith('http'))
            .slice(0, 50); // Limit to top 50 links
            
        // Get domain
        const domain = window.location.hostname;
        
        return { text, links, domain };
    }

    // Delay scan slightly to ensure page content is mostly loaded
    setTimeout(() => {
        const data = extractPageData();
        Scanner.scan(data);
    }, 1500);
})();
