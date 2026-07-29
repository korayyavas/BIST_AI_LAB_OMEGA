"""
BIST AI LAB OMEGA
Explain Engine v0.1

Explainable AI intelligence layer.

Responsibilities:

- Explain AI decisions
- Identify strongest factors
- Identify risks
- Generate human readable reasoning
- Dashboard compatible explanation

Compatible with:

- Fusion Engine
- Confidence Engine
- Decision Brain
- Dashboard
"""

from __future__ import annotations


from datetime import datetime

from typing import Dict, Any, List




class ExplainEngine:


    def __init__(self):


        self.version = (

            "0.1.0"

        )




    # =====================================================
    # MAIN EXPLANATION
    # =====================================================

    def explain(
        self,
        intelligence: Dict[str,Any]
    ):


        score = float(

            intelligence.get(

                "final_score",

                50

            )

        )


        signal = intelligence.get(

            "signal",

            "HOLD"

        )


        scores = intelligence.get(

            "scores",

            {}

        )



        strengths = self.find_strengths(

            scores

        )


        weaknesses = self.find_weaknesses(

            scores

        )



        risk = self.risk_message(

            scores

        )



        return {


            "decision":

                signal,


            "summary":

                self.summary(

                    signal,

                    score

                ),


            "strengths":

                strengths,


            "weaknesses":

                weaknesses,


            "risk_message":

                risk,


            "score":

                round(

                    score,

                    2

                ),


            "generated_at":

                datetime.utcnow().isoformat()

        }




    # =====================================================
    # SUMMARY
    # =====================================================

    def summary(
        self,
        signal,
        score
    ):


        if signal == "STRONG_BUY":


            return (

                f"AI güçlü pozitif sinyal üretti. "

                f"Final skor: {score}"

            )



        if signal == "BUY":


            return (

                f"AI pozitif beklenti oluşturdu. "

                f"Final skor: {score}"

            )



        if signal == "SELL":


            return (

                f"AI negatif görünüm tespit etti. "

                f"Final skor: {score}"

            )



        return (

            f"AI kararı nötr bölgede. "

            f"Final skor: {score}"

        )




    # =====================================================
    # STRONG FACTORS
    # =====================================================

    def find_strengths(
        self,
        scores
    ):


        strengths = []



        for key,value in scores.items():


            if float(value) >= 70:


                strengths.append(

                    {

                        "factor":

                            key,


                        "score":

                            value

                    }

                )



        return sorted(

            strengths,

            key=lambda x:

            x["score"],

            reverse=True

        )




    # =====================================================
    # WEAK FACTORS
    # =====================================================

    def find_weaknesses(
        self,
        scores
    ):


        weaknesses = []



        for key,value in scores.items():


            if float(value) <= 40:


                weaknesses.append(

                    {

                        "factor":

                            key,


                        "score":

                            value

                    }

                )



        return sorted(

            weaknesses,

            key=lambda x:

            x["score"]

        )




    # =====================================================
    # RISK MESSAGE
    # =====================================================

    def risk_message(
        self,
        scores
    ):


        risk = float(

            scores.get(

                "risk_score",

                50

            )

        )



        if risk >= 70:


            return (

                "Yüksek risk seviyesi. "

                "Pozisyon büyüklüğü azaltılmalı."

            )



        if risk >= 50:


            return (

                "Orta risk seviyesi. "

                "Kontrollü pozisyon önerilir."

            )



        return (

            "Risk seviyesi düşük."

        )




    # =====================================================
    # BATCH EXPLANATION
    # =====================================================

    def explain_market(
        self,
        reports
    ):


        results = []



        for item in reports:


            results.append(

                self.explain(

                    item

                )

            )



        return results




    # =====================================================
    # HEALTH
    # =====================================================

    def health(
        self
    ):


        return {


            "service":

                "OMEGA Explain Engine",


            "version":

                self.version,


            "status":

                "READY"

        }



__all__ = [

    "ExplainEngine"

]