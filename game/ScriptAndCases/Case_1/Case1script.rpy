
# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"


#color define:


# Le jeu commence ici
label first_case:
    
    WR """
        Mon nom est Walter,{w=0.5} Walter Romanng.

        je suis avocat de la défense, et aujourd’hui je débute mon second procès.

        En tant que représentant de la défense, je me doit de protéger mon client.

        Et de pouvoir enfin exercer mon talent à un niveau professionel...

        Du moins... je le pense.

        Bien que cela soit très improbable pour une cour de justice.

        Bref, j’ai quelques tours dans mon sac pour protéger mon client.

        Et je ferais n'importe quoi pour.
    """
    
    jump courtroom


label courtroom:
  
    MAE"""
    {color=#27B52C}{font=consola.ttf}8 Août, 8h15{/font}{/color}
    

    {color=#27B52C}{font=consola.ttf}Tribunal Fédéral{/font}{/color}
    
    
    {color=#27B52C}{font=consola.ttf}Salle des accusés N°1{/font}{/color}
    
    """
    WR """
    {i}*Baille*{/i}
    
    La vache... je crois que je suis arrivé trop tôt au tribunal...
    """
    K "Hum... Walter ?"
    
    WR "Ah ! Vous êtes ici inspecteur ?"with vpunch
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
    #fondu au noir sauf Kam
    jump Kam


label Kam:
    
    WR" {color=#80BEE4}(Lui, {w=0.3}C’est l’inspecteur Kam, {w=0.3} ou plutôt, {w=0.5}Eudoe Kam.{p}
        C’est un ami de longue date, {w=0.3}cependant, nous avons pris des chemins différents professionnellement parlant.){/color}"
    WR "{color=#80BEE4}(Ces derniers temps, nous avons été bouleversé par un incident tragique,{w} c’est pour cela qu’il est autant déboussolé.){/color}"
    WR "{color=#80BEE4}(Il faut dire qu’en temps normal c’est un chic type,{w} il est sympathique, mais son statut d’inspecteur laisse à désirer{w=0.1}.{w=0.1}.{w=0.1}. vraiment.){/color}"

    
    
    #Fin du fondu au noir
    K "Walter ?"
    WR "Je ne sais même pas pourquoi on se vouvoie Eudoe. {w}Tu ne penses pas qu'on devrais arreter ?"
    K "Non, continuons,{w} nous pourrons le faire en dehors du tribunal."
    WR "D'accord."
    WR"Bon, comment je vais faire pour défendre mon client moi…"
    K "Pas d’inquiétude,{w=0.2} j’ai de quoi renverser l’accusation !"
    WR"Non Kam...{w=0.2}vous avez surtout un taut de stress hors de la moyenne."
    K "Rho...{w=0.2}"
    K"Beu beu beu ! {w=0.2} C'est n’importe quoi !"
    WR"{color=#80BEE4}(Il perd tout son rôle d’inspecteur…){/color}"
    K "J’ai entendu dire que votre cliente pourrait venir d’un moment à l’autre."
    WR"Je sais oui."
    K"Et votre amie ?"
    WR"Elle est au Lycée."
    K "Ah euh{w=0.1}.{w=0.1}.{w=0.1}.{w=0.1} Vous n’avez pas peur qu’elle puisse rentrer plus tôt ?"
    WR"Hmm ?{w=0.2} C’est-à-dire ?"
    K"Fin,{w=0.2} vous voyez,{w=0.2} si elle n’a plus cours de la journée,{w=0.1} elle ne va pas attendre 17h pour revenir chez elle ?"
    WR "Non non,{w=0.2} j’irais la chercher après le procès."
    K"Hum…{w=0.2} D’accord."
    WR"{color=#80BEE4}(Ma cliente est une jeune fille.){/color}"
    WR"{color=#80BEE4}(Vous savez,{w=0.2} le genre de fille un peu{w=0.1}.{w=0.1}.{w=0.1}.{w=0.2} hyperactive.){/color}"
    WR"{color=#80BEE4}(Elle s’appelle Kale,{w=0.2} Kale Bennett,{w} et est accusée du meurtre de mademoiselle Rose Marshel.){/color}"
    K"En parlant du loup..."
    WR "Elle est arrivée ?"
    K"Non pas encore,{w=0.2} mais j’ai reçu son dossier."
    WR"Ne me le lisez pas,{w=0.2} je le connais déjà, {w=0.2}il est vide."
    K"Ahah !{w=0.2} Ça me rappelle un livre ça !"
    WR"Lequel ?"
    K "C’était un livre sur {i}« Ce que les hommes savent à propos des femmes »{/i}."
    WR"Et ?"
    K "C’est 100 pages blanches…"
    WR"{color=#80BEE4}(Kam tu achètes vraiment des livres aussi frauduleux... ?){/color}"
    #Arrivé de Kale
    jump Kale

