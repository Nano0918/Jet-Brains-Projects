# Orlando Rodriguez
# A short coding challenge that is meant to help the local zoo look after its animals. The program shold be a tool for monitoring animals and their status.


camel = r"""
Switching on camera from habitat with camels...
 ___.-''''-.
/___  @    |
',,,,.     |         _.'''''''._
     '     |        /           \
     |     \    _.-'             \
     |      '.-'                  '-.
     |                               ',
     |                                '',
      ',,-,                           ':;
           ',,| ;,,                 ,' ;;
              ! ; !'',,,',',,,,'!  ;   ;:
             : ;  ! !       ! ! ;  ;   :;
             ; ;   ! !      ! !  ; ;   ;,
            ; ;    ! !     ! !   ; ;     
            ; ;    ! !    ! !     ; ;
           ;,,      !,!   !,!     ;,;
           /_I      L_I   L_I     /_I
Yey, our little camel is sunbathing!"""

lion = r"""
Switching on camera from habitat with lions...
                                               ,w.
                                             ,YWMMw  ,M  ,
                        _.---.._   __..---._.'MMMMMw,wMWmW,
                   _.-""        '''           YP"WMMMMMMMMMb,
                .-' __.'                   .'     MMMMW^WMMMM;
    _,        .'.-'"; `,       /`     .--""      :MMM[==MWMW^;
 ,mM^"     ,-'.'   /   ;      ;      /   ,       MMMMb_wMW"  @\
,MM:.    .'.-'   .'     ;     `\    ;     `,     MMMMMMMW `"=./`-,
WMMm__,-'.'     /      _.\      F'''-+,,   ;_,_.dMMMMMMMM[,_ / `=_}
"^MP__.-'    ,-' _.--""   `-,   ;       \  ; ;MMMMMMMMMMW^``; __|
           /   .'            ; ;         )  )`{  \ `"^W^`,   \  :
          /  .'             /  (       .'  /     Ww._     `.  `"
         /  Y,              `,  `-,=,_{   ;      MMMP`""-,  `-._.-,
        (--, )                `,_ / `) \/"")      ^"      `-, -;"\:
The lion is croaking!"""

deer = r"""
Switching on camera from habitat with deers...
   /|       |\
`__\\       //__'
   ||      ||
 \__`\     |'__/
   `_\\   //_'
   _.,:---;,._
   \_:     :_/
     |@. .@|
     |     |
     ,\.-./ \
     ;;`-'   `---__________-----.-.
     ;;;                         \_\
     ';;;                         |
      ;    |                      ;
       \   \     \        |      /
        \_, \    /        \     |\
          |';|  |,,,,,,,,/ \    \ \_
          |  |  |           \   /   |
          \  \  |           |  / \  |
           | || |           | |   | |
           | || |           | |   | |
           | || |           | |   | |
           |_||_|           |_|   |_|
          /_//_/           /_/   /_/
Our 'Bambi' looks hungry. Let's go to feed it!"""

goose = r"""
Switching on camera from habitat with lovely goose...

                                    _
                                ,-"" "".
                              ,'  ____  `.
                            ,'  ,'    `.  `._
   (`.         _..--.._   ,'  ,'        \    \
  (`-.\    .-""        ""'   /          (  d _b
 (`._  `-"" ,._             (            `-(   \
 <_  `     (  <`<            \              `-._\
  <`-       (__< <           :
   (__        (_<_<          ;
    `------------------------------------------
This bird stares intently at you... (Maybe it's time to change the channel?)"""

bat = r"""
Switching on camera from habitat with bats...
_________________               _________________
 ~-.              \  |\___/|  /              .-~
     ~-.           \ / o o \ /           .-~
        >           \\  W  //           <
       /             /~---~\             \
      /_            |       |            _\
         ~-.        |       |        .-~
            ;        \     /        i
           /___      /\   /\      ___\
                ~-. /  \_/  \ .-~
                   V         V
It looks like this bat is fine."""

rabbit = r"""
Switching on camera from habitat with rabbits...
         ,
        /|      __
       / |   ,-~ /
      Y :|  //  /
      | jj /( .^
      >-"~"-v"
     /       Y
    jo  o    |
   ( ~T~     j
    >._-' _./
   /   "~"  |
  Y     _,  |
 /| ;-"~ _  l
/ l/ ,-"~    \
\//\/      .- \
 Y        /    Y 
 l       I     !
 ]\      _\    /"\
(" ~----( ~   Y.  )
It seems there will be more rabbits soon!"""


list_of_animals = [camel, lion, deer, goose, bat, rabbit]

while True:
    number_of_animal_or_exit = input("Which habitat # do you need?(Type 'exit' to close the program)\n1. Camel 2. Lion 3. Deer 4. Goose 5. Bat 6. Rabbit - ")

    while number_of_animal_or_exit.isalpha():
        if number_of_animal_or_exit != "exit":
            print("\nInvalid Input. Please enter a number between 1 and 6 or the word 'exit'.")
            number_of_animal_or_exit = input("Which habitat # do you need?(Type 'exit' to close the program)\n1. Camel 2. Lion 3. Deer 4. Goose 5. Bat 6. Rabbit - ")

        elif number_of_animal_or_exit == "exit":
            break

        elif number_of_animal_or_exit.isnumeric():
            break


    while number_of_animal_or_exit.isnumeric():
        if (int(number_of_animal_or_exit) < 1) or (int(number_of_animal_or_exit) > 6):
            print("\nInvalid Input. Please enter a number between 1 and 6 or the word 'exit'.")
            number_of_animal_or_exit = input("Which habitat # do you need?(Type 'exit' to close the program)\n1. Camel 2. Lion 3. Deer 4. Goose 5. Bat 6. Rabbit - ")

        if number_of_animal_or_exit == "exit":
            break
        
        elif number_of_animal_or_exit.isalpha():
            print("\nInvalid Input. Please enter a number between 1 and 6 or the word 'exit'.")
            number_of_animal_or_exit = input("Which habitat # do you need?(Type 'exit' to close the program)\n1. Camel 2. Lion 3. Deer 4. Goose 5. Bat 6. Rabbit - ")

        else:
            print()
            print(list_of_animals[int(number_of_animal_or_exit) - 1])
            print("---")
            print("The end of the program. To check another habitat restart the watcher please.\n")
            break
        
    if number_of_animal_or_exit == "exit":
        break


print("\nSee you!\n")