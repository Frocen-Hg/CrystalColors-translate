



label start:




    scene white with Dissolve(4)
    pause 1








    window hide
    nvl clear  
    sn "当我还是个孩子的时候，我在圣诞节愉快地凝视窗外，那时的我从未想过，像雪这样神奇而美妙的东西会造成如此大的破坏。" with Dissolve(1)
    sn "我几乎看不清自己要去哪里，每次迈出一步，我的脚都沉了下去，一种致命的白色紧紧地粘在我身上。"
    sn "如果我回头看，我会看到我的脚步声在每一步之后立即填满，仿佛我一开始就不在那里。"
    sn "我绞尽脑汁想找个目的地，于是决定看看她是否在家。"
    nvl clear  
    sn "我仍然知道去她家的路。半盲，甚至知道我们小时候知道的许多地标都消失了，我把沉重的脚推向了她住的地方。"
    sn "两个街区转瞬即逝。"
    sn "也许我在漫长的冬眠后只是行动迟缓，身体虚弱，也许真的是这种异常的天气阻碍了我的前进。"
    sn "我想知道我们最喜欢的树去了哪里，旧邮箱去了哪里。从什么时候起，我们熟悉的社区发生了如此大的变化？"
    nvl clear   
    nvl hide Dissolve(0.3)
    show sanna standing jacket concerned open at t32
    Sanna "也许这根本不是正确的方式。.." with Dissolve(0.3)


    sn "但当我开始怀疑自己时，我终于瞥见了她的房子。" with Dissolve(0.3)
    nvl clear   
    nvl hide Dissolve(0.3)
    stop music fadeout(6)
    scene white with flashflash
    pause 1
    scene fhouse

    call init_snow from _call_init_snow_2
    call show_snow from _call_show_snow_3
    with flashflash

    pause 2

    sn "For the first time in forever, I was the one knocking on a door." with Dissolve(0.3)
    sn "The sound of my hand on the door echoed hollowly."
    sn "A long silence. I knocked again."
    sn "No one answered."
    nvl clear 
    sn "Her family's doorbell had long been broken, and no one had ever thought to fix it. All I could do was knock a few more times, feeling the cold get to me as I stood in place."
    sn "She probably didn't hear me. If she was home at all, there was a chance that she didn't hear my weak knocks amidst the roaring blizzard."
    sn "No one answered, so I knocked again, this time more frantically."
    nvl clear   
    nvl hide Dissolve(0.3)

    show sanna standing jacket concerned open at t32
    Sanna "Come on. Damn it." with Dissolve(0.3)
    Sanna "..."

    sn "There was no other choice. I began to turn around to leave." with Dissolve(0.3)
    sn "Suddenly a flash of light stopped me in my tracks. Metal. A key."
    sn "The spare key. I can't believe I forgot."
    sn "I squatted near the ground to dig through the snow, digging, digging even as the snow buried my efforts, till I uncovered the little compartment by her front door where that spare key laid."
    sn "I gingerly opened it. To my relief, there the key was."
    nvl clear 
    sn "I squinted as I picked it up. The key, which had still been in the same old place, even retained the silly drawing we scribbled onto it with permanent marker as children."
    sn "I couldn't tell if the picture was a cat or a bird."
    sn "Click."
    sn "The door unlocked with the spare key. I tucked it back where it belonged, where it would perhaps serve Freya again in the future. Then, I entered the house."
    nvl clear   
    nvl hide Dissolve(0.3)



    Sanna "Hello?" with Dissolve(0.3)
    Sanna determined "Is anybody home?"

    sn "My voice reverberated throughout the house. There was no answer." with Dissolve(0.3)
    sn "I knew it couldn't have been that easy."
    sn "After I spent a little bit warming myself up again, away from the pure white precipitation, I stepped back outside to resume my journey."
    nvl clear
    sn "Where next? That question, I had asked myself in the comforts of her home."
    sn "I needed to find her, but I had no clue where to go next."
    sn "I didn't plan this far ahead, and now that I was here... I had no idea what to do."
    nvl clear   
    nvl hide Dissolve(0.3)

    Sanna squint frown "Did I really know her as well as I had thought?" with Dissolve(0.3)

    sn "She mentioned the empty zone to the north many times. Maybe she was there." with Dissolve(0.3)
    sn "Following the street that should head north, I trudged forward. The wind forced my pace to a snail's pace, and not a few times, I nearly fell over, feet entrenched in the snow."
    sn "The harsh wind blowing against my face felt like a thousand invisible needles going through it."
    sn "Whereas my fingers felt numb before, now they felt nothing but stinging pain. Nevertheless, I force myself forward."
    sn "I needed to go as far as I could go."
    nvl clear   
    sn "I had to."
    nvl clear  
    nvl hide Dissolve(0.3)

    scene black with fade
    call delete_snow from _call_delete_snow_2
    pause 5


    scene house with fade


    play music calm2

    show freya closed pout at t21
    Freya "Brrr... It's cold outside."
    show sanna standing pjs smile at t22
    Sanna "Welcome back."
    Freya grin open "Hehe, I'm back."
    Freya "I brought something special today."
    Sanna skeptic "Something special?"
    Freya up scheming "Try and guess, Sanna. I shouldn't make you guess, but it's no fun if you don't get a chance to."
    Sanna "I don't know. A puppy?"
    Freya "You wish."
    Sanna trying "Take a seat first. You must be exhausted trudging through the snow. Let me get you some hot water."
    Freya crossed pleased "Thanks."
    Sanna skeptic "Is it food?"
    Freya awkward "Well, I did bring that too, but that's not quite it either."
    Sanna "So, what is it you're so happy about?"
    Freya up geez "But you haven't guessed yet!"
    Sanna squint concerned "Ahh..."
    Sanna pout "Mmm... I don't know, I give up."
    Freya pout "Boo."
    Freya grin "But here, it's this."
    Sanna skeptic "...what is that?"

    sn "She took out something and showed it to me with an expression as if she had found a priceless treasure." with Dissolve(0.3)
    sn "Something precious. A shining and fragile looking gem."
    nvl clear 

    Sanna crystal "A diamond? What is this?" with Dissolve(0.3)
    Freya crossed smug "It's actually much more valuable than that."
    Sanna "What do you mean?"
    Freya up "Here, let me show you."
    show sanna pjs

    window show
    sn "My first impressions were wrong." with Dissolve(0.3)
    sn "I thought she had found a gemstone that was worth a lot of money."
    sn "But money had no meaning anymore."
    sn "Just like that, she found the mortar and pestle from the kitchen and ground up the fleeting crystal she brought me."
    sn "Even though I had gotten that cup of water for her, she poured the powder into the water and stirred, handing me the cup."
    nvl clear   
    nvl hide Dissolve(0.3)

    Freya "Drink." with Dissolve(0.3)
    Sanna sad "Freya, I don't-"
    Freya guilty crossed "Just trust me."
    Sanna "..."
    Sanna concerned "...fine."
    show freya neutral

    show black with Dissolve(0.3)
    "..."
    hide black with Dissolve(0.3)

    Sanna skeptic "It's sweet... but also..."
    Sanna "...strangely familiar?"
    Freya "I went to the north, near the ruins."
    Sanna sad "You went to such a dangerous place?"
    Freya guilty "Sorry."
    Freya up pleased "But because of that, I met some people."
    Freya grin "They showed me how to find it, and how to use it."
    Sanna concerned "I said it's sweet but not that sweet. Something like this is not worth the danger, Freya."
    Freya crossed guilty "It's medicine. It'll make things alright again."
    show freya serious
    Sanna surprised "Medicine...?"
    Sanna frown "Something like that is really possible? I don't really believe it."
    Sanna "It sounds too suspicious."
    Freya up guilty "I didn't believe it either, but they showed me."
    Freya surprised "I just have to-"
    Freya crossed awkward "...It's a little complicated. But it's medicine that works."
    Freya "...anyway, just trust me on this, okay? Please, I have a really good feeling about this."
    Sanna "..."
    Freya "...Please?"
    Sanna "..."
    Sanna trying "...Alright."

    sn "I was still not really convinced but Freya was not someone who would lie to me." with Dissolve(0.3)
    sn "At the very least she had good intentions. That, I was sure of."
    nvl clear   
    nvl hide Dissolve(0.3)

    scene house with fade
    show freya at t42
    Freya "I've noticed something recently, Sanna." with Dissolve(0.3)
    show sanna sitting blanket plush at t43
    Sanna "Hm?"
    Freya pleased "You kind of look like a worm wrapped up in the blanket, a cute little worm."
    Sanna upset "Cute? Worms are not cute."
    Freya grin up "Yes they are?"
    Sanna contradict "If I were a worm, would you still love me?"
    Freya smug "Of course. I'd build a whole terrarium for you and feed you worm food everyday."
    Sanna squint pout "......"
    Freya geez "Pfft."
    Sanna contradict "I appreciate the thought, but I'm happier being a human after all. Which do you prefer: worm me or human me?"
    Freya smug crossed "Let me see..."
    Sanna surprised "This shouldn't even be a question."
    Freya awkward up "Can't I have both?"
    Sanna squint pout "No, you have to choose one."
    Freya crossed smug "Then, I'll stick with human you, the small and cuddly human Sanna who loves me the most."
    Freya grin "Now, if the other option was a wyrm, I don't know..."
    Sanna squint pout "Hmph."
    Freya "I'd still be choosing you in the end."
    Freya up grin "Which would you choose, Sanna? If I were just plain old me, a worm, or a wyrm?"
    Sanna smile "That's not even a question, Freya. I'd choose the normal, human Freya who I love the most."
    Freya crossed pleased "Aw, I love you the most too."


    sn "I placed my head on her shoulder. And as I started to feel sleepy, she placed her hand over mine." with Dissolve(0.3)
    sn "I felt safe and at ease."
    sn "So warm."
    sn "All I could do was sap away that warmth."
    sn "I wished I could do more than that."
    sn "I wanted to become someone who could support her rather than someone who always had to be supported."
    nvl clear  
    nvl hide Dissolve(0.3)
    stop music fadeout(2)
    nvl hide Dissolve(0.3)


    scene black
    window hide 
    with Dissolve(0.3)
    pause 3


    play music VirulentSnow
    scene field
    call init_snow from _call_init_snow_3
    call show_snow from _call_show_snow_4
    with flashflash

    show sanna standing jacket open surprised at t32
    Sanna "!!"

    sn "Out of the corner of my eyes, I suddenly noticed a flash of red." with Dissolve(0.3)
    sn "Partially buried in the snow but not yet fully enveloped by the white, I found her scarf a few paces away from where I had ultimately stopped."
    sn "I went forward."
    sn "Digging it up, I patted away the dry snow that clung to it."
    sn "This was her scarf, but ...where was the owner?"
    nvl clear  
    sn "With the rate of the snowfall, I estimated that she must have only lost it recently. A spark of hope rose in me that I could reach her soon."
    sn "As much as I wanted to find them, I could not see her footprints in the snow."
    sn "Feeling that the scarf was not wet, only chilly having been in the snow, I placed it around my neck. With the red close to my heart, I felt a little braver already."
    sn "I had to keep going. To give up when I was this close would be such a tragedy."
    nvl clear   
    nvl hide Dissolve(0.3)


    Sanna shout_sad scarf "Freya!" with Dissolve(0.3)
    Sanna "Where are you?"
    show sanna sad
    pause 2

    sn "No one responded." with Dissolve(0.3)
    sn "I wasn't expecting a miracle. I just wanted a happy reality. Nothing had to be perfect. Once we met again, we still had to deal with our grievances, but I had to find her."
    sn "I pulled myself up with my newfound final reserves of strength."
    sn "Relying on instinct alone, I had a gut feeling that she had to be in this direction. Forward, forward, I just had to move forward and reach her."
    sn "Left foot forward. Right foot forward."
    nvl clear   
    sn "The snow cleared even more before my eyes before it slowly came to a stop."
    sn "In the distance, I saw a figure."
    sn "I felt as if I saw her but couldn't get closer. No, she was getting further away; she was going to disappear. I didn't understand why, but that thought tugged at my heart."
    sn "I ran after her."
    nvl clear   
    nvl hide Dissolve(0.3)
    Sanna running scarf "Freya!" with Dissolve(0.3)
    stop music fadeout(2)
    scene black with Dissolve(0.3)
    call delete_snow from _call_delete_snow_3
    pause 3




    sn "She and I, if I were to talk about the two of us, I barely knew where to start." with Dissolve(0.3)
    sn "Even the details of how we first met seemed rather unremarkable."
    sn "Kids growing up in the same district, I didn't find it strange that we crossed paths."
    sn "At some point in time, we simply realized that the other existed. We became acquaintances."
    nvl clear   
    sn "I didn't think that we were particularly compatible people, but before I knew it, we had become inseparable, the best of friends and something more than friends."
    sn "Or so I liked to think."
    nvl clear   
    nvl hide Dissolve(0.3)

    scene fhouse

    play music funk
    show sanna standing jacket open surprised at t22
    Sanna "...A...achoo!" with Dissolve(0.3)
    show freya awkward at t42
    Freya "Bless you."
    Sanna awkward "Thank you, Freya."
    show sanna pout

    sn "There was a time I went outside with Freya. What for, I forgot." with Dissolve(0.3)
    sn "I only remembered thinking that the faded out streets I walked on should have been familiar but looked so foreign. They shouldn't have looked so grey only because of the snow."
    sn "After all, snow wasn't unusual for this country."
    nvl clear   
    nvl hide Dissolve(0.3)


    Sanna "It's snowing outside again." with Dissolve(0.3)
    Sanna mild "Next year, we should really go on a trip to somewhere warm. Like Hawaii or maybe somewhere down south. I hear it's summer there right now."
    Freya "We really should."
    Freya "We've been saying it forever, but it never goes our way. What was it, last year? Even though you didn't get sick, I ended up breaking my arm."
    Sanna sad "And now with the stuff that's been happening outside..."
    Freya up "Yeah... well, who knows, maybe things will get better by next year and we'll finally get to go on our trip."
    Sanna open mild "Where to?"
    Freya grin "Hawaii sounds nice. Ah, but, it might not be in the southern hemisphere. Maybe New Caledonia? We could go to Australia and fight emus too."
    Sanna squint concerned "I will veto the emu fighting right now."
    Freya crossed smug "Better than fighting penguins."
    Sanna "I don't want to be fighting anything."
    Freya geez "Haha. Where do you want to go then?"
    Sanna chill "I don't know. There are too many choices..."
    Sanna "I can't think of anything right now."
    Freya smile "There's always next year to decide."


    sn "Our footsteps crunched on the snow covered ground." with Dissolve(0.3)
    sn "My eyes took in the unfamiliar familiar. Fewer people were outside than usual even when taking into account how most preferred to stay indoors during winter."
    sn "For a moment, I thought I saw a ghost."
    nvl clear   
    nvl hide Dissolve(0.3)

    Sanna determined "..." with Dissolve(0.3)
    Freya guilty "What is it?"
    Sanna "That person..."
    Sanna frown sweat "They look so... washed out."
    Freya serious "Do you know them?"
    Sanna "I..."
    Sanna determined "No."
    Freya "We shouldn't stare. Let's go."
    Sanna "Okay."

    show black with fade
    pause 1
    hide black with Dissolve(0.3)
    show sanna -sweat
    Freya concerned "Any news from your parents?"
    Sanna open "They wanted to be back by the holidays, but..."
    Sanna frown "With the way things are looking, it seems like they're still stuck abroad for another few weeks."
    Freya "...This can't go on forever, they'll be able to come sooner or later."
    Freya awkward "And until they make it back, I'll still be here for you."
    Sanna mild "I know."


    sn "We had the bad habit of putting off our planning till later, which probably contributed to how we never did get to go on the elusive trip we liked to talk about." with Dissolve(0.3)
    sn "Back then, we still had an excess of hope."
    sn "Hope that things would return to normal."
    sn "But my parents never did come back."
    nvl clear   
    nvl hide Dissolve(0.3)

    stop music fadeout(2)
    scene black with Dissolve(0.3)
    pause 3
    play music VirulentSnow

    scene field
    show sanna running scarf frustrated at t32
    call init_snow from _call_init_snow_4
    call show_snow from _call_show_snow_5
    with flashflash

    sn "I kept running." with Dissolve(0.3)
    sn "Running after the figure I saw. It was not moving yet, it seemed like it wasn't getting any closer."
    sn "The snow hindered me, making my feet sink deeper into the white quagmire with each hurried movement. The wind pushed me back. Even my own useless two feet got in the way."
    sn "The snow itself was trying to stop me. I could feel it seeping out of the whiteness, covering my consciousness with an ice-cold haze."
    nvl clear 
    sn "Was I too exhausted to go on? Had my very essence reached its limit in this disappearing plane?"
    sn "I tried to reject the notion because I had to keep going."
    sn "As if the very memory of her were fading away into the white, a harsh wind blew by a thick veil of white snow, blocking my view of her figure."
    sn "No, this wasn't snow. This was just a curse."
    nvl clear 
    sn "What would it try to take away next? My name? My self? Even so, I couldn't let go of the part of me that needed so desperately to take just one more step."
    sn "The wind howled. The snow began to fall once more. White filled my vision."
    nvl clear   
    nvl hide Dissolve(0.3)

    Sanna mouth_open "How dare you try to take her away from me-" with Dissolve(0.3)
    Sanna grit "!!!"
    scene white with flashflash
    sn "My call was choked back in my throat as a powerful blast of arctic wind slammed into me." with Dissolve(0.3)
    sn "The sheer force knocked my small frame out of balance, and I tumbled back into the snow."
    sn "I tried to regain my composure, and power through the gusts of blade-like winds."
    sn "Slowly, step by step, I approached the figure."
    sn "It was..."
    nvl clear   
    nvl hide Dissolve(0.3)

    scene field
    show sanna standing jacket angry scarf squint at t32
    call init_snow from _call_init_snow_5
    call show_snow from _call_show_snow_6
    with flash

    Sanna "A... a tree." with Dissolve(0.3)
    Sanna sad "..."

    sn "I felt my heart sink." with Dissolve(0.3)
    sn "I couldn't bear this any longer. I wanted to go home."
    sn "Or just give up."
    nvl clear   
    nvl hide Dissolve(0.3)

    Sanna closed frown "..." with Dissolve(0.3)
    Sanna "No..."
    Sanna sad "No, that's not it."
    Sanna open frown "She wouldn't give up this easily."
    Sanna mild squint "She would probably laugh at herself for something like this and move on."
    Sanna determined "I..."
    Sanna "I need to be like her."
    Sanna "Give me your strength, Freya."

    sn "I slowly trudged on, through the blizzard." with Dissolve(0.3)
    nvl clear   
    nvl hide Dissolve(0.3)

    stop music fadeout(2)

    scene black with fade
    call delete_snow from _call_delete_snow_4
    pause 2





    scene house with fade
    play music wondering

    show sanna standing pjs blanket frown at t22
    Sanna "I don't think we can go on our trip anymore."
    show freya closed pout at t21
    Freya "Oh."
    Freya open "We haven't talked about that in a long time."
    Freya "Going overseas would be out for the foreseeable future, but... we could always try going on a road trip instead."
    Sanna squint hmph "No emus."
    Freya grin up "Wow. you still remember that?"
    Freya smile crossed "I don't think there are emus in Italy, and I hear it's pretty warm down there in the winter. It's a bit far away, but we could definitely do it by land."
    Sanna smile open "Yea, that would be nice."
    Freya pleased "Or Spain too. I don't know anything about Mediterranean islands, but boats still exist, so maybe that's an option too."
    Sanna frown "But I don't think we can do it anymore."
    Sanna squint concerned "I... can't do it anymore."
    Freya concerned "Sanna..."
    Sanna "I don't think..."
    Freya guilty up "No! You'll get better! You will! I know it!"
    Sanna sad "..."
    Freya "Sanna, you'll get better. It's just the fever."
    Sanna "No... that's not it."
    Sanna open frown "I..."
    Freya surprised "We'll find something, I'll go out and find some medicine. You'll be fine in no time, Sanna! And we'll get to go on that trip, I promise you. We'll--"
    Sanna shout "Freya!"
    show sanna angry
    Freya closed concerned "!!"
    Freya crossed open "..."
    Sanna sad "I can't remember."
    Sanna squint "No matter how hard I try, I can't remember their faces, Freya."
    Freya crossed "Who?"
    Sanna "My parents."
    Sanna "I can't remember what they look like. What they sound like."
    Sanna "...I don't even remember their names."

    sn "Photo albums and diaries had been long wiped clean. My chest felt hollowed out, and I looked at my hands that felt like they'd been drained of color." with Dissolve(0.3)
    sn "Yesterday, today, tomorrow, I couldn't keep track of anything. I didn't know if there would be a tomorrow and what would come after. I questioned when I would cease to be me."
    nvl clear   
    nvl hide Dissolve(0.3)    


    Sanna "I'm fading, Freya. I feel so faint." with Dissolve(0.3)
    Sanna teary "What if I can't remember you anymore?"
    Freya sweat guilty up "I-"
    Freya -sweat awkward crossed "I'm right here."
    Freya "You can feel my heartbeat."
    Freya "I won't leave your side as long as you're willing to let me be with you. I won't let you forget me either. I'll always remind you that I'm here."
    Sanna "...hic..."
    Freya up guilty sweat "So just hang on a little longer until I find... something."
    Sanna closed sad "No, don't go."
    Freya "But, if I don't try..."
    Sanna open "Freya, I just want to spend the end with you."
    Freya concerned "I don't want to spend the end with you. I want to spend the future with you, Sanna."
    Sanna closed -teary frown "......"
    Sanna awkward "Then... just for today, let's pretend that everything is still normal."
    show sanna squint trying
    Freya "......"
    Freya crossed awkward "Alright."



    sn "I had always been bad at make-believe, and Freya was good at it." with Dissolve(0.3)
    sn "But..."
    sn "...what did normal even mean anymore?"
    nvl clear   

    stop music fadeout(2)
    scene black with fade
    pause 2 

    play music ArtificialAntartica

    scene field
    call init_snow from _call_init_snow_6
    call show_snow from _call_show_snow_7
    with flashflash





    sn "Step."
    sn "Step.."
    sn "Step..."
    sn "Step."
    sn "..Step."
    sn "...Step."
    nvl clear 
    sn "The sky, still covered in snow-letting clouds, was dark. I couldn't tell the time of day, but surely night had yet to fall."
    sn "Moving my foot forward once more, I felt my center of mass shift."
    sn "Into the snow I stumbled. For a moment, I felt as if I was drowning in the whiteness that surrounded me in all directions."
    sn "My vision flickered. As I forced myself up to my feet, brushing away the snow on my body to no avail amidst the constant white precipitation, my arms shook."
    nvl clear 
    sn "When I breathed in, a sharp pain pulled in my chest and invisible icicles seemed to sprout in my throat."
    sn "Just how long had I been walking?"
    sn "I pushed myself forward. My ankle seemed to crunch oddly in the ever-accumulating snowfield. If I twisted it, the cold and boots damped the pain."
    sn "Eventually, the snow lightened up."
    sn "Yet when I looked around, there seemed to be nothing here, only a dilapidated ruin of a landscape covered by snow."
    nvl clear 
    sn "So much had disappeared that I could barely tell where I had come to."
    sn "No, I really simply couldn't tell where I was anymore if this place even existed in the world anymore."
    sn "I stumbled again."
    sn "My limbs shook with an unfamiliar exhaustion. As I couldn't find the might in me to stand, I crawled forward a few more meters until I had no more strength left to move."
    sn "What now?"
    nvl clear 
    nvl hide Dissolve(0.3)  

    Sanna "..."
    Sanna "I'll just... close my eyes..."
    Sanna "...and rest for a bit..."

    stop music fadeout(7)
    scene black with dissolve_scene_full
    call delete_snow from _call_delete_snow_5
    pause 5



    play music calm1

    scene house with fade

    show freya closed pout at t21
    Freya "I can't tell if your hands are cold or warm through the gloves." with Dissolve(0.3)
    show sanna standing pjs awkward at t22
    Sanna "My hands are always cold."
    Freya smile up open "I don't mind, I'll just warm you up since mine are always warm. There is a saying too. Cold hands, warm heart."
    Sanna trying blush "Your heart is warmer than mine."
    Freya smug crossed "It's okay, I'll warm your heart too."
    Sanna "Hehe."


    sn "Without any hesitation, she took my hand and gripped it firmly." with Dissolve(0.3)
    sn "When I looked at her, the world seemed to regain its colors, even if only a little bit."
    sn "A certain feeling had been bubbling in my chest for a long time. It wasn't painful at all. Rather, it was something warm and reassuring that I kept hidden away without saying."
    sn "I didn't feel that I needed to say it."
    nvl clear 
    nvl hide Dissolve(0.3) 


    Freya serious "Your cheeks are a bit flushed." with Dissolve(0.3)
    Sanna chill "Really?"
    Freya "They are."
    Freya "Maybe you should be in bed."
    Sanna mild "No, I'm alright. I just..."
    Sanna "I'm a bit tired from being in bed all day, if I'm being honest."
    Freya concerned "O-oh yeah..."
    Sanna trying "But I seem to be feeling better! I guess that crystal stuff really does work."
    Freya neutral up "I told you it works."
    Sanna "I guess it does. Even though you won't tell me what it is."
    hide sanna
    hide freya
    with dissolve
    Freya "*cough*"
    "She was caught in a fit of coughing."
    Sanna "Freya!"
    Freya "I'm fine! I'm fine."
    Freya "It's nothing. Just... a small fever. That's all."
    Sanna "But--"
    Freya "I just need some rest, okay? ...and I'll be fine."
    Freya "Wha- what are you doing?"
    "I pull Freya over into the bed, covering us both with the sheets."
    scene cg1 with dissolve
    Freya "No, I don't want to give it to you-"
    Sanna "Shhh, don't worry about it."
    Sanna "I'll keep you warm."
    Freya "A-alright."
    Sanna "Freya?"
    Freya "Yes?"
    Sanna "I just wanted to say your name."
    Freya "......"
    Freya "I'll trust in you to remember for me if I ever forget."
    Sanna "...yeah."
    Sanna "I trust you too."


    sn "I looked outside through my room's window." with Dissolve(0.3)
    sn "Nothing. No color, just pure white."
    sn "An absence of color."
    sn "I wondered about the other families that were holed up in their homes."
    sn "Struggling, trying to weather the storm. Not knowing when it would light up, if at all."
    sn "Were they trying to hold these small precious moments of daily mundanity?"
    nvl clear 
    sn "Or was it just me, desperately trying to hold myself together. Keep myself as I was."
    sn "The days were blurring together."
    sn "How long had I been stuck here? Five weeks? Two years?"
    sn "I didn't know. Just thinking about it made me scared."
    sn "But Freya was always here."
    sn "As long as she was with me..."
    nvl clear 
    sn "I didn't really mind anything else."
    nvl clear 
    nvl hide Dissolve(0.3) 

    stop music fadeout(2)
    scene black with fade

    pause 6




    play music ArtificialAntartica
    scene white
    Sanna "*gasp*"

    sn "I hoarsely coughed out snow from my lungs." with Dissolve(0.3)
    sn "It was trying to kill me, trying to get inside me."
    sn "I tried to get a grasp of my surroundings. I slowly started to remember."
    sn "I had collapsed in the snow."
    nvl clear 
    sn "Still coughing, I struggled to dig myself out of the thick blanket that was still piling on top of me."
    sn "If I had woken any later I might have suffocated."
    sn "That is, if I didn't freeze to death first."
    nvl clear 
    nvl hide Dissolve(0.3) 

    show sanna standing jacket scarf squint concerned sweat at t32
    call init_snow from _call_init_snow_7
    call show_snow from _call_show_snow_8
    with flashflash

    Sanna "Ungh..." with Dissolve(0.3)
    Sanna "I have to... keep moving..."
    Sanna closed "..."

    sn "Scanning the horizon, there were a few distinct shapes within a few miles." with Dissolve(0.3)
    sn "Some buildings, ruins perhaps, or even a campsite. It was difficult to tell from this far away."
    sn "In any case, it meant shelter, so I headed towards the shadows in the distance."
    nvl clear 
    nvl hide Dissolve(0.3) 

    stop music fadeout(4)
    scene black with fade
    call delete_snow from _call_delete_snow_6
    pause 6




    play music lost
    scene house with fade

    sn "If I closed my eyes, would I forget and be forgotten?"
    sn "Snow continued to fall outside, covering the disappearing world in white. People faded away, losing everything and being lost by a world that no longer sustains memories."
    sn "Today as well, I holed up in my room and waited."
    sn "Knock, knock."
    sn "There was that familiar sound at the door."
    sn "She came again. Even though I told her not to come anymore, she still came here each and every day."
    nvl clear 
    nvl hide Dissolve(0.3) 


    scene door with dissolve
    Freya "Sanna, I brought you some food. And... I also brought you your medicine." with Dissolve(0.3)
    show sanna sitting blank at s43
    Sanna "I thought I told you to stop coming here."
    Freya "You have to take it, alright?"
    Freya "As long as you close your eyes and take it..."
    Freya "Just pretend."
    Freya "Everything will be alright."
    Sanna "I'm used to taking bitter medicine."
    Sanna frown "But I won't take that. It's not medicine, Freya."
    Freya "If you don't take it, you'll disappear. Aren't you afraid of disappearing?"

    sn "That was true." with Dissolve(0.3)
    sn "More than that, I was afraid of her disappearing. Yet I was too much of a coward to open this door and look at her face. If I did, my convictions would waver."
    sn "She couldn't keep going out to find those crystals. She couldn't keep coming back here. She couldn't, not for me."
    sn "Both of us were obstinate."
    nvl clear 
    nvl hide Dissolve(0.3) 



    Sanna "I'm alright even if I disappear." with Dissolve(0.3)
    Freya "Sanna-"
    Sanna blank "Do you remember our special place?"
    Freya "......"
    Sanna "The one we use to play at."
    Freya "...yes."
    Sanna "Is it still there?"
    Freya "..."

    "What was that place again? A park? A lake? I couldn't remember. All I had was a fuzzy feeling that once upon a time, we had spent our childhood at a place."


    Sanna distraught "Sometimes I wonder... the world outside, does it even exist anymore? Is it all covered in snow, or has everything gone, simply disappeared?"
    Sanna "From the world itself, and our memories."
    Freya "You're not wrong."
    Freya "A lot has disappeared. Places I wanted to go with you, places we hold dear, they've crumbled and disappeared."
    Freya "But we're still here. We're still alive, Sanna, so we can't disappear yet."
    Sanna "Is it worth just existing if nothing exists anymore?"
    Freya "If you're still here, then it is."
    Sanna angry "Liar."
    Sanna "What about me?"
    Sanna "What if you're not-"
    Sanna distraught "Freya, aren't you ever scared that if you step out there, you won't be able to come back?"
    Freya "......"
    Freya "I don't really think about it."
    Sanna "After all, the world is ending, isn't it?"
    Freya "...Don't say that."

    sn "I wasn't surprised, not really, but still I found myself at a loss for words. I had simply wanted her answer to be different, for her to think about it and be scared because I was scared." with Dissolve(0.3)
    sn "What if Freya really disappeared and never returned?"
    sn "I couldn't say anything."
    sn "Silence."
    sn "All we did was argue, unable to say anything to each other. I I hated it."
    nvl clear 
    nvl hide Dissolve(0.3) 

    Freya "*cough*"
    Sanna "How far did you have to travel today to find anything?"
    Freya "Not that far."
    Sanna "Don't bother with those crystals anymore. It's wrong to use them."
    Sanna "I'm alright even if I disappear, so..."
    Sanna "Either stop going or stop coming back."
    "She mumbled something but I couldn't hear it."
    Sanna "......"
    Freya "Sanna?"
    Sanna "What?"
    Freya "...No, it's nothing."

    sn "I knew it wasn't nothing but chose not to pursue her murmur." with Dissolve(0.3)
    sn "We exchanged no words, only silence. Only a week ago, this would have been extremely out of place between the two of us, but here we were now."
    sn "I waited for her to say something or leave. What would I even say?"
    sn "I couldn't see her face, but I could still imagine how she would purse her lips in frustration. I wouldn't forget her even if the world disappeared today, even if I ceased to exist today."
    sn "Like she said, we were both stubborn."
    nvl clear 
    nvl hide Dissolve(0.3) 



    Freya "I'll leave this here by the door." with Dissolve(0.3)
    Freya "Take care of yourself, and make sure you're eating properly, alright?"
    Sanna "...You too."
    Freya "Thanks."
    Sanna "......"
    Sanna "Freya?"

    sn "She did not respond, as she had already left." with Dissolve(0.3)
    sn "Freya, my most precious friend, I didn't want her to come, yet I didn't want her to leave."
    sn "If only I could forget all of the sad memories in this world, then all would be well. Yet I couldn't. Instead, the world around us crumbled to pieces bit by bit."
    sn "I, who hadn't left this home for a long time, could only look outside to the white that blanketed the town around us. I could no longer remember what hid underneath the snow."
    nvl clear 
    sn "Perhaps, if the snow ever melted, everything beneath would have already faded away."
    sn "Memories, the world no longer sustained memories. It lost its details, its form, its very shape."
    sn "Forgotten by those around them, forgetting themselves, one day, without anyone noticing, people too lost their individuality and ceased to exist."
    sn "Where did they go? Who were they? Had they even existed? All that remained was the gap they left behind and fragments of broken souls."
    nvl clear 
    sn "That was the illness plaguing those still left behind."
    sn "That was mine as well."
    sn "After a while, I opened my door. As Freya said, she left what she brought by the door. I gingerly picked it up, seeing the food and the so-called medicine."
    sn "The medicine took the form of a crystal, a small, magical-looking thing."
    sn "So frail and fragile, just like our memories."
    nvl clear 
    sn "I didn't want her to go out to retrieve these things, but I couldn't hate her for bringing them to me. Instead, I simply shut her away and rejected her."
    sn "I put the crystal down."
    sn "I wouldn't take this medicine even if it meant I had to disappear."
    sn "Closing the door, I returned to my solitude and waited."
    nvl clear 

    scene black with fade

    sn "On the next day, no knock came at the door." with Dissolve(0.3)
    sn "Then, the next day, no knock came at the door."
    sn "Freya stopped coming back."
    nvl clear 
    nvl hide Dissolve(0.3) 

    Sanna "She's not coming back." with Dissolve(0.3)
    Sanna "You were the one who told her to leave."
    Sanna "She chose the crystals over me."
    Sanna "Maybe she just didn't want to deal with you anymore."

    sn "Outside, the snow didn't stop. The wind howled like someone was crying or screaming. Bitter hail battered the windows and the roof." with Dissolve(0.3)
    sn "I couldn't see beyond the turbulent white that blocked out the sun."
    sn "Inside, all was dark. I felt the cold seeping into my room, into my heart. The heating and insulation of my home still worked fine, but I couldn't find the warmth."
    sn "Where had the warmth gone? I was cold."
    nvl clear 
    sn "I worried, worried, and worried. Maybe Freya hated me now, but what if she was still outside, what if she had really gotten into trouble... what if something bad happened?"
    sn "Even as I wallowed, she never returned."
    sn "I dragged myself to the door, the door to the outside world. Extending my hand to the handle, I couldn't bring myself to open it yet."
    sn "Thud, thud, went the wind, the snow, and the hail at the door."
    sn "The outside world was scary."
    nvl clear 
    sn "Would I simply wait and see? No, that was unacceptable. Even if I were to disappear, at this moment, I still existed. My body still breathed and moved and remembered."
    sn "To idle about and think of the future when said future might not even exist was such a waste."
    sn "Throwing away the hesitation called thinking, I threw the door open."
    sn "Cold flew at my body. I squeezed my eyes shut as the chilling wind and snow went right into my face, stumbling and falling on my butt at the sudden shock."
    nvl clear 
    sn "Before I even got a chance to step out, the storm threw the door back shut."
    sn "I wiped the snow out of my eyes with the sleeves of my now wet shirt. I felt as if I had been given a wake up call. Was I an idiot?"
    sn "I hadn't even gotten changed."
    nvl clear 
    sn "Taking a slow, deep breath, I calmed myself down and pondered upon what I would do next. For someone who spent her days thinking, surely I could be considered terrible at it."
    sn "My head was filled with transient clouds, so I once more stopped and decided to go outside, this time with a tad more arrangement."
    sn "I dug through the closet to find clothes: a sweater, a jacket, proper pants, boots, and all. Lacing my boots with difficulty, I prepared myself to go outside."
    sn "I returned to the final door between the inside and the outside."
    nvl clear 
    sn "Firmly holding onto the handle, I opened the door slowly against the force of the storm and stepped outside. Then, I closed the door, squinting as the snow battered against me."
    sn "I couldn't even count how long it had been since I last left my home."
    nvl clear 
    nvl hide Dissolve(0.3) 
    Sanna "Goodbye, home. I promise to come back to you with her."

    sn "Waving the door goodbye, I began to walk, wondering if my dear home will still be here by the time I return."

    stop music fadeout(2)
    scene black with fade
    pause 2





    play music FrozenFuchsia
    scene facility
    call init_snow from _call_init_snow_8
    call show_snow from _call_show_snow_9
    with flashflash
    nvl clear 
    sn "As I approached closer to the shapes I saw in the distance, I realised that they were indeed just two buildings... albeit strange looking buildings." with Dissolve(0.3)
    sn "They had almost no distinct features, just pure black blocks."
    sn "There were no signs of life anywhere."
    sn "I cautiously wander inside of the structures, taking my time to slowly check out my surroundings."
    nvl clear 
    nvl hide Dissolve(0.3) 

    Sanna "Some sort of... military base?" with Dissolve(0.3)

    scene infacility with fade

    sn "When I entered one of the buildings it was clear that my guess was close, but wrong." with Dissolve(0.3)
    sn "It was not a military complex, but a research facility."
    sn "Except... it looked like everyone had gone up and left."
    sn "The lights were still on, and there was heating."
    sn "There were some odd-looking computers that were still on and functional."
    sn "Monitors displaying charts of data that I didn't really comprehend."
    nvl clear 
    nvl hide Dissolve(0.3)


    sn "Various research papers were scattered around, as if someone had been frantically looking for something." with Dissolve(0.3)
    sn "After wandering for a little bit more I stumbled upon a peculiar looking room."
    sn "It was a room completely surrounded in glass, making easy access to monitor from the outside."
    sn "The contents of the room itself was bare, all except for a table and something that resembled a tray."
    sn "It was obvious that there was supposed to be something it was meant to hold but now it was missing."
    nvl clear 
    sn "I only realized later that there was a hole on the other side of the room, the glass was shattered."
    sn "Someone had come here and took whatever this place was holding."
    sn "Something that they weren't supposed to take."
    nvl clear 
    sn "Everything felt a bit out of place, and suddenly it seemed like I was not supposed to be here."
    sn "I wanted to leave as soon as possible."
    sn "I took a deep breath once I was outside of the building complex."
    nvl clear 
    nvl hide Dissolve(0.3) 

    Sanna "Freya... where are you?" with Dissolve(0.3)

    sn "There was only one place left to check, it seemed." with Dissolve(0.3)
    sn "I took another deep breath and tried to steady my mental state."
    sn "Then I headed towards the other building."
    nvl clear 
    nvl hide Dissolve(0.3) 


    stop music fadeout(2)
    scene black with fade
    call delete_snow from _call_delete_snow_7
    pause 2




    scene house with fade

    show Rfreya concerned at t41
    Freya "......"
    Freya "(How much longer can I keep this up...?)"
    show sanna standing pjs at t44
    Sanna "Keep what up?"
    hide Rfreya
    show freya sweat up guilty at t41
    Freya "...!?"

    play music goodbye

    Sanna "...What can't you tell me?"
    Freya concerned crossed "......"
    Sanna sad "Is it something related to me?"
    Freya "It's not related to you."

    Sanna angry "You're a bad liar, Freya. I've always been able to tell."

    Freya up guilty "If I said it, even you wouldn't believe me. ...Ah, I've really messed up this time, haven't I?"
    show freya awkward
    Sanna "So it's something important."
    Sanna determined "Related to me? This illness? The medicine you've been bringing me...?"
    Freya crossed concerned "......"
    Sanna concerned "The last one, huh?"
    Sanna "Yes, it seems that my third guess was the right one."
    Freya awkward up "Is there any way I can convince you to not dig any further?"
    Sanna angry "No, I want to ask you what you've been hiding from me, Freya. What are the crystals you've been bringing me?"
    Freya serious -sweat up "They're medicine."
    Sanna "Beyond that."
    Freya crossed "They're just..."
    Freya closed concerned "...it's complicated."
    Sanna "Just tell me."
    "She breathed a heavy sigh."
    Freya up serious open "They're the things that people leave behind once they disappear."
    Freya "It's their leftover essence that eventually congeals into crystal form after a while under the right conditions."
    Freya "I don't really understand much of it myself but..."
    Freya crossed "It's like... a part of someone. Their memories. Their color."
    Sanna frown squint "W-what?"
    Sanna "I've been..."

    sn "I felt sick. A rolling, undulating feeling in my chest filled me with nausea." with Dissolve(0.3)
    sn "I felt sick, not because I really felt sick about eating that medicine but because I didn't feel as sick as I thought I would."
    sn "I felt empty that Freya had lied to me about something this important. I felt empty that I knew I probably could still forgive her."
    nvl clear 
    nvl hide Dissolve(0.3) 



    Sanna open "What have I been consuming?" with Dissolve(0.3)
    Sanna angry "Why didn't you tell me?"
    Freya guilty up "I... I know you wouldn't take them if you knew the truth."
    Sanna "Did you know from the start?"
    Freya crossed serious "No. Someone told me later on."
    Sanna "That's a lie."
    Sanna sad teary "Don't go out to find them anymore, Freya. I won't take the crystals anymore."
    Freya concerned "...Sanna..."



    sn "I didn't understand..." with Dissolve(0.3)
    sn "So complacent and happy just to be with her each day, feeling assured that a miracle had arrived to stop my deterioration, I had been so, so blind."
    sn "Her image in my eyes became blurred."
    sn "When had tears flooded my eyes? I was really a crybaby, I thought as my shoulders shook with the anguish I couldn't articulate."
    sn "She reached out a hand to wipe away my tears, but I took a step back."
    nvl clear 
    sn "Roughly rubbing my eyes that just wouldn't stop leaking, I tried to look her in the eye for the last time. I felt as if I were looking at a stranger."
    sn "The world disappeared. I slowly began to crumble apart. The places we knew, the people we met, the memories we made, all of them had scattered long ago."
    sn "They turned pure white like the snow outside, so prettily that without thinking, I could almost just embrace it and forget everything."
    sn "Except it was a painful thing, as painful as the snow was cold and suffocating."
    nvl clear 
    sn "Without realizing, the dear and precious bond between us had frayed and turned into something I no longer recognized as if it too wanted to disappear."
    sn "I didn't want that."
    sn "I didn't want to lose her."
    nvl clear 
    nvl hide Dissolve(0.3) 

    show sanna crying squint sad
    Sanna "I think you should just go." with Dissolve(0.3)
    Freya up concerned "......"
    Freya crossed sweat closed "......"
    window hide
    hide freya with dissolve
    pause 2
    scene black with fade



    sn "Thus, I was now alone." with Dissolve(0.3)
    sn "Even as I reminisced about the past, when I opened my eyes, she wasn't here. Of course she wasn't here. I was the one who chased her away."
    sn "She came to knock at my door each and every day. I refused to open it for her; I turned her away."
    sn "Looking out the window, I noticed the snow had started to fall again."
    sn "The sky darkened. When I went to prepare food and eat, I couldn't help but feel that everything tasted like nothing."
    nvl clear 
    sn "Not strong, not faint, not bland or disgusting, it just tasted like nothing."
    sn "After the meal, I swallowed some pills dry. Vitamins, supplements, these weren't medicine either. I didn't like the bitter aftertaste of medicine tablets."
    sn "In the end, medicine was bitter, wasn't it? If not in taste then in essence."
    sn "My mind wandered to before everything fell apart, but remembering was so terribly difficult as if my past had already crumbled to nothing."
    nvl clear
    sn "This illness would devour me one day."
    sn "Should I have asked it to devour me faster?"
    sn "The snowfall grew heavier and heavier until I couldn't see past the veil of white at my window."
    sn "I wondered if Freya was alright, if she was outside even as a snowstorm raged. I didn't even know anything outside of my home anymore."
    sn "I felt like a bird in a cage or perhaps a caterpillar in a chrysalis partially torn open by someone else."
    nvl clear    
    sn "I was unable to fly, unable to struggle, trapped in an indescribable shell made by my own self. Maybe I was like a worm that couldn't have become a butterfly to begin with."
    sn "The outside world was scary. What if there was already nothing there?"
    sn "Holing up inside, today as well, I waited."
    sn "I waited."
    nvl clear 
    nvl hide Dissolve(0.3) 

    stop music fadeout(4)
    pause 6




    scene facility
    call init_snow from _call_init_snow_9
    call show_snow from _call_show_snow_10
    with fade


    sn "The black cube-like building was identical to the other one next to it." with Dissolve(0.3)
    sn "However, on the inside, it couldn't be any different."
    nvl clear 
    nvl hide Dissolve(0.3) 

    play music funk

    scene crystals with fade
    call delete_snow from _call_delete_snow_8
    sn "The walls, the floor, the ceiling was all covered in the familiar crystalline substance." with Dissolve(0.3)
    sn "It was like a growth, flowing everywhere, consuming, eating away at everything it touched."
    sn "It was everywhere, filling every orifice it could find. Covering every surface it could see."
    sn "Jagged and sharp edges threatened to cut and shred as I tried to make my way past various structures of crystal formed from the ground."
    nvl clear 
    sn "In the middle of the room, there was a figure laying on the ground."
    nvl clear 
    nvl hide Dissolve(0.3) 

    show sanna running scarf gasp teary at t32
    Sanna "Freya!" with Dissolve(0.3)
    hide sanna with dissolve

    sn "I ran over and kneeled over her." with Dissolve(0.3)
    sn "She turned to face me."
    sn "She spoke. Her lips moved, but I couldn't hear her voice. Surely, my ears weren't broken. Her voice did not reach me. Why couldn't I hear her?"
    sn "I staggered closer to her."
    sn "...That expression on her face was so..."
    sn "Painful."
    nvl clear
    sn "For the first time, I noticed that she was fading away too. When had that started? Such a thing wouldn't happen to a person immediately."
    sn "She placed a hand on my cheek. She was saying something to me. I couldn't feel the warmth of her hand through the glove."
    sn "Then she kissed me on the lips."
    nvl clear
    sn "Apparently, first kisses tasted sweet like hope, but all I could feel was sour, bitterness."
    sn "The kiss that lasted for too short a period ended. She broke away from me and spoke, or maybe simply mouthed, to me that precious phrase of 'I love you.'"
    sn "Love, the love she spoke of was the same type of love I'd been holding inside."
    nvl clear 
    nvl hide Dissolve(0.3) 


    Sanna "...Tell me that later when we've properly reconciled... when I can properly tell you that my feelings are the same as yours." with Dissolve(0.3)
    Sanna "Why are you fading away too?"
    Freya "(I guess even I wasn't immune to it.)"
    Sanna "......"
    Freya "(I'm sorry. I never got a chance to apologize.)"
    Freya "(I shouldn't have lied to you.)"
    Freya "(I can see you want to say it's alright.)"
    Freya "(I just... wanted to make things right. Even if how I did it was wrong.)"
    Freya "(I'm sorry Sanna. I won't do it again, I won't betray your trust anymore.)"
    Freya "(...Even if not in this lifetime, not in this world anymore.)"
    Freya "(For the rest of our time here and for if we ever meet again after everything disappears.)"
    Sanna "I can't hear your voice."
    Sanna "Don't look as if you're about to disappear!"
    Sanna "Don't... don't do this to me..."


    sn "Even though I knew that she was talking and inexplicably could tell the words she spoke, I still couldn't hear her voice." with Dissolve(0.3)
    sn "I still remembered. I still remembered that she existed, that she was such an important existence to me. I hadn't forgotten her, so she couldn't fade away yet."
    sn "Her name? Of course it was-"
    sn "My mind stalled. She was someone so important to me. I wanted to call out her name again and tell her that I would remember her for her if she herself forgot."
    sn "I had promised. She had requested it of me."
    nvl clear 
    sn "I grabbed her tightly, my own voice not escaping my throat. She hugged me back. Her hugs were so very firm, so very solid. She was still there."
    sn "Then, I realized that I was also dissipating."
    sn "I felt her whisper into my ear, something that I could not hear. She gripped me so tightly that it nearly hurt as if she was also afraid I'd fade away."
    nvl clear 
    sn "Her name, her existence, her everything, how could I forget any of that?"
    sn "Not now, I wouldn't let her go yet."
    sn "Even if the world wanted to take her away, it would have to take both of us away at the same time. We promised each other that we would remember each other for each other."
    nvl clear 
    nvl hide Dissolve(0.3) 



    Sanna "Freya!" with Dissolve(0.3)
    Sanna "You're Freya!"
    Sanna "You can't... disappear."
    Sanna "You can't... you--"
    Freya "Sanna-"

    sn "My vision blurred." with Dissolve(0.3)
    sn "Finally, I heard her voice."
    sn "At that moment, my consciousness snapped, and everything turned dark."
    nvl clear 


    stop music
    scene black


    pause 6




    sn "I woke up to a familiar ceiling. For a moment, I questioned if I had really rushed out into a snowstorm and reunited with Freya at what seemed like the edge of the world." with Dissolve(0.3)
    sn "It didn't feel real. Mere fragments of a fever dream or a hallucination."
    sn "I was afraid that I had only dreamed what happened and she was gone."
    sn "Sitting up and looking around in a panic, I was flooded with relief. Soon, I drifted off to sleep again. My exhaustion finally caught up to me."
    nvl clear 
    nvl hide Dissolve(0.3) 

    pause 6

    play music calm1
    Freya "Achoo!" with Dissolve(0.3)
    scene cg2 with fade
    Freya "Being sick sucks."
    Sanna "You're lucky you're only 'sick'. I really don't know how you dragged us back home."
    Freya "Isn't there anything that'll make me healthy in a jiffy?"
    Sanna "I think there's still cold medicine somewhere in the medicine cabinet."
    Freya "The cherry flavored syrup stuff?"
    Sanna "No. I think... it's the honey lemon flavored one that tastes like fertilizer."
    Freya "Is it alright if I say that I don't want to have any of that?"
    Sanna "Pfft."
    Sanna "Of course. It's healthier for your body to fight off the cold itself than to rely on medicine from the start if it's just a cold."
    Freya "Alas."
    Freya "Speaking of medicine, the crystals disappeared already, didn't they?"
    Sanna "Yea, they did."
    Freya "So fast. Well, it's not like I can find anymore around here anyhow. That's a weird weight off my shoulders."
    Sanna "...If you find more, you should take them."
    Freya "Hm?"
    Sanna "...This might be hypocritical of me, but... if I disappeared and left one behind, I would want for you to keep living, so..."
    Freya "Geez, don't say that."
    Freya "That's not to say I don't feel the same way. If I disappeared before you, I would want you to keep living too."
    Freya "I don't plan to actively go search out the crystals anymore."
    Freya "As for what would happen if we do stumble upon one, well, I guess we can discuss it when we get there."
    Sanna "Yea."
    Sanna "Just one thing. You're not allowed to disappear before me."
    Freya "Isn't that kind of unfair?"
    Sanna "Nope."
    Freya "Alright, then neither of us is allowed to go before the other. That sounds about right, doesn't it?"
    "I nodded."
    Freya "So, can you tell me again that you love me?"
    Sanna "Hm, I love you."
    Freya "Hehe."
    Sanna "In a romantic way."
    Freya "I don't know if you said what you like about me, so could you tell me?"
    Sanna "I love the way that you're kind and caring, the part of you that's sometimes silly but comes through with things in the end. I like how you're positive even when I'm gloomy."
    Sanna "And you're warm. I love it when you hold my hand. I always feel comfortable when you're by my side."
    Sanna "Maybe this is strange to say, but I like the timbre of your voice."
    Sanna "I also like your strength and honest earnestness even when you make mistakes."
    Sanna "I just love you a lot because you're you. I wish I had told you earlier, so maybe I'm also happy that you were the one who ended up confessing first."
    Sanna "What do you like about me?"
    Freya "I like your everything."
    Freya "Your pretty green eyes, your silky hair, the way you smile, the way you laugh, your slightly cool body temperature, and your delicate fingers."
    Freya "Your stubborn behavior, the way you're just a little picky about food, how your eyes will just light up when you're happy, and how you'll rely on me when you're sad."
    Freya "I can naturally keep going. I've been in love with you for a long time. Although I've learned something new recently that I like about you."
    "She gave me a quick peck on the lips."
    Freya "The soft taste of your lips."
    Sanna "Y-you tease!"
    Freya "I love you too."
    "I playfully smacked her with a pillow and then buried my face in it in embarrassment for a few seconds."
    stop music fadeout(2)
    Freya "What should we do from now on?"
    play music ending
    Sanna "Let's go on the trip we've always been talking about."
    Freya "Where to?"
    Sanna "I think we don't need a destination. We never could decide, so maybe it's better if we just head off on the trip and go where our hearts tell us to."
    Freya "A trip, huh? With the way things are, the only option is a road trip."
    Freya "The snow will melt, and the roads will be alright to drive on. Yes, I think that's a good idea. As soon as the weather turns better, we can set out on the trip."
    Freya "Until then, I guess we have to prepare for it and get ourselves ready."
    Sanna "Do you know how to drive?"
    Freya "Legally speaking..."
    Sanna "Illegally speaking?"
    Freya "I don't have a license, but I can ride a motorbike just fine."
    Freya "There should be one in the garage at home. The sidecar is big enough to store quite a bit of supplies."
    Sanna "I like that idea. A road trip via motorbike."
    Freya "Right? Doesn't it sound like fun?"
    Sanna "Yea, it does."

    scene black with fade
    pause 1
    scene cg3 with Dissolve(3)
    pause 5

    sn "Talking about a trip, we always did that, but actually going on the trip, we had yet to do so." with Dissolve(0.3)
    sn "If we were to talk about tomorrow, the scarce tomorrows that might not exist anymore after the next today, we wanted to spend that tomorrow together."
    sn "Rather than staying holed up inside forever, going out together to see what remained of the world was a better way to end it."
    sn "For all that had disappeared, so much more remained to be seen."
    nvl clear 
    sn "When spring came, the roads melted. We were still here. Thus, on that road trip we went."
    sn "Like an item on our long-time bucket list crossed off, we travelled the roads that had crumbled under the pale skies."
    sn "She showed me all that was beautiful in this world."
    sn "Eventually both of us would disappear. Like snow that melted away in the spring, we would leave no footprints, not here."
    nvl clear 
    sn "Yet the impressions we made in each other's hearts wouldn't be erased."
    sn "The world lost its colors, reverting to a pure white canvas. She and I continued onward in the small but fulfilling journey of our short but precious lives."
    sn "When I closed my eyes, I simply remembered her and was remembered."
    nvl clear 
    nvl hide Dissolve(0.3) 
    pause 1

    scene cg4 with Dissolve(3)
    pause 8
    stop music fadeout(3)
    scene black with Dissolve(3)
    pause 6
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
