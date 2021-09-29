import time, sys, os 

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    LIGHTMAGENTA = '\033[95m'


print(bcolors.OKBLUE + '====================================== CODENATION ============================================' + bcolors.ENDC)
print(bcolors.OKBLUE + '██████████  ██████████  ██████████  ██      ██' + bcolors.ENDC, bcolors.WARNING + ' ██████████  ██████████  ██      ██  ████████' + bcolors.ENDC)
print(bcolors.OKBLUE + '    ██      ██          ██      ██  ████  ████' + bcolors.ENDC, bcolors.WARNING + '         ██  ██      ██  ██      ██  ██      ██' + bcolors.ENDC)
print(bcolors.OKBLUE + '    ██      ██████████  ██████████  ██  ██  ██' + bcolors.ENDC, bcolors.WARNING + '     ██████  ██      ██  ██      ██  ████████' + bcolors.ENDC)
print(bcolors.OKBLUE + '    ██      ██          ██      ██  ██      ██' + bcolors.ENDC, bcolors.WARNING + '         ██  ██      ██  ██      ██  ██      ██' + bcolors.ENDC)
print(bcolors.OKBLUE + '    ██      ██████████  ██      ██  ██      ██' + bcolors.ENDC, bcolors.WARNING + '         ██  ██████████  ██████████  ██      ██' + bcolors.ENDC)
print(bcolors.OKBLUE + '====================================== CODENATION ============================================' + bcolors.ENDC)
print(bcolors.FAIL + '                          ╔══════════════════════════════════╗' + bcolors.ENDC)
print(bcolors.FAIL + '                          ║   By: Lou, Richard and Stephen   ║' + bcolors.ENDC)
print(bcolors.FAIL + '                          ╚══════════════════════════════════╝' + bcolors.ENDC)
print(bcolors.FAIL + '                                  A life less ordinary' + bcolors.ENDC)


def start_game():
    print("Welcome, \n")
    time.sleep(1)
    print("to the weird and the wonderful. \n")
    time.sleep(1)
    print("Be ready to take a trip into the mouth of madness...\n")
    time.sleep(1.5)
    print("The twilight zone...\n")
    time.sleep(1.5)    
    print(". . . \n")
    time.sleep(1.5)
    print("Get on with the bloody story!\n")
    time.sleep(1.5)
    print("We dont have all day, dude!\n")
    time.sleep(1.5)
    print("Coughs, alright okay\n")
    print("They don't pay me enough for this... \n")
    time.sleep(1.5)
    print("Okay, its time to play the game!\n")
    time.sleep(1.5)
    print("ᶦ ᵈᵉᶠᶠᵒ ⁿᵉᵉᵈ ᵗᵒ ˢᵖᵉᵃᵏ ᵗᵒ ᵐʸ ᵃᵍᵉⁿᵗ\n")
    time.sleep(1.5)
    print(bcolors.OKBLUE + '                                           _..' + bcolors.ENDC)
    print(bcolors.OKBLUE + "                          /}_{\           /.-" + bcolors.ENDC)
    print(bcolors.OKBLUE + '                         ( a a )-.___...--/."' + bcolors.ENDC)
    print(bcolors.OKBLUE + '                         ==._.==         ;' + bcolors.ENDC)
    print(bcolors.OKBLUE + "                         /  /   / /, | | |" + bcolors.ENDC)
    print(bcolors.OKBLUE + '                        {_;/   {_//    MEOW' + bcolors.ENDC)
    print("\n")
    time.sleep(1.5)
    wake_up()


def wake_up():
    global name 
    print("𝗯𝗲𝗲𝗽. 𝗯𝗲𝗲𝗽. 𝗯𝗲ep. beep. beep. \n")
    time.sleep(2)
    print("it's morning.\n")                  
    time.sleep(1.5)
    print("birds are singing 𝅘𝅥𝅮 𝅘𝅥 𝅘𝅥𝅮 \n")
    time.sleep(1.5)
    print("i think they're taunting you . . . \n")
    time.sleep(1.5)
    print("but the day is waiting! =^v^= \n")
    time.sleep(2)
    name = input("what is your name? \n")
    time.sleep(1.5)
    print(f"good morning, {name}! \n") 
    time.sleep(2)
    sleep()
        

        
