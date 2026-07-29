"""
BIST AI LAB OMEGA
Confidence Engine v0.1

AI decision reliability layer.

Responsibilities:

- Measure agent agreement
- Calculate confidence score
- Detect conflicting intelligence
- Filter weak signals
- Decision safety control

Compatible with:

- Fusion Engine
- Decision Brain
- Regime Engine
- AI Orchestrator
"""

from __future__ import annotations


from datetime import datetime

from typing import Dict, Any, List




class ConfidenceEngine:


    def __init__(self):


        self.version = (

            "0.1.0"

        )




    # =====================================================
    # MAIN CONFIDENCE CALCULATION
    # =====================================================

    def calculate(
        self,
        agent_results: List[Dict[str,Any]]
    ):


        if not agent_results:


            return {


                "confidence":

                    50,


                "level":

                    "LOW",


                "agreement":

                    50

            }




        scores = []


        signals = []



        for agent in agent_results:


            if not isinstance(

                agent,

                dict

            ):

                continue



            score = self.extract_score(

                agent

            )


            scores.append(

                score

            )



            signal = agent.get(

                "signal"

            )



            if signal:

                signals.append(

                    signal

                )




        if not scores:


            return {


                "confidence":

                    50,


                "level":

                    "LOW"

            }




        agreement = self.agreement(

            scores

        )



        signal_consensus = self.signal_consensus(

            signals

        )



        confidence = (

            agreement * 0.6

            +

            signal_consensus * 0.4

        )



        return {


            "confidence":

                round(

                    confidence,

                    2

                ),


            "agreement":

                round(

                    agreement,

                    2

                ),


            "signal_consensus":

                round(

                    signal_consensus,

                    2

                ),


            "level":

                self.level(

                    confidence

                ),


            "generated_at":

                datetime.utcnow().isoformat(),


            "version":

                self.version

        }




    # =====================================================
    # SCORE EXTRACTOR
    # =====================================================

    def extract_score(
        self,
        agent
    ):


        keys = [


            "technical_score",


            "news_score",


            "kap_score",


            "macro_score",


            "risk_score"

        ]



        for key in keys:


            if key in agent:


                return float(

                    agent[key]

                )



        if "confidence" in agent:


            return float(

                agent["confidence"]

            )



        return 50




    # =====================================================
    # AGREEMENT SCORE
    # =====================================================

    def agreement(
        self,
        scores
    ):


        if not scores:

            return 50



        highest = max(

            scores

        )


        lowest = min(

            scores

        )



        difference = highest - lowest



        agreement = 100 - difference



        return max(

            0,

            min(

                100,

                agreement

            )

        )




    # =====================================================
    # SIGNAL CONSENSUS
    # =====================================================

    def signal_consensus(
        self,
        signals
    ):


        if not signals:


            return 50



        positive = 0


        negative = 0


        neutral = 0



        for signal in signals:


            if signal in [

                "BUY",

                "STRONG_BUY"

            ]:


                positive += 1



            elif signal in [

                "SELL",

                "STRONG_SELL"

            ]:


                negative += 1



            else:


                neutral += 1




        total = len(

            signals

        )



        dominant = max(

            positive,

            negative,

            neutral

        )



        return (

            dominant /

            total

        ) * 100




    # =====================================================
    # CONFIDENCE LEVEL
    # =====================================================

    def level(
        self,
        score
    ):


        if score >= 80:


            return "VERY_HIGH"



        if score >= 65:


            return "HIGH"



        if score >= 45:


            return "MEDIUM"



        return "LOW"




    # =====================================================
    # DECISION FILTER
    # =====================================================

    def can_trade(
        self,
        confidence
    ):


        if isinstance(

            confidence,

            dict

        ):


            value = confidence.get(

                "confidence",

                50

            )


        else:


            value = confidence



        return float(

            value

        ) >= 65




    # =====================================================
    # HEALTH
    # =====================================================

    def health(
        self
    ):


        return {


            "service":

                "OMEGA Confidence Engine",


            "version":

                self.version,


            "status":

                "READY"

        }



__all__ = [

    "ConfidenceEngine"

]