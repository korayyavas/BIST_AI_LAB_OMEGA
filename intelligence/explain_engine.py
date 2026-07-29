"""
BIST AI LAB OMEGA
Explain Engine v2.0 PRO

Explainable AI layer.

Responsibilities:

- Convert AI scores into human explanation
- Generate decision summary
- Detect strengths
- Detect weaknesses
- Create risk message

Compatible with:

- Fusion Engine
- Confidence Engine
- AI Orchestrator
- Dashboard
"""

from __future__ import annotations


from datetime import datetime


from typing import Dict, Any, List




class ExplainEngine:



    def __init__(
        self
    ):


        self.version = "2.0.0"




    # =====================================================
    # MAIN EXPLANATION
    # =====================================================

    def explain(
        self,
        intelligence
    ):


        if not isinstance(

            intelligence,

            dict

        ):


            return self.default()




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



        strengths = self.detect_strengths(

            scores

        )



        weaknesses = self.detect_weaknesses(

            scores

        )



        return {


            "decision":

                signal,


            "summary":

                self.summary(

                    score,

                    signal

                ),


            "strengths":

                strengths,


            "weaknesses":

                weaknesses,


            "risk_message":

                self.risk_message(

                    scores

                ),


            "score":

                round(

                    score,

                    2

                ),


            "generated_at":

                datetime.utcnow().isoformat(),


            "version":

                self.version

        }




    # =====================================================
    # SUMMARY
    # =====================================================

    def summary(
        self,
        score,
        signal
    ):


        if signal == "STRONG_BUY":


            return (

                "AI güçlü pozitif sinyal üretiyor. "

                f"Final skor: {round(score,2)}"

            )



        if signal == "BUY":


            return (

                "AI pozitif fırsat görüyor. "

                f"Final skor: {round(score,2)}"

            )



        if signal == "SELL":


            return (

                "AI negatif risk sinyali üretiyor. "

                f"Final skor: {round(score,2)}"

            )



        if signal == "WEAK_SELL":


            return (

                "AI zayıf görünüm tespit etti. "

                f"Final skor: {round(score,2)}"

            )



        return (

            "AI kararı nötr bölgede. "

            f"Final skor: {round(score,2)}"

        )




    # =====================================================
    # STRENGTH DETECTION
    # =====================================================

    def detect_strengths(
        self,
        scores
    ):


        strengths = []



        if not isinstance(

            scores,

            dict

        ):


            return strengths



        for key,value in scores.items():


            try:


                if float(value) >= 70:


                    strengths.append(

                        key

                    )



            except Exception:


                continue




        return strengths

        # =====================================================
    # WEAKNESS DETECTION
    # =====================================================

    def detect_weaknesses(
        self,
        scores
    ):


        weaknesses = []



        if not isinstance(

            scores,

            dict

        ):


            return weaknesses



        for key,value in scores.items():


            try:


                if float(value) <= 40:


                    weaknesses.append(

                        key

                    )



            except Exception:


                continue




        return weaknesses




    # =====================================================
    # RISK MESSAGE
    # =====================================================

    def risk_message(
        self,
        scores
    ):


        if not isinstance(

            scores,

            dict

        ):


            return (

                "Risk analizi mevcut değil."

            )



        risk = float(

            scores.get(

                "risk_score",

                50

            )

        )



        if risk >= 75:


            return (

                "Yüksek risk seviyesi. "

                "Pozisyon büyüklüğü kontrollü tutulmalı."

            )



        if risk >= 50:


            return (

                "Orta risk seviyesi. "

                "Kontrollü pozisyon önerilir."

            )



        return (

            "Düşük risk seviyesi. "

            "Risk koşulları olumlu."

        )




    # =====================================================
    # DEFAULT
    # =====================================================

    def default(
        self
    ):


        return {


            "decision":

                "HOLD",


            "summary":

                "AI analizi oluşturulamadı.",


            "strengths":

                [],


            "weaknesses":

                [],


            "risk_message":

                "Risk bilgisi yok.",


            "score":

                50,


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

                "OMEGA Explain Engine",


            "version":

                self.version,


            "status":

                "READY"

        }




__all__ = [

    "ExplainEngine"

]
    