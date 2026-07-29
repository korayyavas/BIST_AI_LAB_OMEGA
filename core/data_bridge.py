"""
BIST AI LAB OMEGA
Data Bridge v1.3 PRO

Unified data communication layer.

Responsibilities:

- Connect downloader
- Connect feature pipeline
- Create model ready data
- Normalize market data flow
- Provide safe fallback

Architecture:

Downloader
    |
    ↓
Data Bridge
    |
    ↓
Feature Pipeline
    |
    ↓
AI Agents

"""

from __future__ import annotations


import logging


from datetime import datetime



logger = logging.getLogger(__name__)




class DataBridge:



    def __init__(
        self,
        downloader=None,
        feature_pipeline=None
    ):


        self.downloader = downloader


        self.feature_pipeline = feature_pipeline



        self.version = "1.3.0"




    # =====================================================
    # SINGLE SYMBOL FEATURE CREATION
    # =====================================================

    def create_features(
        self,
        symbol
    ):


        try:


            raw = self.download_symbol(

                symbol

            )



            if raw is None:


                return None




            if self.feature_pipeline:


                return self.feature_pipeline.process(

                    raw

                )



            return raw




        except Exception:


            logger.exception(

                "Feature creation failed %s",

                symbol

            )


            return None




    # =====================================================
    # DOWNLOAD SINGLE SYMBOL
    # =====================================================

    def download_symbol(
        self,
        symbol
    ):


        try:


            if self.downloader is None:


                return None



            if hasattr(

                self.downloader,

                "download"

            ):


                return self.downloader.download(

                    symbol

                )



            if hasattr(

                self.downloader,

                "download_symbol"

            ):


                return self.downloader.download_symbol(

                    symbol

                )



        except Exception:


            logger.exception(

                "Download failed %s",

                symbol

            )



        return None




    # =====================================================
    # MARKET DOWNLOAD
    # =====================================================

    def fetch_market(
        self,
        symbols
    ):


        result = {}



        if not symbols:


            return result



        for symbol in symbols:


            try:


                result[symbol] = self.create_features(

                    symbol

                )



            except Exception:


                result[symbol] = None



        return result

        # =====================================================
    # BATCH FEATURE PROCESSING
    # =====================================================

    def create_batch_features(
        self,
        symbols
    ):


        results = {}



        if not symbols:


            return results




        for symbol in symbols:


            try:


                results[symbol] = self.create_features(

                    symbol

                )



            except Exception:


                results[symbol] = None



        return results




    # =====================================================
    # DATA NORMALIZATION
    # =====================================================

    def normalize_market_data(
        self,
        data
    ):


        if data is None:


            return None



        try:


            if hasattr(

                data,

                "copy"

            ):


                return data.copy()



            if isinstance(

                data,

                dict

            ):


                return dict(

                    data

                )



        except Exception:


            pass



        return data




    # =====================================================
    # DATA STATUS
    # =====================================================

    def status(
        self
    ):


        return {


            "service":

                "OMEGA Data Bridge",


            "version":

                self.version,


            "downloader":

                self.downloader is not None,


            "feature_pipeline":

                self.feature_pipeline is not None,


            "status":

                "READY"

        }




    # =====================================================
    # HEALTH
    # =====================================================

    def health(
        self
    ):


        return {


            "service":

                "OMEGA Data Bridge",


            "version":

                self.version,


            "status":

                "READY",


            "timestamp":

                datetime.utcnow().isoformat()

        }




__all__ = [

    "DataBridge"

]