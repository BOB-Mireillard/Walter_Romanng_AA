
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
    K"Ouais ! Si t'a décidé de la défendre, c'est que t'es sûr de toi !"
    WR"{color=#80BEE4}(Kam... J'ai décidé de la défendre parce que c'est une amie d'enfance...){/color}"
    WR"Euh, j'ai pas vraiment..."
    #show benet crying
    WR"J'veux dire...! J'ai pas vraiment tout le rapport de l'affaire..."
    K"Ah bon ?"
    ##changer peut etre un dialogue par 1 pour show les images
    WR"Oui, j'ai... Euh... Le rapport d'autopsie... l'arme du crime... Un plan de la maison."
#######################" Maybe flashback"
    K "Ah d'ailleurs, il faut savoir que le dossier sera immédiatement envoyé aux oubliettes après le procès."
    WR"Quoi ?!!"with vpunch
    K"C'est une tradition quand les procureurs sont tués, on ne garde plus leurs affaires."
    WR"Je ne pourrais plus jamais toucher au dossier après le procès ?"
    K"Oui."
    #Kam regarde le 4e mur 
    K"Souviens toi bien de ca Walter."
    K"c'est d'ailleur la raison de mon chagrin..."
#########################################
    WR "Bon. Qui est ce procureur ?"
    #monter skyboarder
    K "Mr Skyboarder, je crois bien."
    WR "C'est qui ce monsieur encore ?"
    K"Un procureur qui travaillait...{w=0.2} Avec la victime."
    K"Cependant."
    K"Il y a un deuxième procureur..."
    WR "UN{w=0.1} DEUXIEME{w=0.1} PROCUREUR ?!?!?!" with vpunch
    KA"Mais-"
    KA"Comment c'est possible enfin !?"
    K "Quand un procureur se fait tuer, on parle beaucoup de lui vous savez."
    K "Et plusieurs procureurs ont voulut prendre l'accusation !"
    WR "Comme qui ?"
    K"Je ne sais pas, mais il y avait{w=0.2} pleins,{w=0.2} pleins,{w=0.2} pleins de gens en costumes qui voulait le dossier ! "
    WR "Aïe ! C'est vraiment mal parti..."
    KA "Je vais être déclarée coupable, c'est ca... ?"
    # **fondu au noir avec Kale**
    WR "{color=#80BEE4}(C'est mon amie après tout...){/color}"
    WR "{color=#80BEE4}(Je n'ai pas le choix...{w} je n'ai pas le droit à l'erreur.){/color}"
    WR "{color=#80BEE4}(Jamais je n'abandonnerais ! Ma carrière d'avocat...){/color}"
    WR "{color=#80BEE4}(NE FAIT QUE COMMENCER !){/color}" with vpunch
    #kale disparait
    WR"{w=0.3}{color=#80BEE4}(C'est donc ça,{w=0.2} être avocat de la défense ?){/color}"
    WR"{color=#80BEE4}(Commencer sans rien avoir, et remonter les pistes jusqu'à la victoire...){/color}"
    WR"{color=#80BEE4}(Tout cela est vrai, puisque ça rime...){/color}"
    WR"{color=#80BEE4}(C'est peut-être ça la magie de la justice.){/color}"
    WR"{color=#80BEE4}(Après tout, elle serait incapable de tuer quelqu'un, je la connais bien, c'est mon amie){/color}"
    WR"{color=#80BEE4}(Si je montre un semblant d'insécurité, ça va réduire ma plaidoirie à néant, il faut que j'assure !){/color}"
    #fin du fondu
    KA"Romanng ?"

    WR "?!" with vpunch
    WR "Vous pouvez compter sur moi."
    huissier"Le procès va bientôt débuter, la défence et l'accusée sont appelés à rejoindre la salle d'audience !"
    K"Bon, il est temps d'y aller ?"
    WR"Je suppose que oui."
    KA"Oh là là je stresse !! Mon cœur bat si vite !"
    WR"Pas d'inquiétude ! Je me sens prêt !"
    K"T'inqiète pas Walter, on est bien."
    #fondu au nègre
    WR"Et c'est ainsi que mon second procès commença,{w=0.2} dans la crainte,{w=0.2} livré à moi-même,{w=0.1} sans connaitre l'affaire."
    WR"Et j'était loin de me douter de ce que ce procès allait m'approter."
    jump huit_h_quarante

