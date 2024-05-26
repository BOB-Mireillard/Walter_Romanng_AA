#ici ducoup c une case de merde qui sera surement perdu dans les fichiers du jeux
label koala:
    image zoo="zoo.png"
    scene zoo
    
    image walter concentrate ="walter concentrate.png"
    image walter pointing ="walter pointing.png"
    image walter chocked ="walter chocked.png"
    image walter wtf ="walter wtf.png"
    image kam help ="kam help.png"
    image kam confident ="kam confident.png"
    image kam happy ="kam happy.png"
    
    show kam help
    K"Walter je crois qu'on a affaire non pas à un homme..."
    hide kam help
    show walter concentrate 
    WR"Une femme ?"
    hide walter concentrate
    show Kam angry
    K"Non plus.."
    hide Kam angry
    show walter pointing
    WR"Un enfant ?!"
    hide walter pointing
    show Kam angry
    K"Toujours pas."
    hide Kam angry
    show walter chocked
    WR"A quoi alors ??"
    hide walter chocked
    show kam confident
    K"Un Koala."
    hide kam confident
    show walter chocked
    WR"???"
    WR"Qu'est ce qui vous fait dire ça ?"
    hide walter chocked
    show kam happy
    K"Tout d'abord, on est dans un zoo."
    hide kam happy
    show walter wtf
    WR"Oui, et ?"
    hide walter wtf
    show kam angry
    K"Et enfin, Nous sommes actuellement..."
    K"Dans l'enclos des Koalas."
