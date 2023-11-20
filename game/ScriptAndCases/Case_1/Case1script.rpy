# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"


#color define:


# Le jeu commence ici
label first_case:
    
    WR """
        Mon nom est Walter,{cps=2} {/cps} Walter Romanng.

        je suis avocat de la défense, et aujourd’hui je débute mon second procès.

        En tant que représentant de la défense, je me doit de protéger mon client.

        Et de pouvoir enfin exercer mon talent à un niveau professionel...

        Du moins... je le pense.

        Bien que cela soit très improbable pour une cour de justice.

        Bref, j’ai quelques tours dans mon sac pour protéger mon client.

        Et je ferais n'importe quoi pour.
    """
    
  
    "{color=#27B52C}{font=consola.ttf}8 Août, 8h15{/font}{/color}"
    "{color=#27B52C}{font=consola.ttf}Tribunal Fédéral{/font}{/color}"
    "{color=#27B52C}{font=consola.ttf}Salle des accusés N°1{/font}{/color}"
    jump courtroom


label courtroom:
    WR """
    {i}*Baille*{/i}
    
    La vache... je crois que je suis arrivé trop tôt au tribunal...
    """
    K "Hum... Walter ?"
    with vpunch
    WR "Ah ! Vous êtes ici inspecteur ?"
    K " Je me charge malheureusement de l'affaire..."
    WR "\"Malheureusement\" ? C'est à dire ?"
    K"Nous parlons du procès pour ce meurtre là…"
    WR"Je sais, je sais..."
    WR"Ne vous en faites pas, j’ai une totale confiance en celle que je défends aujourd’hui."
    K"Vous êtes sûr... ?"
    WR"Totalement.{p}{color=#80BEE4}(C’est qu’il a l’air fatigué le Kam…){/color}"
    K"Monsieur... Je sais ce que vous vous dites…"
    K"Pourquoi suis-je tant anormal par rapport aux autres jours ?"
    WR"{color=#80BEE4}(Si vous saviez à quel point j’me soucie de comment j’vais pouvoir défendre mon client, inspecteur…){/color}"
    K"C’est que… Je ne vois pas comment vous pouvez supporter ça…"
    WR"On s'y fait."
    K"Je travaille désormais avec le procureur Skyboarder."
    WR"Ah !? {p=0.5}Et… C’est qui ce fameux procureur ?"
    K" Vous ne le connaissez pas ?"
    WR" Jamais entendu parler."
    K" C’est un procureur{cps=3}...{/cps} sympa ? Je suppose."
    WR" Vous ne le connaissez pas, pas vrai ?"
    K" Non pas vraiment, il faut dire que c’est la première affaire que je traite avec lui."
    WR" Il viendra au procès ?"
    K" Non, enfin..."
    K" Je ne crois pas."
    WR" {color=#80BEE4}(Hé bien dis donc, c’est qu’il est pas très futé le Kam !){/color}"
    K"Hé, je sais à quoi vous pensez Walter : {i}\n\"eugngngn il est pas très futé le Kam ! \"{/i}"
    K" Mais je suis tout autant déboussolé que vous, vous savez !"

    
    
    
    
 

    
    
    



return
