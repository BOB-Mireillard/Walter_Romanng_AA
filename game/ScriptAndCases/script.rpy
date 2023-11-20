# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"
# Déclarez les personnages utilisés dans le jeu.
##
# Le jeu commence ici

##############################################################################""
#test du son
######################################""
##regular taps, medium intervals
#define sounds = ['audio/A1.ogg', 'audio/A2.ogg', 'audio/A3.ogg', 'audio/A4.ogg', 'audio/A5.ogg']

##light taps, smaller intervals
#define sounds = ['audio/B1.ogg', 'audio/B2.ogg', 'audio/B3.ogg', 'audio/B4.ogg', 'audio/B5.ogg']


##both combined
define sounds = ['audio/bip.ogg']

init python:
    def type_sound(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show": #if text's being written by character, spam typing sounds until the text ends
            renpy.sound.play(renpy.random.choice(sounds), loop =True)
## a  quand on aura plusieurs sound en 
            #for i in range (50):
                #renpy.sound.queu(renpy.random.choice(sounds))
            
            #dumb way to do it but it works, dunno if it causes memory leaks but it's almost 6AM :v



        elif event == "slow_done" or event == "end":
            renpy.sound.stop()


#example of a character with the typing sound
define Type = Character("Character with typing", callback=type_sound)


#just don't add the character callback if you don't want that ound
define NoType = Character("Character without typing")

#regular narration that doesn't have a character attached to it, add an # to it if you don't want that
define narrator = Character(callback=type_sound)




##example:

image WR ="WR.png"
# Déclarez les personnages utilisés dans le jeu.
define WR = Character(('Romanng'), color="#ffffffff", callback=type_sound)
label start:
    stop music fadeout 1
    menu:
        "intro":
            jump start_intro
        "Case 1":
            jump first_case

    
    
    



return
