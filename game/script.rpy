# I'VE. BECOME SO NUMB. 

define nat = Character("Natascha", who_color="#985298")
define vas = Character("Vasili", who_color="#580000")
define p = Character("You")
define narrator = Character(None, what_italic = True)

default nv_stab = 30 # At 0, breakup. 60 cure.
default nat_trust = 3
default vas_trust = 3
default day = 0
default child_die_streak = 0
default cash = 0

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

            p "Oh, I'm so sorry. Natascha I presume"

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
    "Natascha and Vasili sit down"

    menu:
        p "{i}I need to ask one of these clients questions to figure out what is going on…{/i}"
        "Natascha":
            jump nat_1_questions
        "Vasili":
            jump vas_2_questions

    # This ends the game.

    return

label day_over:
    p "I think that's enough for today, see you two for the next appointment"
    $ day += 1
    $ cash += 50
    jump start

label nv_continue:
    show bg folder with dissolve(0.5)
    if nv_stab >=60:
        jump nv_stab_cure
    elif nv_stab <=0:
        jump nv_stab_breakup
    elif nv_cure == 5:
        jump nv_cure_scene
    elif nv_breakup == 3:
        jump nv_breakup_scene
    elif day == 30:
        jump nv_day_max_scene
    menu:
        "What is happening today?"
        "Natascha and Vasili appointment":
            jump nv_re_enter
        "Pass the day and do nothing":
            jump do_nothing_day

label do_nothing_day:
    "You do nothing today. "
    if nat_trust < 1:
        jump nv_trust_fail
    if vas_trust < 3:
        extend "Vasili has forgotten your payment. "
        $ child_die_streak += 1
        if child_die_streak == 1 or child_die_streak == 2:
            extend "It's the [child_die_streak] day in a row he's forgotten, I need to get friendlier with him."
        elif child_die_streak >=3:
            jump children_ded
    "You do nothing today, +$50. Natascha and Vasili don't seem to be doing any better, however"
    $ cash += 50
    $ nv_stab -= 5 # discuss increase/modification (scale over time not talked?)

label nv_re_enter:  
    "The couple re-enter your office"
    p "Welcome back!"
    menu:
        "Who do you want to talk to today?"
        "Natascha":
            jump nat_1_questions
        "Vasili":
            jump vas_2_questions
        

label nat_1_questions:
    menu:
        "Childhood":
            jump nat_1a
        "Family":
            jump nat_1b
        

label nat_1a:
    p "Natascha, is it ok if I ask about your childhood?  The more I know of your upbringing, the better I can understand the… {i}dysfunctions{/i} of your relationship.  If you don’t feel comfortable I understand."
    if nat_trust < 4:
        nat "I… Don’t want to talk about that.  I am sorry."
        jump day_over
    else:
        nat "If it will help, yes. Me and Vasili were together since childhood, not romantically at first. But he was my only friend growing up, "
        #(blush) 
        extend "he used to be so sweet.  "
        #(flustered) 
        nat "N-n-not that he isn’t now! I-I am just such a klutz and he has to deal with me so much he gets tired. It’s hard for him to show his love like he used to."
        #(sad)
        nat "I-I’m just so much to deal with."
        p "Hmm... I see"
        menu:
            "What should I do now?"
            "Ask about other relationships":
                jump nat_1a_a
            "Compliment strength":
                jump nat_1a_b
            "Call the relationship stale":
                jump nat_1a_c
            
label nat_1a_a:
    p "Natascha, you never mentioned anyone but Vasili, have you had any other relationships?"
    nat "Uh… I don’t remember any other relationships.  There was one… {w}but Vasili saved me from the heartache"
    menu:
        "What should I do now?"
        "Commend Natascha for being faithful to Vasili":
            jump nat_1a_a_a
        "Question Natascha about the previous relationship":
            jump nat_1a_a_b
        
