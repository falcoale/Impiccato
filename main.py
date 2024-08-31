import json
import random
import sys


def exit(randomWord):
    print("Hai perso! La parola corretta era " + randomWord + ". Per ricominciare il gioco, scrivi python main.py.")
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
        return stadi[-1]  # Mostra l'ultimo stadio se gli errori sono oltre il limite


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


def check(errori, stadi, tentativo, randomWord, valori_correnti):
    if len(tentativo) == 1:  # Se l'utente inserisce una sola lettera
        if tentativo in randomWord:  # Se la lettera è presente nella parola da indovinare
            nuova_parola = list(valori_correnti)
            for i in range(len(randomWord)):
                if randomWord[i] == tentativo:  # Aggiorna la posizione corretta
                    nuova_parola[i] = tentativo
            valori_correnti = "".join(nuova_parola)
            print(f"Parola da indovinare: {valori_correnti}")
        else:
            errori += 1
            print(disegno_impiccato(errori, stadi))
            print("Nessuna lettera è corretta. Riprova.")

        return errori, valori_correnti == randomWord, valori_correnti

    elif len(tentativo) == len(randomWord):  # Se l'utente inserisce una parola intera
        if tentativo == randomWord:
            print("Bravo! Hai indovinato la parola!")
            return errori, True, randomWord
        else:
            errori += 1
            print(disegno_impiccato(errori, stadi))
            print(f"La parola inserita '{tentativo}' non è corretta.")
            print(f"Parola da indovinare: {valori_correnti}")
            return errori, False, valori_correnti

    else:
        print(
            f"La parola da te inserita non ha lo stesso numero di caratteri della parola da indovinare. La parola da indovinare ha {len(randomWord)} lettere.")
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
            tentativo = input(str("Inserisci una lettera o la parola intera: "))
            errori, indovinato, valori_correnti = check(errori, stadi, tentativo, randomWord, valori_correnti)
            if indovinato:
                print("Hai vinto!")
                break  # Esci dal ciclo se l'utente ha indovinato la parola
            if errori >= len(stadi):  # Corretto il limite degli errori
                exit(randomWord)  # Esci dal gioco se hai raggiunto il limite di errori


if __name__ == "__main__":
    main()
