# ticket_triage.py
# Simple Python script I built to auto-categorize and route support tickets
# (Used at ModSquad & Nature’s Finest to automate escalation)

import re

def triage_ticket(subject: str, description: str) -> dict:
    """Auto-classifies ticket and suggests next action"""
    text = (subject + " " + description).lower()
    
    if re.search(r'(api|postman|graphql|error 4|timeout)', text):
        return {"category": "API/Integration", "priority": "High", "action": "Route to Engineering + check logs with SQL"}
    
    elif re.search(r'(copilot|microsoft 365|azure|cloud)', text):
        return {"category": "M365/Cloud", "priority": "Medium", "action": "Use Chrome DevTools + provide walkthrough"}
    
    elif re.search(r'(login|session|payment)', text):
        return {"category": "Access/Payment", "priority": "High", "action": "Immediate response via Slack"}
    
    return {"category": "General", "priority": "Low", "action": "Standard KB article"}

# Example usage (anonymized)
if __name__ == "__main__":
    result = triage_ticket(
        "API call failing with 500 error",
        "Integration with our platform stopped working after update"
    )
    print(result)
