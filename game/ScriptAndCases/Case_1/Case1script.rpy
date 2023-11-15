# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"
image BOB ="BOB.png"
# Déclarez les personnages utilisés dans le jeu.
define bob = Character(_('BOB'), color="#c8ffc8")

# Le jeu commence ici
label first_case:
    show BOB at right
    bob "salut"
    menu:

        bob "eske tu veux"

        "oui":

            jump c

        "non":

            jump d
label c:
    bob "dakor"
    jump aa
label d:
    bob "ok"
    jump aa
label aa:
    bob "AAAAAAAA"
    jump start_intro

    
    
    



return
