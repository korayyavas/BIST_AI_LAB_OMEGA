"""
BIST AI LAB OMEGA
Risk Brain v0.1

Institutional risk management layer.

Responsibilities:

- Portfolio risk calculation
- Value at Risk estimation
- Position limit control
- Stress testing
- Drawdown protection
- Crisis mode detection

Compatible with:

- Portfolio Brain
- Decision Brain
- Regime Engine
- AI Orchestrator
"""

from __future__ import annotations


from datetime import datetime

from typing import Dict, Any, List




class RiskBrain:


    def __init__(
        self,
        max_position=0.20,
        max_portfolio_risk=0.60
    ):


        self.max_position = max_position


        self.max_portfolio_risk = max_portfolio_risk


        self.version = (

            "0.1.0"

        )




    # =====================================================
    # PORTFOLIO RISK ANALYSIS
    # =====================================================

    def analyze(
        self,
        portfolio
    ):


        if not isinstance(

            portfolio,

            dict

        ):


            return self.default_result()



        positions = portfolio.get(

            "portfolio",

            []

        )



        total_risk = 0


        warnings = []



        for item in positions:


            allocation = float(

                item.get(

                    "allocation",

                    0

                )

            )



            risk = float(

                item.get(

                    "risk",

                    50

                )

            )



            position_risk = (

                allocation

                *

                risk

                /

                100

            )



            total_risk += position_risk



            if allocation > (

                self.max_position *

                100

            ):


                warnings.append(

                    {

                        "symbol":

                            item.get(

                                "symbol"

                            ),


                        "type":

                            "POSITION_LIMIT_EXCEEDED"

                    }

                )



        risk_score = min(

            total_risk,

            100

        )



        return {


            "risk_score":

                round(

                    risk_score,

                    2

                ),


            "risk_level":

                self.level(

                    risk_score

                ),


            "warnings":

                warnings,


            "generated_at":

                datetime.utcnow().isoformat(),


            "version":

                self.version

        }




    # =====================================================
    # VALUE AT RISK
    # =====================================================

    def calculate_var(
        self,
        capital,
        volatility
    ):


        try:


            var = (

                capital

                *

                volatility

                /

                100

            )


            return round(

                var,

                2

            )



        except Exception:


            return 0




    # =====================================================
    # STRESS TEST
    # =====================================================

    def stress_test(
        self,
        portfolio,
        market_drop=-10
    ):


        capital = float(

            portfolio.get(

                "capital",

                0

            )

        )



        impact = (

            capital

            *

            abs(

                market_drop

            )

            /

            100

        )



        return {


            "scenario":

                f"Market {market_drop}%",


            "estimated_loss":

                round(

                    impact,

                    2

                ),


            "remaining_capital":

                round(

                    capital-impact,

                    2

                )

        }




    # =====================================================
    # CRISIS MODE
    # =====================================================

    def crisis_check(
        self,
        regime,
        risk_score
    ):


        if regime in [

            "CRISIS",

            "BEAR"

        ]:


            return True



        if risk_score >= 80:

            return True



        return False




    # =====================================================
    # RISK LEVEL
    # =====================================================

    def level(
        self,
        score
    ):


        if score <= 25:

            return "LOW"



        if score <= 50:

            return "MEDIUM"



        if score <= 75:

            return "HIGH"



        return "CRITICAL"




    # =====================================================
    # DEFAULT
    # =====================================================

    def default_result(
        self
    ):


        return {


            "risk_score":

                50,


            "risk_level":

                "MEDIUM",


            "warnings":

                []

        }




    # =====================================================
    # HEALTH
    # =====================================================

    def health(
        self
    ):


        return {


            "service":

                "OMEGA Risk Brain",


            "version":

                self.version,


            "status":

                "READY"

        }



__all__ = [

    "RiskBrain"

]