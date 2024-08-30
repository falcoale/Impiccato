import json
import random
import sys



def exit(randomWord):
    print("Hai perso! La parola corretta era " + randomWord + ". Per ricominciare il gioco il gioco scrivi python main.py.")
    sys.exit('Hai terminato le vite')  # Esci dal gioco

def carica_stadi():
    try:
        with open('stadi.json', 'r') as file:
            stadi = json.load(file)
            return stadi
    except Exception as e:
        print(f"Errore nel caricamento del file JSON: {e}")
        return []

def disegno_impiccato(errori, stadi):
    if 0 <= errori < len(stadi):
        return stadi[errori]
    else:
        exit(randomWord)

def genWord():
    try:
        with open('parole.json', 'r') as file:
            parole = json.load(file)
            if parole:
                return random.choice(parole)
            else:
                print("Il file JSON è vuoto.")
                return None
    except Exception as e:
        print(f"Errore: {e}")
        return None


def check(errori, stadi, tentativo, randomWord, valori_correnti, num_lettere):
    if len(tentativo) != len(randomWord):
        print(f"La parola da te inserita non ha lo stesso numero di caratteri della parola da inserire. La parola da indovinare ha {num_lettere} lettere.")
        return errori, False, valori_correnti

    if tentativo == randomWord:
        print("Bravo! Hai indovinato la parola!")
        return errori, True, valori_correnti
    else:
        indovinato = False
        nuova_parola = list(valori_correnti)

        for i in range(len(randomWord)):
            if randomWord[i] == tentativo[i]:  # Controlla se la lettera è corretta
                nuova_parola[i] = tentativo[i]  # Aggiorna la posizione corretta
                indovinato = True

        valori_correnti = "".join(nuova_parola)  # Converti nuovamente in stringa

        if indovinato:
            errori += 1  # Incrementa gli errori
            print(disegno_impiccato(errori, stadi)) # Printi gli stadi
            print(f"Parola da indovinare: {valori_correnti}")
        else:
            errori += 1
            print(disegno_impiccato(errori, stadi))
            print("Nessuna lettera è corretta. Riprova.")

        return errori, False, valori_correnti

def main():
    errori = 0
    stadi = carica_stadi()

    if not stadi:
        print("Nessuno stadio caricato.")
        return

    print(disegno_impiccato(errori, stadi))
    randomWord = genWord()
    if randomWord:
        num_lettere = len(randomWord)
        valori_correnti = "_" * num_lettere
        print("Parola da indovinare:", valori_correnti)


        while True:
            tentativo = input(str("Inserisci la parola: "))
            errori, indovinato, valori_correnti = check(errori, stadi, tentativo, randomWord, valori_correnti, num_lettere)
            if indovinato:
                break  # Esci dal ciclo se l'utente ha indovinato la parola, altrimenti tentativi infiniti
            if errori >= len(stadi) - 1:
                exit(randomWord)  # Esci dal gioco se hai raggiunto il limite di errori

if __name__ == "__main__":
    main()
