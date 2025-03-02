


class Schedule():
    """
    Stores the yearly of the game schedule
    Who plays who
    Think simplest data structure is a dictionary
    schedule: {
                date(week1): [
                        (team1, team2), 
                        (team3, team4), 
                        (team5, team6),
                        (team7, team8), 
                        (team9, team10), 
                        (team11, team12), 
                        (team13, team14), 
                        (team15, team16),
                        (team17, team18), 
                        (team19, team20)
                        ],

                date(week2): [
                        (team1, team2), 
                        (team3, team4), 
                        (team5, team6),
                        (team7, team8), 
                        (team9, team10), 
                        (team11, team12), 
                        (team13, team14), 
                        (team15, team16),
                        (team17, team18), 
                        (team19, team20)
                        ]
    }
    """
    schedule = dict()
    def __init__(self) -> None:
        self.schedule = self.get_game_schedules()
        self.index = 0

    def get_game_schedule(self):
        """
        Make an api call to espn to get this information
        or to fpl to get this information
        """

    def __iter__(self):
        return self 

    def __next__(self):
        """
        Can we call this to get the next item in this iterator
        """
        


