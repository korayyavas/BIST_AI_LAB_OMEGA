"""
BIST AI LAB OMEGA
Fusion Engine v0.1

Multi-agent intelligence fusion layer.

Responsibilities:

- Combine AI agent outputs
- Calculate final intelligence score
- Dynamic agent weighting
- Generate investment ranking
- Explain score composition
- Fusion compatible output

Agents:

- Technical
- Prediction
- News
- KAP
- Risk
- Macro

Compatible with:

- AI Orchestrator
- Confidence Engine
- Decision Brain
- Portfolio Brain
"""

from __future__ import annotations


from datetime import datetime

from typing import Dict, Any, List




class FusionEngine:


    def __init__(
        self,
        weights=None
    ):


        self.weights = weights or {


            "technical_score":

                0.25,


            "prediction_score":

                0.25,


            "news_score":

                0.15,


            "kap_score":

                0.15,


            "risk_score":

                0.10,


            "macro_score":

                0.10


        }


        self.version = (

            "0.1.0"

        )




    # =====================================================
    # MAIN FUSION
    # =====================================================

    def fuse(
        self,
        symbol,
        agent_results: List[Dict[str,Any]]
    ):


        combined = {


            "technical_score":

                50,


            "prediction_score":

                50,


            "news_score":

                50,


            "kap_score":

                50,


            "risk_score":

                50,


            "macro_score":

                50

        }



        explanations = []



        for result in agent_results:


            if not isinstance(

                result,

                dict

            ):

                continue



            agent = result.get(

                "agent"

            )



            # Technical

            if agent == "Technical Agent":


                combined["technical_score"] = (

                    result.get(

                        "technical_score",

                        50

                    )

                )


                explanations.append(

                    "Teknik analiz katkısı"

                )



            # Prediction

            elif agent == "Prediction Agent":


                prediction = float(

                    result.get(

                        "prediction",

                        0

                    )

                )


                combined["prediction_score"] = self.prediction_score(

                    prediction

                )


                explanations.append(

                    "AI model tahmini"

                )



            # News

            elif agent == "News Agent":


                combined["news_score"] = (

                    result.get(

                        "news_score",

                        50

                    )

                )



                explanations.append(

                    "Haber duyarlılığı"

                )



            # KAP

            elif agent == "KAP Agent":


                combined["kap_score"] = (

                    result.get(

                        "kap_score",

                        50

                    )

                )



                explanations.append(

                    "Kurumsal gelişmeler"

                )



            # Risk

            elif agent == "Risk Agent":


                risk = float(

                    result.get(

                        "risk_score",

                        50

                    )

                )


                combined["risk_score"] = (

                    100 -

                    risk

                )


                explanations.append(

                    "Risk düzenlemesi"

                )



            # Macro

            elif agent == "Macro Agent":


                combined["macro_score"] = (

                    result.get(

                        "macro_score",

                        50

                    )

                )


                explanations.append(

                    "Makro ortam"

                )




        final_score = self.calculate(

            combined

        )



        return {


            "symbol":

                symbol,


            "agents":

                agent_results,


            "scores":

                combined,


            "final_score":

                round(

                    final_score,

                    2

                ),


            "confidence":

                self.confidence(

                    combined

                ),


            "explanation":

                explanations,


            "signal":

                self.signal(

                    final_score

                ),


            "generated_at":

                datetime.utcnow().isoformat(),


            "version":

                self.version

        }




    # =====================================================
    # SCORE CALCULATION
    # =====================================================

    def calculate(
        self,
        scores
    ):


        total = 0



        for key,weight in self.weights.items():


            total += (

                scores.get(

                    key,

                    50

                )

                *

                weight

            )



        return max(

            0,

            min(

                100,

                total

            )

        )




    # =====================================================
    # PREDICTION SCORE
    # =====================================================

    def prediction_score(
        self,
        prediction
    ):


        score = 50 + (

            prediction *

            5

        )



        return max(

            0,

            min(

                100,

                score

            )

        )




    # =====================================================
    # CONFIDENCE
    # =====================================================

    def confidence(
        self,
        scores
    ):


        values = list(

            scores.values()

        )


        deviation = max(values) - min(values)



        confidence = 100 - deviation



        return round(

            max(

                0,

                min(

                    100,

                    confidence

                )

            ),

            2

        )




    # =====================================================
    # SIGNAL
    # =====================================================

    def signal(
        self,
        score
    ):


        if score >= 85:

            return "STRONG_BUY"



        if score >= 70:

            return "BUY"



        if score <= 35:

            return "SELL"



        return "HOLD"




    # =====================================================
    # MARKET FUSION
    # =====================================================

    def rank(
        self,
        reports
    ):


        return sorted(

            reports,

            key=lambda x:

            x.get(

                "final_score",

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

                "OMEGA Fusion Engine",


            "version":

                self.version,


            "status":

                "READY"

        }



__all__ = [

    "FusionEngine"

]