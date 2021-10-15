import os


def trova_rima(verso, caratteri_rima):
    """Data una frase trova l'ultima parola
        da questa seleziona un n di caratteri finali
        trova tutte le parole che finiscono con quei caratteri
    """
    parole_del_verso = verso.split(' ')
    rima = parole_del_verso[-1]
    lettere_per_rima = rima[-caratteri_rima:]
    cmd = 'findstr /E /S ' + lettere_per_rima + ' parole.txt'
    lista_rime = os.system(cmd)
    print(lista_rime)


def scrivere_poema(poema):
    """ Fa scrivere all' utente i versi del poema.

        poema: lista vuota    
    """
    # Scrivere un verso
    # Descrizione per utente
    print("""
          Scrivi il tuo primo verso, l' ultima parola sarà selezionata per trovare una rima
          """)
    verso = input('Scrivi il tuo primo verso : ')
    poema.append(verso)

    # Scelta caratteri per rima
    # Descrizione per utente
    print("""
          Scrivi il numero di lettere finali della parola per trovare una rima
          Per esempio : 3
          """)
    caratteri_rima = int(
        input('Scrivi il numero di lettere da utilizzare per la rima : '))

    # Stampa la lista delle parole per la rima
    trova_rima(verso, caratteri_rima)

    # Seleziona la parola dall' elenco
    # Descrizione per utente
    print("""
          Scegli una parola dall' elenco soprastante
          """)
    rima_scelta = input('Scrivi qui la parola scelta : ')

    # Mostra lo stato attuale del testo
    print(""" 
          Scrivi il resto del secondo verso
          
          {}
          
          ______________________________{}
          """.format(verso, rima_scelta))

    # Scrive il secondo verso
    secondo_verso = input(
        ' Scrivi adesso il verso senza la parola per la rima : ') + " " + rima_scelta
    poema.append(secondo_verso)

    # Mostra il poema in composizione
    separatore = "-----------------------------------------------------"
    print(separatore)
    for riga in poema:
        print(riga)
    print(separatore)


def salva_poema(poema, ):
    """ Salva la poesia in un file """
    if len(poema) == 8 or len(poema) % 4 == 0:
        salva = input('Vuoi salvare il tuo poema ? (s/n) : ')
        if salva.lower() == 's':
            with open('poema.txt', 'w') as file:
                for riga in poema:
                    file.writelines(riga+'\n')