def sleep():     
    sleep_ans = input("did you sleep well? \n yes / no \n ")
    time.sleep(1.5)
    if sleep_ans.upper() == "Y" or sleep_ans.upper() == "YES":                        
        print("that's great to hear! \n") 
        time.sleep(1.5)
        print("i wish i could say it showed. :) \n")  
        time.sleep(1.5) 
        check_food()    
    elif sleep_ans.upper() == "N" or sleep_ans.upper() == "NO":
        print("haha! oh, you.\n")
        time.sleep(1.5)
        print("it shows :) \n")
        time.sleep(1.5)
        check_food()
    else: 
        print("let's try that again... \n")
        time.sleep(5)
        sleep()


    # # # #

def check_food():
    check_fd = input(f"{name}, your stomach is growling. do you think it's time to get up? \n yes / no \n")
    time.sleep(1.5)
    if check_fd.upper() == "Y" or check_fd.upper() == "YES":
        print("nice! up and at 'em!\n")   
        time.sleep(1.5)
        mirror() 
    elif check_fd.upper() == "N" or check_fd.upper() == "NO":
            print("are you sure? i really think it's time to check the kitchen....\n")
            time.sleep(1.5)
            check_food()
    # keep looping "are you sure?" until user says yes
    else: 
        print("are you understanding me? \n")
        time.sleep(1.5)
        check_food()


# Add ascii after every section
    # # # #


def mirror():
    print("you slither out of bed.\n")
    time.sleep(1)
    print("ah, yes.\n")
    time.sleep(1)
    print("there's that shiny glass panel, leant on the wall..... \n")
    time.sleep(1.5)
    mirror_ans = input("you can look if you want....? \n yes / no \n")
    if mirror_ans.upper() == "Y" or mirror_ans.upper() == "YES":
        print("you look in the mirror....\n")
        time.sleep(1.5)
        print("thankfully, everything looks as normal.\n")
        time.sleep(1.5)
        print("you begin cleaning your ear with your paw\n")
        time.sleep(1.5)
        window1()

    elif mirror_ans.upper() == "NO" or mirror_ans.upper() == "N":     
        print("not this time...\n")
        time.sleep(1.5)
        window1()
    else:
        print("what were we talking about?\n")
        time.sleep(1.5)
        mirror()

    # # # #


def window1():
    print(bcolors.OKBLUE + "     /|_______/|" + bcolors.ENDC)
    print(bcolors.OKBLUE + "    /  o   o   |" + bcolors.ENDC)
    print(bcolors.OKBLUE + "   ( ==  ^  == )" + bcolors.ENDC)
    print(bcolors.OKBLUE + "    )         (" + bcolors.ENDC)
    print(bcolors.OKBLUE + "   (           )" + bcolors.ENDC)
    print(bcolors.OKBLUE + "  ( (  )   (  ) )" + bcolors.ENDC)
    print(bcolors.OKBLUE + " (__(__)---(__)__) \n" + bcolors.ENDC)
    print("after scratching at the walls for a while, you wander over to the window. \n")
    time.sleep(1.5)
    print("sleepily, you nudge open the curtains to see…\n")
    time.sleep(1.5)
    print(". . . \n")
    time.sleep(1.5)
    print("fire \n")
    time.sleep(1.5)
    print("so much fire \n")                
    time.sleep(2)
    print("it's covering the horizon \n")    
    time.sleep(2)
    print("it's engulfing everything \n")       
    time.sleep(2)
    print("is this the end of the world? \n")      
    time.sleep(2)
    print("your whiskers are tingling . . .\n") 
    time.sleep(2)
    print("is that next door's dog? poor lil thing is on fire! \n")              
    time.sleep(2)
    print("  . \n")                                 
    time.sleep(1)
    print("  . \n")                                
    time.sleep(1)
    print("  . \n")   
    time.sleep(1)                                
    window2()


    ## ascii art!

    # # # #


def window2():
    print("you stand and ponder for a while, before.... \n")
    time.sleep(1.)
    print(" . . . \n")
    time.sleep(1.5)
    window2_ans = input("...going to investigate? \n yes / no \n")
    time.sleep(1.5)
    if window2_ans.upper() == "Y" or window2_ans.upper() == "YES":   
        print("why would you do that? \n") 
        time.sleep(1.5)
        print("are you crazy? \n")
        time.sleep(1.5)
        print(f"you think you, {name}, can take on an apocalypse....? \n")
        time.sleep(1.5)
        print("well, if you insist.... \n")
        time.sleep(1.5)
        print("you leave to take a closer look \n")
        time.sleep(1.5)
        print("you see things you can't unsee \n")
        time.sleep(1.5)
        print("why did you think your little cat head could cope with this? \n")
        time.sleep(1.5)
        
        print("ah, well. \n")
        time.sleep(1.5)
        print("let's stop nosying. \n")
        time.sleep(0.5)
        print("  . \n")      
        time.sleep(0.5)
        print("  . \n")     
        time.sleep(0.5)
        print("  . \n")      
        time.sleep(0.5)
        breakfast()
    elif window2_ans.upper() == "NO" or window2_ans.upper() == "N":
        print(f"that's okay, {name}! we don't have to go outside today. \n")
        time.sleep(1.5)
        breakfast()
    else:
        print("\n are we speaking the same language? \n")
        time.sleep(1.5) 
        print("try again \n")
        time.sleep(1.5)
        window2()

    # # # #

 
