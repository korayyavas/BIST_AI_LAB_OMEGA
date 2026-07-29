"""
BIST AI LAB OMEGA
Fusion Engine v2.0 PRO

Advanced intelligence fusion layer.

Responsibilities:

- Combine all AI agents
- Normalize scores
- Apply dynamic weights
- Generate final AI score
- Generate trading signal
- Provide explainable fusion output

Architecture:

Technical Agent
Prediction Agent
News Agent
KAP Agent
Risk Agent
Macro Agent

        |
        ↓

Fusion Engine

        |
        ↓

Final Intelligence Score
Decision Signal
"""

from __future__ import annotations


from datetime import datetime


from typing import Dict, Any, List



class FusionEngine:


    def __init__(
        self
    ):


        self.version = "2.0.0"



        self.weights = {


            "technical_score":

                0.25,


            "prediction_score":

                0.25,


            "news_score":

                0.15,


            "kap_score":

                0.10,


            "macro_score":

                0.15,


            "risk_score":

                0.10

        }




    # =====================================================
    # MAIN FUSION
    # =====================================================

    def fuse(
        self,
        symbol,
        agents
    ):


        scores = self.extract_scores(

            agents

        )



        normalized = self.normalize_scores(

            scores

        )



        final_score = self.calculate_final_score(

            normalized

        )



        signal = self.generate_signal(

            final_score

        )



        return {


            "symbol":

                symbol.upper(),


            "scores":

                normalized,


            "final_score":

                round(

                    final_score,

                    2

                ),


            "signal":

                signal,


            "agents":

                agents,


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
        agents
    ):


        result = {



            "technical_score":

                50,


            "prediction_score":

                50,


            "news_score":

                50,


            "kap_score":

                50,


            "macro_score":

                50,


            "risk_score":

                50


        }



        for agent in agents:


            if not isinstance(

                agent,

                dict

            ):


                continue



            for key in result:


                if key in agent:


                    result[key] = agent[key]



        return result

        # =====================================================
    # NORMALIZE SCORES
    # =====================================================

    def normalize_scores(
        self,
        scores
    ):


        normalized = {}



        for key,value in scores.items():


            try:


                normalized[key] = round(


                    max(

                        0,

                        min(

                            100,

                            float(value)

                        )

                    ),


                    2

                )



            except Exception:


                normalized[key] = 50




        return normalized




    # =====================================================
    # FINAL SCORE CALCULATION
    # =====================================================

    def calculate_final_score(
        self,
        scores
    ):


        total = 0



        weight_sum = 0



        for key,weight in self.weights.items():


            value = scores.get(

                key,

                50

            )



            total += (


                float(value)

                *

                weight


            )



            weight_sum += weight




        if weight_sum == 0:


            return 50




        score = total / weight_sum




        # =============================================
        # RISK ADJUSTMENT
        # =============================================


        risk = scores.get(

            "risk_score",

            50

        )



        if risk > 70:


            score -= 10




        elif risk < 30:


            score += 5




        return max(

            0,

            min(

                100,

                score

            )

        )




    # =====================================================
    # SIGNAL GENERATOR
    # =====================================================

    def generate_signal(
        self,
        score
    ):


        if score >= 85:


            return "STRONG_BUY"



        if score >= 70:


            return "BUY"



        if score >= 55:


            return "HOLD"



        if score >= 40:


            return "WEAK_SELL"



        return "SELL"




    # =====================================================
    # TOP LEVEL RANKING
    # =====================================================

    def rank(
        self,
        reports,
        limit=10
    ):


        if not isinstance(

            reports,

            list

        ):


            return []



        sorted_reports = sorted(

            reports,

            key=lambda x:

                x.get(

                    "final_score",

                    0

                ),

            reverse=True

        )



        return sorted_reports[:limit]

        # =====================================================
    # BATCH FUSION
    # =====================================================

    def batch_fuse(
        self,
        reports
    ):


        results = []



        if not isinstance(

            reports,

            list

        ):


            return results




        for item in reports:


            if not isinstance(

                item,

                dict

            ):


                continue



            symbol = item.get(

                "symbol",

                ""

            )


            agents = item.get(

                "agents",

                []

            )



            results.append(

                self.fuse(

                    symbol,

                    agents

                )

            )



        return self.rank(

            results

        )




    # =====================================================
    # EXPLANATION DATA
    # =====================================================

    def explain_fusion(
        self,
        scores
    ):


        strengths = []


        weaknesses = []



        for key,value in scores.items():


            if value >= 70:


                strengths.append(

                    key

                )



            elif value <= 40:


                weaknesses.append(

                    key

                )



        return {


            "strengths":

                strengths,


            "weaknesses":

                weaknesses,


            "generated_at":

                datetime.utcnow().isoformat()

        }




    # =====================================================
    # HEALTH
    # =====================================================

    def health(
        self
    ):


        return {


            "service":

                "OMEGA Fusion Engine",


            "version":

                self.version,


            "weights":

                self.weights,


            "status":

                "READY"

        }




__all__ = [

    "FusionEngine"

]