# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"


# Le jeu commence ici
#color define

label start_intro:
  play music "audio/ost/Test_musique_dintro.mp3" 
  scene black with dissolve
  


 
  WR"""
  Chaque être vivant en craint un autre…{w=1.7}{nw}
  
  Certains ont peur du poids de leurs péchés.{w=2.1}{nw}

  D’autre ne s’en soucie plus.{w=2.7}{nw}
  
  La pluie et le vent font retentir les échos de la vie. {w=1.7}{nw}
  
  Et quand elle s’arrête ?{w=1.5}{nw}
  
  ... {w=1.1}{nw}
  
  Ce monde est cruel.{w=1.5}{nw}
  
  Nous sommes tous par défauts livrés à nous-mêmes. {w=2.5}{nw}
  
  Craignant les autres, tout cela instauré dans une chaîne \ndont nous sommes les maillons. {w=3.5}{nw}
  
  Mais tel le pygargue, guettant sa proie.{w=1.5}{nw}

  """ 
  "La balance trouve toujours,{w=1.2} le bon côté ou pencher." 
  stop music fadeout 1
  jump first_case

    
    



return
