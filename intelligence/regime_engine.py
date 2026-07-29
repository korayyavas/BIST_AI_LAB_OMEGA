"""
BIST AI LAB OMEGA
Regime Engine v0.1

Market regime intelligence layer.

Responsibilities:

- Detect market conditions
- Identify bull/bear cycles
- Measure market strength
- Detect crisis conditions
- Guide AI aggressiveness

Regimes:

- BULL
- RECOVERY
- NEUTRAL
- SIDEWAYS
- BEAR
- CRISIS

Compatible with:

- Market Brain
- Decision Brain
- Portfolio Brain
- AI Orchestrator
"""

from __future__ import annotations


from datetime import datetime

from typing import Dict, Any, List




class RegimeEngine:


    def __init__(self):


        self.version = (

            "0.1.0"

        )




    # =====================================================
    # MAIN ANALYSIS
    # =====================================================

    def analyze(
        self,
        market_data
    ):


        if not market_data:


            return self.default()



        scores = []


        risks = []


        signals = []



        for item in market_data:


            if not isinstance(

                item,

                dict

            ):

                continue



            score = float(

                item.get(

                    "final_score",

                    item.get(

                        "score",

                        50

                    )

                )

            )


            risk = float(

                item.get(

                    "risk",

                    item.get(

                        "risk_score",

                        50

                    )

                )

            )



            scores.append(

                score

            )


            risks.append(

                risk

            )



            signal = item.get(

                "signal"

            )


            if signal:

                signals.append(

                    signal

                )




        avg_score = self.average(

            scores

        )


        avg_risk = self.average(

            risks

        )


        positive_ratio = self.signal_ratio(

            signals

        )



        regime = self.detect(

            avg_score,

            avg_risk,

            positive_ratio

        )



        return {


            "regime":

                regime,


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


            "positive_signal_ratio":

                round(

                    positive_ratio,

                    2

                ),


            "description":

                self.description(

                    regime

                ),


            "generated_at":

                datetime.utcnow().isoformat(),


            "version":

                self.version

        }




    # =====================================================
    # REGIME DETECTOR
    # =====================================================

    def detect(
        self,
        score,
        risk,
        positive_ratio
    ):


        # Extreme danger

        if risk >= 85:


            return "CRISIS"



        # Strong market

        if (

            score >= 75

            and

            positive_ratio >= 60

            and

            risk <= 50

        ):


            return "BULL"



        # Recovery phase

        if (

            score >= 60

            and

            positive_ratio >= 45

        ):


            return "RECOVERY"



        # Weak market

        if (

            score <= 35

        ):


            if risk >= 70:


                return "CRISIS"



            return "BEAR"




        # Sideways

        if (

            45 <= score <= 60

        ):


            return "SIDEWAYS"



        return "NEUTRAL"




    # =====================================================
    # SIGNAL RATIO
    # =====================================================

    def signal_ratio(
        self,
        signals
    ):


        if not signals:


            return 50



        positive = 0



        for signal in signals:


            if signal in [


                "BUY",

                "STRONG_BUY"

            ]:


                positive += 1



        return (

            positive /

            len(signals)

        ) * 100




    # =====================================================
    # DESCRIPTION
    # =====================================================

    def description(
        self,
        regime
    ):


        descriptions = {


            "BULL":

                "Piyasa güçlü pozitif trend bölgesinde.",


            "RECOVERY":

                "Piyasa toparlanma sürecinde.",


            "SIDEWAYS":

                "Yatay ve kararsız piyasa koşulu.",


            "NEUTRAL":

                "Belirsizlik seviyesi dengeli.",


            "BEAR":

                "Negatif piyasa baskısı mevcut.",


            "CRISIS":

                "Yüksek riskli piyasa koşulu."

        }



        return descriptions.get(

            regime,

            "Bilinmeyen piyasa durumu."

        )




    # =====================================================
    # AVERAGE
    # =====================================================

    def average(
        self,
        values
    ):


        if not values:


            return 50



        return sum(values) / len(values)




    # =====================================================
    # DEFAULT
    # =====================================================

    def default(
        self
    ):


        return {


            "regime":

                "NEUTRAL",


            "market_score":

                50,


            "risk_score":

                50

        }




    # =====================================================
    # HEALTH
    # =====================================================

    def health(
        self
    ):


        return {


            "service":

                "OMEGA Regime Engine",


            "version":

                self.version,


            "status":

                "READY"

        }



__all__ = [

    "RegimeEngine"

]