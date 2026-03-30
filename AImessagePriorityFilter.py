urgentwords = ["deadline", "asap", "submit", "required", "action", "emergency", "due", "important","urgent","submission","important"]
chillwords = ["newsletter", "weekly", "reminder", "potluck", "info", "optional", "update","sale","discount","offer"]

def Classifymessage(text):
    text = text.lower()
    score = 0
    foundurgent = []
    foundchill = []

  
    for word in urgentwords:
        if word in text:
            score += 1
            foundurgent.append(word)
            
    for word in chillwords:
        if word in text:
            score -= 1
            foundchill.append(word)

    print(" Assistant Analysis")
    
    if score > 0:
        print("Status:  HIGH PRIORITY")
        print(f"Reasoning: I noticed urgent terms like: {', '.join(foundurgent)}.")
        print("Recommendation: You should probably handle this task soon!")
    elif score < 0:
        print("Status:  LOW PRIORITY")
        print(f"Reasoning: This looks like a routine update (Keywords: {', '.join(foundchill)}).")
        print("Recommendation: Read this when you have some free time.")
    else:
        print("Status: GENERAL MESSAGE")
        print("Reasoning: I didn't find any specfic stress-trigers or routine keywords.")
        print("Recommendation: Use your best judgment on this one.")

print("Hello! I'm your Asistant. Paste a message below, and I'll help you filter the noise.")
usermsg = input("What does the message say? ")

Classifymessage(usermsg)