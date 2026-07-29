"""
BIST AI LAB OMEGA
Decision Brain v0.1

AI decision management layer.

Responsibilities:

- Convert intelligence into actions
- Combine score + confidence + regime
- Generate BUY / SELL / HOLD
- Risk based decision modification
- Portfolio action control

Compatible with:

- AI Orchestrator
- Portfolio Brain
- Fusion Engine
- Regime Engine
"""

from __future__ import annotations


from datetime import datetime

from typing import Dict, Any




class DecisionBrain:


    def __init__(
        self,
        buy_threshold=70,
        sell_threshold=35
    ):


        self.buy_threshold = buy_threshold


        self.sell_threshold = sell_threshold


        self.version = (

            "0.1.0"

        )




    # =====================================================
    # MAIN DECISION
    # =====================================================

    def decide(
        self,
        intelligence: Dict[str,Any]
    ):


        score = float(

            intelligence.get(

                "final_score",

                intelligence.get(

                    "score",

                    50

                )

            )

        )


        confidence = self._confidence(

            intelligence

        )


        regime = self._regime(

            intelligence

        )


        risk = self._risk(

            intelligence

        )



        action = self._action(

            score,

            confidence,

            regime,

            risk

        )



        return {


            "symbol":

                intelligence.get(

                    "symbol",

                    ""

                ),


            "action":

                action,


            "score":

                score,


            "confidence":

                confidence,


            "market_regime":

                regime,


            "risk":

                risk,


            "reason":

                self._reason(

                    action,

                    score,

                    confidence,

                    regime,

                    risk

                ),


            "generated_at":

                datetime.utcnow().isoformat(),


            "version":

                self.version

        }




    # =====================================================
    # ACTION ENGINE
    # =====================================================

    def _action(
        self,
        score,
        confidence,
        regime,
        risk
    ):


        # Crisis protection

        if regime == "CRISIS":

            return "SELL"



        if risk >= 80:

            return "REDUCE"



        if (

            score >= self.buy_threshold

            and

            confidence >= 70

        ):


            if regime in [

                "BULL",

                "RECOVERY"

            ]:

                return "STRONG_BUY"



            return "BUY"




        if score <= self.sell_threshold:


            return "SELL"




        return "HOLD"




    # =====================================================
    # CONFIDENCE EXTRACT
    # =====================================================

    def _confidence(
        self,
        intelligence
    ):


        confidence = intelligence.get(

            "confidence",

            {}

        )


        if isinstance(

            confidence,

            dict

        ):


            return float(

                confidence.get(

                    "confidence",

                    50

                )

            )



        return float(

            confidence or 50

        )




    # =====================================================
    # REGIME EXTRACT
    # =====================================================

    def _regime(
        self,
        intelligence
    ):


        regime = intelligence.get(

            "market_regime",

            intelligence.get(

                "regime",

                {}

            )

        )



        if isinstance(

            regime,

            dict

        ):


            return regime.get(

                "regime",

                "UNKNOWN"

            )



        return regime




    # =====================================================
    # RISK EXTRACT
    # =====================================================

    def _risk(
        self,
        intelligence
    ):


        agents = intelligence.get(

            "agents",

            {}

        )



        risk_agent = agents.get(

            "Risk Agent",

            {}

        )



        if isinstance(

            risk_agent,

            dict

        ):


            return float(

                risk_agent.get(

                    "risk_score",

                    50

                )

            )



        return 50




    # =====================================================
    # EXPLANATION
    # =====================================================

    def _reason(
        self,
        action,
        score,
        confidence,
        regime,
        risk
    ):


        return {


            "decision":

                action,


            "score":

                score,


            "confidence":

                confidence,


            "regime":

                regime,


            "risk":

                risk,


            "message":

                f"AI karar: {action}. "

                f"Skor {score}, "

                f"Güven {confidence}, "

                f"Piyasa {regime}, "

                f"Risk {risk}."

        }




    # =====================================================
    # BATCH DECISION
    # =====================================================

    def decide_market(
        self,
        reports
    ):


        results = []



        for item in reports:


            results.append(

                self.decide(

                    item

                )

            )



        return sorted(

            results,

            key=lambda x:

            x.get(

                "score",

                0

            ),

            reverse=True

        )




    # =====================================================
    # HEALTH
    # =====================================================

    def health(
        self
    ):


        return {


            "service":

                "OMEGA Decision Brain",


            "version":

                self.version,


            "status":

                "READY"

        }



__all__ = [

    "DecisionBrain"

]