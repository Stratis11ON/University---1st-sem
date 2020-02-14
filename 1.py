from re import sub

biggestWords = [] # Οι μεγαλύτερες λέξεις

# Φωνήεντα σε αγγλικά και Ελληνικά
Vowels = "[aeioyuαεηιυοωάέήίύόώ]"

# Παίρνουμε το κείμενο του αρχείου και κάνουμε τα γράμματα μικρά
# το αρχείο να είναι encoded σε ANSI
text = open("text.txt", "r").read().lower()

# αφαιρούμε τα σημεία στίξης
text = sub("[!@#$.,;:]", "", text)

# περνάμε τις λέξεις σε λίστα
text = text.split(" ")

# ταξινομούμε την λίστα ανάλογα με το μέγεθος των λέξεων με την χρήση της Selection Sort με τις μεγαλύτερες λέξεις πρώτες
for i in range(len(text)-1): # για κάθε λέξη του κειμένου
    pos = i
    for j in range(i+1, len(text)):
        if len(text[j]) > len(text[pos]):
            pos = j
    text[pos], text[i] = text[i], text[pos]

# προσθέτουμε τις πρώτες 5 σε μια λίστα
for i in range(5):
    biggestWords.append(text[i])

for word in biggestWords:
    word = sub(Vowels, "", word) # αφαιρούμε τα φωνήεντα
    print(word[::-1]) # εκτυπώνουμε τις λέξεις ανάποδα
