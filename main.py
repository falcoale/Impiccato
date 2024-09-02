import json
import random
import sys
import subprocess
import os
import platform
import tkinter as tk
from tkinter import filedialog, messagebox

def open_file(filepath):  # Apri un file con Sistema Operativo personalizzato
    if platform.system() == 'Darwin':  # macOS
        subprocess.call(('open', filepath))
    elif platform.system() == 'Windows':  # Windows
        subprocess.call([r'C:\Windows\System32\notepad.exe', filepath])
    else:  # Linux
        subprocess.call(('xdg-open', filepath))  # linux variants

def clear():  # Pulisci la console con Sistema Operativo personalizzato
    if platform.system() == 'Windows':
        os.system('cls')  # Comando per Windows
    else:
        os.system('clear')  # Comando per macOS e Linux

def chiedi_file_json():
    root = tk.Tk()
    root.withdraw()  # Nascondi la finestra principale

    while True:
        file_path = filedialog.askopenfilename(title="Seleziona un file .json",
                                               filetypes=[("File JSON", "*.json")])
        if not file_path:
            messagebox.showerror("Errore", "Nessun file selezionato. Per favore, seleziona un file .json.")
            continue

        if not file_path.endswith('.json'):
            messagebox.showerror("Errore", "Il file selezionato non è un file .json. Riprova.")
            continue

        messagebox.showinfo("Successo", f"File '{file_path}' caricato con successo.")
        return file_path  # Restituisci il percorso del file selezionato

def scelte():
    clear()
    scelta = input(f'Benvenuto nel gioco dell\'Impiccato by falcole 2.0.0 (Ultimo update 1 Settembre 2024)\n'
                  f'Attraverso l\'inserimento di un numero entrerai in quella sezione.\n'
                  f'[1] Gioca\n'
                  f'[2] Modifica il dizionario (modifica del json)\n'
                  f'[3] Crediti\n'
                  f'[4] Esci\n'
                  f'>> ')

    if scelta.isdigit():
        scelta = int(scelta)
    else:
        print(f'La tua scelta "{scelta}" non è valida, riprova.')
        scelte()
        return

    if scelta == 1:
        dizionario = scegli_dizionario(None)  # Passa None come argomento
        if dizionario:  # Solo se un dizionario è stato selezionato
            main(dizionario)
        else:
            print("Nessun dizionario valido selezionato. Torno al menu principale.")
            scelte()
    elif scelta == 2:
        dizionario_scelte()
    elif scelta == 3:
        credits()
    elif scelta == 4:
        sys.exit()
    else:
        print(f'La tua scelta "{scelta}" non è valida, riprova.')
        scelte()


def scegli_dizionario(dizionario):
    if dizionario:
        # Se è stato fornito un dizionario, lo usiamo direttamente
        return dizionario
    else:
        # Elenca tutti i file .json nella directory corrente
        files = [f for f in os.listdir() if f.endswith('.json')]
        if not files:
            print("Nessun file dizionario trovato nella directory.")
            return None

        # Visualizza i file .json disponibili
        print("Seleziona un dizionario tra i file json disponibili:")
        for i, file in enumerate(files, 1):
            print(f"[{i}] {file}")

        # Chiede all'utente di scegliere un file
        while True:
            scelta = input(">> ")
            if scelta.isdigit():
                scelta = int(scelta)
                if 1 <= scelta <= len(files):
                    return files[scelta - 1]
                else:
                    print("Scelta non valida, riprova.")
            else:
                print("Input non valido, riprova.")

def dizionario_scelte():
    clear()
    dizionario_scelta = input(f'Benvenuto nella sezione per modificare il dizionario del gioco.\n'
                              f'A cosa può essere utile questa sezione?\n'
                              f'Beh molto semplice. Se sei un\'organizzatore di giochi o cose così, personalizzare il dizionario\n'
                              f'a tuo piacimento può essere veramente utile per rendere il gioco unico e genuino.\n'
                              f'SAttraverso l\'inserimento di un numero entrerai in quella sezione.\n'
                              f'[1] Per vedere l\'attuale dizionario\n'
                              f'[2] Creo un tuo dizionario\n'
                              f'[3] Torna al menu principale\n'
                              f'>> ')

    if dizionario_scelta.isdigit():
        dizionario_scelta = int(dizionario_scelta)
    else:
        print(f'La tua scelta "{dizionario_scelta}" non è valida, riprova.')
        dizionario_scelte()
        return

    if dizionario_scelta == 1:
        filepath = "parole.json"
        open_file(filepath)
        clear()
        dizionario_scelte()
    elif dizionario_scelta == 2:
        dizionario = crea_dizionario_proprio()
        if dizionario:  # Solo se un dizionario è stato creato o caricato
            print(f"Dizionario utilizzato: {dizionario}")
    elif dizionario_scelta == 3:
        scelte()
    else:
        print(f'La tua scelta "{dizionario_scelta}" non è valida, riprova.')
        dizionario_scelte()

