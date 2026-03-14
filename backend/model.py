import json
import re
from typing import List, Dict

# Load keywords
def load_keywords(file_path: str = "scam_keywords.json") -> List[str]:
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
            return data.get("keywords", [])
    except FileNotFoundError:
        return []

KEYWORDS = load_keywords()

def clean_text(text: str) -> str:
    """Basic text cleaning."""
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def analyze_domain(domain: str) -> Dict[str, any]:
    """Analyzes the domain for suspicious patterns."""
    reasons = []
    score = 0
    
    # Suspicious TLDs
    suspicious_tlds = ['.xyz', '.top', '.loan', '.win', '.bid', '.gq', '.cf', '.tk', '.ml']
    if any(domain.endswith(tld) for tld in suspicious_tlds):
        score += 30
        reasons.append(f"Suspicious top-level domain detected ({domain.split('.')[-1]})")

    # Keywords in domain
    scam_domain_keywords = ['login', 'secure', 'verify', 'update', 'account', 'banking', 'support', 'wallet']
    if any(kw in domain.lower() for kw in scam_domain_keywords):
        score += 30
        reasons.append("Suspicious keyword found in domain name")

    return {"score": score, "reasons": reasons}

def analyze_text(text: str) -> Dict[str, any]:
    """Checks for phishing keywords in the page text."""
    reasons = []
    score = 0
    cleaned_text = clean_text(text)
    
    found_keywords = []
    for kw in KEYWORDS:
        if kw in cleaned_text:
            found_keywords.append(kw)
    
    if found_keywords:
        score += 30
        reasons.append(f"Phishing language detected: {', '.join(found_keywords[:3])}...")
        
    return {"score": score, "reasons": reasons}

def analyze_links(links: List[str]) -> Dict[str, any]:
    """Analyzes links for suspicious patterns."""
    reasons = []
    score = 0
    
    suspicious_link_count = 0
    for link in links:
        if any(kw in link.lower() for kw in ['verify', 'login', 'update', 'secure']):
            suspicious_link_count += 1
            
    if suspicious_link_count > 3:
        score += 20
        reasons.append(f"Multiple suspicious links detected ({suspicious_link_count})")
        
    return {"score": score, "reasons": reasons}

def get_risk_score(text: str, links: List[str], domain: str) -> Dict[str, any]:
    """Calculates the final risk score and compiles reasons."""
    domain_res = analyze_domain(domain)
    text_res = analyze_text(text)
    links_res = analyze_links(links)
    
    total_score = domain_res["score"] + text_res["score"] + links_res["score"]
    all_reasons = domain_res["reasons"] + text_res["reasons"] + links_res["reasons"]
    
    # Cap score at 100
    total_score = min(total_score, 100)
    
    return {
        "risk_score": total_score,
        "reasons": all_reasons
    }
