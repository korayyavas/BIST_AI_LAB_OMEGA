"""
BIST AI LAB OMEGA
Backtest Brain v0.1

AI strategy simulation layer.

Responsibilities:

- Historical AI decision testing
- Portfolio simulation
- Performance measurement
- Sharpe ratio calculation
- Maximum drawdown
- Win/Loss analysis
- Strategy comparison

Compatible with:

- Decision Brain
- Portfolio Brain
- Risk Brain
- AI Orchestrator
"""

from __future__ import annotations


from datetime import datetime

from typing import Dict, Any, List




class BacktestBrain:


    def __init__(
        self,
        initial_capital=100000
    ):


        self.initial_capital = initial_capital


        self.version = (

            "0.1.0"

        )




    # =====================================================
    # MAIN BACKTEST
    # =====================================================

    def run(
        self,
        historical_data: List[Dict[str,Any]]
    ):


        capital = self.initial_capital


        trades = []


        equity_curve = [

            capital

        ]



        if not historical_data:


            return self.empty_result()



        for item in historical_data:


            action = item.get(

                "action",

                "HOLD"

            )


            return_value = float(

                item.get(

                    "return",

                    0

                )

            )



            if action in [

                "BUY",

                "STRONG_BUY"

            ]:


                profit = (

                    capital

                    *

                    return_value

                    /

                    100

                )


                capital += profit



                trades.append(

                    {

                        "action":

                            action,


                        "return":

                            return_value,


                        "profit":

                            round(

                                profit,

                                2

                            )

                    }

                )



            equity_curve.append(

                capital

            )



        performance = self.performance(

            equity_curve,

            trades

        )



        return {


            "initial_capital":

                self.initial_capital,


            "final_capital":

                round(

                    capital,

                    2

                ),


            "return_percent":

                round(

                    (

                        (

                            capital

                            -

                            self.initial_capital

                        )

                        /

                        self.initial_capital

                    )

                    *

                    100,

                    2

                ),


            "trades":

                trades,


            "performance":

                performance,


            "generated_at":

                datetime.utcnow().isoformat(),


            "version":

                self.version

        }




    # =====================================================
    # PERFORMANCE METRICS
    # =====================================================

    def performance(
        self,
        equity_curve,
        trades
    ):


        returns = []


        for i in range(1,len(equity_curve)):


            previous = equity_curve[i-1]


            current = equity_curve[i]



            if previous:


                returns.append(

                    (

                        current -

                        previous

                    )

                    /

                    previous

                )



        return {


            "sharpe_ratio":

                self.sharpe_ratio(

                    returns

                ),


            "max_drawdown":

                self.max_drawdown(

                    equity_curve

                ),


            "win_rate":

                self.win_rate(

                    trades

                ),


            "trade_count":

                len(

                    trades

                )

        }




    # =====================================================
    # SHARPE RATIO
    # =====================================================

    def sharpe_ratio(
        self,
        returns
    ):


        if not returns:

            return 0



        avg = sum(

            returns

        ) / len(returns)



        variance = sum(

            (

                x - avg

            ) ** 2

            for x in returns

        ) / len(returns)



        if variance == 0:

            return 0



        return round(

            avg /

            (

                variance ** 0.5

            ),

            2

        )




    # =====================================================
    # MAX DRAWDOWN
    # =====================================================

    def max_drawdown(
        self,
        equity_curve
    ):


        peak = equity_curve[0]


        max_loss = 0



        for value in equity_curve:


            if value > peak:


                peak = value



            drawdown = (

                peak -

                value

            ) / peak



            if drawdown > max_loss:


                max_loss = drawdown



        return round(

            max_loss *

            100,

            2

        )




    # =====================================================
    # WIN RATE
    # =====================================================

    def win_rate(
        self,
        trades
    ):


        if not trades:

            return 0



        wins = 0



        for trade in trades:


            if trade.get(

                "profit",

                0

            ) > 0:


                wins += 1



        return round(

            (

                wins /

                len(trades)

            )

            *

            100,

            2

        )




    # =====================================================
    # STRATEGY COMPARISON
    # =====================================================

    def compare(
        self,
        strategies
    ):


        return sorted(

            strategies,

            key=lambda x:

            x.get(

                "return_percent",

                0

            ),

            reverse=True

        )




    # =====================================================
    # EMPTY RESULT
    # =====================================================

    def empty_result(
        self
    ):


        return {


            "status":

                "NO_BACKTEST_DATA",


            "initial_capital":

                self.initial_capital

        }




    # =====================================================
    # HEALTH
    # =====================================================

    def health(
        self
    ):


        return {


            "service":

                "OMEGA Backtest Brain",


            "version":

                self.version,


            "status":

                "READY"

        }



__all__ = [

    "BacktestBrain"

]