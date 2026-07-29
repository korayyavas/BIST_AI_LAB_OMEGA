"""
BIST AI LAB OMEGA
Model Engine v0.1

Professional AI model management layer.

Responsibilities:

- Load AI models
- Model version control
- Feature validation
- Prediction generation
- Confidence calculation
- Ensemble ready architecture
- Model health monitoring

Compatible with:

- Prediction Agent
- Feature Engine
- AI Orchestrator
- Market Brain
"""

from __future__ import annotations


import os

import logging

from datetime import datetime

from typing import Dict, Any, List, Optional


import joblib

import pandas as pd



logger = logging.getLogger(__name__)




class ModelEngine:


    def __init__(
        self,
        model_path="models/bist_ai_model.pkl"
    ):


        self.model_path = model_path


        self.model = None


        self.features = []


        self.model_version = (
            "unknown"
        )


        self.ready = False


        self.load()




    # =====================================================
    # MODEL LOAD
    # =====================================================

    def load(
        self
    ):


        try:


            if not os.path.exists(

                self.model_path

            ):


                self.ready = False

                return



            bundle = joblib.load(

                self.model_path

            )



            if isinstance(

                bundle,

                dict

            ):


                self.model = bundle.get(

                    "model"

                )


                self.features = bundle.get(

                    "features",

                    []

                )


                self.model_version = bundle.get(

                    "version",

                    "unknown"

                )


            else:


                self.model = bundle



            self.ready = (

                self.model is not None

            )



        except Exception:


            logger.exception(

                "Model loading failed"

            )


            self.ready = False




    # =====================================================
    # SINGLE PREDICTION
    # =====================================================

    def predict(
        self,
        feature_data: pd.DataFrame
    ) -> Dict[str, Any]:


        if not self.ready:


            return self.default_result()



        try:


            latest = feature_data.tail(

                1

            ).copy()



            if self.features:


                X = latest[

                    self.features

                ]


            else:


                X = latest



            prediction = self.model.predict(

                X

            )[0]



            prediction = float(

                prediction

            )



            confidence = self.confidence(

                prediction

            )



            return {


                "prediction":

                    round(

                        prediction,

                        4

                    ),


                "confidence":

                    confidence,


                "signal":

                    self.signal(

                        prediction

                    ),


                "model_version":

                    self.model_version,


                "generated_at":

                    datetime.utcnow().isoformat()

            }



        except Exception:


            logger.exception(

                "Prediction failed"

            )


            return self.default_result()




    # =====================================================
    # MARKET PREDICTION
    # =====================================================

    def predict_market(
        self,
        dataset: Dict[str,pd.DataFrame]
    ):


        results = []



        for symbol,data in dataset.items():


            result = self.predict(

                data

            )


            result["symbol"] = symbol



            results.append(

                result

            )



        return sorted(

            results,

            key=lambda x:

            x.get(

                "confidence",

                0

            ),

            reverse=True

        )




    # =====================================================
    # CONFIDENCE
    # =====================================================

    def confidence(
        self,
        prediction
    ):


        try:


            confidence = 50 + (

                abs(

                    float(prediction)

                )

                *

                5

            )


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


        except Exception:


            return 50




    # =====================================================
    # SIGNAL
    # =====================================================

    def signal(
        self,
        prediction
    ):


        if prediction >= 5:

            return "STRONG_BUY"



        if prediction >= 2:

            return "BUY"



        if prediction <= -5:

            return "STRONG_SELL"



        if prediction < 0:

            return "SELL"



        return "HOLD"




    # =====================================================
    # DEFAULT
    # =====================================================

    def default_result(
        self
    ):


        return {


            "prediction":

                0,


            "confidence":

                50,


            "signal":

                "HOLD",


            "model_version":

                self.model_version

        }




    # =====================================================
    # MODEL INFO
    # =====================================================

    def info(
        self
    ):


        return {


            "model_path":

                self.model_path,


            "features":

                len(

                    self.features

                ),


            "version":

                self.model_version,


            "ready":

                self.ready

        }




    # =====================================================
    # HEALTH
    # =====================================================

    def health(
        self
    ):


        return {


            "service":

                "OMEGA Model Engine",


            "version":

                "0.1.0",


            "model_ready":

                self.ready,


            "status":

                "READY"

        }



__all__ = [

    "ModelEngine"

]