label nat_1a_a_a:
    p "Natascha, I commend you for being so faithful to Vasili."
    $ vas_trust += 1
    $ nv_stab += 5
    nat "That is how love is supposed to be, right?"
    #(blush)

    jump day_over

label nat_1a_a_b:
    p "Natascha tell me more about this boy before Vasili."
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
        "Tell her that Vasili was probably wrong":
            p "Natascha, Vasili was wrong, that boy probably had feelings for you."
            vas "That’s preposterous! Look at her! How can anyone love… THIS.  She’s lucky to have me!"
            $ vas_trust -= 3

            if nat_trust <5:
                nat "H-H-He's right..."
                $ nv_stab += 10
            else:
                nat "Vasili… why would you lie about that…"
                $ nv_stab -= 20
                $ nv_breakup += 1
                

            jump day_over
        "Say nothing":
            jump day_over
        
label nat_1a_b:
    p "Natascha I must commend you for coming to me to try and fix any issues the two of you might have had instead of just leaving for another man."
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
    v "Of course not dear, this therapist is seeming more like a quack by the second." 
    $ vas_trust -= 1

    jump day_over

label nat_1b:
    p "Can I ask about your family?  It’s nice to get a feel for someone’s guidance when trying to diagnose issues."
    if nat_trust < 3:
        nat "I apologize, but I doubt that will help me fix my marriage…"
        jump day_over
    else:
        nat "I don’t mind talking about this… I had three brothers and a father."
        p "No mother?"
        nat "She... left when I was young"
        menu:
            "What should I do now?"
            "Ask about her father ":
                jump nat_1b_a
            "Ask about her brothers":
                jump nat_1b_b
            "Insult her about it":
                jump nat_1b_c

label nat_1b_a:
    p "What was your father like? Was he a nice man?"
    if nat_trust < 4:
        nat "{i}Glances at Vasili{/i} I-I don't want to talk about him. He didn't like Vasili much."
        jump day_over
    else:
        nat "The kindest! He called me his little leopard! He used to give the best hugs!"
        vas "If he was friendly, he wouldn't have said those things about me… Dont forget that."
        nat "Oh darling, he was just worried about me!  He didn’t mean anything he said!"
        vas "BAH! I have nothing more to say about it!"
        p "I see."

        p "What happened between your father and Vasili?"
        vas "ABSOLUTELY NOTHING! And yet, when I started getting romantically involved with his daughter, he bad mouthed me and called me manipulative!"

        menu:
            "What should I say?"
            "Side with her father":
                jump nat_1b_a_a_a
            "Side with Vasili":
                jump nat_1b_a_a_b

label nat_1b_a_a_a:
    p "Sometimes an outside perspective can show our deepest issues…"
    vas "That's ridiculous! You are a SHIT therapist!"
    nat "My father was always good at reading people…" 
    $ nv_breakup += 1
    $ vas_trust -= 2
    vas "Your father was stupid!"

    jump day_over

label nat_1b_a_a_b:
    p "Preposterous! You have been nothing but good to Natascha!"
    vas "FINALLY, someone else sees sense.  I’m glad we came to you, anyone else would have no sense!"
    nat "I guess he was a bit… over dramatic." 
    $ nv_stab += 5
    $ vas_trust += 2

    jump day_over

label nat_1b_b:
    p "You mentioned three brothers, what was that like? I can't imagine it was comfortable living with that many men."
    nat "On the contrary, it made me as strong as I am today.  We fought constantly and I slowly started winning. Family truly does make one stronger, emotionally and, in my case, physically!"
    p "Three older brothers I’m guessing?"
    nat "Two actually, I have one younger brother. Such a frail boy. His name is Avali."  
    nat "He was actually the one who asked me to come here. He was so worried. It was cute. But I came anyway!"
    vas "Little twerp is wasting my money."

    menu:
            "What should I say?"
            "Defend Natascha's brother":
                jump nat_1b_b_a
            "Stay silent":
                jump day_over

