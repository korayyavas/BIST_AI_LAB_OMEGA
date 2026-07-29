"""
BIST AI LAB OMEGA
Confidence Engine v2.0 PRO

AI confidence calculation layer.

Responsibilities:

- Measure agent agreement
- Measure signal consensus
- Calculate confidence score
- Detect weak intelligence
- Prevent fake confidence

Compatible with:

- Fusion Engine
- AI Orchestrator
- Dashboard
"""

from __future__ import annotations


from datetime import datetime


from typing import List, Dict, Any




class ConfidenceEngine:



    def __init__(
        self
    ):


        self.version = "2.0.0"




    # =====================================================
    # MAIN CALCULATION
    # =====================================================

    def calculate(
        self,
        agents
    ):


        if not isinstance(

            agents,

            list

        ) or not agents:


            return self.default()




        agreement = self.calculate_agreement(

            agents

        )



        consensus = self.calculate_consensus(

            agents

        )



        data_quality = self.calculate_data_quality(

            agents

        )



        confidence = (

            agreement * 0.40

            +

            consensus * 0.35

            +

            data_quality * 0.25

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

                    consensus,

                    2

                ),


            "data_quality":

                round(

                    data_quality,

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
    # AGREEMENT
    # =====================================================

    def calculate_agreement(
        self,
        agents
    ):


        scores = []



        for agent in agents:


            if not isinstance(

                agent,

                dict

            ):


                continue



            value = self.extract_score(

                agent

            )



            scores.append(

                value

            )



        if not scores:


            return 50




        average = sum(scores) / len(scores)



        deviation = sum(

            abs(

                x - average

            )

            for x in scores

        ) / len(scores)




        agreement = 100 - deviation



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

    def calculate_consensus(
        self,
        agents
    ):


        signals = []



        for agent in agents:


            if not isinstance(

                agent,

                dict

            ):


                continue



            signal = agent.get(

                "signal"

            )



            if signal:


                signals.append(

                    signal

                )




        if not signals:


            return 50




        buy = 0

        sell = 0

        hold = 0



        for signal in signals:


            if signal in [


                "BUY",

                "STRONG_BUY"

            ]:


                buy += 1



            elif signal in [


                "SELL",

                "WEAK_SELL"

            ]:


                sell += 1



            else:


                hold += 1




        total = len(signals)



        strongest = max(

            buy,

            sell,

            hold

        )



        return round(

            (

                strongest /

                total

            )

            *

            100,

            2

        )




    # =====================================================
    # DATA QUALITY
    # =====================================================

    def calculate_data_quality(
        self,
        agents
    ):


        if not agents:


            return 0



        valid = 0



        total = len(

            agents

        )



        for agent in agents:


            if not isinstance(

                agent,

                dict

            ):


                continue



            values = list(

                agent.values()

            )



            if any(

                value not in [

                    None,

                    "",

                    0

                ]

                for value in values

            ):


                valid += 1




        quality = (

            valid /

            total

        ) * 100



        return round(

            quality,

            2

        )




    # =====================================================
    # SCORE EXTRACTION
    # =====================================================

    def extract_score(
        self,
        agent
    ):


        keys = [


            "technical_score",

            "prediction_score",

            "news_score",

            "kap_score",

            "risk_score",

            "macro_score"

        ]



        for key in keys:


            if key in agent:


                try:


                    return float(

                        agent[key]

                    )


                except Exception:


                    pass




        return 50




    # =====================================================
    # LEVEL
    # =====================================================

    def level(
        self,
        confidence
    ):


        if confidence >= 85:


            return "VERY_HIGH"



        if confidence >= 70:


            return "HIGH"



        if confidence >= 50:


            return "MEDIUM"



        return "LOW"




    # =====================================================
    # DEFAULT
    # =====================================================

    def default(
        self
    ):


        return {


            "confidence":

                50,


            "agreement":

                50,


            "signal_consensus":

                50,


            "data_quality":

                0,


            "level":

                "LOW",


            "generated_at":

                datetime.utcnow().isoformat(),


            "version":

                self.version

        }




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