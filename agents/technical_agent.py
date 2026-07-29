"""
BIST AI LAB OMEGA
Technical Agent v1.0 PRO

Technical intelligence specialist.

Responsibilities:

- Read feature pipeline output
- Analyze EMA trend
- Analyze RSI momentum
- Analyze MACD direction
- Analyze volatility
- Generate technical score
- Produce explainable signals

Compatible with:

- DataBridge
- Feature Pipeline
- AI Orchestrator
- Fusion Engine
"""

from __future__ import annotations


from datetime import datetime


from typing import Dict, Any




class TechnicalAgent:


    def __init__(
        self
    ):


        self.name = (

            "Technical Agent"

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


            if market_data is None:


                return self.default(

                    symbol

                )




            row = self.latest_row(

                market_data

            )



            score = 50


            signals = []



            # =================================================
            # TREND ANALYSIS
            # =================================================


            close = self.value(

                row,

                "CLOSE",

                0

            )


            ema20 = self.value(

                row,

                "EMA20",

                close

            )


            ema50 = self.value(

                row,

                "EMA50",

                close

            )



            if close > ema20:


                score += 10


                signals.append(

                    "PRICE_ABOVE_EMA20"

                )


            else:


                score -= 10




            if ema20 > ema50:


                score += 15


                signals.append(

                    "UPTREND_CONFIRMED"

                )


            else:


                score -= 10




            # =================================================
            # RSI
            # =================================================


            rsi = self.value(

                row,

                "RSI14",

                50

            )



            if 50 <= rsi <= 70:


                score += 15


                signals.append(

                    "RSI_POSITIVE"

                )


            elif rsi > 70:


                score -= 5


                signals.append(

                    "RSI_OVERBOUGHT"

                )


            elif rsi < 30:


                score += 5


                signals.append(

                    "RSI_RECOVERY"

                )




            # =================================================
            # MACD
            # =================================================


            macd = self.value(

                row,

                "MACD",

                0

            )


            macd_signal = self.value(

                row,

                "MACD_SIGNAL",

                0

            )



            if macd > macd_signal:


                score += 15


                signals.append(

                    "MACD_BULLISH"

                )


            else:


                score -= 10


                signals.append(

                    "MACD_WEAK"

                )




            # =================================================
            # VOLATILITY
            # =================================================


            volatility = self.value(

                row,

                "VOLATILITY",

                0

            )



            if volatility > 5:


                score -= 10


                signals.append(

                    "HIGH_VOLATILITY"

                )




            score = max(

                0,

                min(

                    100,

                    score

                )

            )



            return {


                "agent":

                    self.name,


                "symbol":

                    symbol.upper(),


                "technical_score":

                    round(

                        score,

                        2

                    ),


                "trend":

                    self.trend(

                        close,

                        ema20,

                        ema50

                    ),


                "signals":

                    signals,


                "generated_at":

                    datetime.utcnow().isoformat(),


                "version":

                    self.version

            }




        except Exception:


            return self.default(

                symbol

            )




    # =====================================================
    # DATA READER
    # =====================================================

    def latest_row(
        self,
        data
    ):


        if hasattr(

            data,

            "iloc"

        ):


            return data.iloc[-1]



        if isinstance(

            data,

            dict

        ):


            return data



        return {}




    # =====================================================
    # SAFE VALUE
    # =====================================================

    def value(
        self,
        row,
        key,
        default
    ):


        try:


            return float(

                row.get(

                    key,

                    default

                )

            )


        except Exception:


            return default




    # =====================================================
    # TREND
    # =====================================================

    def trend(
        self,
        close,
        ema20,
        ema50
    ):


        if close > ema20 > ema50:


            return "STRONG_UPTREND"



        if close > ema20:


            return "UPTREND"



        if close < ema50:


            return "DOWNTREND"



        return "NEUTRAL"




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

                symbol,


            "technical_score":

                50,


            "trend":

                "UNKNOWN",


            "signals":

                []

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

    "TechnicalAgent"

]