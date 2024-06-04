#ici on déplace les persos


define sounds = ['audio/sounds/bip2.mp3','audio/sounds/bip3.mp3','audio/sounds/bip4.mp3']
define typewrite_sounds= ['audio/sounds/A1.ogg', 'audio/sounds/A2.ogg', 'audio/sounds/A3.ogg', 'audio/sounds/A4.ogg', 'audio/sounds/A5.ogg','audio/sounds/B1.ogg', 'audio/sounds/B2.ogg', 'audio/sounds/B3.ogg', 'audio/sounds/B4.ogg', 'audio/sounds/B5.ogg']
init python:
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

############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################

#example of a character with the typing sound
define Type = Character("Character with typing", callback=type_sound)
#just don't add the character callback if you don't want that ound
define NoType = Character("Character without typing")
#regular narration that doesn't have a character attached to it, add an # to it if you don't want that

# Narrator
define narrator = Character(callback=type_sound)

# Where and Where context
define MAE = Character(callback=type_sound_typewrite) #MAE pour machine a ecrire

# Walter Romanng, Main Character
define WR = Character(('Romanng'), color="#ffffffff", callback=type_sound)

# Eudoe Kam, Walter's BFF, Inspector
define K = Character(('Kam'), color="#ffffffff", callback=type_sound)

# Kale Bennett
define KA = Character(('Kale Bennett'), color="#ffffffff", callback=type_sound)

# Orchid Kassilth
define OS = Character(('Orchid'), color="#ffffffff", callback=type_sound)

# Juge
define JUGE = Character(('Juge'), color="#ffffffff", callback=type_sound)

# Silver Skyboarder
define SS = Character(('Skyboarder'), color="#ffffffff", callback=type_sound)
# Huissier
define huissier =Character(('Huissier'),color="#ffffffff",callback=type_sound)

############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################

# Define sprites

#Kam
image Kam angry="Kam/kam angry.png"

