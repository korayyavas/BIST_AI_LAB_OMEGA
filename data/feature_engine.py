"""
BIST AI LAB OMEGA
Feature Engine v0.1

Professional feature generation layer.

Responsibilities:

- Technical indicator calculation
- Feature normalization
- AI model input preparation
- Multi symbol processing
- ML compatible output

Features:

- EMA20
- EMA50
- RSI14
- MACD
- MACD Signal
- ATR
- Momentum
- Volatility
- Returns

Compatible with:

- Prediction Agent
- Technical Agent
- Model Engine
- Market Brain
"""

from __future__ import annotations


import logging

from typing import Dict, Any


import pandas as pd



logger = logging.getLogger(__name__)




class FeatureEngine:


    def __init__(self):

        self.version = (
            "0.1.0"
        )



    # =====================================================
    # SINGLE FEATURE BUILD
    # =====================================================

    def transform(
        self,
        dataframe: pd.DataFrame
    ) -> pd.DataFrame:


        if dataframe is None:

            return pd.DataFrame()



        if dataframe.empty:

            return dataframe



        try:


            df = dataframe.copy()



            df = self._normalize_columns(

                df

            )



            # =============================
            # RETURNS
            # =============================

            df["RETURN"] = (

                df["CLOSE"]

                .pct_change()

                *

                100

            )



            # =============================
            # EMA
            # =============================

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



            # =============================
            # RSI
            # =============================

            df["RSI14"] = self._rsi(

                df["CLOSE"]

            )



            # =============================
            # MACD
            # =============================

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



            # =============================
            # ATR
            # =============================

            df["ATR"] = self._atr(

                df

            )



            # =============================
            # MOMENTUM
            # =============================

            df["MOMENTUM"] = (

                df["CLOSE"]

                -

                df["CLOSE"]

                .shift(

                    10

                )

            )



            # =============================
            # VOLATILITY
            # =============================

            df["VOLATILITY"] = (

                df["RETURN"]

                .rolling(

                    20

                )

                .std()

            )



            df = df.dropna()



            return df



        except Exception:


            logger.exception(

                "Feature generation failed"

            )


            return pd.DataFrame()




    # =====================================================
    # MULTI SYMBOL
    # =====================================================

    def transform_many(
        self,
        market_data: Dict[str,pd.DataFrame]
    ):


        result = {}



        for symbol,data in market_data.items():


            features = self.transform(

                data

            )


            if not features.empty:


                result[symbol] = features



        return result




    # =====================================================
    # RSI
    # =====================================================

    def _rsi(
        self,
        series,
        period=14
    ):


        delta = series.diff()



        gain = delta.clip(

            lower=0

        )


        loss = (

            -delta.clip(

                upper=0

            )

        )



        avg_gain = (

            gain.rolling(

                period

            )

            .mean()

        )


        avg_loss = (

            loss.rolling(

                period

            )

            .mean()

        )



        rs = (

            avg_gain /

            avg_loss

        )



        return (

            100 -

            (

                100 /

                (

                    1 +

                    rs

                )

            )

        )




    # =====================================================
    # ATR
    # =====================================================

    def _atr(
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

            df["HIGH"]

            -

            df["CLOSE"]

            .shift()

        ).abs()



        low_close = (

            df["LOW"]

            -

            df["CLOSE"]

            .shift()

        ).abs()



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



        return (

            true_range

            .rolling(

                period

            )

            .mean()

        )




    # =====================================================
    # COLUMN NORMALIZER
    # =====================================================

    def _normalize_columns(
        self,
        df
    ):


        df.columns = [

            str(x).upper()

            for x in df.columns

        ]


        return df




    # =====================================================
    # HEALTH
    # =====================================================

    def health(
        self
    ):


        return {


            "service":

                "OMEGA Feature Engine",


            "version":

                self.version,


            "status":

                "READY"

        }



__all__ = [

    "FeatureEngine"

]