def breakfast():
    print("anyway . . . \n")
    time.sleep(1.5) 
    print("you made it to the kitchen! \n go you. ")
    time.sleep(1.5)
    print("time for breakfast, what would you like to have?  \n")
    time.sleep(1.5) 
    print("choose a number between 1 and 3!\n")
    #
    breakfast_ans = int(input())
    if breakfast_ans == 1:
        print("would you look at that! we're having milk and biscuits \n")
        time.sleep(1.5) 
        tv()
    elif breakfast_ans == 2:
        print("you're having lasagne. nice \n")
        time.sleep(1.5) 
        tv()
    elif breakfast_ans == 3:
        print("today, you're enjoying the leftovers on the kitchen side \n")
        time.sleep(1.5)
        tv()
    else: 
        print("close! \n")
        time.sleep(1.5)
        print("so close \n")
        time.sleep(1.5)
        print(f"but, {name}...\n")
        time.sleep(1.5)
        print("that wasn't a number between 1 and 3. \n") 
        time.sleep(1.5)
        breakfast()



    # # # #


def tv():
    print("what a lovely breakfast! \n")
    time.sleep(1.5)
    print("nice and filling \n")
    time.sleep(1.5) 
    print("so... how do you want to spend your morning? \n")
    time.sleep(1.5) 
    tv_ans = input("fancy sitting down to watch some tv? \n yes / no \n ")
    if tv_ans.upper() == "YES" or tv_ans.upper() == "Y":
        print("you stretch out on the sofa and change the channel to the news \n")
        time.sleep(2) 
        print(". . . \n")
        time.sleep(3) 
        print("the news is showing some unsettling things... \n")
        time.sleep(1.5)
        tv2()
    elif tv_ans.upper() == "NO" or tv_ans.upper() == "N":
        print("of course.\n")
        time.sleep(1.5) 
        print("maybe tomorrow! \n")
        time.sleep(1.5) 
        print("...would you look at the time!\n")
        time.sleep(1.5) 
        door_noise()
    else:
        print("let's try that again... \n")
        time.sleep(1.5)
        tv()
            

    # # # #


def tv2():
    tv2_ans = input("turn off the tv? \n yes / no \n")
    if tv2_ans.upper() == "YES" or tv2_ans.upper() == "Y":
        print("good idea. \n")
        time.sleep(1.5) 
        print("many things are happening.... \n")
        time.sleep(1.5) 
        print(". . . \n")
        time.sleep(1.5) 
        print("can you smell tuna? \n")
        time.sleep(1.5)
        door_noise()
    elif tv2_ans.upper() == "NO" or tv2_ans.upper() == "N":
        print("come on now \n")
        time.sleep(1.5) 
        print("why are you subjecting yourself to this? \n")          
        time.sleep(1.5) 
        print(". . .\n")
        time.sleep(1.5) 
        print("it's time for bed. \n")
        time.sleep(1.5)
        print(" . . .  \n")
        rint("maybe after some sleep, \n ")
        time.sleep(1.5)
        print("you'll do better tomorrow \n")
        time.sleep(2)
        wake_up()
    else: 
        print("i didn't catch that... \n")
        time.sleep(1.5)
        tv2()


    # # # # ascii 


def door_noise():
    print("let's do something fun before lunch :) what shall we- \n") 
    time.sleep(1) 
    print("! ! ! \n")
    time.sleep(2) 
    print("....there's a noise outside the front door... \n")
    time.sleep(1.5) 
    print(". . . \n")
    door_noise_ans = input("let's take a look...? \n yes / no \n")
    if door_noise_ans.upper() == "YES" or door_noise_ans.upper() == "Y":
        print("very bold of you. \n")
        time.sleep(1.5)
        print("i don't think you're big enough to take on what's out there \n")
        time.sleep(1.5)
        print("but okay! \n")
        time.sleep(1.5)
        outdoor()
    elif door_noise_ans.upper() == "NO" or door_noise_ans.upper() == "N":
        print("safety first! \n")
        time.sleep(1.5) 
        indoor()
    else: 
        print("try answering that again \n")
        time.sleep(1.5) 
        print("you were mumbling a bit, there \n")
        time.sleep(1.5) 
        door_noise()




    # # # #


        #  if leave

