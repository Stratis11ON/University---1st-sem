def stringToASCII(string):
    # δημιουργούμε μια μεταβλητή, αρχικά τύπου string, για να αποθηκεύσουμε τους αριθμούς του ASCII code
    endNum = ""

    # παίρνουμε το ASCII code του κάθε χαρακτήρα του αρχικού string μέσω της συνάρτησης ord
    # και το προσθέτουμε στην μεταβλητή endNum
    for char in string:
        endNum += str(ord(char))

    # μετατρέπουμε την μεταβλητή αποθήκευσης ASCII code σε ακέραιο αριθμό
    endNum = int(endNum)

    # τέλος ελέγχει αν ο αριθμός είναι πρώτος και εκτυπώνει το αποτέλεσμα
    if endNum > 1:
        for i in range(2, endNum//2+1): # αρκεί μέχρι το μισό του αριθμού καθώς μετα το αποτέλεσμα δεν θα είναι ακέραιο
            if (endNum % i) == 0:
               print("Ο αριθμός",endNum,"που προήλθε από το κείμενο","'",string,"'","δεν είναι πρώτος.")
               print(i,"times",endNum//i,"is",endNum)
               break
        else:
            print("Ο αριθμός",endNum,"που προήλθε από το κείμενο","'",string,"'","είναι πρώτος.")

    else:
        print("Ο αριθμός",endNum,"που προήλθε από το κείμενο","'",string,"'","δεν είναι πρώτος.")
