"""
BIST AI LAB OMEGA
Market Brain v0.1

Global market intelligence layer.

Responsibilities:

- BIST market condition analysis
- Sector rotation detection
- Risk appetite calculation
- Market opportunity scanning
- Leader stock detection
- Market regime support

Compatible with:

- AI Orchestrator
- Regime Engine
- Portfolio Brain
- Decision Brain
- Dashboard
"""

from __future__ import annotations


from datetime import datetime

from typing import Dict, Any, List




class MarketBrain:


    def __init__(self):


        self.version = (

            "0.1.0"

        )



    # =====================================================
    # MARKET ANALYSIS
    # =====================================================

    def analyze(
        self,
        intelligence
    ):


        symbols = self._symbols(

            intelligence

        )



        if not symbols:


            return {


                "market_status":

                    "UNKNOWN",


                "market_score":

                    50,


                "opportunities":

                    []

            }



        scores = []

        risks = []



        for item in symbols:


            if not isinstance(

                item,

                dict

            ):

                continue



            scores.append(

                self._score(

                    item

                )

            )


            risks.append(

                self._risk(

                    item

                )

            )



        avg_score = self._average(

            scores

        )


        avg_risk = self._average(

            risks

        )



        status = self._market_state(

            avg_score,

            avg_risk

        )



        leaders = self.find_leaders(

            symbols

        )



        return {


            "market_status":

                status,


            "market_score":

                round(

                    avg_score,

                    2

                ),


            "risk_score":

                round(

                    avg_risk,

                    2

                ),


            "leaders":

                leaders,


            "opportunities":

                self.find_opportunities(

                    symbols

                ),


            "generated_at":

                datetime.utcnow().isoformat(),


            "version":

                self.version

        }




    # =====================================================
    # SYMBOL LIST
    # =====================================================

    def _symbols(
        self,
        data
    ):


        if not isinstance(

            data,

            dict

        ):

            return []



        return (

            data.get(

                "symbols"

            )

            or

            data.get(

                "all_symbols"

            )

            or

            []

        )




    # =====================================================
    # SCORE
    # =====================================================

    def _score(
        self,
        item
    ):


        return float(

            item.get(

                "final_score",

                item.get(

                    "score",

                    50

                )

            )

        )




    # =====================================================
    # RISK
    # =====================================================

    def _risk(
        self,
        item
    ):


        return float(

            item.get(

                "risk",

                item.get(

                    "risk_score",

                    50

                )

            )

        )




    # =====================================================
    # MARKET STATE
    # =====================================================

    def _market_state(
        self,
        score,
        risk
    ):


        if risk >= 80:

            return "HIGH_RISK"



        if score >= 75 and risk <= 50:

            return "BULLISH"



        if score <= 35:

            return "BEARISH"



        return "NEUTRAL"




    # =====================================================
    # LEADERS
    # =====================================================

    def find_leaders(
        self,
        symbols,
        limit=10
    ):


        return sorted(

            symbols,

            key=lambda x:

            float(

                x.get(

                    "score",

                    x.get(

                        "final_score",

                        0

                    )

                )

            ),

            reverse=True

        )[:limit]




    # =====================================================
    # OPPORTUNITY SCANNER
    # =====================================================

    def find_opportunities(
        self,
        symbols
    ):


        result = []



        for item in symbols:


            score = float(

                item.get(

                    "score",

                    item.get(

                        "final_score",

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



            if (

                score >= 70

                and

                confidence >= 60

            ):


                result.append(

                    {


                        "symbol":

                            item.get(

                                "symbol"

                            ),


                        "score":

                            score,


                        "confidence":

                            confidence

                    }

                )



        return result




    # =====================================================
    # SECTOR ROTATION
    # =====================================================

    def sector_rotation(
        self,
        symbols,
        sector_map
    ):


        sectors = {}



        for item in symbols:


            symbol = item.get(

                "symbol"

            )


            sector = sector_map.get(

                symbol,

                "UNKNOWN"

            )


            score = float(

                item.get(

                    "score",

                    50

                )

            )


            if sector not in sectors:

                sectors[sector] = []



            sectors[sector].append(

                score

            )



        result = {}



        for sector,values in sectors.items():


            result[sector] = round(

                sum(values)

                /

                len(values),

                2

            )



        return sorted(

            result.items(),

            key=lambda x:

            x[1],

            reverse=True

        )




    # =====================================================
    # AVERAGE
    # =====================================================

    def _average(
        self,
        values
    ):


        if not values:

            return 50



        return sum(values) / len(values)




    # =====================================================
    # HEALTH
    # =====================================================

    def health(
        self
    ):


        return {


            "service":

                "OMEGA Market Brain",


            "version":

                self.version,


            "status":

                "READY"

        }



__all__ = [

    "MarketBrain"

]