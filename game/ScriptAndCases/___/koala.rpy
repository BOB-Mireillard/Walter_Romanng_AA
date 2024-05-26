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
    hide kam helps with dissolve
    
    show walter concentrate with dissolve
    WR"Une femme ?"
    hide walter concentrates
    show Kam angry
    K"Non plus.."
    hide Kam angrys
    show walter pointing
    WR"Un enfant ?!"
    hide walter pointings
    show Kam angry
    K"Toujours pas."
    hide Kam angrys
    show walter chocked
    WR"A quoi alors ??"
    hide walter chockeds
    
    show kam confident
    K"Un Koala."
    hide kam confidents
    show walter chocked
    WR"???"
    WR"Qu'est ce qui vous fait dire ça ?"
    hide walter chockeds
    show kam happy
    K"Tout d'abord, on est dans un zoo."
    hide kam happys
    show walter wtf
    WR"Oui, et ?"
    hide walter wtfs
    show kam angry
    K"Et enfin, Nous sommes actuellement..."
    K"Dans l'enclos des Koalas."
