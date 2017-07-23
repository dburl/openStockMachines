

class MarketEngine:
    def __init__(self, mrkt_objects, time_keeper):
        self.mrkt_objects = mrkt_objects
        self.time_keeper = time_keeper

    def run(self):
        while(self.time_keeper.next() != -1):
            for mo in self.mrkt_objects:
                mo.update()
