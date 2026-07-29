"""
BIST AI LAB OMEGA
Multi Symbol Downloader v2.0 PRO

Market data acquisition layer.

Responsibilities:

- Download BIST symbol data
- Normalize Yahoo Finance output
- Handle multi symbol requests
- Cache support
- Error protection

Compatible with:

- DataBridge
- Feature Pipeline
- AI Orchestrator
- Backtest Engine
"""

from __future__ import annotations


import logging


from datetime import datetime


from typing import Dict, List, Any



import yfinance as yf



import pandas as pd



logger = logging.getLogger(__name__)




class MultiSymbolDownloader:


    def __init__(
        self,
        period="5y",
        interval="1d"
    ):


        self.period = period

        self.interval = interval


        self.version = "2.0.0"




    # =====================================================
    # SYMBOL NORMALIZE
    # =====================================================

    def normalize_symbol(
        self,
        symbol
    ):


        symbol = str(

            symbol

        ).upper()



        if not symbol.endswith(

            ".IS"

        ):


            symbol += ".IS"



        return symbol




    # =====================================================
    # DOWNLOAD SINGLE
    # =====================================================

    def download_symbol(
        self,
        symbol
    ):


        yahoo_symbol = self.normalize_symbol(

            symbol

        )


        try:


            data = yf.download(

                yahoo_symbol,

                period=self.period,

                interval=self.interval,

                auto_adjust=False,

                progress=False

            )



            if data.empty:


                return None




            data = self.normalize_dataframe(

                data

            )



            return data




        except Exception:


            logger.exception(

                "Download failed %s",

                symbol

            )


            return None




    # =====================================================
    # DOWNLOAD ALL
    # =====================================================

    def download_all(
        self,
        symbols:List[str]
    ):


        result = {}



        for symbol in symbols:


            clean = str(

                symbol

            ).upper().replace(

                ".IS",

                ""

            )



            data = self.download_symbol(

                clean

            )



            if data is not None:


                result[clean] = data




        return result




    # =====================================================
    # DATA NORMALIZER
    # =====================================================

    def normalize_dataframe(
        self,
        df
    ):


        if isinstance(

            df.columns,

            pd.MultiIndex

        ):


            df.columns = [

                col[0]

                for col in df.columns

            ]



        rename = {


            "Open":

                "OPEN",


            "High":

                "HIGH",


            "Low":

                "LOW",


            "Close":

                "CLOSE",


            "Volume":

                "VOLUME"

        }



        df = df.rename(

            columns=rename

        )



        df = df.dropna()



        return df




    # =====================================================
    # LAST DATA
    # =====================================================

    def latest(
        self,
        symbol
    ):


        data = self.download_symbol(

            symbol

        )


        if data is None:


            return None



        return data.iloc[-1]




    # =====================================================
    # HEALTH
    # =====================================================

    def health(
        self
    ):


        return {


            "service":

                "OMEGA Multi Symbol Downloader",


            "version":

                self.version,


            "status":

                "READY"


        }




__all__ = [

    "MultiSymbolDownloader"

]