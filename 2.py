from re import sub

# Φωνήεντα σε αγγλικά και Ελληνικά
Vowels = "[aeioyuαεηιυοωάέήίύόώ]"

# Παίρνουμε το κείμενο του αρχείου και κάνουμε τα γράμματα μικρά
# το αρχείο να είναι encoded σε ANSI
text = open("text.txt", "r").read().lower()

# αφαιρούμε τα σημεία στίξης
text = sub("[!@#$.,;:]", "", text)

# περνάμε τις λέξεις σε λίστα
text = text.split(" ")

for word in text:
    negativeLetters = 0 # αρχικοποιούμε το πλήθος των αρνητικών συμφώνων
    wordWithoutVowels = sub(Vowels, "", word) # αφαιρούμε τα φωνήεντα
    # μετράμε τα αρνητικά σύμφωνα γράμματα
    for char in wordWithoutVowels:
        if char in "fckr":
            negativeLetters += 1

    # αν τα αρνητικά σύμφωνα είναι περισσότερα από τα μισά σύμφωνα (συνολικά) της λέξης
    if negativeLetters > len(wordWithoutVowels)/2:
        print(word, "is negative.")
    # αν τα όχι αρνητικά σύμφωνα είναι περισσότερα από τα μισά σύμφωνα (συνολικά) της λέξης
    else:
        print(word, "is positive.")
