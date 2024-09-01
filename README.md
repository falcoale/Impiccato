# Gioco dell'Impiccato 🎉

![Gioco dell'Impiccato Banner](https://github.com/user-attachments/assets/bfd4bb29-7e14-4ead-9c65-4449224daf55)

Benvenuto nel **Gioco dell'Impiccato**! 👋🏻

Hai mai giocato a questo classico gioco durante le elementari, magari disegnando l'impiccato sulla lavagna? Se la risposta è sì, sei nel posto giusto! Ho creato un semplice programmino in Python per riportare alla memoria quella bella nostalgia.

## 📋 Indice

- [Introduzione](#introduzione)
- [Caratteristiche](#caratteristiche)
- [Installazione](#installazione)
- [Come Giocare](#come-giocare)
  - [Avvio del Gioco](#avvio-del-gioco)
  - [Sezioni del Menu](#sezioni-del-menu)
    - [1. Gioca](#1-gioca)
    - [2. Modifica del Dizionario](#2-modifica-del-dizionario)
    - [3. Crediti](#3-crediti)
    - [4. Esci](#4-esci)
- [Tutti gli Stadi](#tutti-gli-stadi)
- [Crediti](#crediti)
- [Licenza](#licenza)

## 🎮 Caratteristiche

- **Interfaccia Intuitiva**: Naviga facilmente tra le opzioni del gioco.
- **Dizionari Personalizzabili**: Crea o modifica i dizionari delle parole per rendere il gioco unico.
- **Grafica dell'Impiccato**: Visualizza lo stato dell'impiccato dopo ogni errore.
- **Supporto Multiplatforma**: Funziona su Windows, macOS e Linux.

## 🛠️ Installazione

1. **Clona il repository**:

   ```bash
   git clone https://github.com/tuo-username/gioco-impiccato.git
   ```

2. **Naviga nella cartella del progetto**:

   ```bash
   cd gioco-impiccato
   ```

3. **Assicurati di avere Python installato**. Puoi scaricarlo da [python.org](https://www.python.org/downloads/).

4. **Installa le dipendenze necessarie** (se ce ne sono):

   ```bash
   pip install -r requirements.txt
   ```

## 🕹️ Come Giocare

### Avvio del Gioco

Apri il terminale (CMD su Windows, Terminal su macOS/Linux), naviga nella cartella del progetto e avvia il gioco con:

```bash
python main.py
```

Si presenterà così:

![Avvio del Gioco](https://github.com/user-attachments/assets/bfd4bb29-7e14-4ead-9c65-4449224daf55)

### Sezioni del Menu

#### [1] Gioca

Il programma ti chiederà di selezionare un dizionario disponibile.

![Selezione Dizionario](https://github.com/user-attachments/assets/dfc8dbba-28fe-4766-874c-a4ca8f200dad)

**Esempio**: Se scegli il dizionario [2]

![Dizionario Selezionato](https://github.com/user-attachments/assets/4bbb89a4-c994-4d54-8106-180a8b774047)

_(Nella versione su GitHub non si vedrà la parola.. se no che gioco sarebbe?)_

![Gioco in Corso](https://github.com/user-attachments/assets/9c36d38d-48ab-4cea-9851-38178626dba7)

Dopo ogni errore, il programma disegnerà una parte dell'impiccato, proprio come alle elementari con il gessetto.

![Errore](https://github.com/user-attachments/assets/647d287f-89c4-42cd-84aa-00d873f861eb)

Se indovini una o più lettere, verranno segnate nella posizione corretta per aiutarti.

#### [2] Modifica del Dizionario

Il programma ti mostrerà diverse opzioni:

1. **Vedi il dizionario caricato**:

   ![Visualizza Dizionario](https://github.com/user-attachments/assets/c9b655e0-dd6d-422b-9304-5d3336ed7534)

2. **Crea un dizionario personalizzato**:

   ![Crea Dizionario](https://github.com/user-attachments/assets/c5a813a5-777d-469e-ac87-0d3d9941c094)

   - **Inserisci le parole direttamente nel CMD**:

     ![Inserisci Parole](https://github.com/user-attachments/assets/04136b53-cfab-46c9-b633-90d747dc3e98)

     **Esempio di Input**:

     ```
     Inserisci le parole separate dalla virgola:
     >> mela, tavolo, gatto
     ```

   - **Carica un file JSON**:

     Esempio di file:

     ```json
     ["mela", "tavolo", "gatto"]
     ```

     Selezioniamo il file:

     ![Carica File](https://github.com/user-attachments/assets/4c069e11-4370-4fee-b3ec-e660ce83e2df)

     Messaggio di successo:

     ![Successo Caricamento](https://github.com/user-attachments/assets/cfec1e12-f431-402d-8fee-23bf4cb0127d)

3. **Torna al menu principale**:

   Anche qui, semplice, torni al menu principale.

#### [3] Crediti

Scopri chi ha sviluppato questo fantastico gioco!

#### [4] Esci

Uscirà dal programma.

## 🖼️ Tutti gli Stadi

### PRIMO

![Primo Stadio](https://github.com/user-attachments/assets/62e30572-d516-4fac-be92-4312c7456559)

### SECONDO

![Secondo Stadio](https://github.com/user-attachments/assets/9a3757ad-8358-4883-9bd9-8b8b716a393e)

### TERZO

![Terzo Stadio](https://github.com/user-attachments/assets/e249e6eb-edfb-424e-817b-51772461659e)

### QUARTO

![Quarto Stadio](https://github.com/user-attachments/assets/a23294b2-4009-4a51-8dff-b484f5cb19cb)

### QUINTO

![Quinto Stadio](https://github.com/user-attachments/assets/f9aba5b7-8863-45ee-a534-9d4bbbbaa616)

### SESTO

![Sesto Stadio](https://github.com/user-attachments/assets/a84db58c-8283-48a3-bcce-71447ceda279)

### SETTIMO

![Settimo Stadio](https://github.com/user-attachments/assets/1fbd3809-57b9-48df-a2f9-226e5cd2a7ac)

### OTTAVO (Sconfitta)

Chiuderà automaticamente il programma dopo la sconfitta.

![Ottavo Stadio](https://github.com/user-attachments/assets/239c14e6-0283-490d-8741-4cffb4fa8ea8)

## 👨‍💻 Crediti

Sviluppato interamente da **Alessandro Falcari**.

- **Profilo GitHub**: [@falcoale](https://github.com/falcoale)
- **Database delle Parole**: [Link al Gist](https://gist.github.com/sinanatra/23cc714cb98b2568d664eb6b4b46f6d6)

**Versione Gioco**: v.2.0.0  
**Linguaggio**: Python

---

## 📜 Licenza

Non è permesso riutilizzare o vendere il programma senza il mio consenso. Siate onesti!

---

## 📬 Contatti

Per domande, suggerimenti o contributi, sentiti libero di aprire un [issue](https://github.com/tuo-username/gioco-impiccato/issues) o contattarmi direttamente tramite GitHub.

---

**Buon divertimento e buona fortuna! 🍀**

# Gioco dell'Impiccato 🎉

![Gioco dell'Impiccato Banner](https://github.com/user-attachments/assets/bfd4bb29-7e14-4ead-9c65-4449224daf55)

Benvenuto nel **Gioco dell'Impiccato**! 👋🏻

Hai mai giocato a questo classico gioco durante le elementari, magari disegnando l'impiccato sulla lavagna? Se la risposta è sì, sei nel posto giusto! Ho creato un semplice programmino in Python per riportare alla memoria quella bella nostalgia.

## 📋 Indice

- [Introduzione](#introduzione)
- [Caratteristiche](#caratteristiche)
- [Installazione](#installazione)
- [Come Giocare](#come-giocare)
  - [Avvio del Gioco](#avvio-del-gioco)
  - [Sezioni del Menu](#sezioni-del-menu)
    - [1. Gioca](#1-gioca)
    - [2. Modifica del Dizionario](#2-modifica-del-dizionario)
    - [3. Crediti](#3-crediti)
    - [4. Esci](#4-esci)
- [Tutti gli Stadi](#tutti-gli-stadi)
- [Crediti](#crediti)
- [Licenza](#licenza)

## 🎮 Caratteristiche

- **Interfaccia Intuitiva**: Naviga facilmente tra le opzioni del gioco.
- **Dizionari Personalizzabili**: Crea o modifica i dizionari delle parole per rendere il gioco unico.
- **Grafica dell'Impiccato**: Visualizza lo stato dell'impiccato dopo ogni errore.
- **Supporto Multiplatforma**: Funziona su Windows, macOS e Linux.

## 🛠️ Installazione

1. **Clona il repository**:

   ```bash
   git clone https://github.com/tuo-username/gioco-impiccato.git
   ```

2. **Naviga nella cartella del progetto**:

   ```bash
   cd gioco-impiccato
   ```

3. **Assicurati di avere Python installato**. Puoi scaricarlo da [python.org](https://www.python.org/downloads/).

4. **Installa le dipendenze necessarie** (se ce ne sono):

   ```bash
   pip install -r requirements.txt
   ```

## 🕹️ Come Giocare

### Avvio del Gioco

Apri il terminale (CMD su Windows, Terminal su macOS/Linux), naviga nella cartella del progetto e avvia il gioco con:

```bash
python main.py
```

Si presenterà così:

![Avvio del Gioco](https://github.com/user-attachments/assets/bfd4bb29-7e14-4ead-9c65-4449224daf55)

### Sezioni del Menu

#### [1] Gioca

Il programma ti chiederà di selezionare un dizionario disponibile.

![Selezione Dizionario](https://github.com/user-attachments/assets/dfc8dbba-28fe-4766-874c-a4ca8f200dad)

**Esempio**: Se scegli il dizionario [2]

![Dizionario Selezionato](https://github.com/user-attachments/assets/4bbb89a4-c994-4d54-8106-180a8b774047)

_(Nella versione su GitHub non si vedrà la parola... se no che gioco sarebbe?)_

![Gioco in Corso](https://github.com/user-attachments/assets/9c36d38d-48ab-4cea-9851-38178626dba7)

Dopo ogni errore, il programma disegnerà una parte dell'impiccato, proprio come alle elementari con il gessetto.

![Errore](https://github.com/user-attachments/assets/647d287f-89c4-42cd-84aa-00d873f861eb)

Se indovini una o più lettere, verranno segnate nella posizione corretta per aiutarti.

#### [2] Modifica del Dizionario

Il programma ti mostrerà diverse opzioni:

1. **Vedi il dizionario caricato**:

   ![Visualizza Dizionario](https://github.com/user-attachments/assets/c9b655e0-dd6d-422b-9304-5d3336ed7534)

2. **Crea un dizionario personalizzato**:

   ![Crea Dizionario](https://github.com/user-attachments/assets/c5a813a5-777d-469e-ac87-0d3d9941c094)

   - **Inserisci le parole direttamente nel CMD**:

     ![Inserisci Parole](https://github.com/user-attachments/assets/04136b53-cfab-46c9-b633-90d747dc3e98)

     **Esempio di Input**:

     ```
     Inserisci le parole separate dalla virgola:
     >> mela, tavolo, gatto
     ```

   - **Carica un file JSON**:

     Esempio di file:

     ```json
     ["mela", "tavolo", "gatto"]
     ```

     Selezioniamo il file:

     ![Carica File](https://github.com/user-attachments/assets/4c069e11-4370-4fee-b3ec-e660ce83e2df)

     Messaggio di successo:

     ![Successo Caricamento](https://github.com/user-attachments/assets/cfec1e12-f431-402d-8fee-23bf4cb0127d)

3. **Torna al menu principale**:

   Anche qui, semplice, torni al menu principale.

#### [3] Crediti

Scopri chi ha sviluppato questo fantastico gioco!

#### [4] Esci

Uscirà dal programma.

## 🖼️ Tutti gli Stadi

### PRIMO

![Primo Stadio](https://github.com/user-attachments/assets/62e30572-d516-4fac-be92-4312c7456559)

### SECONDO

![Secondo Stadio](https://github.com/user-attachments/assets/9a3757ad-8358-4883-9bd9-8b8b716a393e)

### TERZO

![Terzo Stadio](https://github.com/user-attachments/assets/e249e6eb-edfb-424e-817b-51772461659e)

### QUARTO

![Quarto Stadio](https://github.com/user-attachments/assets/a23294b2-4009-4a51-8dff-b484f5cb19cb)

### QUINTO

![Quinto Stadio](https://github.com/user-attachments/assets/f9aba5b7-8863-45ee-a534-9d4bbbbaa616)

### SESTO

![Sesto Stadio](https://github.com/user-attachments/assets/a84db58c-8283-48a3-bcce-71447ceda279)

### SETTIMO

![Settimo Stadio](https://github.com/user-attachments/assets/1fbd3809-57b9-48df-a2f9-226e5cd2a7ac)

### OTTAVO (Sconfitta)

Chiuderà automaticamente il programma dopo la sconfitta.

![Ottavo Stadio](https://github.com/user-attachments/assets/239c14e6-0283-490d-8741-4cffb4fa8ea8)

## 👨‍💻 Crediti

Sviluppato interamente da **Alessandro Falcari**.

- **Profilo GitHub**: [@falcoale](https://github.com/falcoale)
- **Database delle Parole**: [Link al Gist](https://gist.github.com/sinanatra/23cc714cb98b2568d664eb6b4b46f6d6)

**Versione Gioco**: v.2.0.0  
**Linguaggio**: Python

---

## 📜 Licenza

Non è permesso riutilizzare o vendere il programma senza il mio consenso. Siate onesti!

---

## 📬 Contatti

Per domande, suggerimenti o contributi, sentiti libero di aprire un [issue](https://github.com/tuo-username/gioco-impiccato/issues) o contattarmi direttamente tramite GitHub.

---

**Buon divertimento e buona fortuna! 🍀**
