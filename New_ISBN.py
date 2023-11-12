from tkinter import*

def L(a):
    '''Une fonction qui permet de transformer un nombre de classe int en une liste :
    -Pour cela cette fonction utilise une condition et une boucle while.
    -Cette fonction se repose principalement sur la division euclidienne.
    '''
    if a == 0: 
        #Dans le cas où le nombre est 0, la fonction retournera [0]
        return [0]
    #On associe une liste à tab
    tab = []
    #Tant que le nombre 'a' sera supérieur à 0 on exécutera le programme ci dessous
    while a > 0:
        #On associe à b le reste de la division euclidienne de 'a' par 10
        b = a % 10
        #On insere b (le reste) à la premiere position de la liste tab
        tab.insert(0, b)
        #On associe à 'a' le quotient de la division euclidienne de 'a' par 10, ainsi le processus sera repeter jusqu'a ce que a soit inferieur ou = à 0
        a = a // 10
    return tab


def validation_isbn():
    '''Cette fonction permet de confirmer la validation d'un isbn :
    -Elle utilise principalement des conditions.
    -Elle utilise des opérations arithmétiques
    -Elle utilise egalement la fonction précédente 'L' pour transformer un nombre en une liste'''
    # Récupération de l'ISBN saisi dans le champ de texte
    isbn = Isbn.get()

    # Conversion de l'ISBN en une liste
    tab=L(isbn)

    # Initialisation de la variable b
    b = 0

    # Vérification de la longueur de l'ISBN (doit contenir 13 chiffres)
    if len(tab) == 13:
        # Suite d'opérations pour pouvoir calculer la clé de controle.
        for i in range(12):
            if i % 2 == 0:
                tab[i] = int(tab[i]) * 1
            else:
                tab[i] = int(tab[i]) * 3
            b = b + tab[i]

        # Calcul de la clé de contrôle
        if b % 10 == 0:
            cle_controle = 0
        else:
            cle_controle = 10 - (b % 10)

        # Vérification de la clé de contrôle
        if cle_controle == int(tab[12]):
            TexteC['text'] = "L'ISBN est bien validé."
        else:
            TexteC['text'] = "L'ISBN n'est pas validé."
    else:
        TexteC['text'] = "L'ISBN doit contenir 13 chiffres."
        # Assertion pour vérifier que l'ISBN contient exactement 13 chiffres
        assert len(str(isbn)) == 13, "L'ISBN doit contenir exactement 13 chiffres"

# Création de la fenêtre principale
F = Tk()
F.geometry('1000x500')
F.title('ISBN')
F['bg'] = 'black'
F.resizable(height=False, width=False)

# Création des textes
Texte = Label(F, text='Veuillez saisir votre ISBN ci-dessous :', font=("Verdana", 15, "italic bold"), fg='white', bg='black')
TexteB = Label(F, text="N'oubliez pas d entrer les 13 chiffres de l'ISBN", font=('Verdana', 12, 'italic bold'), fg='white', bg='black')
TexteC = Label(F, text='', font=('Verdana', 12, 'italic bold underline'), fg='white', bg='black')

Texte.pack()
TexteB.pack()
TexteC.place(x=360, y=400)

# Création de l'entrée Isbn et du champ de saisie ISBN
Isbn = IntVar()
isbn_entry = Entry(F, textvariable=Isbn)
isbn_entry.place(x=430, y=200)

# Bouton d'entrée pour appeler la fonction validation_isbn
BT = Button(F, text="Entrer", bg='white', fg='black', font=('Verdana', 14, 'bold underline'), command=validation_isbn)
BT.pack(side=LEFT, padx=450)

# Lancement de la boucle principale de l'interface graphique
F.mainloop()

