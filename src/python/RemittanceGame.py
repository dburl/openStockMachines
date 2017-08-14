
from datetime import datetime, timedelta
from marketsim.Exchange import Exchange, InfMonthlyStandingOrder
from marketsim.RetroAgent import RetroAgent
from marketsim.Constants import CCYMARKET, CCY
from marketsim.TimeKeeper import TimeKeeper
from marketsim.MarketEngine import MarketEngine
from marketsim.MarketModel import MarketModel


if __name__ == "__main__":
    print("Configuring...")

    market_model_1 = MarketModel(CCYMARKET.EURGBP)  # market model is container of one market data and its behavior
    market_model_2 = MarketModel(CCYMARKET.EURUSD)
    exchange = Exchange(market_model_1)
    exchange.add_market(market_model_2)

    agent = RetroAgent(exchange, {CCYMARKET.EURGBP}, CCY.EUR)
    agent_salary = InfMonthlyStandingOrder(CCY.GBP, 1000, agent.budget[CCY.GBP])
    exchange.add_order(agent_salary)

    time_keeper = TimeKeeper('2016-01-01', '2017-01-01', timedelta(days=1))

    engine = MarketEngine({exchange, agent}, time_keeper)

    print("MarketEngine starting @ {}".format(time_keeper.current()))

    engine.run()

    print("MarketEngine ending @ {}".format(time_keeper.current()))
