# Citizen AI Project
# Author: balagurusamy + AI
# Language: Python

import random

class CitizenAI:
    def __init__(self, citizen_name):
        self.citizen_name = citizen_name

    def govt_services(self, query):
        services = {
            "aadhaar": "You can apply/update Aadhaar at UIDAI website: https://uidai.gov.in",
            "passport": "You can apply for Passport at https://www.passportindia.gov.in",
            "voter": "Register for Voter ID at https://www.nvsp.in",
            "pan": "Apply for PAN at https://www.onlineservices.nsdl.com"
        }
        for key, value in services.items():
            if key in query.lower():
                return value
        return "Sorry, I don't have information on that service."

    def report_issue(self, query):
        issues = {
            "road": "Your road complaint has been noted. Local municipality will be informed.",
            "electricity": "Electricity issue reported. Power board will check it soon.",
            "water": "Water supply issue reported to the local corporation.",
            "sanitation": "Sanitation complaint logged. Cleaning team will attend."
        }
        for key, value in issues.items():
            if key in query.lower():
                return value
        return "Sorry, I could not identify the issue. Please try again."

    def awareness(self):
        tips = [
            "Every citizen has the right to equality before law.",
            "As a citizen, it is your duty to vote responsibly.",
            "You should keep your city clean by avoiding littering.",
            "Paying taxes honestly is a citizen’s responsibility."
        ]
        return random.choice(tips)

    def random_tip(self):
        tips = [
            "Plant a tree in your neighborhood.",
            "Help senior citizens with digital services.",
            "Promote eco-friendly transport.",
            "Participate in local community services."
        ]
        return random.choice(tips)

    def ask(self, query):
        if any(word in query.lower() for word in ["aadhaar", "passport", "voter", "pan"]):
            return self.govt_services(query)
        elif any(word in query.lower() for word in ["road", "electricity", "water", "sanitation"]):
            return self.report_issue(query)
        elif "awareness" in query.lower():
            return self.awareness()
        elif "tip" in query.lower():
            return self.random_tip()
        else:
            return "I am Citizen AI. I can help with government services, issue reporting, awareness, and tips."

# ---------- MAIN PROGRAM ----------
if __name__ == "__main__":
    print("------ Citizen AI Assistant ------")
    name = input("Enter your name: ")
    ai = CitizenAI(name)

    while True:
        query = input(f"\n{name}, enter your query (or type 'exit' to quit): ")
        if query.lower() == "exit":
            print("Thank you for using Citizen AI. Goodbye!")
            break
        print("Citizen AI:", ai.ask(query))