label Kale:
    
    KA"Monsieuuurrr !!!" with vpunch
    WR"Arghh !"with vpunch 
    WR"Vous m’avez fait peur !!!"
    KA"Sauvez moi j’vous en prie !{w=0.2} J’ai rien fait et me voilà avec des menottes aux poignets !"
    WR"{color=#80BEE4}(Hum… Je vais essayer…){/color}"
    K"{i}Dis lui un truc Walter !{/i}"
    WR"Euh… {w=0.2}Bien sûr...{w=0.2}voyons..."
    KA"Je comprends pas !!!{w=0.3}"
    KA"Pourquoi moi ???"with vpunch
    WR"A vrai dire{w=0.1}.{w=0.1}.{w=0.1}.{w=0.2} Moi non plus je ne sais pas pourquoi ça m’arrive à moi..."
    KA"J’ai {b}PAS{/b} tué cette femme !"
    WR"Encore heureux."
    WR"{color=#80BEE4}(Elle est très énergique dit donc...){/color}"
    K"Walter arrête de parler comme ça ! Tu vas la stresser !"
    WR"Mais-{w=0.2} Et moi ?!"
    K"T’es avocat de la défense, tu peux pas te permettre de douter de toi !"
    WR"{color=#80BEE4}(Pour une fois, Kam marque un point...){/color}"
    WR"TU AS RAISON KAM !!" with vpunch
    WR"{color=#80BEE4}(Wow...{w=0.2}J'aurais jamais cru dire ça un jour...){/color}"
    WR"{b}BON !!{/b}"with vpunch
    KA"Ah !{w=0.2} Cette lueur dans vos yeux monsieur !"
    WR"Je vais vous tirer d’affaire Madame Bennett !"
    KA"Vous pouvez m’appeler Kale…"
    WR"Ah euh...{w=0.2} Madame Kale ?"
    K"Walter… {w=0.2}On dit pas madame Kale.{w=0.2} On dit juste…{w=0.2} Kale."
    WR"{color=#80BEE4}(Il à mangé du lion ce matin Kam !){/color}"
    KA"Monsieur, vous avez décidé de me défendre !"
    WR"{color=#80BEE4}(Je suis loin d’avoir Alzheimer Kale…){/color}"
    

    # Here the A key is used to say that the information is True 
    # If it is true, we go to the success label
    # if not, we go to the failure corresponding label
    # which goes back to where we made a mistake
    
    #ici la touche A serivrait à dire que l'affirmation est vrai
    # Si elle est vraie, on passe au label succes
    # sinon on passe au label echec correspondant
    # qui reviens au label où l'on s'est trompé
    init python:
        def labeljump(label_name):
            renpy.jump(label_name)
    
        
    # label Testimony:
    #     KA"information 1"
    #     key "z" action Jump("Kale")
        # python:
        #     def on_key_event(e):
        #         if e.event_type == keyboard.KEY_DOWN and e.name == 'z':
        #             labeljump("Kale")
        #     keyboard.hook(on_key_event)

        # $ labeljump("Kale")
    # Définition de l'étiquette Testimony






        # if A pressed: 
    #         jump fail_T1
    #     # Else:
    #         jump T2
    # label T2:

    #     KA"information 2" # True information
    #     # If A pressed: 
    #         jump success
    #     # Else:
    #         jump T3
    # label T3:

    #     KA"information 3"
    #     # if A pressed: 
    #         jump fail_T3
    #     # Else:
    #         jump Testimony

            



    

 

    
    
    



return
