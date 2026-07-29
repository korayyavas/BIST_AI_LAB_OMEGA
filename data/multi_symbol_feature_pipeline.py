"""
BIST AI LAB OMEGA
Multi Symbol Feature Pipeline v2.0 PRO

Feature engineering layer.

Responsibilities:

- Generate technical indicators
- Normalize market features
- Prepare AI model input
- Feed Technical Agent
- Feed Prediction Agent

Compatible with:

- DataBridge
- MultiSymbolDownloader
- AI Orchestrator
- Model Engine
"""

from __future__ import annotations


import logging


import pandas as pd


import numpy as np



logger = logging.getLogger(__name__)




class MultiSymbolFeaturePipeline:



    def __init__(
        self
    ):


        self.version = (

            "2.0.0"

        )




    # =====================================================
    # PROCESS ALL SYMBOLS
    # =====================================================

    def process_all(
        self,
        market_data
    ):


        result = {}



        if not isinstance(

            market_data,

            dict

        ):


            return result




        for symbol,data in market_data.items():


            try:


                result[symbol] = self.process_symbol(

                    data

                )



            except Exception:


                logger.exception(

                    "Feature failed %s",

                    symbol

                )



        return result




    # =====================================================
    # SINGLE SYMBOL
    # =====================================================

    def process_symbol(
        self,
        df
    ):



        if df is None or len(df) == 0:


            return None




        data = df.copy()



        data = self.add_returns(

            data

        )



        data = self.add_moving_average(

            data

        )



        data = self.add_rsi(

            data

        )



        data = self.add_macd(

            data

        )



        data = self.add_volatility(

            data

        )



        data = self.add_atr(

            data

        )



        data = data.dropna()



        return data




    # =====================================================
    # RETURNS
    # =====================================================

    def add_returns(
        self,
        df
    ):


        df["RETURN"] = (

            df["CLOSE"]

            .pct_change()

            *

            100

        )


        return df




    # =====================================================
    # MOVING AVERAGES
    # =====================================================

    def add_moving_average(
        self,
        df
    ):


        df["EMA20"] = (

            df["CLOSE"]

            .ewm(

                span=20

            )

            .mean()

        )



        df["EMA50"] = (

            df["CLOSE"]

            .ewm(

                span=50

            )

            .mean()

        )



        df["SMA200"] = (

            df["CLOSE"]

            .rolling(

                200

            )

            .mean()

        )



        return df




    # =====================================================
    # RSI
    # =====================================================

    def add_rsi(
        self,
        df,
        period=14
    ):


        delta = df["CLOSE"].diff()



        gain = delta.where(

            delta > 0,

            0

        )



        loss = -delta.where(

            delta < 0,

            0

        )



        avg_gain = gain.rolling(

            period

        ).mean()



        avg_loss = loss.rolling(

            period

        ).mean()



        rs = avg_gain / avg_loss



        df["RSI14"] = (

            100 -

            (

                100 /

                (

                    1 +

                    rs

                )

            )

        )


        return df




    # =====================================================
    # MACD
    # =====================================================

    def add_macd(
        self,
        df
    ):


        ema12 = (

            df["CLOSE"]

            .ewm(

                span=12

            )

            .mean()

        )



        ema26 = (

            df["CLOSE"]

            .ewm(

                span=26

            )

            .mean()

        )



        df["MACD"] = (

            ema12 -

            ema26

        )



        df["MACD_SIGNAL"] = (

            df["MACD"]

            .ewm(

                span=9

            )

            .mean()

        )



        return df




    # =====================================================
    # VOLATILITY
    # =====================================================

    def add_volatility(
        self,
        df
    ):


        df["VOLATILITY"] = (

            df["RETURN"]

            .rolling(

                20

            )

            .std()

        )



        return df




    # =====================================================
    # ATR
    # =====================================================

    def add_atr(
        self,
        df,
        period=14
    ):


        high_low = (

            df["HIGH"]

            -

            df["LOW"]

        )



        high_close = (

            abs(

                df["HIGH"]

                -

                df["CLOSE"].shift()

            )

        )



        low_close = (

            abs(

                df["LOW"]

                -

                df["CLOSE"].shift()

            )

        )



        ranges = pd.concat(

            [

                high_low,

                high_close,

                low_close

            ],

            axis=1

        )



        true_range = ranges.max(

            axis=1

        )



        df["ATR"] = (

            true_range

            .rolling(

                period

            )

            .mean()

        )



        return df




    # =====================================================
    # LATEST FEATURE ROW
    # =====================================================

    def latest(
        self,
        df
    ):


        if df is None or len(df)==0:


            return {}



        return df.iloc[-1].to_dict()




    # =====================================================
    # HEALTH
    # =====================================================

    def health(
        self
    ):


        return {


            "service":

                "OMEGA Feature Pipeline",


            "version":

                self.version,


            "status":

                "READY"

        }




__all__ = [

    "MultiSymbolFeaturePipeline"

]