def outdoor():
    print(". . . ")
    time.sleep(1.5)
    print("after a swift amazon same-day delivery, \n")
    time.sleep(1.5)
    print("you venture out, dressed in your brand new shiny knight's armour \n")
    time.sleep(1.5)
    print("which was a bargain \n")
    time.sleep(1.5)
    print("and arrived in great condition, too \n")
    time.sleep(1.5)
    print(bcolors.LIGHTMAGENTA + """ _,.
     ,` -.)
    ( _/-\\-._
   /,|`--._,-^|            ,
   \_| |`-._/||          ,'|
     |  `-, / |         /  /
     |     || |        /  /
      `r-._||/   __   /  /
  __,-<_     )`-/  `./  /
 '  \   `---'   \   /  /
     |   ^__^    |./  /
     /  (o  o)   |/  /
 \_/' \  =\/=   |/  /
  |    |   _,^-'/  /
  |    , ``  (\/  /_
   \,.->._    \X-=/^
   (  /   `-._//^`
    `Y-.____(__}
     |     {__)
           ()""" + bcolors.ENDC)    
    time.sleep(1.5)
    print(" . . . \n")
    time.sleep(1.5)
    print("not 5 steps from the front door, \n")
    time.sleep(1.5)
    being()



                    

def being():                     
    print("you encounter a huge, unknown, terrifying being \n")
    time.sleep(1.5) 
    print("it's at least twenty times your size and probably posesses god-like powers \n")
    time.sleep(1.5) 
    being_ans = input("do you want to take the being on? \n yes / no \n")
    if being_ans.upper() == "YES" or being_ans.upper() == "Y":  
        print("that's not very smart of you. \n")
        time.sleep(1.5) 
        print("you are a cat. \n")
        time.sleep(2) 
        print("you seem to have no regard for your own safety \n")
        time.sleep(1.5) 
        print("  . \n")     
        time.sleep(1.5) 
        print("  . \n")     
        time.sleep(1.5) 
        print("  . \n")      
        time.sleep(2) 
        print("you initiate a fight with the unnamed being. \n")
        time.sleep(3) 
        print("unsurprisingly, it wins. \n")
        time.sleep(2) 
        print("you die. \n")
        time.sleep(2) 
        print("END OF GAME \n")
        time.sleep(3)
        print("maybe after some sleep, \n ")
        time.sleep(1.5)
        print("you'll do better tomorrow . . . \n")
        restart()

    elif being_ans.upper() == "NO" or being_ans.upper() == "N": 
        print("i think that's a smart move. \n")
        time.sleep(1.5) 
        print("don't take this the wrong way, \n")
        time.sleep(1.5) 
        print("but i didn't think you'd win anyway. \n") 
        time.sleep(1.5)
        back_home()
    else:   
        print("that's not an option, sorry \n")
        time.sleep(1.5) 
        print("try again?\n")
        time.sleep(1.5)
        being()
        
    # # # #



def back_home():
    back_home_ans = input("go back home? \n yes / no \n")
    if back_home_ans.upper() == "YES" or back_home_ans.upper() == "Y": 
        print("yes, thank you.... \n")
        time.sleep(1.5)
        print("i don't like it out here, \n")
        time.sleep(1.5) 
        print("i think that's enough of the outside for today. \n") 
        time.sleep(1.5) 
        indoor() 

    elif back_home_ans.upper() == "NO" or back_home_ans.upper() == "N":
        print("this is ridiculous... \n")
        time.sleep(2) 
        print("i see you have chosen death...\n")
        time.sleep(1.5) 
        print(". . .\n")
        time.sleep(1.5) 
        print("you patter onwards, almost unphased by today's terrors\n")
        time.sleep(1.5) 
        print("it might be worth looking into seeing a therapist...\n")
        time.sleep(2) 
        print(" . . .\n ")
        time.sleep(1.5) 
        print("soon enough, again,\n")
        time.sleep(1.5) 
        being()
    else:
        print("try again... \n")
        time.sleep(1.5)
        print("you can do it! \n")
        time.sleep(1.5)
        back_home()
  

        # # # # 

        # if stay indoors