label huit_h_quarante:
    MAE"""
    {color=#27B52C}{font=consola.ttf}8 Août, 8h40{/font}{/color}
    

    {color=#27B52C}{font=consola.ttf}Tribunal Fédéral{/font}{/color}
    
    
    {color=#27B52C}{font=consola.ttf}Salle d'audiance N°1{/font}{/color}
    
    """


    "BROUAHAHAHAHAHAHAH"
    # **JUGE marteau**
    JUGE"Je déclare la séance ouverte pour le procès de Madame Kale Bennett."
    JUGE"Est-ce que l'accusation et la dégense sont prête ?"
    SS"L'accusation est prête."
    OS "Hum...{w=0.3} l'accusation est en mesure de prouver la culpabilité de madame Bennett."
    WR "..."
    JUGE "Qu'en est-il de la défense ?"
    WR "..."
    WR "{color=#80BEE4}(Je...{w=0.3}Je stresse oh mon dieu... !){/color}"
    JUGE"Monsieur Romanger ?"
    WR"Ah! Euh... Romanger ?"
    OS "Votre honneur ! Il ne s'appelle pas « Ro-manger », il se nomme Romanng... "
    OS"Vous savez,{w=0.2} Ro-{w=0.25}mangue."
    WR"Euh... Merci..."
    JUGE "Êtes-vous prêt monsieur Romanng ?"
    WR "Oui. Je-{nw}"
    WR"Fin, la défense est prête votre honneur !"
    WR "{color=#80BEE4}(Non ce n'est pas vrai...{w} mais je ne veux pas effrayer Kale...)"
    JUGE"J'aimerais que la défense fasse son exposé préliminaire."
    WR"Moi ? Euh-"
    JUGE"Vous êtes prêt bien-sûr ?"
    WR"Aboslument ! Laissez-moi juste, un peu de temps..."with vpunch
    KA"Vous connaissez la victime au moins ?"
    WR"Bien sûr que je connais la victime ! C'est..."
    menu Qui_est_la_victime:
        "Qui est la victime ?"
        "Madame Marshel":
            jump victime_is_rose
            #block of code to run
        "Kale Bennett":
            jump victime_is_kale
        "Eudoe Kam":
            jump victime_is_kam
            #block of code to run
label victime_is_kam:
    WR"Eudoe Kam ?"
    K"Hein ?? MOI ?? QU'EST CE QUE J'AI FAIT ???" with vpunch
    KA"Mais c'est l'inspecteur !"
    WR"Ah ! Oui, pardon Kam... En fait la victime c'est..."
    jump Qui_est_la_victime
label victime_is_kale:
    WR"Kale Bennett !"
    KA"MAIS C'EST MOI !" with vpunch
    WR"Quoi ?Ah... Mes excuses, la victime est en fait..." with vpunch
    jump Qui_est_la_victime
label victime_is_rose:
    WR"Madame Marshel..."
    JUGE"Monsieur Romanng, nous vous attendons toujours pour votre exposé préliminaire."
    WR"Oui, votre honneur."
    WR"La défense plaide...{w} Non coupable !"
    OS"Comment osez-vous plaider non-coupable sur une telle affaire !?" with vpunch
    WR"Moi ? Hé bien..."
    JUGE "Qu'en est-il de l'accusation ?"
    OS"Nous, l'accusation, plaidons coupable.{w} Madame Bennett s'est rendue au domicile de Madame Marshel pour la tuer, avec mobile."
    JUGE"Bien, veuillez introduire les preuves madame Kassilth."
    OS"Très bien, d'abord, nous avons ce couteau de 15cm de longueur."
    OS"C'est un couteau de cuisine simple, qui à été utilisé pour poignarder la victime à différentes reprise."
    OS"Oh, et il à été lavé par la suite."
    OS"Il a ensuite été déposé devant la victime."
    WR "{color=#80BEE4}(Ça me crispe tellement...)"
    OS"Voici un plan de la salle où la victime a été retrouvée, c'était un débarras où y figurais plusieurs caisses et matériaux inutilisés."
    OS"Et j'ai ici le rapport d'autopsie de la victime, elle aurait été poignardée à plusieurs reprise entre 14 heures et 15 heures."
    OS"Ses plaies présentent des morceaux de verres mais également de métal provenent du couteau."
    OS"J'ai également:"
    OS"Un verre d'eau renversé par terre."
    OS"Un plan de la maison, dans l'ensemble, des traces de luttes, des fenêtres brisées, du sang au sol, et d'autres détails alarmants."
    OS"De plus, sous la table, il est écrit le nom de la coupable."
    OS"Puis nous avons récupéré les morceaux de verre issu de la fenêtre qui a été brisée."
    WR"{color=#80BEE4}(Ça fait un paquet de preuve !)" with vpunch
    JUGE "Bien, faites venir votre premier témoin à la barre."
    OS"J'appelle, l'accusée, Kale Bennett à la barre."
    JUGE "L'accusée n'a pas le droit de témoigner contre elle-même voyons !" with vpunch
    OS"Elle nous donnera sa version des faits, et la défense pourra contre-argumenter."
    # **deskslam
    WR"ÇA N'A AUCUN SENS ! Vous voyez bien que je ne peux argumenter contre mon client !"
    OS"Refusez-vous l'opportunité de disculper votre client ?"
    KA"Je vais me disculper ?!"with vpunch
    OS"En effet."
    WR"{color=#80BEE4}(C'est un piège, tombe pas dedans !)"
    WR"Kal-{nw=2}"
    OS"N'interférez pas !"
    JUGE"Accusée !"
    JUGE"Voulez-vous témoigner ?"
    KA"OUI !" with vpunch
    WR"{color=#80BEE4}(C'est déjà mal parti... Elle va s'incriminer...)"
    OS"Bien, alors, témoignez."
    KA"AVEC PLAISIR !"with vpunch
    narrator "DEPOSITION DU TEMOIN"

    
