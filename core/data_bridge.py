"""
BIST AI LAB OMEGA
Data Bridge v1.0 PRO

Central data communication layer.

Responsibilities:

- Connect market data sources
- Normalize symbol data
- Feed feature pipeline
- Feed AI agents
- Feed prediction engine
- Cache market data
- Provide unified interface

Architecture:

DATA SOURCE
    |
    ↓
DATA BRIDGE
    |
    ├── Feature Engine
    ├── Prediction Agent
    ├── Technical Agent
    ├── Risk Agent
    └── AI Orchestrator

Compatible with:

- MultiSymbolDownloader
- MultiSymbolFeaturePipeline
- AIOrchestrator
- Dashboard API
"""

from __future__ import annotations


import logging

from datetime import datetime, timedelta


from typing import Dict, Any, Optional, List



logger = logging.getLogger(__name__)




class DataBridge:


    def __init__(
        self,
        downloader=None,
        feature_pipeline=None
    ):


        self.downloader = downloader

        self.feature_pipeline = feature_pipeline


        self.cache = {}


        self.cache_time = {}


        self.cache_duration = timedelta(

            minutes=15

        )


        self.version = (

            "1.0.0"

        )




    # =====================================================
    # SYMBOL NORMALIZE
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
    # FETCH SINGLE
    # =====================================================

    def fetch_symbol(
        self,
        symbol
    ):


        symbol = self.normalize_symbol(

            symbol

        )



        cached = self.get_cache(

            symbol

        )


        if cached:


            return cached




        try:


            if self.downloader:


                data = self.downloader.download_all(

                    [

                        symbol

                    ]

                )



                if isinstance(

                    data,

                    dict

                ):


                    result = data.get(

                        symbol

                    )



                    if result is not None:


                        self.set_cache(

                            symbol,

                            result

                        )


                        return result




        except Exception:


            logger.exception(

                "Data fetch failed %s",

                symbol

            )



        return None




    # =====================================================
    # FEATURE GENERATION
    # =====================================================

    def create_features(
        self,
        symbol
    ):


        raw = self.fetch_symbol(

            symbol

        )



        if raw is None:


            return None




        try:


            if self.feature_pipeline:


                result = self.feature_pipeline.process_all(

                    {

                        symbol:

                            raw

                    }

                )



                return result.get(

                    symbol

                )



        except Exception:


            logger.exception(

                "Feature creation failed %s",

                symbol

            )



        return raw




    # =====================================================
    # BATCH DATA
    # =====================================================

    def fetch_market(
        self,
        symbols: List[str]
    ):


        normalized = [

            self.normalize_symbol(x)

            for x in symbols

        ]



        result = {}



        for symbol in normalized:


            result[symbol] = self.create_features(

                symbol

            )



        return result