label nat_1b_b_a:
    p "Don’t speak like that about her brother, it’s obvious she loves him very much, and your being rude."
    nat "No, no, Avali is a handful sometimes, and sometimes, he gets on Vasili’s nerves."  
    nat "But Vasili{w 0.2}.{w 0.2}.{w 0.2}.{w 0.5} deals with it."
    p "How does he deal with it?"
    vas "I beat sense into him. The way my father did it." 
    nat "Y-Y-you beat him?!?! How could you?!"
    vas "He needs it, he never learns Natty!"
    nat "I-I-Im gonna be sick."
    $ nv_stab -= 15
    $ nat_trust += 2 
    $ nv_breakup += 1

    jump day_over

label nat_1b_c:
    # you are an awful person. love, Dale
    p "What happened to your mother? Did she hate you enough just to leave?" 
    p "You must be the problem, one daughter and you couldn’t even act feminine."
    p "What do your brothers or father think of you now? Or did they cut all contact with you?"
    p "A woman,{w 0.6} working at the docks. {w 0.6}In this day and age. {w 0.6}Disgraceful."
    vas "HAHAHA finally someone who can think like me! See Natty?" 
    $ nv_stab += 3
    $ vas_trust += 1
    nat "I-I-I can’t help it. I-I-Its not true... {i}avoids eye contact{/i}" 
    $ nat_trust -= 2
    jump day_over

label vas_2_questions:
    menu:
        "Upbringing":
            jump vas_2a
        "Childhood with Natascha":
            jump vas_2b

label vas_2a:
    p "Vasili may I ask what your upbringing was like? I ask this to all of my clients since it might give me an insight to any uhh... {i}problems{/i} occurring in the relationship." 
    p "If you don’t feel comfortable talking about your childhood that’s alright too."
    vas "I had a very normal upbringing in most senses, the most outstanding thing I can think of is that I was adopted."
    vas "But I was adopted by a father that truly cared for me.  He fed me{w}, clothed me{w}, sent me to school{w}, beat me when I misbehaved{w}, and taught me right or wrong.  Altogether a stellar father."
    
    menu:
        "Where should I go with this next?"
        "Ask about abuse":
            jump vas_2a_a
        "Ask about biological parents":
            jump vas_2a_b
        "Compliment father":
            jump vas_2a_c
        
    
label vas_2a_a:
    p "Has your father ever done something he shouldn't have done as a parent? Perhaps, hurt you in some way?"
    if vas_trust < 5:
        vas "You tryin' to say my father did something wrong? {p}{i}scoff{/i}"
        vas "That man did everything right"
        jump day_over
    else:
        vas "He hurt me yes, but in some ways, it was a requirement for my growth as a young boy."
        vas "I was always getting into trouble and I needed discipline. I guess he was... showing his love."
        menu:
            "Tell Vassili he was abused as a child":
                jump vas_2a_a_a
            "Compliment the father’s discipline technique":
                jump vas_2a_a_b
            
label vas_2a_a_a:
    p "Vasilli, the punishments your father used to teach you… What were they?"
    vas  "Friend, do not get me wrong, my father never did anything to me that I didn’t deserve." 
    vas "Looking back I can see he loved me greatly. The worst he’s ever done is beat me for the things I did."
    p "What did you do to deserve the beatings?"
    vas "There was this one time, keep in mind I was young, where I wanted a toy rocket." 
    vas "I asked both my mother and my father but they said children have no need for things."
    p "Children have no need for toys?"
    vas "Ahh, I see where your coming from, but the toys are a luxury for the aristocrats."
    p "I see." 
    p "*internally* {i}I don’t think my children would be too happy if they had no toys at home. God knows, I don't have enough time for them…{/i}"
    p "Continue."
    vas "Ah yes, anyway, I wanted the toy rocket so badly, I considered stealing it."
    p "I see so they beat you for stealing?"
    vas "No No No, I am no thief! But they did read my plans in my journal."
    vas "That was enough to make papa angry. He burned my hand with a spoon. I never thought about stealing again."
    p "I thought you said he beat you."
    vas "Beat, burn, what is the difference, all discipline right?"
    p "*internally* {i}This is a turning point for Vasilli. I can either choose to help his relationship, or make him feel like he needs me more than ever. What should I do?{/i}"

    $ nv_stab += 10
    $ nv_cure += 1
    jump day_over

