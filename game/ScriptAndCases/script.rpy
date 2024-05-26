python:
    import keyboard
# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"
# Déclarez les personnages utilisés dans le jeu.
##
# Le jeu commence ici

##############################################################################""
#test du son
######################################""


#### Code pour les touches: attaquer
screen attack(check):
    key 'a' action Jump(check) 
####################################


init python:
    
    vpunch_o = Move((0, 10), (0, -10), .1, bounce=True, repeat=True, delay=.275)
    vpunch = Move((0, 50), (0, -50), .1, bounce=True, repeat=True, delay=.275)

label start:
    
    menu:

        "intro":
            jump start_intro
        "Case 1":
            jump first_case
        "Case1 (courtroom)":
            jump courtroom
        "kam (courtroom)":
            jump Kam
        "Kale":
            jump Kale
        "Koala":
            jump koala
        "8h40":
            jump huit_h_quarante

    
    
    



return