def indoor():                        
    print(". . .") 
    time.sleep(1.5)  
    print("you go back to the kitchen \n")
    time.sleep(1.5)
    print("and open the fridge\n")
    time.sleep(1.5)
    print("taking out your fav milk, you take a gulp \n")
    time.sleep(1.5)
    print("thinking to yourself, oooh it'll be one of those days \n")
    time.sleep(1.5)
    print(". . .")
    time.sleep(1.5)
    print("was that... a noise at the door again? \n")
    time.sleep(1.5)
    print("last time we looked... it was scary....\n")
    time.sleep(1.5)
    indoor_ans = input("do you want to check the front door? \n yes / no \n")
    if indoor_ans.upper() == "YES" or indoor_ans.upper() == "Y":
        print("you best had, need to see who is there\n")
        time.sleep(1.5)
        print("it could be something important\n")
        time.sleep(1.5)
        print("you'd best go answer it...\n")   
        last_door()
    elif indoor_ans.upper() == "NO" or indoor_ans.upper() == "N":
        print("ok. back to bed\n")
        time.sleep(1.5)
        print("tomorrow is another day\n")
        time.sleep(1.5)
        start_game()
    else:     
        print("please stop dawdling. \n")
        time.sleep(1.5)
        print("i need an answer. \n")
        time.sleep(1.5)
        indoor()


        # insert cat drinking milk ascii



def last_door():
    print("you patter to the door, unsteadily, \n ")
    time.sleep(1.5)
    print("unsure of what to expect. \n")
    time.sleep(1.5)
    print("what terrors could await you? \n")
    time.sleep(1.5)
    print("when will it end? \n")
    time.sleep(1.5)
    # sad or scared ascii lol
    print("you warily open the door, and you see a large, unfamiliar figure \n")
    time.sleep(1.5)
    print("there's too much apocalypse and debris happening for you to tell \n ")
    time.sleep(1.5)
    print("what this large figure's motives are...\n")
    time.sleep(1.5)
    print("the large figure reaches out a hand to you. \n")
    time.sleep(1.5)
    last_door_ans = input("do you take it? \n yes / no \n")
    if last_door_ans.upper() == "YES" or last_door_ans.upper() == "Y":
        print("you take the strange figure's hand. \n")
        time.sleep(1.5)
        print("the ground begins to rumble. \n")
        time.sleep(1.5)
        print("a gigantic cat-face shaped ship erupts from the front yard, \n")
        time.sleep(1.5)
        print("completely ruining the fence's paintwork. \n")
        time.sleep(1.5)
        print("the large figure leads you to the ship, explaining, \n")
        time.sleep(1.5)
        print("the end of the world was meant for the humans....\n")
        time.sleep(1.5)
        print("don't worry, you're safe now.")
        time.sleep(1.5)
        print(" =^v^=  =^v^=  =^v^= ")
        time.sleep(2)
        #ascii art happy!!!!

    elif last_door_ans.upper() == "NO" or last_door_ans.upper() == "N":
        print("deciding against your instincts, you close the door on the strange figure. \n")
        time.sleep(1.5)
        print("but already... \n")
        time.sleep(1.5)
        print("it sounds like the ground is rumbling? \n")
        time.sleep(1.5)
        print("how strange... \n")
        time.sleep(1.5)
        print("you hop onto the windowsill, just in time to see a gigantic cat-face shaped ship \n")
        print("erupting from the back yard,")
        time.sleep(1.5)
        print("before zooming off into space \n")
        time.sleep(1.5)
        print("a note falls to the ground near your feet \n")
        time.sleep(1.5)
        print("it reads, \n")
        time.sleep(2)
        print(" 'we'll try again tomorrow.' ")
        time.sleep(2)
        print(" 'please be prepared this time...'")
        time.sleep(2)
        restart()
    else:     
        restart()
            



def restart():
    time.sleep(1.5)
    restart_ans = input("try the day again? yes / no \n")
    if restart_ans.upper() == "YES" or restart_ans.upper() == "Y":
        print("i'm sure you'll do better this round...\n")
        time.sleep(1.5)
        print("maybe try to self sabotage less... \n")
        time.sleep(1.5)
        print("")  
        wake_up()
    if restart_ans.upper() == "NO" or restart_ans.upper() == "N":
        print("okay.\n")
        time.sleep(1.5)
        print("goodbye\n")
        time.sleep(1.5)
        print("")  
    else: 
        print("i didn't catch that. try again? \n")
        time.sleep(1.5)
        restart()

start_game()