label vas_2a_a_b:
    p "So rare to see a father who cares for their children so much, that they would raise a hand to them." 
    p "Your father has good senses. Otherwise you would not have grown to such a fine young man."
    vas "I am glad you see it that way, Natascha thought that it was abuse. I told her, \"no Natty, there are children who are ACTUALLY abused who am I to lower their worth?\""
    p "I don’t expect much from someone who had no mother.  How would she know parenting when she was missing two from the start?"
    #Again, you are an awful person. Love, Dale

    $ nv_stab += 5
    $ vas_trust += 3
    jump day_over

label vas_2a_b:
    p "So adoption... that couldn’t have been good for you."  
    p "Do you know who your biological parents are?"
    vas "I remember a man and a woman were stressed about something and then I didn’t see them anymore."  
    vas "The time and place where I remember from makes me believe they were my biologicals."
    vas "I don’t remember much after that. Just that I wasn’t wanted."
    p "How old were you when you were adopted?"
    vas "I was a very young boy, chum, I can’t exactly remember... maybe seven?"
    menu:
        "Reason about why they gave you up":
            jump vas_2a_b_a
        "Say nothing":
            p "..."
            jump day_over
        

label vas_2a_b_a:
    p "If you were seven, that would place them giving you away during the recession, maybe they couldn’t afford you."  
    p "It doesn’t mean you weren’t wanted."
    vas "So what, I was still tossed aside…"
    p "Do you think maybe that you attack Natascha emotionally because the only way you were shown love is the threat of abandonment and anger?"
    vas "W-W-What?  That’s preposterous… isn’t it?" 
    $ nv_cure += 1
    jump day_over

label vas_2a_c:
    p "It sounds like your father wanted the best for you to grow up to be a tough individual."
    vas "Yes he only wanted the best for me. He was a good man. Although Natty seems to disagree."
    nat "H-he was abu…"
    vas "For the last time, you dolt, he was old fashioned not abusive."
    $ vas_trust += 1
    jump day_over

label vas_2b:
    p "So how did the two of you meet?"
    vas "Well, chum, to be honest, my mother forced me to make friends with my dear Natty"
    menu:
        "Ask about if he wanted to be friends with her":
            jump vas_2b_a
        "Ask if they ever got along with each other":
            jump vas_2b_b
        "Tell him he is a saint":
            jump vas_2b_c

label vas_2b_a:
    p "You said you were forced to be Natascha’s friend did a part of you ever actually want to?"
    nat "He says this constantly. I don’t believe it myself.  He's just trying to be tough."
    vas "I was forced to be friends with you. {w}My mother pitied you. {w}She knew you had no mother, and she asked me to hang out with you."
    vas "Everytime I brought you home, she tried mothering you. It was preposterous."
    nat "Even if that were true! Why would you propose then, surely she wouldn't tell you to do that!"
    vas "I had wasted so much time on you I thought I should get something from it."  
    vas "Turns out I was stupid to do even that. {w}I could’ve married Hilla."
    nat "The girl with the buck teeth?!"
    vas "Buck teeth, but easily identifiable as a woman."

    menu:
        "You love Natascha correct?":
            jump vas_2b_a_a
        "...":
            jump vas_2b_a_b
        
