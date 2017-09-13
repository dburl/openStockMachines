from datetime import timedelta
from marketsim.Exchange import Exchange
from marketsim.RetroAgent import RetroAgent
from marketsim.Constants import CCYMARKET, CCY
from marketsim.TimeKeeper import TimeKeeper
from marketsim.MarketEngine import MarketEngine
from marketsim.MarketModel import MarketModel, PerfectFXModel
from marketsim.Strategy import MonthlySalary, BuyEuros
from Logger import *

if __name__ == "__main__":
    set_global_logger()
    get_global_log().info("Configuring...")

    time_keeper = TimeKeeper('2016-01-01', '2016-03-03', timedelta(days=1))

    market_eurgbp = MarketModel(CCYMARKET.EURGBP)  # market model is container of one market data
    market_eurusd = PerfectFXModel(CCYMARKET.EURUSD)  # models simulate different behaviors  (e.g. fees)
    exchange = Exchange(market_eurgbp)  # Exchange operates on Market Models and executes agent orders
    exchange.add_market(market_eurusd)

    agent = RetroAgent(time_keeper, exchange, {CCYMARKET.EURGBP}, CCY.EUR)
    agent.strategies.append(MonthlySalary(CCY.GBP, 1000))  # add salary strategy as repetitive income from nowhere
    agent.strategies.append(BuyEuros())  # add dummy strategy that buys euros if any other equity/currency available

    get_global_log().info("MarketEngine starting @ {}".format(time_keeper.current()))

    engine = MarketEngine({exchange, agent}, time_keeper)
    engine.run()

    get_global_log().info("MarketEngine ending @ {}".format(time_keeper.current()))
