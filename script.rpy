



label start:




    scene white with Dissolve(4)
    pause 1








    window hide
    nvl clear  
    sn "当我还是个孩子的时候，我在圣诞节愉快地凝视窗外，那时的我从未想过，像雪这样神奇而美妙的东西会造成如此大的破坏。" with Dissolve(1)
    sn "我根本看不清眼前的路途，每当我抬脚迈步，靴子都会深深陷入雪中，一种致命的纯白紧紧地粘在我身上。"
    sn "如果我在风雪中回头，我会看到每次迈步留下的靴印立刻就被蓬松的风雪掩埋，仿佛我一开始就不在那里。"
    sn "在这样的风雪中，我几乎无处可去，迷茫之后，我决定去看看她是否在家。"
    nvl clear  
    sn "我仍然记得去她家的路。尽管在这样的风雪中很难看得清四周，甚至很多我们小时候知道的事物都消失了，我只能疲惫的迈步向她家的方向。"
    sn "两个街区的距离并不太远。"
    sn "也许我只是因为睡的太久太沉而行动迟缓，疲惫虚弱，又也许真的是因为这严酷的天气让我无法前进。"
    sn "我很怀念那些事物，我们曾经最喜欢的树，路边的旧邮箱，他们都去哪里了？我们熟悉的社区什么时候变成了这样？"
    nvl clear   
    nvl hide Dissolve(0.3)
    show sanna standing jacket concerned open at t32
    Sanna "也许我早就迷路了……" with Dissolve(0.3)


    sn "但当我开始自我怀疑时，终于，她的房子就在前面了。" with Dissolve(0.3)
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

    sn "这是我有生以来第一次敲门。" with Dissolve(0.3)
    sn "我把手放在门上的声音空洞地回响着。"
    sn "长时间的沉默。我又敲了一下。"
    sn "没有人回答。"
    nvl clear 
    sn "她家的门铃早就坏了，从来没有人想过要修好它。我所能做的就是再敲几下，站在原地时感觉寒冷袭来。"
    sn "她可能没有听到我的声音。如果她在家，她有可能在咆哮的暴风雪中没有听到我微弱的敲门声。"
    sn "没有人回答，所以我又敲了敲门，这次更疯狂了。"
    nvl clear   
    nvl hide Dissolve(0.3)

    show sanna standing jacket concerned open at t32
    Sanna "来吧，该死的。" with Dissolve(0.3)
    Sanna "..."

    sn "别无选择。我开始转身离开。" with Dissolve(0.3)
    sn "突然，一道闪光挡住了我的去路。金属。一把钥匙。"
    sn "备用钥匙。真不敢相信我忘了。"
    sn "我蹲在地上挖雪，挖，挖，即使雪埋了我的努力，直到我发现了她前门旁边的小隔间，备用钥匙就放在那里。"
    sn "我小心翼翼地打开它。令我欣慰的是，钥匙就在那里。"
    nvl clear 
    sn "我眯起眼睛把它捡起来。钥匙仍然放在原来的地方，甚至保留了我们小时候用永久性记号笔潦草地画的愚蠢的画。"
    sn "我分不清这幅画是猫还是鸟。"
    sn "Click."
    sn "门用备用钥匙开锁了。我把它塞回原处，也许将来会再次为Freya服务。然后，我进了屋子。"
    nvl clear   
    nvl hide Dissolve(0.3)



    Sanna "你好？" with Dissolve(0.3)
    Sanna determined "有人在家吗？"

    sn "我的声音在房子里回荡。没有人回答。" with Dissolve(0.3)
    sn "我知道这不可能那么容易。"
    sn "在我花了一点时间再次热身后，远离了纯白色的降水，我回到外面继续我的旅程。"
    nvl clear
    sn "下一步在哪里？这个问题，我在她家舒适的地方问过自己。"
    sn "我需要找到她，但我不知道下一步该去哪里。"
    sn "我没有计划这么远，现在我在这里。..我不知道该怎么办。"
    nvl clear   
    nvl hide Dissolve(0.3)

    Sanna squint frown "我真的像我想象的那样了解她吗？" with Dissolve(0.3)

    sn "她多次提到北边的空地。也许她在那里。" with Dissolve(0.3)
    sn "沿着应该向北走的街道，我步履沉重地向前走去。风把我的步伐逼得像蜗牛一样，有好几次，我差点摔倒，双脚陷在雪地里。"
    sn "狂风吹过我的脸，感觉就像一千根无形的针穿过它。"
    sn "虽然我的手指以前感觉麻木，但现在除了刺痛什么也感觉不到。尽管如此，我还是强迫自己前进。"
    sn "我需要尽我所能去。"
    nvl clear   
    sn "我必须这么做。"
    nvl clear  
    nvl hide Dissolve(0.3)

    scene black with fade
    call delete_snow from _call_delete_snow_2
    pause 5


    scene house with fade


    play music calm2

    show freya closed pout at t21
    Freya "Brrr... 外面很冷。"
    show sanna standing pjs smile at t22
    Sanna "欢迎回来。"
    Freya grin open "Hehe, 我回来了。"
    Freya "我今天带来了一些特别的东西。"
    Sanna skeptic "有什么特别的吗？"
    Freya up scheming "猜猜看，桑娜。我不应该让你猜，但如果你没有机会猜，那就不好玩了。"
    Sanna "我不知道。小狗？"
    Freya "想得美！"
    Sanna trying "请先就座。在雪地里跋涉，你一定累坏了。我给你拿些热水来。"
    Freya crossed pleased "谢谢你"
    Sanna skeptic "是食物吗？"
    Freya awkward "好吧，我也带了，但也不完全是这样。"
    Sanna "那么，你为什么这么高兴？"
    Freya up geez "但你还没猜到呢！"
    Sanna squint concerned "啊啊……"
    Sanna pout "Mmm...我不知道，放弃啦放弃。"
    Freya pout "Boo."
    Freya grin "但在这里，就是这个。"
    Sanna skeptic "…那是什么？"

    sn "她拿出一些东西，带着一种好像找到了无价之宝的表情给我看。" with Dissolve(0.3)
    sn "珍贵的东西。一颗闪闪发光、看起来很脆弱的宝石。"
    nvl clear 

    Sanna crystal "钻石？这是什么？" with Dissolve(0.3)
    Freya crossed smug "它实际上比这更有价值。"
    Sanna "什么意思？"
    Freya up "来，让我给你看看。"
    show sanna pjs

    window show
    sn "我的第一印象是错误的。" with Dissolve(0.3)
    sn "我以为她找到了一块价值不菲的宝石。"
    sn "但钱已经没有意义了。"
    sn "就这样，她从厨房里找到了研钵和杵，把她带给我的稍纵即逝的水晶磨碎了。"
    sn "尽管我给她倒了一杯水，她还是把粉末倒进水里搅拌，递给我杯子。"
    nvl clear   
    nvl hide Dissolve(0.3)

    Freya "喝吧" with Dissolve(0.3)
    Sanna sad "Freya, 为什——"
    Freya guilty crossed "Just trust me."
    Sanna "..."
    Sanna concerned "……好吧，好吧。"
    show freya neutral

    show black with Dissolve(0.3)
    "..."
    hide black with Dissolve(0.3)

    Sanna skeptic "这很甜……但也……"
    Sanna "……奇怪地熟悉？"
    Freya "我去了北方，靠近废墟。"
    Sanna sad "你去了这么危险的地方？"
    Freya guilty "对不起"
    Freya up pleased "但正因为如此，我遇到了一些人。"
    Freya grin "他们教我如何找到它，以及如何使用它。"
    Sanna concerned "我说它很甜，但没那么甜。弗雷娅，这样的事情不值得冒险。"
    Freya crossed guilty "这是药。它会让事情好转的。"
    show freya serious
    Sanna surprised "药...?"
    Sanna frown "这样的事情真的有可能吗？我真的不相信。"
    Sanna "听起来太可疑了。"
    Freya up guilty "我也不相信，但他们给我看了。"
    Freya surprised "我必须-"
    Freya crossed awkward "……这有点复杂。但这是有效的药物。"
    Freya "……不管怎样，相信我，好吗？拜托，我对此感觉很好。"
    Sanna "..."
    Freya "...求你了？"
    Sanna "..."
    Sanna trying "...好吧。"

    sn "我仍然没有真正被说服，但Freya不会对我撒谎。" with Dissolve(0.3)
    sn "至少她是出于好意。我敢肯定。"
    nvl clear   
    nvl hide Dissolve(0.3)

    scene house with fade
    show freya at t42
    Freya "我最近注意到了一些事情，Sanna。" with Dissolve(0.3)
    show sanna sitting blanket plush at t43
    Sanna "Hm?"
    Freya pleased "你看起来有点像一条裹在毯子里的虫子，一条可爱的小虫子。"
    Sanna upset "可爱？虫子不可爱。"
    Freya grin up "Yes they are?"
    Sanna contradict "如果我是一只虫子，你还会爱我吗？"
    Freya smug "当然。我会给你建一个完整的饲养箱，每天喂你虫子吃。"
    Sanna squint pout "......"
    Freya geez "Pfft."
    Sanna contradict "我很欣赏这个想法，但毕竟我作为一个人更快乐。你更喜欢哪一种：蠕虫还是人类？"
    Freya smug crossed "让我看看……"
    Sanna surprised "这甚至不应该是个问题。"
    Freya awkward up "我不能两者都吃吗？"
    Sanna squint pout "不，你必须选一个。"
    Freya crossed smug "那么，我会坚持和人类你在一起，那个最爱我的小而可爱的人类Sanna。"
    Freya grin "现在，如果另一个选择是大沃姆，我不知道……"
    Sanna squint pout "Hmph."
    Freya "我最终还是会选择你。"
    Freya up grin "桑娜，你会选择哪一个？如果我只是一个普通的老我，一条虫子，还是一只大沃姆？"
    Sanna smile "这根本不是问题，芙蕾雅。我会选择我最爱的正常的人类芙蕾雅"
    Freya crossed pleased "啊，我也最爱你。"


    sn "我把头靠在她的肩膀上。当我开始感到困倦时，她把手放在我的手上。" with Dissolve(0.3)
    sn "我感到安全和放松。"
    sn "好暖和。"
    sn "我所能做的就是吸走那股温暖。"
    sn "我希望我能做得更多。"
    sn "我想成为一个可以支持她的人，而不是一个总是需要支持的人。"
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
    Sanna "！！！"

    sn "我的眼角突然闪过一道红光。" with Dissolve(0.3)
    sn "部分被埋在雪中，但还没有完全被白色覆盖，我在离我最终停下来的地方几步远的地方发现了她的围巾。"
    sn "我向前走了。"
    sn "我把它挖了起来，拍掉了粘在上面的干雪。"
    sn "这是她的围巾，但是……主人在哪里？"
    nvl clear  
    sn "以降雪的速度，我估计她一定是最近才失去的。我心中燃起了一丝希望，我很快就能找到她。"
    sn "尽管我很想找到它们，但我在雪地里看不到她的脚印。"
    sn "感觉围巾没有湿，只是在雪地里有点冷，我把它戴在脖子上。随着红色贴近我的心，我已经觉得有点勇敢了。"
    sn "我必须继续前进。在我如此接近的时候放弃将是一场悲剧。"
    nvl clear   
    nvl hide Dissolve(0.3)


    Sanna shout_sad scarf "Freya!" with Dissolve(0.3)
    Sanna "你在……哪里……"
    show sanna sad
    pause 2

    sn "没有人回应。" with Dissolve(0.3)
    sn "我没有期待奇迹。我只是想要一个幸福的现实。没有什么是完美的。一旦我们再次见面，我们仍然需要处理我们的不满，但我必须找到她。"
    sn "我用新发现的最后力量储备把自己拉了起来。"
    sn "仅凭直觉，我就有一种直觉，她必须朝这个方向走。向前，向前，我只需要向前走，找到她。"
    sn "左脚向前。右脚向前。"
    nvl clear   
    sn "雪在我眼前越下越大，然后才慢慢停了下来。"
    sn "在远处，我看到一个人影。"
    sn "我感觉好像看见她了，但无法靠近。不，她离得更远了；她要消失了。我不明白为什么，但这个想法牵动了我的心。"
    sn "我追着她跑。"
    nvl clear   
    nvl hide Dissolve(0.3)
    Sanna running scarf "Freya!" with Dissolve(0.3)
    stop music fadeout(2)
    scene black with Dissolve(0.3)
    call delete_snow from _call_delete_snow_3
    pause 3




    sn "她和我，如果我谈论我们俩，我几乎不知道从哪里开始。" with Dissolve(0.3)
    sn "就连我们初次见面的细节似乎也不起眼。"
    sn "在同一个地区长大的孩子们，我并不觉得我们相遇很奇怪。"
    sn "在某个时间点，我们只是意识到另一个存在。我们成了熟人。"
    nvl clear   
    sn "我不认为我们是特别合得来的人，但在我意识到之前，我们已经变得密不可分，是最好的朋友，而且不仅仅是朋友。"
    sn "或者我喜欢这么想。"
    nvl clear   
    nvl hide Dissolve(0.3)

    scene fhouse

    play music funk
    show sanna standing jacket open surprised at t22
    Sanna "...A...achoo!" with Dissolve(0.3)
    show freya awkward at t42
    Freya "祝福你。"
    Sanna awkward "谢谢你，Freya."
    show sanna pout

    sn "有一次我和Freya出去了。为什么，我忘了。" with Dissolve(0.3)
    sn "我只记得当时想，我走过的那些褪色的街道应该很熟悉，但看起来很陌生。它们不应该仅仅因为雪而看起来如此灰暗。"
    sn "毕竟，雪对这个国家来说并不罕见。"
    nvl clear   
    nvl hide Dissolve(0.3)


    Sanna "外面又下雪了。" with Dissolve(0.3)
    Sanna mild "明年，我们真的应该去一个温暖的地方旅行。比如夏威夷，或者南方的某个地方。我听说那里现在是夏天。"
    Freya "我们真的应该。"
    Freya "我们一直这么说，但从来没有按照我们的方式去做。去年发生了什么事？即使你没有生病，我最终还是摔断了胳膊。"
    Sanna sad "现在外面发生的事情……"
    Freya up "是啊……好吧，谁知道呢，也许到明年情况会好转，我们终于可以开始旅行了。"
    Sanna open mild "去哪里？"
    Freya grin "夏威夷听起来不错。啊，但是，它可能不在南半球。也许是新喀里多尼亚？我们也可以去澳大利亚和鸸鹋打架。"
    Sanna squint concerned "我现在就否决动车组的比赛。"
    Freya crossed smug "总比和企鹅打架好。"
    Sanna "我什么都不想打架。"
    Freya geez "哈哈。那你想去哪里？"
    Sanna chill "我不知道。选择太多了……"
    Sanna "我现在什么都想不起来。"
    Freya smile "总有明年的事情要做决定。"


    sn "我们的脚步在白雪覆盖的地面上嘎吱嘎吱作响。" with Dissolve(0.3)
    sn "我的眼睛看到了陌生熟悉的东西。即使考虑到冬天最喜欢待在室内，外面的人也比平时少。"
    sn "有那么一会儿，我以为我看到了鬼。"
    nvl clear   
    nvl hide Dissolve(0.3)

    Sanna determined "..." with Dissolve(0.3)
    Freya guilty "这是什么？"
    Sanna "那个人…"
    Sanna frown sweat "他们看起来……太疲惫了。"
    Freya serious "你认识他们吗？"
    Sanna "我…"
    Sanna determined "不"
    Freya "我们不应该盯着看。我们走吧。"
    Sanna "好的。"

    show black with fade
    pause 1
    hide black with Dissolve(0.3)
    show sanna -sweat
    Freya concerned "你父母有消息吗？"
    Sanna open "他们想在假期前回来，但是……"
    Sanna frown "就目前的情况来看，他们似乎还要在国外呆上几个星期。"
    Freya "……这不可能永远持续下去，他们迟早会来的。"
    Freya awkward "在他们回来之前，我还会在你身边。"
    Sanna mild "我知道。"


    sn "我们有一个坏习惯，就是把计划推迟到以后，这可能导致我们从来没有参加过我们喜欢谈论的难以捉摸的旅行。" with Dissolve(0.3)
    sn "那时候，我们仍然抱有过多的希望。"
    sn "希望一切能恢复正常。"
    sn "但我父母再也没回来。"
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

    sn "我一直在跑。" with Dissolve(0.3)
    sn "追着我看到的身影跑。它还没有动，似乎没有再靠近。"
    sn "雪阻碍了我，每一个匆忙的动作都让我的脚更深地陷入白色的泥潭。风把我推了回去。就连我自己无用的两只脚也挡住了路。"
    sn "雪本身正试图阻止我。我能感觉到它从白色中渗出，用冰冷的薄雾笼罩着我的意识。"
    nvl clear 
    sn "我是不是太累了，无法继续？在这架消失的飞机上，我的本质是否已经达到了极限？"
    sn "我试图拒绝这个想法，因为我必须继续前进。"
    sn "仿佛对她的记忆正在消失在白色中，一阵狂风吹过厚厚的白雪，挡住了我对她身影的视线。"
    sn "不，这不是雪。这只是诅咒。"
    nvl clear 
    sn "接下来它会夺走什么？我的名字？我的自我？即便如此，我还是无法放下自己迫切需要再迈出一步的部分。"
    sn "风呼啸着。雪又开始下了。白色充满了我的视野。"
    nvl clear   
    nvl hide Dissolve(0.3)

    Sanna mouth_open "你怎么敢试图把她从我身边带走-" with Dissolve(0.3)
    Sanna grit "!!!"
    scene white with flashflash
    sn "一股强大的北极风猛烈地吹向我，我的电话哽咽了。" with Dissolve(0.3)
    sn "巨大的力量把我的小身躯撞得失去了平衡，我滚回了雪地里。"
    sn "我试图在阵阵狂风中恢复镇静和力量。"
    sn "慢慢地，一步一步地，我走近了那个身影。"
    sn "那是……"
    nvl clear   
    nvl hide Dissolve(0.3)

    scene field
    show sanna standing jacket angry scarf squint at t32
    call init_snow from _call_init_snow_5
    call show_snow from _call_show_snow_6
    with flash

    Sanna "一棵……树。" with Dissolve(0.3)
    Sanna sad "..."

    sn "我感觉我的心沉了下去。" with Dissolve(0.3)
    sn "我再也忍受不了了。我想回家。"
    sn "或者干脆放弃。"
    nvl clear   
    nvl hide Dissolve(0.3)

    Sanna closed frown "..." with Dissolve(0.3)
    Sanna "No..."
    Sanna sad "不，不是这样的。"
    Sanna open frown "她不会轻易放弃的。"
    Sanna mild squint "她可能会因为这样的事情而自嘲，然后继续前进。"
    Sanna determined "I..."
    Sanna "我需要像她一样。"
    Sanna "给我你的力量，Freya."

    sn "我在暴风雪中慢慢跋涉。" with Dissolve(0.3)
    nvl clear   
    nvl hide Dissolve(0.3)

    stop music fadeout(2)

    scene black with fade
    call delete_snow from _call_delete_snow_4
    pause 2





    scene house with fade
    play music wondering

    show sanna standing pjs blanket frown at t22
    Sanna "我想我们不能再去旅行了。"
    show freya closed pout at t21
    Freya "哦。"
    Freya open "我们已经很久没谈过这个了。"
    Freya "在可预见的未来，出国是不可能的，但是……我们总是可以试着去公路旅行。"
    Sanna squint hmph "没有鸸鹋。"
    Freya grin up "哇，你还记得吗？"
    Freya smile crossed "我觉得意大利没有鸸鹋，我听说那里冬天很暖和。有点远，但我们肯定可以在陆地上做到。"
    Sanna smile open "是的，那太好了。"
    Freya pleased "或者西班牙也是。我对地中海岛屿一无所知，但船仍然存在，所以也许这也是一个选择。"
    Sanna frown "但我觉得我们再也做不到了。"
    Sanna squint concerned "我……再也受不了了。"
    Freya concerned "Sanna..."
    Sanna "我不认为……"
    Freya guilty up "不！你会好起来的！你会的！我知道！"
    Sanna sad "..."
    Freya "Sanna，你会好起来的。只是发烧。"
    Sanna "不……不是这样的。"
    Sanna open frown "I..."
    Freya surprised "我们会找到一些东西的，我会出去找些药的。你很快就会好的，Sanna！我向你保证，我们会去旅行的。我们会——"
    Sanna shout "Freya!"
    show sanna angry
    Freya closed concerned "！！"
    Freya crossed open "..."
    Sanna sad "我不记得了。"
    Sanna squint "不管我怎么努力，我都记不起他们的脸了，Freya."
    Freya crossed "谁？"
    Sanna "我的父母。"
    Sanna "我不记得它们是什么样子的。它们听起来是什么样子。"
    Sanna "……我甚至不记得他们的名字了。"

    sn "相册和日记早就被擦干净了。我的胸膛感觉被掏空了，看着我的手，感觉好像已经失去了颜色。" with Dissolve(0.3)
    sn "昨天、今天、明天，我什么都记不清了。我不知道明天是否会到来，之后会发生什么。我问自己什么时候会不再是我。"
    nvl clear   
    nvl hide Dissolve(0.3)    


    Sanna "我快晕了，芙蕾雅。我感觉好晕。" with Dissolve(0.3)
    Sanna teary "如果我再也不记得你了怎么办？"
    Freya sweat guilty up "我——"
    Freya -sweat awkward crossed "我就在这里。"
    Freya "你能感觉到我的心跳。"
    Freya "只要你愿意让我和你在一起，我就不会离开你。我也不会让你忘记我。我会永远提醒你我在这里。"
    Sanna "...hic..."
    Freya up guilty sweat "所以再等一会儿，直到我找到……什么。"
    Sanna closed sad "不，别走。"
    Freya "但是，如果我不尝试……"
    Sanna open "Freya，我只想和你共度余生。"
    Freya concerned "我不想和你一起度过最后。我想和你共度未来，Sanna."
    Sanna closed -teary frown "......"
    Sanna awkward "那么……就今天而言，让我们假装一切都很正常。"
    show sanna squint trying
    Freya "......"
    Freya crossed awkward "好吧。"



    sn "我一直不擅长假装，而Freya很擅长。" with Dissolve(0.3)
    sn "但..."
    sn "……正常甚至意味着什么？"
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
    sn "天空仍然被飘雪的云朵覆盖着，一片漆黑。我不知道一天中的时间，但肯定夜幕还没有降临。"
    sn "再次向前移动我的脚，我感觉到我的重心转移了。"
    sn "我跌跌撞撞地走进雪地。有那么一瞬间，我觉得自己仿佛淹没在四周环绕的白色中。"
    sn "我的视线一闪而过。当我强迫自己站起来，在持续的白色降水中拂去身上的雪却无济于事时，我的手臂在颤抖。"
    nvl clear 
    sn "我吸气时，胸口一阵剧痛，喉咙里似乎长出了看不见的冰柱。"
    sn "我走了多久？"
    sn "我向前推了推。在不断积雪的雪地里，我的脚踝似乎奇怪地扭伤了。如果我扭了一下，寒冷和靴子会减轻疼痛。"
    sn "雪终于变浅了。"
    sn "然而，当我环顾四周时，这里似乎什么都没有，只有一片被雪覆盖的破败的废墟。"
    nvl clear 
    sn "太多东西都消失了，我几乎说不清自己到哪里去了。"
    sn "不，如果这个地方在世界上还存在，我真的不知道我在哪里了。"
    sn "我又绊倒了。"
    sn "我的四肢因一种陌生的疲惫而颤抖。由于我找不到站立的力量，我又向前爬了几米，直到我没有力气再动了。"
    sn "现在怎么办？"
    nvl clear 
    nvl hide Dissolve(0.3)  

    Sanna "..."
    Sanna "我……闭上眼睛……"
    Sanna "…休息一会儿……"

    stop music fadeout(7)
    scene black with dissolve_scene_full
    call delete_snow from _call_delete_snow_5
    pause 5



    play music calm1

    scene house with fade

    show freya closed pout at t21
    Freya "我无法通过手套判断你的手是冷还是热。" with Dissolve(0.3)
    show sanna standing pjs awkward at t22
    Sanna "我的手总是很冷。"
    Freya smile up open "我不介意，我会温暖你的，因为我的总是温暖的。也有一句谚语。冰冷的手，温暖的心。"
    Sanna trying blush "你的心比我的温暖。"
    Freya smug crossed "没关系，我也会温暖你的心。"
    Sanna "呵呵"


    sn "她毫不犹豫地握住我的手，紧紧地抓住它。" with Dissolve(0.3)
    sn "当我看着她时，世界似乎恢复了色彩，即使只是一点点。"
    sn "一种感觉在我胸口翻腾了很长时间。一点也不疼。相反，这是一种温暖而令人安心的感觉，我默默地藏了起来。"
    sn "我觉得我不需要说出来。"
    nvl clear 
    nvl hide Dissolve(0.3) 


    Freya serious "你的脸颊有点红。" with Dissolve(0.3)
    Sanna chill "真的吗？"
    Freya "他们是。"
    Freya "也许你应该上床睡觉了。"
    Sanna mild "不，我很好。我只是……"
    Sanna "说实话，我整天躺在床上有点累。"
    Freya concerned "哦，是的……"
    Sanna trying "但我似乎感觉好多了！我想水晶确实有效。"
    Freya neutral up "我早就告诉过你，这很有效。"
    Sanna "我想是的。即使你不告诉我它是什么。"
    hide sanna
    hide freya
    with dissolve
    Freya "*cough*"
    "她突然咳嗽起来。"
    Sanna "Freya!"
    Freya "我很好！我很好。"
    Freya "没什么。只是……有点发烧。仅此而已。"
    Sanna "但是——"
    Freya "我只是需要休息一下，好吗？……我会没事的。"
    Freya "你在干什么？"
    "我把弗雷娅拉到床上，用床单盖住我们俩。"
    scene cg1 with dissolve
    Freya "不，我不想把它给你——"
    Sanna "嘘，别担心。"
    Sanna "我会给你保暖的。"
    Freya "好吧。"
    Sanna "Freya?"
    Freya "什么事？"
    Sanna "我只是想说你的名字。"
    Freya "......"
    Freya "如果我忘记了，我相信你会替我记住的。"
    Sanna "...yeah."
    Sanna "我也相信你。"


    sn "我透过房间的窗户向外看。" with Dissolve(0.3)
    sn "没什么。没有颜色，只有纯白色。"
    sn "没有颜色。"
    sn "我想知道其他躲在家里的家庭。"
    sn "挣扎着，试图度过这场风暴。不知道它什么时候会亮，如果有的话。"
    sn "他们是不是想留住这些日常平凡的珍贵时刻？"
    nvl clear 
    sn "还是只有我一个人，拼命地试图把自己团结起来。保持原样。"
    sn "日子模糊了。"
    sn "我被困在这里多久了？五周？两年？"
    sn "我不知道。一想到它，我就害怕。"
    sn "但弗雷娅一直都在这里。"
    sn "只要她和我在一起……"
    nvl clear 
    sn "我真的不介意别的。"
    nvl clear 
    nvl hide Dissolve(0.3) 

    stop music fadeout(2)
    scene black with fade

    pause 6




    play music ArtificialAntartica
    scene white
    Sanna "*喘息*"

    sn "我嘶哑地咳嗽出肺里的雪。" with Dissolve(0.3)
    sn "它想杀了我，想钻进我的身体。"
    sn "我试图了解周围的环境。我慢慢地开始想起来。"
    sn "我倒在雪地里了。"
    nvl clear 
    sn "我还在咳嗽，挣扎着从仍压在身上的厚毯子里爬出来。"
    sn "如果我再晚一点醒来，我可能会窒息而死。"
    sn "也就是说，如果我没有先冻死的话。"
    nvl clear 
    nvl hide Dissolve(0.3) 

    show sanna standing jacket scarf squint concerned sweat at t32
    call init_snow from _call_init_snow_7
    call show_snow from _call_show_snow_8
    with flashflash

    Sanna "Ungh..." with Dissolve(0.3)
    Sanna "我必须……继续前进……"
    Sanna closed "..."

    sn "扫描地平线，几英里内有几个不同的形状。" with Dissolve(0.3)
    sn "可能是一些建筑、废墟，甚至是一个露营地。从这么远的地方很难分辨出来。"
    sn "无论如何，这意味着庇护所，所以我朝远处的阴影走去。"
    nvl clear 
    nvl hide Dissolve(0.3) 

    stop music fadeout(4)
    scene black with fade
    call delete_snow from _call_delete_snow_6
    pause 6




    play music lost
    scene house with fade

    sn "如果我闭上眼睛，我会忘记和被遗忘吗？"
    sn "雪继续飘落在外面，用白色覆盖着消失的世界。人们渐渐消失了，失去了一切，被一个不再有记忆的世界所淹没。"
    sn "今天，我也躲在房间里等着。"
    sn "Knock, knock."
    sn "门口传来熟悉的声音。"
    sn "她又来了。尽管我告诉她不要再来了，她还是每天都来这里。"
    nvl clear 
    nvl hide Dissolve(0.3) 


    scene door with dissolve
    Freya "Sanna，我给你带了些食物。还有……我还给你带了药。" with Dissolve(0.3)
    show sanna sitting blank at s43
    Sanna "我记得我告诉过你不要来这里。"
    Freya "你必须接受，好吗？"
    Freya "只要你闭上眼睛，把它……"
    Freya "假装吧。"
    Freya "一切都会好起来的。"
    Sanna "我习惯吃苦药。"
    Sanna frown "但我不会吃的。这不是药，Freya."
    Freya "如果你不接受，你就会消失。你不怕消失吗？"

    sn "那是真的。" with Dissolve(0.3)
    sn "不仅如此，我还害怕她消失。但我太胆小了，不敢打开这扇门看着她的脸。如果我这样做，我的信念就会动摇。"
    sn "她不能一直出去找那些水晶。她不能一直回到这里。她不能，对我来说不行。"
    sn "我们俩都很固执。"
    nvl clear 
    nvl hide Dissolve(0.3) 



    Sanna "即使我消失了，我也很好。" with Dissolve(0.3)
    Freya "Sanna-"
    Sanna blank "你还记得我们的特殊地方吗？"
    Freya "......"
    Sanna "我们以前玩的那个。"
    Freya "...yes."
    Sanna "它还在吗？"
    Freya "..."

    "那又是什么地方？公园？湖泊？我不记得了。我只是有一种模糊的感觉，仿佛很久以前，我们在一个地方度过了童年。"


    Sanna distraught "有时候我想知道……外面的世界，它还存在吗？是全被雪覆盖了，还是一切都消失了，只是消失了？"
    Sanna "来自世界本身，以及我们的记忆。"
    Freya "你没有错。"
    Freya "很多东西都消失了。我想和你一起去的地方，我们珍视的地方，都崩溃了，消失了。"
    Freya "但我们还在这里。我们还活着，Sanna，所以我们还不能消失。"
    Sanna "如果什么都不存在，仅仅存在就值得吗？"
    Freya "如果你还在这里，那就在这里。"
    Sanna angry "骗子。"
    Sanna "那我呢？"
    Sanna "如果你不是——"
    Sanna distraught "Freya，你从来没有害怕过，如果你走出去，就再也回不来了吗？"
    Freya "......"
    Freya "我真的没想过。"
    Sanna "毕竟，世界正在走向终结，不是吗？"
    Freya "……别这么说。"

    sn "我并不感到惊讶，也不是真的，但我还是发现自己无话可说。我只是想让她的答案不同，让她想想，因为我害怕而害怕。" with Dissolve(0.3)
    sn "如果芙蕾雅真的消失了，再也没有回来怎么办？"
    sn "我什么也说不出来。"
    sn "沉默."
    sn "我们只是吵架，什么也说不出来。我讨厌这样。"
    nvl clear 
    nvl hide Dissolve(0.3) 

    Freya "*cough*"
    Sanna "你今天要走多远才能找到任何东西？"
    Freya "没那么远。"
    Sanna "别再为那些水晶费心了。使用它们是不对的。"
    Sanna "即使我消失了，我也很好，所以……"
    Sanna "要么停止前进，要么停止归来。"
    "她喃喃自语，但我听不见。"
    Sanna "......"
    Freya "Sanna?"
    Sanna "什么？"
    Freya "...No, it's nothing."

    sn "我知道这不是什么，但我选择不去理会她的低语。" with Dissolve(0.3)
    sn "我们没有说话，只有沉默。就在一周前，这对我们俩来说还非常不合适，但我们现在在这里。"
    sn "我等着她说点什么或离开。我该说什么呢？"
    sn "我看不见她的脸，但我仍然可以想象她会沮丧地捂着嘴唇。即使世界今天消失了，即使我今天不复存在，我也不会忘记她。"
    sn "就像她说的，我们都很固执。"
    nvl clear 
    nvl hide Dissolve(0.3) 



    Freya "我把这个放在门边。" with Dissolve(0.3)
    Freya "照顾好自己，确保你吃得健康，好吗？"
    Sanna "...你也是。"
    Freya "谢谢。"
    Sanna "......"
    Sanna "Freya?"

    sn "她没有回应，因为她已经离开了。" with Dissolve(0.3)
    sn "Freya，我最珍贵的朋友，我不想让她来，但我不想她离开。"
    sn "如果我能忘记这个世界上所有的悲伤记忆，那么一切都会好起来的。但我不能。相反，我们周围的世界一点一点地崩溃了。"
    sn "我已经很久没有离开过这个家了，只能向外看，看到我们周围城镇的白色。我再也不记得雪下藏着什么了。"
    nvl clear 
    sn "也许，如果雪融化了，下面的一切都会消失。"
    sn "记忆，世界不再有记忆。它失去了细节、形式和形状"
    sn "被周围的人遗忘，忘记自己，有一天，在没有人注意到的情况下，人们也失去了个性，不再存在。"
    sn "他们去了哪里？他们是谁？他们曾经存在过吗？剩下的只有他们留下的缺口和破碎的灵魂碎片。"
    nvl clear 
    sn "那是困扰那些仍然留在后面的人的疾病。"
    sn "那也是我的。"
    sn "过了一会儿，我打开门。正如Freya所说，她把带来的东西留在了门口。我小心翼翼地把它捡起来，看到了食物和所谓的药。"
    sn "这种药呈水晶状，一种看起来很神奇的小东西。"
    sn "如此脆弱，就像我们的记忆一样。"
    nvl clear 
    sn "我不想让她出去取回这些东西，但我不能恨她把它们带给我。相反，我只是把她拒之门外，拒绝了她。"
    sn "我放下水晶。"
    sn "即使这意味着我必须消失，我也不会吃这种药。"
    sn "关上门，我回到孤独中等待。"
    nvl clear 

    scene black with fade

    sn "第二天，没有敲门声。" with Dissolve(0.3)
    sn "然后，第二天，没有敲门声。"
    sn "Freya不再回来了。"
    nvl clear 
    nvl hide Dissolve(0.3) 

    Sanna "她不会回来了。" with Dissolve(0.3)
    Sanna "是你让她离开的。"
    Sanna "她选择水晶而不是我。"
    Sanna "也许她只是不想再和你打交道了。"

    sn "外面，雪没有停。风呼啸着，就像有人在哭或尖叫。刺骨的冰雹打在窗户和屋顶上。" with Dissolve(0.3)
    sn "我看不见挡住太阳的湍流白色。"
    sn "屋里一片漆黑。我感觉到寒意正渗入我的房间，渗入我的心。我家的供暖和保温仍然很好，但我找不到温暖。"
    sn "温暖去哪儿了？我冷了。"
    nvl clear 
    sn "我担心，担心，担心。也许弗雷娅现在恨我，但如果她还在外面，如果她真的遇到了麻烦怎么办……如果发生了什么坏事怎么办？"
    sn "即使我大打出手，她也再也没有回来。"
    sn "我把自己拖到门口，那扇门通向外面的世界。我把手伸到把手上，还没来得及打开。"
    sn "门上的风、雪和冰雹砰砰作响"
    sn "外面的世界很可怕。"
    nvl clear 
    sn "我会只是等着看吗？不，这是不可接受的。即使我消失了，在这一刻，我仍然存在。我的身体仍然在呼吸、移动和记忆。"
    sn "当说未来可能根本不存在时，无所事事地思考未来是一种浪费。"
    sn "我扔掉了被称为思考的犹豫，把门打开了。"
    sn "寒意扑向我的身体。我闭上眼睛，寒风和雪直冲我的脸，在突如其来的冲击下跌跌撞撞地落在我的屁股上。"
    nvl clear 
    sn "我还没来得及出门，暴风雨就把门关上了。"
    sn "我用现在湿了的衬衫袖子擦去眼睛里的雪。我觉得自己好像被叫醒了。我是个白痴吗？"
    sn "我甚至还没换衣服。"
    nvl clear 
    sn "我慢慢地深吸一口气，冷静下来，思考下一步该怎么办。对于一个整天都在思考的人来说，我肯定会被认为很糟糕。"
    sn "我的脑海里充满了短暂的云朵，所以我再次停下来，决定出去，这次有了更多的安排。"
    sn "我在壁橱里翻找衣服：一件毛衣、一件夹克、一条合适的裤子、靴子等等。我艰难地穿上靴子，准备出门。"
    sn "我回到了内外之间的最后一扇门。"
    nvl clear 
    sn "我紧紧抓住把手，顶住风暴的力量慢慢打开门，走到外面。然后，我关上门，眯着眼睛看着雪打在我身上。"
    sn "我甚至数不清我上次离开家已经有多久了。"
    nvl clear 
    nvl hide Dissolve(0.3) 
    Sanna "再见，回家。我保证会和她一起回到你身边。"

    sn "挥手告别，我开始走，想知道我亲爱的家在我回来的时候是否还会在这里。"

    stop music fadeout(2)
    scene black with fade
    pause 2





    play music FrozenFuchsia
    scene facility
    call init_snow from _call_init_snow_8
    call show_snow from _call_show_snow_9
    with flashflash
    nvl clear 
    sn "当我走近远处看到的形状时，我意识到它们确实只是两座建筑……尽管看起来很奇怪。" with Dissolve(0.3)
    sn "它们几乎没有明显的特征，只有纯黑色的方块。"
    sn "到处都没有生命的迹象。"
    sn "我小心翼翼地在建筑内漫步，慢慢地检查周围的环境。"
    nvl clear 
    nvl hide Dissolve(0.3) 

    Sanna "某种…军事基地？" with Dissolve(0.3)

    scene infacility with fade

    sn "当我进入其中一栋建筑时，很明显我的猜测很接近，但错了。" with Dissolve(0.3)
    sn "这不是一个军事综合体，而是一个研究设施。"
    sn "除了……看起来每个人都走了。"
    sn "灯还亮着，还有暖气。"
    sn "有些看起来很奇怪的电脑仍然在运行。"
    sn "监视器显示我并不真正理解的数据图表。"
    nvl clear 
    nvl hide Dissolve(0.3)


    sn "各种研究论文散落一地，仿佛有人一直在疯狂地寻找什么。" with Dissolve(0.3)
    sn "我又走了一会儿，偶然发现了一个外观奇特的房间。"
    sn "这是一个完全被玻璃包围的房间，很容易从外面看到监视器。"
    sn "房间里的东西空空如也，除了一张桌子和一个类似托盘的东西。"
    sn "很明显，它应该有一些东西，但现在它不见了。"
    nvl clear 
    sn "后来我才意识到房间的另一边有个洞，玻璃碎了。"
    sn "有人来到这里，拿走了这个地方的一切。"
    sn "他们不应该拿走的东西。"
    nvl clear 
    sn "一切都有点不合时宜，突然间，我似乎不应该在这里。"
    sn "我想尽快离开。"
    sn "我走出建筑群后深吸了一口气。"
    nvl clear 
    nvl hide Dissolve(0.3) 

    Sanna "Freya... 你在哪里？" with Dissolve(0.3)

    sn "似乎只剩下一个地方可以检查了。" with Dissolve(0.3)
    sn "我又深吸了一口气，试图稳定我的精神状态。"
    sn "然后我朝另一栋楼走去。"
    nvl clear 
    nvl hide Dissolve(0.3) 


    stop music fadeout(2)
    scene black with fade
    call delete_snow from _call_delete_snow_7
    pause 2




    scene house with fade

    show Rfreya concerned at t41
    Freya "......"
    Freya "(我还能坚持多久……？)"
    show sanna standing pjs at t44
    Sanna "继续什么？"
    hide Rfreya
    show freya sweat up guilty at t41
    Freya "...!?"

    play music goodbye

    Sanna "……你不能告诉我什么？"
    Freya concerned crossed "......"
    Sanna sad "这和我有关吗？"
    Freya "这和你无关。"

    Sanna angry "弗雷娅，你撒谎不好。我一直都能看出。"

    Freya up guilty "如果我说了，连你都不会相信我……啊，这次我真的搞砸了，不是吗？"
    show freya awkward
    Sanna "所以这很重要。"
    Sanna determined "跟我有关？这种病？你给我带的药……？"
    Freya crossed concerned "......"
    Sanna concerned "最后一个，嗯？"
    Sanna "是的，看来我的第三个猜测是正确的。"
    Freya awkward up "我有什么办法可以说服你不要再挖了吗？"
    Sanna angry "不，我想问你，你一直在瞒着我什么，芙蕾雅。你给我带的水晶是什么？"
    Freya serious -sweat up "它们是药。"
    Sanna "超越这一点。"
    Freya crossed "他们只是……"
    Freya closed concerned "……这很复杂。"
    Sanna "告诉我。"
    "她深深地叹了一口气。"
    Freya up serious open "它们是人们消失后留下的东西。"
    Freya "这是它们剩下的精华，在适当的条件下，一段时间后最终凝结成晶体。"
    Freya "我自己也不太明白，但是……"
    Freya crossed "这就像……某人的一部分。他们的记忆。他们的肤色。"
    Sanna frown squint "什么？"
    Sanna "我一直……"

    sn "我觉得不舒服。我胸口一阵起伏的感觉让我恶心。" with Dissolve(0.3)
    sn "我觉得不舒服，不是因为我真的对吃那种药感到恶心，而是因为我没有像我想象的那么恶心。"
    sn "弗雷娅在这么重要的事情上骗了我，我感到很空虚。我知道我可能仍然可以原谅她，我感到空虚。"
    nvl clear 
    nvl hide Dissolve(0.3) 



    Sanna open "我一直在吃什么？" with Dissolve(0.3)
    Sanna angry "你为什么不告诉我？"
    Freya guilty up "我……我知道如果你知道真相，你就不会接受它们。"
    Sanna "你从一开始就知道吗？"
    Freya crossed serious "不，后来有人告诉我的。"
    Sanna "那是个谎言。"
    Sanna sad teary "别再出去找它们了，芙蕾雅。我再也不拿水晶了。"
    Freya concerned "...Sanna..."



    sn "我不明白..." with Dissolve(0.3)
    sn "每天和她在一起，我感到如此自满和快乐，确信奇迹已经到来，阻止了我的恶化，我一直如此盲目。"
    sn "她在我眼中的形象变得模糊了。"
    sn "什么时候泪水夺眶而出？我真的是个爱哭的孩子，我想，我的肩膀因为无法表达的痛苦而颤抖。"
    sn "她伸手去擦我的眼泪，但我后退了一步。"
    nvl clear 
    sn "我不停地揉着眼睛，最后一次试着看着她的眼睛。我觉得自己好像在看着一个陌生人。"
    sn "世界消失了。我慢慢地开始崩溃。我们认识的地方，我们遇到的人，我们留下的记忆，都早已消散。"
    sn "它们变得像外面的雪一样洁白，如此美丽，以至于我几乎可以不假思索地拥抱它，忘记一切。"
    sn "除了这是一件痛苦的事情，就像雪一样寒冷和令人窒息。"
    nvl clear 
    sn "不知不觉，我们之间珍贵的纽带已经磨损，变成了我不再认识的东西，好像它也想消失。"
    sn "我不想那样。"
    sn "我不想失去她。"
    nvl clear 
    nvl hide Dissolve(0.3) 

    show sanna crying squint sad
    Sanna "我觉得你应该走了。" with Dissolve(0.3)
    Freya up concerned "......"
    Freya crossed sweat closed "......"
    window hide
    hide freya with dissolve
    pause 2
    scene black with fade



    sn "因此，我现在独自一人。" with Dissolve(0.3)
    sn "就在我回忆过去的时候，当我睁开眼睛时，她不在这里。当然她不在。是我把她赶走的。"
    sn "她每天都来敲我的门。我拒绝为她开门；我把她拒之门外。"
    sn "我朝窗外望去，发现雪又开始下了。"
    sn "天空变暗了。当我去准备食物和吃饭时，我忍不住觉得一切都毫无味道。"
    nvl clear 
    sn "不浓，不淡，不平淡或恶心，只是尝起来什么都没有。"
    sn "饭后，我吞下了一些干药丸。维生素、补充剂，这些也不是药。我不喜欢药片的苦味。"
    sn "最后，药是苦的，不是吗？如果不是味道，那就是本质。"
    sn "在一切崩溃之前，我的思绪一直在徘徊，但回忆起来是如此困难，仿佛我的过去已经化为乌有。"
    nvl clear
    sn "这种病总有一天会吞噬我的。"
    sn "我应该让它更快地吞噬我吗？"
    sn "雪越下越大，直到我透过窗户的白色面纱看不见了。"
    sn "我想知道芙蕾雅是否还好，她是否在外面，即使暴风雪肆虐。我甚至对家外的一切都一无所知。"
    sn "我感觉自己像笼子里的一只鸟，或者可能是被别人部分撕开的蛹中的毛毛虫。"
    nvl clear    
    sn "我无法飞翔，无法挣扎，被困在自己做的一个难以形容的壳里。也许我就像一条虫子，一开始就不可能变成蝴蝶。"
    sn "外面的世界很可怕。如果那里已经什么都没有了怎么办？"
    sn "今天我也在里面等着。"
    sn "我等着。"
    nvl clear 
    nvl hide Dissolve(0.3) 

    stop music fadeout(4)
    pause 6




    scene facility
    call init_snow from _call_init_snow_9
    call show_snow from _call_show_snow_10
    with fade


    sn "黑色立方体状建筑与旁边的另一座建筑完全相同。" with Dissolve(0.3)
    sn "然而，从内部来看，情况不会有什么不同。"
    nvl clear 
    nvl hide Dissolve(0.3) 

    play music funk

    scene crystals with fade
    call delete_snow from _call_delete_snow_8
    sn "墙壁、地板、天花板都覆盖着熟悉的晶体物质。" with Dissolve(0.3)
    sn "它就像一种生长，到处流动，消耗，吃掉它所触及的一切。"
    sn "它无处不在，填满了它能找到的每一个孔口。覆盖了它能看到的每一表面。"
    sn "当我试图穿过地面形成的各种水晶结构时，锯齿状和锋利的边缘有可能被切割和撕裂。"
    nvl clear 
    sn "在房间的中央，有一个人影躺在地上。"
    nvl clear 
    nvl hide Dissolve(0.3) 

    show sanna running scarf gasp teary at t32
    Sanna "Freya!" with Dissolve(0.3)
    hide sanna with dissolve

    sn "我跑过去跪在她身上。" with Dissolve(0.3)
    sn "她转过身来面对我。"
    sn "她说话了。她的嘴唇动了动，但我听不见她的声音。当然，我的耳朵没有碎。她的声音我听不到。为什么我听不清她？"
    sn "我摇摇晃晃地靠近她。"
    sn "……她脸上的表情太……"
    sn "痛苦."
    nvl clear
    sn "我第一次注意到她也在逐渐消失。这是什么时候开始的？这样的事情不会马上发生在一个人身上。"
    sn "她把手放在我的脸颊上。她在对我说什么。我无法通过手套感受到她的手的温暖。"
    sn "然后她吻了我的嘴唇。"
    nvl clear
    sn "显然，初吻尝起来像希望一样甜蜜，但我能感觉到的只有酸涩和苦涩。"
    sn "持续时间太短的吻结束了。她挣脱了我，对我说，或者只是用嘴说，‘我爱你’这句珍贵的话。"
    sn "爱，她所说的爱和我内心所持有的爱是一样的。"
    nvl clear 
    nvl hide Dissolve(0.3) 


    Sanna "……等我们和好了再告诉我……等我能正确地告诉你我的感受和你的一样。" with Dissolve(0.3)
    Sanna "你为什么也渐渐消失了？"
    Freya "(我想就连我也不能幸免。)"
    Sanna "......"
    Freya "(对不起。我从来没有机会道歉。)"
    Freya "(我不该骗你。)"
    Freya "(我看得出来你想说没关系。)"
    Freya "(我只是……想把事情做好。即使我做得不对。.)"
    Freya "(对不起，Sanna。我不会再这样做了，我不会再辜负你的信任了。)"
    Freya "(……即使不是在今生，也不是在这个世界上。)"
    Freya "(在我们剩下的时间里，以及在一切消失后我们是否还能再见面。)"
    Sanna "我听不见你的声音。"
    Sanna "别看起来好像要消失了！"
    Sanna "别……别这样对我……"


    sn "尽管我知道她在说话，而且莫名其妙地能说出她说的话，但我还是听不见她的声音。" with Dissolve(0.3)
    sn "我仍然记得。我仍然记得她存在，她对我来说是如此重要。我没有忘记她，所以她还没有消失。"
    sn "她的名字？当然是——"
    sn "我的思绪停滞不前。她对我来说是一个非常重要的人。我想再喊一次她的名字，告诉她，如果她自己忘记了，我会替她记住她的。"
    sn "我答应过。她要求我这么做。"
    nvl clear 
    sn "我紧紧地抱住她，我的声音无法从喉咙里传出。她也拥抱了我。她的拥抱非常坚定，非常坚定。她还在那里。"
    sn "然后，我意识到我也在消散。"
    sn "我感觉到她在我耳边低语，我听不见。她紧紧地抓着我，几乎疼得要命，好像她也担心我会消失。"
    nvl clear 
    sn "她的名字、她的存在、她的一切，我怎么能忘记呢？"
    sn "现在不行，我还不会让她走的。"
    sn "即使世界想带走她，也必须同时带走我们俩。我们彼此承诺，我们会永远记住对方。"
    nvl clear 
    nvl hide Dissolve(0.3) 



    Sanna "Freya!" with Dissolve(0.3)
    Sanna "You're Freya!"
    Sanna "你不能……消失。"
    Sanna "你不能……你——"
    Freya "Sanna-"

    sn "我的视力模糊。" with Dissolve(0.3)
    sn "我终于听到了她的声音。"
    sn "那一刻，我的意识崩溃了，一切都变得黑暗起来。"
    nvl clear 


    stop music
    scene black


    pause 6




    sn "我醒来时看到了一个熟悉的天花板。有那么一瞬间，我怀疑自己是否真的冲进了一场暴风雪，在看似世界边缘的地方与Freya重聚。" with Dissolve(0.3)
    sn "感觉不真实。只是发烧梦或幻觉的碎片。"
    sn "我担心我只是梦到发生了什么，她走了。"
    sn "惊恐地坐起来环顾四周，我如释重负。很快，我又睡着了。我的疲惫终于袭来。"
    nvl clear 
    nvl hide Dissolve(0.3) 

    pause 6

    play music calm1
    Freya "Achoo!" with Dissolve(0.3)
    scene cg2 with fade
    Freya "生病很糟糕。"
    Sanna "你很幸运，你只是‘生病了’。我真的不知道你是怎么把我们拖回家的。"
    Freya "难道没有什么能让我在短时间内变得健康吗？"
    Sanna "我想药柜里还有感冒药。"
    Freya "樱桃味的糖浆？"
    Sanna "不，我想……这是蜂蜜柠檬味的，尝起来像肥料。"
    Freya "我说我不想吃这些，可以吗？"
    Sanna "Pfft."
    Sanna "当然。如果只是感冒，那么对抗感冒本身比从一开始就依靠药物更健康。"
    Freya "Alas."
    Freya "说到医学，晶体已经消失了，不是吗？"
    Sanna "是的，他们做到了。"
    Freya "太快了。好吧，反正我在这里找不到更多的东西了。我肩上的负担真奇怪。"
    Sanna "……如果你发现更多，你应该把它们拿走。"
    Freya "Hm?"
    Sanna "……这可能是我的虚伪，但是……如果我消失了，留下一个，我希望你能继续活下去，所以……"
    Freya "天哪，别这么说。"
    Freya "这并不是说我没有同样的感觉。如果我在你之前消失了，我希望你也能继续活下去。"
    Freya "我不打算再主动去寻找水晶了。"
    Freya "至于如果我们偶然发现一个，会发生什么，好吧，我想我们到那里后可以讨论一下。"
    Sanna "是的。"
    Sanna "只有一件事。你不能在我面前消失。"
    Freya "这难道不公平吗？"
    Sanna "不。"
    Freya "好吧，那我们俩都不能先走。听起来不错，不是吗？"
    "我点点头。"
    Freya "那么，你能再告诉我一次你爱我吗？"
    Sanna "嗯，我爱你。"
    Freya "Hehe."
    Sanna "以一种浪漫的方式。"
    Freya "我不知道你是否说过你喜欢我什么，你能告诉我吗？"
    Sanna "我喜欢你善良和关心的方式，你有时很愚蠢，但最终会克服困难。我喜欢你即使在我沮丧的时候也能保持积极的态度。"
    Sanna "你很温暖。我喜欢你牵着我的手。你在我身边的时候，我总是感觉很舒服。"
    Sanna "也许这听起来很奇怪，但我喜欢你的音色。"
    Sanna "我也喜欢你的力量和诚实的认真，即使你犯了错误。"
    Sanna "我非常爱你，因为你就是你。我真希望我早点告诉你，所以也许我也很高兴你是第一个忏悔的人。"
    Sanna "你喜欢我什么？"
    Freya "我喜欢你的一切。"
    Freya "你漂亮的绿眼睛，丝滑的头发，你微笑的样子，你笑的样子，稍微凉爽的体温，还有你精致的手指。"
    Freya "你固执的行为，你对食物有点挑剔，你高兴的时候眼睛会亮起来，你难过的时候会依赖我。"
    Freya "我自然可以继续下去。我已经爱你很久了。虽然我最近学到了一些我喜欢你的新东西。"
    "她飞快地吻了我一下嘴唇。"
    Freya "你嘴唇的柔软味道。"
    Sanna "Y-you tease!"
    Freya "我也爱你。"
    "我开玩笑地用枕头拍打她，然后尴尬地把脸埋在枕头里几秒钟。"
    stop music fadeout(2)
    Freya "从现在开始我们该怎么办？"
    play music ending
    Sanna "让我们继续我们一直在谈论的旅行吧。"
    Freya "去哪里？"
    Sanna "我认为我们不需要目的地。我们永远无法决定，所以也许我们最好还是出发，去我们内心告诉我们的地方。"
    Freya "旅行，对吧？照目前的情况，唯一的选择就是公路旅行。"
    Freya "雪会融化的，道路可以继续行驶。是的，我认为这是个好主意。一旦天气好转，我们就可以出发了。"
    Freya "在那之前，我想我们必须做好准备，让自己做好准备。"
    Sanna "你会开车吗？"
    Freya "从法律上讲……"
    Sanna "Illegally speaking?"
    Freya "我没有驾照，但我骑摩托车很好。"
    Freya "家里的车库里应该有一辆。这辆边车足够大，可以存放相当多的物资。"
    Sanna "我喜欢这个主意。骑摩托车公路旅行。"
    Freya "对吧？听起来很有趣，不是吗？"
    Sanna "是的，确实如此。"

    scene black with fade
    pause 1
    scene cg3 with Dissolve(3)
    pause 5

    sn "说到旅行，我们总是这样做，但实际上去旅行，我们还没有这样做。" with Dissolve(0.3)
    sn "如果我们谈论明天，那些在下一个今天之后可能不再存在的稀缺的明天，我们想一起度过明天。"
    sn "与其永远躲在里面，不如一起出去看看世界上剩下的东西，这是结束它的更好方式。"
    sn "尽管所有这些都消失了，但还有更多的东西有待观察。"
    nvl clear 
    sn "春天来了，路都融化了。我们还在这里。因此，在那次公路旅行中，我们去了。"
    sn "就像我们长期以来的遗愿清单上的一项被划掉一样，我们走过了在苍白的天空下坍塌的道路。"
    sn "她向我展示了这个世界上所有美丽的东西。"
    sn "最终我们俩都会消失。就像春天融化的雪一样，我们不会留下足迹，也不会在这里。"
    nvl clear 
    sn "然而，我们在彼此心中留下的印象不会被抹去。"
    sn "世界失去了色彩，回到了一张纯白的画布上。她和我继续在我们短暂而珍贵的生命中，在虽小但充实的旅程中前进。"
    sn "当我闭上眼睛时，我只是想起了她，被人记住了。"
    nvl clear 
    nvl hide Dissolve(0.3) 
    pause 1

    scene cg4 with Dissolve(3)
    pause 8
    stop music fadeout(3)
    scene black with Dissolve(3)
    pause 6
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