label vas_2b_a_a:
    p "You love Natascha correct?"
    vas "Of course I love my wife!"
    p "Then why not compliment her?"
    vas "B-because"
    p "Because what Vasili?"
    vas "If I do that… she’ll realize I am not good enough for her and leave me."
    nat "Vasi, why would you think that? I love you!"
    vas "I-I-I am not sure…" 
    $ nv_cure += 1
    
    jump day_over

label vas_2b_a_b:
    p "..."
    vas "I should have married Hilla."
    nat "I-I-I am sorry I am not her!  I’m sorry I can’t compete with her!"
    "Natascha storms out of the room"
    vas "Natty! Get back here!"
    "Vasili struggles to get up and hobbles after her"

    $ nv_breakup += 1
    $ nv_stab -+ 20
    jump day_over


label vas_2b_b:
    p "In all your years together, did you ever like being together?"
    vas "Of course! I love Natascha!"
    nat "Y-y-you do?"
    vas "Natty, how could you say such a thing! Of course I do."
    p "See, that's good, show her the affection you have!"
    vas "To answer your question, we’ve always been good. "
    vas "Recently, however, Natty has had her brother fill her head with LIES."

    menu:
        "Argue for more than one view":
            jump vas_2b_b_a
        "Say nothing":
            p "I see..."
            jump day_over
        
label vas_2b_b_a:
    p "Sometimes an outside perspective is key in understanding our own shortcomings."
    vas "Are you agreeing with her gremlin brother?!"
    p "Vasili, I have only met you just today, you seem charming but someone who's known you for a while is saying you need help. And according to rumors, everyone agrees."
    vas "I-I-I am sorry, I thought… people were ok with how I was."
    nat "I am Vasili, I love you."
    vas "I want to change Natty. I really do."
    $ nv_cure += 1
    $ nv_stab += 20

    jump day_over

label vas_2b_c:
    p "Vasili you’re such a kind person for dealing with her, truly a saint."
    vas "Thank you, chum, my dear Natty is lucky to have me."
    nat "Y-Yes of course I am."
    $ vas_trust += 1
    $ nv_stab += 20
    $ nat_trust -= 1
    jump day_over

label nv_breakup_scene:
    p "Natascha divorced Vasili, she realized that things were not gonna change.  Vasili… {w}did not take it well."
    p  "He {w 0.6}.{w 0.6}.{w 0.6}. hung himself in the family attic last week."
    p  "My cash flow has stopped. {w}My children are hungry. {w}I fear we will not make it."

    return

label nv_cure_scene:
    p "Vasili has been striving to improve, his love for Natascha is showing more and more, and he has been trying to make amends."
    p "I fixed this relationship correctly, but I fear for my children. {w}They have not eaten in days. {w}I have not eaten in days."
    p "I need a new client soon."

    return

label nv_day_max_scene:
    p "It has been a month. {w}I keep milking this couple for every cent they make."
    p "My family will be safe for years, and I think they will be none the wiser." 
    p "I feel bad for Natascha but there's nothing I can do… my family needs food."

    return

label nv_stab_breakup:
    p "The funny thing about a couple breaking up is that the couple does not need a {i}couple’s therapist anymore.{/i}"
    p "I have no client. {w}And soon I will starve. {w}At least I am happy that awful relationship is over."

    return

label nv_stab_cure:
    p "If brainwashing was a thing, I believe I have brainwashed Natascha into thinking of Vasili as a king and herself his concubine."
    p "She listens without hesitation. {w}{p}She continues to be the only one to work, and Vasili continues to keep his grip over her." 
    p "Instead of being grateful for my work, however, I have not found another client and he refuses to help me."
    p "Soon my family will perish."

    return

label nv_trust_fail:
    p "The couple stopped showing up after that. {w}I must have lost the trust of Natascha, it was her who convinced Vasili to come to me, afterall."
    p "I need to find a new client soon, my family is hungry and I fear we won't have much longer."

    return

label children_ded:
    p "My family has not eaten in days. {w}My children have moved on from this wretched world."
    p "I shall be joining them soon."

    return