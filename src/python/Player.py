"""
Observation base class for various market specific observation sub classes
"""
class Observation:
    def __init__(self, observedtime):
        self.timestamp = observedtime
"""
FXObservation sub class records an exchange rate at single pt in time between currencies
"""
class FXObservation(Observation):
    def __init__(self, observedtime, buycurrency, sellcurrency, exhangerate):
        Observation.__init__(observedtime)
        self.buyccy = buycurrency
        self.sellccy = sellcurrency
        self.fxrate = fxrate

"""
CBObservation sub class records an interest rate at single pt in time of a central bank
"""
class CBObservation(Observation):
    def __init__(self, observedtime, centralbank, interestrate):
        Observation.__init__(observedtime)
        self.cbank = centralbank
        self.irrate = irrate

"""
Agent base class for various agents with varied strategies for observing and determining markets
"""
class Agent:
    def __init__(self):
        pass
    def Observe(self, observation):
        raise NotImplementedError("Observe not implemented yet")
    def GetPrice(self, timestamp):
        raise NotImplementedError("GetPrice not implemented yet")
"""
RetroAgent implements Agent that makes decisions based on previous FX observations
"""
class RetroAgent(Agent):
    def __init__(self):
        Agent.__init__(self)
    def Observe(self, fxobservation):
        #store all observation
        #update previous verdicts
        raise NotImplementedError("TODO: Observe impl RetroAgent")
    def GetPrice(self, timestamp):
        raise NotImplementedError("TODO: GetPrice impl using previous fx observations")
"""
BrokerAgent implements Agent that makes spot rates based on central bank interest rates
"""
class BrokerAgent(Agent):
    def __init(self):
        Agent.__init__(self)
    def Observe(self, cbobservation):
        raise NotImplementedError("TODO: Observe impl BrokerAgent")
    def GetPrice(self, timestamp):
        raise NotImplementedError("TODO: GetPrice impl using previous CB observations")

"""
Player uses an Agent to make plays based on observations
"""
class Player:
    def __init__(self, agent):
        self.agent = agent
    def MakeObservations(self):
        raise NotImplementedError("TODO: make player observations")
    def MakePlays(self):
        raise NotImplementedError("TODOL make player plays")



if __name__ == "__main__":
    p = Player(RetroAgent)  #TODO implement Player and Agents
    p.MakeObservations()    #TODO implement observation source
    p.MakePlays()           #TODO implement game deifinition
