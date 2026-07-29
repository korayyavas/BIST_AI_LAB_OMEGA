"""
BIST AI LAB OMEGA
Market Data Engine v0.1

Professional market data layer.

Responsibilities:

- Multi symbol data download
- Historical OHLCV management
- Data normalization
- Cache support
- Clean dataframe output
- AI pipeline compatible structure

Compatible with:

- Feature Engine
- Prediction Agent
- Technical Agent
- Market Brain
"""

from __future__ import annotations


import logging

from datetime import datetime, timedelta

from typing import Dict, Any, List, Optional


import pandas as pd


import yfinance as yf



logger = logging.getLogger(__name__)




class MarketDataEngine:


    def __init__(
        self,
        period="5y",
        cache_minutes=30
    ):


        self.period = period

        self.cache_minutes = cache_minutes

        self.cache = {}

        self.version = (
            "0.1.0"
        )




    # =====================================================
    # SINGLE SYMBOL DOWNLOAD
    # =====================================================

    def fetch(
        self,
        symbol: str
    ) -> pd.DataFrame:


        symbol = self.normalize_symbol(

            symbol

        )



        cached = self._cache_get(

            symbol

        )



        if cached is not None:

            return cached




        try:


            ticker = (

                symbol

                +

                ".IS"

            )



            data = yf.download(

                ticker,

                period=self.period,

                progress=False

            )



            if data.empty:


                return pd.DataFrame()



            data = self.normalize_dataframe(

                data

            )



            self._cache_set(

                symbol,

                data

            )



            return data



        except Exception:


            logger.exception(

                "Market data failed %s",

                symbol

            )


            return pd.DataFrame()




    # =====================================================
    # MULTI SYMBOL DOWNLOAD
    # =====================================================

    def fetch_many(
        self,
        symbols: List[str]
    ) -> Dict[str,pd.DataFrame]:


        result = {}



        for symbol in symbols:


            data = self.fetch(

                symbol

            )


            if not data.empty:


                result[

                    self.normalize_symbol(symbol)

                ] = data



        return result




    # =====================================================
    # DATA NORMALIZER
    # =====================================================

    def normalize_dataframe(
        self,
        dataframe
    ):


        df = dataframe.copy()



        # yfinance multi-index fix

        if isinstance(

            df.columns,

            pd.MultiIndex

        ):


            df.columns = [

                x[0]

                for x in df.columns

            ]



        df.columns = [

            str(x).upper()

            for x in df.columns

        ]



        required = [

            "OPEN",

            "HIGH",

            "LOW",

            "CLOSE",

            "VOLUME"

        ]



        for col in required:


            if col not in df.columns:

                df[col] = None



        df = df.dropna(

            subset=[

                "CLOSE"

            ]

        )



        return df




    # =====================================================
    # LATEST DATA
    # =====================================================

    def latest(
        self,
        symbol
    ):


        data = self.fetch(

            symbol

        )



        if data.empty:

            return None



        return data.tail(

            1

        ).to_dict(

            "records"

        )[0]        
# =====================================================
    # CACHE
    #=====================================================

    def _cache_get(
        self,
        key
    ):


        item = self.cache.get(

            key

        )


        if not item:

            return None



        created,data = item



        if (

            datetime.utcnow()

            -

            created

        ) > timedelta(

            minutes=self.cache_minutes

        ):


            del self.cache[key]

            return None



        return data




    def _cache_set(
        self,
        key,
        value
    ):


        self.cache[key] = (

            datetime.utcnow(),

            value

        )




    # =====================================================
    # SYMBOL NORMALIZER
    # =====================================================

    def normalize_symbol(
        self,
        symbol
    ):


        return str(

            symbol

        ).upper().replace(

            ".IS",

            ""

        )




    # =====================================================
    # HEALTH
    # =====================================================

    def health(
        self
    ):


        return {


            "service":

                "OMEGA Market Data Engine",


            "version":

                self.version,


            "cache_size":

                len(

                    self.cache

                ),


            "status":

                "READY"

        }




__all__ = [

    "MarketDataEngine"

]   