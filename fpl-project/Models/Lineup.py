import Player 

class Lineup:
    def __init__(
        self,
        captain: Player,
        vice_captain: Player,
        gk: Player,
        defenders: list,
        midfielders: list,
        strikers: list,
        bench: list) -> None:

        self.captain = captain
        self.vice_captain = vice_captain
        self.gk = gk
        self.defenders = defenders
        self.midfielders = midfielders
        self.strikers = strikers
        self.bench = bench 

        self.validate()


    def validate(self):
        #make sure roster has 16 players
        roster_size = len(self.defenders) + len(self.midfielders) + len(self.strikers) + len(self.bench) 
        if self.gk and roster_size==15:
            print("Squad size is valid")

        #check that all defenders are indeed defenders
        for player in self.defenders:
            if not player.position == "defender":
                print("Invalid number of defenders")


        #check that all defenders are indeed midfielder
        for player in self.midfidlers:
            if not player.position == "midfielder":
                print("Invalid number of midfielders")

        #check that all defenders are indeed defenders
        for player in self.strikers:
            if not player.position == "striker":
                print("Invalid number of strikers")