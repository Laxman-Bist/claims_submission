import csv
import os

DATA_FILE = "data/claims.csv"

def submit_claim(policy_number, claim_amount, date_of_incident):
    claim_id = get_next_claim_id()
    claim = {
        "claim_id": claim_id,
        "policy_number": policy_number,
        "claim_amount": claim_amount,
        "date_of_incident": date_of_incident,
        "status": "Submitted",
        "payout_amount": 0.0
    }
    save_claim(claim)

def get_next_claim_id():
    if not os.path.exists(DATA_FILE):
        return 1
    with open(DATA_FILE, "r") as file:
        reader = csv.DictReader(file)
        claims = list(reader)
    return len(claims) + 1

def save_claim(claim):
    file_exists = os.path.exists(DATA_FILE)
    with open(DATA_FILE, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=claim.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(claim)