"""
BIST AI LAB OMEGA
Portfolio Brain v0.1

AI portfolio management layer.

Responsibilities:

- Portfolio construction
- Position sizing
- Risk allocation
- Cash management
- Sector balance
- AI ranking integration

Compatible with:

- AI Orchestrator
- Fusion Engine
- Risk Agent
- Decision Engine
"""

from __future__ import annotations


from datetime import datetime

from typing import Dict, Any, List




class PortfolioBrain:


    def __init__(
        self,
        capital=100000,
        max_position=0.20,
        cash_reserve=0.15
    ):


        self.capital = capital


        self.max_position = max_position


        self.cash_reserve = cash_reserve


        self.version = (

            "0.1.0"

        )




    # =====================================================
    # BUILD PORTFOLIO
    # =====================================================

    def build(
        self,
        intelligence_report
    ):


        candidates = self._extract_candidates(

            intelligence_report

        )


        if not candidates:


            return {


                "portfolio":

                    [],


                "cash":

                    self.capital,


                "status":

                    "NO_CANDIDATES"

            }



        selected = []


        available_capital = (

            self.capital *

            (

                1 -

                self.cash_reserve

            )

        )



        for item in candidates:


            allocation = self._allocation(

                item

            )


            amount = (

                available_capital *

                allocation

            )



            selected.append(

                {


                    "symbol":

                        item.get(

                            "symbol"

                        ),



                    "score":

                        item.get(

                            "final_score",

                            item.get(

                                "score",

                                50

                            )

                        ),



                    "allocation":

                        round(

                            allocation *

                            100,

                            2

                        ),



                    "amount":

                        round(

                            amount,

                            2

                        ),



                    "reason":

                        item.get(

                            "explanation",

                            []

                        )

                }

            )



        return {


            "capital":

                self.capital,


            "cash_reserve":

                round(

                    self.cash_reserve *

                    100,

                    2

                ),


            "portfolio":

                selected,


            "generated_at":

                datetime.utcnow().isoformat(),


            "status":

                "PORTFOLIO_READY"

        }




    # =====================================================
    # CANDIDATE EXTRACTOR
    # =====================================================

    def _extract_candidates(
        self,
        report
    ):


        if not isinstance(

            report,

            dict

        ):

            return []



        return report.get(

            "symbols",

            report.get(

                "all_symbols",

                []

            )

        )




    # =====================================================
    # ALLOCATION ENGINE
    # =====================================================

    def _allocation(
        self,
        item
    ):


        score = float(

            item.get(

                "final_score",

                item.get(

                    "score",

                    50

                )

            )

        )



        confidence = float(

            item.get(

                "confidence",

                50

            )

        )



        risk_factor = 1



        agents = item.get(

            "agents",

            {}

        )



        risk = agents.get(

            "Risk Agent",

            {}

        )



        if isinstance(

            risk,

            dict

        ):


            risk_value = float(

                risk.get(

                    "risk_score",

                    50

                )

            )


            risk_factor = (

                1 -

                (

                    risk_value /

                    100

                )

            )



        weight = (

            (

                score /

                100

            )

            *

            (

                confidence /

                100

            )

            *

            risk_factor

        )



        return min(

            weight,

            self.max_position

        )




    # =====================================================
    # SECTOR BALANCE
    # =====================================================

    def sector_balance(
        self,
        portfolio,
        sector_map
    ):


        sectors = {}



        for item in portfolio:


            symbol = item.get(

                "symbol"

            )


            sector = sector_map.get(

                symbol,

                "UNKNOWN"

            )



            sectors[sector] = (

                sectors.get(

                    sector,

                    0

                )

                +

                item.get(

                    "allocation",

                    0

                )

            )



        return sectors




    # =====================================================
    # RISK CHECK
    # =====================================================

    def risk_check(
        self,
        portfolio
    ):


        warnings = []



        for item in portfolio:


            if item.get(

                "allocation",

                0

            ) > (

                self.max_position *

                100

            ):


                warnings.append(

                    {

                        "symbol":

                            item.get(

                                "symbol"

                            ),


                        "warning":

                            "Position too large"

                    }

                )



        return warnings




    # =====================================================
    # HEALTH
    # =====================================================

    def health(
        self
    ):


        return {


            "service":

                "OMEGA Portfolio Brain",


            "version":

                self.version,


            "status":

                "READY"

        }



__all__ = [

    "PortfolioBrain"

]