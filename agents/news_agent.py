"""
BIST AI LAB OMEGA
News Agent v1.0 PRO

News intelligence specialist.

Responsibilities:

- Analyze market news
- Calculate sentiment score
- Measure news impact
- Support batch intelligence
- Provide explainable output

Compatible with:

- News Service
- AI Orchestrator
- Fusion Engine
"""

from __future__ import annotations


from datetime import datetime


import logging


from typing import Dict, Any, List



logger = logging.getLogger(__name__)




class NewsAgent:


    def __init__(
        self,
        news_service=None
    ):


        self.news_service = news_service


        self.name = (

            "News Agent"

        )


        self.version = (

            "1.0.0"

        )




    # =====================================================
    # MAIN ANALYSIS
    # =====================================================

    def analyze(
        self,
        symbol,
        market_data=None
    ):


        try:


            if self.news_service:


                data = self.news_service.score(

                    symbol

                )



                if isinstance(

                    data,

                    dict

                ):


                    score = data.get(

                        "score",

                        50

                    )


                    count = data.get(

                        "count",

                        0

                    )


                else:


                    score = data


                    count = 0



            else:


                score = 50


                count = 0




            score = self.normalize(

                score

            )



            return {


                "agent":

                    self.name,


                "symbol":

                    symbol.upper(),


                "news_score":

                    score,


                "sentiment":

                    self.sentiment(

                        score

                    ),


                "news_count":

                    count,


                "impact":

                    self.impact(

                        score,

                        count

                    ),


                "generated_at":

                    datetime.utcnow().isoformat(),


                "version":

                    self.version

            }




        except Exception:


            logger.exception(

                "News Agent failed %s",

                symbol

            )


            return self.default(

                symbol

            )




    # =====================================================
    # NORMALIZE
    # =====================================================

    def normalize(
        self,
        score
    ):


        try:


            return round(

                max(

                    0,

                    min(

                        100,

                        float(score)

                    )

                ),

                2

            )


        except Exception:


            return 50




    # =====================================================
    # SENTIMENT
    # =====================================================

    def sentiment(
        self,
        score
    ):


        if score >= 70:


            return "POSITIVE"



        if score <= 35:


            return "NEGATIVE"



        return "NEUTRAL"




    # =====================================================
    # IMPACT
    # =====================================================

    def impact(
        self,
        score,
        count
    ):


        if count == 0:


            return "LOW"



        if abs(

            score - 50

        ) >= 25:


            return "HIGH"



        return "MEDIUM"




    # =====================================================
    # DEFAULT
    # =====================================================

    def default(
        self,
        symbol
    ):


        return {


            "agent":

                self.name,


            "symbol":

                symbol.upper(),


            "news_score":

                50,


            "sentiment":

                "NEUTRAL",


            "news_count":

                0,


            "impact":

                "LOW"

        }




    # =====================================================
    # HEALTH
    # =====================================================

    def health(
        self
    ):


        return {


            "agent":

                self.name,


            "version":

                self.version,


            "status":

                "READY"

        }




__all__ = [

    "NewsAgent"

]