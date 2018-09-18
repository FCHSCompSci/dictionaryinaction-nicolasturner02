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
    input("do you want to play Shen,Nautilus,or Aatrox")
    if input != Shen:
        return (champs)
    input("do you want to play with that champ yes or no")
    if input == no:
        sys.exit
