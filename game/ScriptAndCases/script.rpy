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
# 'audio/sounds/bip1.ogg'
define sounds = ['audio/sounds/bip2.mp3','audio/sounds/bip3.mp3','audio/sounds/bip4.mp3']
define typewrite_sounds= ['audio/sounds/A1.ogg', 'audio/sounds/A2.ogg', 'audio/sounds/A3.ogg', 'audio/sounds/A4.ogg', 'audio/sounds/A5.ogg','audio/sounds/B1.ogg', 'audio/sounds/B2.ogg', 'audio/sounds/B3.ogg', 'audio/sounds/B4.ogg', 'audio/sounds/B5.ogg']

init python:
    vpunch_o = Move((0, 10), (0, -10), .1, bounce=True, repeat=True, delay=.275)
    vpunch = Move((0, 50), (0, -50), .1, bounce=True, repeat=True, delay=.275)

    def type_sound(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done": #if text's being written by character, spam typing sounds until the text ends
            for i in range (50):
                renpy.sound.queue(renpy.random.choice(sounds))
        elif event == "slow_done":
            renpy.sound.stop()
    def type_sound_typewrite(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done": #if text's being written by character, spam typing sounds until the text ends
            for i in range (50):
                renpy.sound.queue(renpy.random.choice(typewrite_sounds))
        elif event == "slow_done":
            renpy.sound.stop()


#example of a character with the typing sound
define Type = Character("Character with typing", callback=type_sound)


#just don't add the character callback if you don't want that ound
define NoType = Character("Character without typing")

#regular narration that doesn't have a character attached to it, add an # to it if you don't want that
define narrator = Character(callback=type_sound)
define MAE = Character(callback=type_sound_typewrite) #MAE pour machine a





##example:

image WR ="WR.png"
# Déclarez les personnages utilisés dans le jeu.
define WR = Character(('Romanng'), color="#ffffffff", callback=type_sound)
define K = Character(('Kam'), color="#ffffffff", callback=type_sound)
label start:
    stop music fadeout 1
    
    menu:

        "intro":
            jump start_intro
        "Case 1":
            jump first_case
        "Case1 (courtroom)":
            jump courtroom

    
    
    



return