label case_A_A_A:
    #case, proces, temoignage A=1
    "aaa"

    show screen attack("one_pm")
    KA"I went to the victim's house around 1 pm."
    # I want to skip the "one_pm" label if I don't call "attack" 
    label one_pm:
        WR"Wait a minute !"
    # and when this speech end:
    hide screen attack
    # It goes here (so either you directly go here, either you pass by one_pm)
    KA"I loved her you know, she was my best friend..."





    KA"Mais après être arrivée, je me sentait très fatiguée,{w=0.3} je n'avais jamais ressenti ça !"
    KA"Rose m'a demandée d'aller m'endormir, ce que j'ai donc fait."
    KA"À mon réveil, il y avait...{w} Du sang partout !"
    KA"Il y avait quelqu'un dans la maison, qui criait dans tout les sens !"
    KA"Puis ensuite, sur un coup de tête, on m'a menottée... Pourquoi ?"
    KA"Je vous jure que je suis innocente !"
label case_A_A_A_next:
    WR"{color=#80BEE4}(Cela me semble, compromis ?)"
    
    WR"{color=#80BEE4}(Je ne sais même pas comment m'en sortir devant ce témoignage, je crois qu'il n'y a pas de contradiction...?)"
    # Vue sur orchid
    WR"{color=#80BEE4}(La procureure à l'air chiffon.)"
    OS"Très bien; La victime à fait entendre sa version des faits."
    OS"Avez-vous une raison appparente de pourquoi vous vous êtes endormie ?"
    KA"Non, absulument pas."
    OS"Hmm... Très bien."
    JUGE"Monsieur Romanng ?"
    WR"Oui votre honneur ?"
    JUGE"Je vous sens stressé. Êtes-vous sûr de vouloir défendre votre client ?"
    WR"Bien sûr !"
    JUGE"Très bien, vous avez fait entendre à cette cour votre capacité."
    JUGE"Alors veuillez commencer votre contre interrogatoire."
    WR"Bien sûr..."
    #flm de faire le contre interrogatoire mtn chepa encore comment faire
    
