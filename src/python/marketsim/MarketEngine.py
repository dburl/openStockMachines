from Logger import *

class MarketEngine:
    def __init__(self, mrkt_objects, time_keeper):
        self.mrkt_objects = mrkt_objects
        self.time_keeper = time_keeper

    def run(self):
        while(self.time_keeper.next() != -1):
            get_global_log().debug("MarketEngine - {}".format(self.time_keeper.current()))
            for mo in self.mrkt_objects:
                mo.update(self.time_keeper.current())

        get_global_log().info("--- MarketEngine - END OF RUN ---")
        for mo in self.mrkt_objects:
            get_global_log().info(mo)
