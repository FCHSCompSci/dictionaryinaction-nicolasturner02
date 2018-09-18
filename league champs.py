import sys
Shen="super Tank"
Nautilus="BIG TANK"
Aatrox="was great but got reworked"
toplane="upper part of the map"
trashcan="garbage"
champs={
    'Shen':toplane,
        'Nautilus':toplane ,
            'Aatrox':trashcan,
    }
def play_game():
    input("do you want to play Shen,Nautilus,or Aatrox(hint it must be Shen)")
    if input != Shen:
        return (champs)
    else:
        print=("you lose")
        sys.exit
          