## HE TAMER APRES LE CONTRE INTERROGATOIRE DE MES COUILLES

    #la walter cherche a trouver pk kale c'est endormie
    WR"Votre honneur ! Ce verre d'eau est sûrement notre suspect numéro un !"
    JUGE"Ce verre d'eau ?"
    WR"Hé oui !"
    "{b}BROUHAHAHAHAHAH{/b}"
    JUGE"Silence dans la cour !" with vpunch
    JUGE "Veuillez-nous expliquer monsieur Romanng."
    WR "Voyez-vous, ce verre à sûrement dû être usé par madame Bennett après être rentrée dans la maison."
    OS "C'est insensé ! Vous n'avez aucune preuve pour corroborer vos propos !"
    WR"Je suis bien navré de faire des propositions insensées, mais c'est simplement parce que la preuve est limitée."
    OS "Que voulez-vous dire ?"
    WR"Le contenu de ce verre n'a pas été analysé, tout simplement parce que la victime ne présentait pas de traces qu'elle aurait été droguée via ve verre."
    WR"Mais qui nous dit que ce verre n'a pas drogué..."
    WR "{b}MA{/b} CLIENTE ?" with vpunch
    KA"Je ne me souviens pas avoir bu dans ce verre..."
    WR"!!!" with vpunch
    KA"Du moins, je ne me souviens pas de ce qu'il s'est passé avant de m'être endormie."
    OS"Votre honneur, je crois que le témoin n'est pas apte à témoigner."
    #objection#
    WR"Ce que dit le témoin prouve tout à fait qu'elle aurait pu être droguée !"
    WR "Je demande à la cour que ce cas soit examiné."
    #objection
    OS"C'est insensé, absolument rien ne prouve cela !"
    WR"Cette éventualité ne peut être écartée de l'affaire au vu des doutes qui planent sur cette preuve."
    WR"Il serait prudent d'examiner le contenu du verre restant."
    #marteau
    JUGE "Assez. Ce verre semble poser problème..."
    JUGE "Je demande à ce que la preuve soit examinée en détail."
    JUGE "L'accusation a-t-elle d'autres témoins ?"
    SS "Bien sûr !"
    WR"{color=#80BEE4}(Le deuxième procureur...)"
    JUGE"Vous daignez enfin à vous réveiller..."
    SS"Oui votre honneur, j'aimerais appeler un témoin."
    JUGE"Qu'en est-il ?"
    SS"L'insecteur de police ayant travaillé sur cette affaire, l'inspecteur KAM !"
    WR"{color=#80BEE4}(Allez Kam ! Il est temps de te cuisiner.)"
    #fondu au nègre
    K"Bien le bonjour."
    JUGE "Bonjour, veuillez décliner votre identité, s'il vous plaît."
    K"Je suis Eudoe Kam, inspecteur de police."
    K"Je suis l'inspecteur en charge de cette affaire, et l'un des premiers à être arrivé sur la scène du crime."
    JUGE "Je vois."
    SS"Très bien, maintenant inspecteur, veuillez nous dire ce que vous savez sur la victime !"
    window hide 
    pause
    #Déposition du témoin
    "Etat de la victime"
    K"Selon le rapport d'autopsie, la victime est morte entre 14 heures et 15 heures."
    K"Les plaies de la victime ont étés difficiles à examiner."
    K"Nous sommes presque sûr que l'arme du crime est le couteau."
    K"Les plaies de la victime présentent des traces de verre et de métal."
    K"Ce qui laisse à penser que c'est Marshel qui à explosé la vitre en essayant d'échapper à son meurtrier."
    K"La victime a sûrement été prise par surprise lorsqu'elle quittait sa chambre..."
    JUGE "Très bien, je vois."
    JUGE "Est-ce que quelqu'un ici a une objection à faire sur ce que l'inspecteur a dit ?"
    WR "Hmmm..."
    WR "Une objection ?"
    SS "Oui."
    SS "Le mot qui permet de réfuter une allégation."
    WR"{color=#80BEE4}(Ai-je une preuve permettant de réfuter le témoignage de Kam ?)"
    KA "Monsieur ne vous attardez pas sur les petits détails..."
    WR "{color=#80BEE4}(Les petits détails hein ?)"
    WR "Non."
    WR "Je ne pense pas avoir d'objection pour l'instant."
    WR"{color=#80BEE4}(Je dois juste me contenter de me souvenir de ce dernier.)"
    JUGE "Très bien, l'inspecteur a-t-il d'autres informations à révéler à cette cour ?"
    SS "Monsieur Kam va nous parler du déroulement du crime."
    JUGE "Très bien, veuillez témogner."
    WR'"Témoigner" votre honneur.'
    JUGE "Je dis ce que je veux."
    WR "!!" with vpunch
    #Déposition du témoin
    "Témognage sur le déroulement du crime."
    K"Le meurtrier a ouvert la porte de la maison."
    K"La victime qui sortait de sa chambre s'est retrouvée nez à nez avec lui."
    K"Le meurtrier a essayé immédiatement de la poignarder mais elle s'est débattue."
    K"Dans l'altercation, la vitre a été brisée par madame Marshel."
    K"Dans la finalité, la victime a été poignardée à plusieurs reprises, au même endroit !"
    K"Pour finir, le meurtrier a été laver son couteau et a déplacé la victime dans l'arrière salle."

    WR "{color=#80BEE4}(C'est,{w} effroyable.)"
    WR "{color=#80BEE4}(Pourquoi j'ai accepté cette affaire...)"
    JUGE "Monsieur Romanng ?"
    WR "Oh euh, donc vous dites que la victime s'est débattue et a brisé la vitre ?"
    K"C'est certain."
    JUGE "Très bien, veuillez contre interroger le témoin monsieur Romanng."
    #contre interrogatoir

    K"""
    {color=#27B52C} Le meurtrier a ouvert la porte de la maison.

    {color=#27B52C}La victime qui sortait de sa chambre s'est retrouvée nez à nez avec lui.

    {color=#27B52C}Le meurtrier a essayé immédiatement de la poignarder mais elle s'est débattue.

    {color=#27B52C}Dans l'altercation, la vitre a été brisée par madame Marshel.

    {color=#27B52C}Dans la finalité, la victime a été poignardée à plusieurs reprises, au même endroit !
    
    {color=#27B52C}Pour finir, le meurtrier a été laver son couteau et a déplacé la victime dans l'arrière salle.
    """





    
    




    


    


    
    




            



    

 

    
    
    



return
