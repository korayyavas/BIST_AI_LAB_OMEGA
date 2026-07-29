"""
BIST AI LAB OMEGA
Regime Engine v2.0 PRO

Market regime intelligence layer.

Responsibilities:

- Detect market environment
- Analyze AI score distribution
- Determine market trend regime
- Provide macro context
- Support portfolio decisions

Compatible with:

- AI Orchestrator
- Fusion Engine
- Portfolio Brain
"""

from __future__ import annotations


from datetime import datetime


from typing import List, Dict, Any




class RegimeEngine:


    def __init__(
        self
    ):


        self.version = "2.0.0"




    # =====================================================
    # MAIN ANALYSIS
    # =====================================================

    def analyze(
        self,
        reports
    ):


        if not isinstance(

            reports,

            list

        ) or not reports:


            return self.default()




        scores = self.extract_scores(

            reports

        )



        average = self.average_score(

            scores

        )



        regime = self.detect_regime(

            average

        )



        signals = self.generate_signals(

            average,

            regime

        )



        return {


            "regime":

                regime,


            "score":

                round(

                    average,

                    2

                ),


            "signals":

                signals,


            "market_condition":

                self.condition(

                    average

                ),


            "generated_at":

                datetime.utcnow().isoformat(),


            "version":

                self.version

        }




    # =====================================================
    # SCORE EXTRACTION
    # =====================================================

    def extract_scores(
        self,
        reports
    ):


        scores = []



        for report in reports:


            if not isinstance(

                report,

                dict

            ):


                continue



            score = report.get(

                "final_score",

                50

            )



            try:


                scores.append(

                    float(score)

                )



            except Exception:


                continue




        return scores




    # =====================================================
    # AVERAGE SCORE
    # =====================================================

    def average_score(
        self,
        scores
    ):


        if not scores:


            return 50




        return sum(scores) / len(scores)




    # =====================================================
    # REGIME DETECTION
    # =====================================================

    def detect_regime(
        self,
        score
    ):


        if score >= 75:


            return "BULL_MARKET"



        if score >= 60:


            return "POSITIVE"



        if score <= 35:


            return "BEAR_MARKET"



        if score <= 45:


            return "NEGATIVE"



        return "NEUTRAL"
        # =====================================================
    # SIGNAL GENERATOR
    # =====================================================

    def generate_signals(
        self,
        score,
        regime
    ):


        signals = []



        if regime == "BULL_MARKET":


            signals.append(

                "STRONG_BUY_ENVIRONMENT"

            )


            signals.append(

                "RISK_APPETITE_HIGH"

            )



        elif regime == "POSITIVE":


            signals.append(

                "SELECTIVE_BUY"

            )



        elif regime == "BEAR_MARKET":


            signals.append(

                "CAPITAL_PROTECTION"

            )


            signals.append(

                "HIGH_RISK_ENVIRONMENT"

            )



        elif regime == "NEGATIVE":


            signals.append(

                "DEFENSIVE_MODE"

            )



        else:


            signals.append(

                "WAIT_AND_OBSERVE"

            )



        return signals




    # =====================================================
    # MARKET CONDITION
    # =====================================================

    def condition(
        self,
        score
    ):


        if score >= 80:


            return "VERY_STRONG"



        if score >= 65:


            return "STRONG"



        if score >= 50:


            return "NORMAL"



        if score >= 35:


            return "WEAK"



        return "CRITICAL"




    # =====================================================
    # PORTFOLIO MODE
    # =====================================================

    def portfolio_mode(
        self,
        regime
    ):


        modes = {


            "BULL_MARKET":

                "AGGRESSIVE",


            "POSITIVE":

                "GROWTH",


            "NEUTRAL":

                "BALANCED",


            "NEGATIVE":

                "DEFENSIVE",


            "BEAR_MARKET":

                "CAPITAL_PRESERVATION"


        }



        return modes.get(

            regime,

            "BALANCED"

        )




    # =====================================================
    # DEFAULT
    # =====================================================

    def default(
        self
    ):


        return {


            "regime":

                "NEUTRAL",


            "score":

                50,


            "signals":

                [

                    "WAIT_AND_OBSERVE"

                ],


            "market_condition":

                "NORMAL",


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

                "OMEGA Regime Engine",


            "version":

                self.version,


            "status":

                "READY"

        }




__all__ = [

    "RegimeEngine"

]