def crea_dizionario_proprio():
    clear()
    dizionario_proprio_scelte = input(
        f'Benvenuto nella sezione di creazione del dizionario!\n'
        f'Attraverso l\'inserimento di un numero entrerai nella sezione scelta.\n'
        f'[1] Inserisci tu le parole qui \n'
        f'[2] Carica un file con estensione .json (es. [parola, tavolo, gatto])\n'
        f'[3] Torna alla sezione precedente\n'
        f'>> '
    )

    if dizionario_proprio_scelte.isdigit():
        dizionario_proprio = int(dizionario_proprio_scelte)
    else:
        print(f'La tua scelta "{dizionario_proprio_scelte}" non è valida, riprova.')
        return None

    if dizionario_proprio == 1:
        new_parole = input('Inserisci le parole separate dalla virgola:\n>> ')
        parole = [parola.strip() for parola in new_parole.split(',')]
        nome_dizionario = input('Inserisci il nome del file da creare (senza estensione):\n>> ')
        try:
            with open(f'{nome_dizionario}.json', 'w') as file:
                json.dump(parole, file, ensure_ascii=False, indent=4)
            print(f'Dizionario creato e salvato come "{nome_dizionario}.json"')
            return f'{nome_dizionario}.json'
        except IOError as e:
            print(f"Errore nella creazione del file: {e}")
            return None
    elif dizionario_proprio == 2:
        file_path = chiedi_file_json()
        return file_path  # Restituisce il percorso del file caricato
    elif dizionario_proprio == 3:
        dizionario_scelte()
    else:
        print(f'La tua scelta "{dizionario_proprio_scelte}" non è valida, riprova.')
        return None

def credits():
    clear()
    github_profile_link = "https://github.com/falcoale"
    database_link = "https://gist.github.com/sinanatra/23cc714cb98b2568d664eb6b4b46f6d6"
    print(f'Questo gioco è stato sviluppato interamente da Alessandro Falcari. {github_profile_link}\n'
          f'Json usato per le parole = {database_link}\n'
          f'Versione gioco = v.2.0.0\n'
          f'Linguaggio = Python\n'
          f'[0] Torna al menu principale\n'
          f'>> ')
    back_home = input()
    if back_home == '0':
        scelte()
    else:
        print(f'La tua scelta "{back_home}" non è valida, riprova.')
        credits()

def exit(randomWord):
    sys.exit(0)  # Esci dal gioco

def carica_stadi():
    try:
        with open('stadi/stadi.json', 'r') as file:
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

def genWord(dizionario):
    try:
        with open(dizionario, 'r') as file:
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
            valori_correnti = "".join(nuova_parola)  # Converte lista a stringa
            print(f"Parola da indovinare: {valori_correnti}")  # Printi la parola da indovinare con indizi (es. parola = gatto; valori_correnti = ga__o)
        else:
            errori += 1  # Incrementi var errori
            print(disegno_impiccato(errori, stadi))  # Printi lo stadio (con errore incrementato vedi stadi/stadi.json)
            print("Nessuna lettera è corretta. Riprova.")  # Printi messaggio di errore

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

    else:  # Se il numero delle lettere del tentativo non è uguale al numero di lettere della parola da indovinare
        print(f"La parola da te inserita non ha lo stesso numero di caratteri della parola da indovinare. La parola da indovinare ha {len(randomWord)} lettere.")  # Printi il messaggio di errore
        return errori, False, valori_correnti

def main(dizionario=None):  # Funzione principale del gioco
    errori = 0
    stadi = carica_stadi()

    if not stadi:
        print("Nessuno stadio caricato.")
        return

    dizionario = scegli_dizionario(dizionario)
    if not dizionario:
        print("Nessun dizionario valido selezionato. Uscita dal gioco.")
        return

    print(disegno_impiccato(errori, stadi))
    randomWord = genWord(dizionario)
    if randomWord:
        num_lettere = len(randomWord)
        valori_correnti = "_" * num_lettere
        print("Parola da indovinare:", valori_correnti)

        while True:
            tentativo = input("Inserisci una lettera o la parola intera: ")
            errori, indovinato, valori_correnti = check(errori, stadi, tentativo, randomWord, valori_correnti)
            if indovinato:
                print("Hai vinto!")
                exit(randomWord)
                break
            if errori >= len(stadi):
                print("Hai perso! La parola corretta era " + randomWord + ". Per ricominciare il gioco, scrivi python main.py.")
                exit(randomWord)

if __name__ == "__main__":
    scelte()
    main()
