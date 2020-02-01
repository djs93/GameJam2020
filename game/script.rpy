﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define nat = Character("Natasha", who_color="#985298")
define vas = Character("Vasili", who_color="#580000")
define p = Character("You")
define narrator = Character(None, what_italic = True)

default nv_stab = 0
default nat_trust = 0
default vas_trust = 0
default day = 0

default nv_cure = 0 # Trigger special ending on 5
default nv_breakup = 0 # Trigger special ending on 3
# The game starts here.

label start:

    if day == 0:
        jump nv_intro
    else:
        jump nv_continue

label nv_intro:
    scene bg computer

    "You look at your computer, the time reads 5:15 PM"
    "You glance up, open is an email detailing an appointment that should have started 15 minutes ago"

    play sound "audio/effects/two knocks.mp3"

    pause 1.6

    p "Come in"

    "A person enters the room, you can't quite distinguish if it's a man or a woman"

    menu:
        p "Ahh, welcome! I've been expecting you..."
        "M'am":
            nat "{i}Blushes and smiles{/i} Thank you. My husband says that I look too manly to be seen as a real woman."
            $ nv_stab += 1
            $ nat_trust += 1
            vas "Please help me through the door dear dearest."
            vas "{i}Turns to you{/i}."
            vas "Forgive her ignorance, she seems to sometimes forget i'm a cripple. {i}laughs{/i}"

            nat "{i}Helps Vasili through the door{/i} Sorry, I was not thinking"
        "Sir":
            nat "I..I’m a woman {i}she takes off her hat to reveal a short ponytail{/i}"
            nat "I understand, I had a feeling you wouldn't notice, no one does."
            $ nv_stab -= 1
            $ nat_trust -= 1
            vas "{i}HAHAHAHA{/i}, this man meant no harm, if only you {i}LOOKED{/i} feminine, this wouldn't happen dear."
            vas "Now please help your {i}crippled{/i} husband through this door."

            p "Oh, I'm so sorry. Natasha I presume"

            nat "{i}Nods and helps Vasili thorugh the door{/i} Yes, Vasili, darling I am sorry, I was not thinking"
        
    vas "My friend said that this place was the last word in therapy for couples, however it appears it is the last word in taste as well, we may be peasantry, but at least your windows are solid, and our walls have no mold."

    menu:
        p "..."
        "Insult Vasili":
            p "You’ll have to forgive the appearance of my office, it's the best I can do for someone who is paying such a low fee.  Its either new carpets, or food for my children.  Not that I imagine you have any {i}shortage{/i} of food. {i}points out stomach{/i}"
            vas "{i}Opens and closes his mouth a few times unable to respond{/i} I- I meant nothing by it."
            $ nv_stab -= 1
            $ vas_trust -= 1
        "Agree with Vasili":
            p "Many apologies sir, it has been a rough year.  And this is all my family can afford with our financial situation."
            vas "Ah chum, no worries, we don’t choose our situations, they choose us!"
            $ vas_trust += 1
        
    p "Now if you may, please sit down and we can continue"
    "Natasha and Vasili sit down"

    menu:
        p "{i}I need to ask one of these clients questions to figure out what is going on…{/i}"
        "Natasha":
            jump nat_1_questions
        "Vasili":
            jump vas_1_questions

    # This ends the game.

    return

label day_over:
    p "I think that's enough for today, see you two for the next appointment"
    $ day += 1
    jump start

label nv_continue:
    "The couple re-enter your office"

label nat_1_questions:
    menu:
        "Childhood":
            jump nat_1a
        "Family":
            jump nat_1b
        

label nat_1a:
    p "Natascha, is it ok if I ask about your childhood?  The more I know of your upbringing, the better I can understand the… {i}dysfunctions{/i} of your relationship.  If you don’t feel comfortable I understand."
    if nvtrust < 4:
        nat "I… Don’t want to talk about that.  I am sorry."
        jump day_over
    else:
        nat " If it will help yes. Me and Vasili were together since childhood, not romantically at first. But he was my only friend growing up, "
        #(blush) 
        extend "he used to be so sweet.  "
        #(flustered) 
        nat "N-n-not that he isn’t now! I- I am just such a klutz and he has to deal with me so much he gets tired. It’s hard for him to show his love like he used to."
        #(sad)
        nat "I- I’m just so much to deal with."
        p "Hmm... I see"
        menu "1_a_choices":
            "What should I do now?"
            "Ask about other relationships":
                jump nat_1a_a
            "Compliment strength":
                jump nat_1a_b
            "Call the relationship stale":
                jump nat_1a_c
            
label nat_1a_a:
    p "Natasha, you never mentioned anyone but Vasili, have you had any other relationships?"
    nat "Uh… I don’t remember any other relationships.  There was one… {w}but Vasili saved me from the heartache"
    menu:
        "What should I do now?"
        "Commend Natasha for being faithful to Vasili":
            jump nat_1a_a_a
        "Question Natasha about the previous relationship":
            jump nat_1a_a_b
        
label nat_1a_a_a:
    p "Natasha, I commend you for being so faithful to Vasili."
    $ vas_trust += 1
    $ nv_stab += 5
    nat "That is how love is supposed to be, right?"
    #(blush)

    jump day_over

label nat_1a_a_b:
    p "Natasha tell me more about this boy before Vasili."
    #if nat_trust <5:
    #   nat "It’s in the past, no need to bring that up again."
    #    jump day_over
    #else:
    nat "There was a baker, his name was Dimitri."
    #(blush)
    nat "I thought he was sweet on me, he gave me extra rolls and sometimes he would slip some flowers into my orders."
    #(sad)
    nat "It was a stupid thought though.  Vasili explained to me that it was a marketing ploy."
    nat "I just can’t believe I was so stupid to think someone would like me like that."
    vas "Can't trust bakers! Hahahahehe"

    menu:
        ""
        "Tell her that Vasili was probably wrong":
            p "Natasha, Vasili was wrong, that boy probably had feelings for you."
            vas "That’s preposterous! Look at her! How can anyone love… THIS.  She’s lucky to have me!"
            $ vas_trust -= 3

            if nat_trust <5:
                nat "H-H-He's right..."
                $ nv_stab += 10
            else:
                nat "Vasili… why would you lie about that…"
                $ nv_stab -= 20
                $ nv_breakup += 1
                if nv_breakup == 3:
                    jump nv_breakup_scene

            jump day_over
        "Say nothing":
            jump day_over
        
label nat_1a_b:
    p "Natasha I must commend you for coming to me to try and fix any issues the two of you might have had instead of just leaving for another man."
    p "Many couples are not strong enough to try to fix their issues."
    nat "Of course, I love my husband."
    $ nv_stab += 1 
    $ nat_trust += 1
    vas "We are the strongest, after all."
    $ vas_trust += 1

    jump day_over

label nat_1a_c:
    p "Maybe, things happened too quickly for each of you."  
    p "There could be a possibility that this relationship is not one of love, but actually just because each of you have no one else."
    nat "C-C-can that happen?"
    $ nv_stab -= 1
    $ nat_trust -= 1
    $ nv_breakup += 1
    if nv_breakup == 3:
        jump nv_breakup_scene
    v Of course not dear, this therapist is seeming more like a quack by the second. 
    $ vas_trust -= 1

    jump day_over

label nat_1b:
    p "Can I ask about your family?  It’s nice to get a feel for someone’s guidance when trying to diagnose issues."
    if nvtrust < 3:
        nat "I apologize, but I doubt that will help me fix my marriage…"

label vas_1_questions:
    "not implemented"