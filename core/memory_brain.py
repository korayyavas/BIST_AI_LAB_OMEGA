"""
BIST AI LAB OMEGA
Memory Brain v0.1

Long term AI memory layer.

Responsibilities:

- Store analysis history
- Store prediction results
- Store decision history
- Track stock behavior
- Provide experience retrieval
- Feed self learning system

Compatible with:

- Self Learning Brain
- AI Orchestrator
- Fusion Engine
- Backtest Brain
"""

from __future__ import annotations


import json

import os

from datetime import datetime

from typing import Dict, Any, List, Optional




class MemoryBrain:


    def __init__(
        self,
        memory_file="omega_memory.json"
    ):


        self.memory_file = memory_file


        self.memory = {


            "analysis":

                [],


            "predictions":

                [],


            "decisions":

                [],


            "performance":

                []


        }


        self.version = (

            "0.1.0"

        )


        self.load()




    # =====================================================
    # LOAD MEMORY
    # =====================================================

    def load(
        self
    ):


        try:


            if os.path.exists(

                self.memory_file

            ):


                with open(

                    self.memory_file,

                    "r",

                    encoding="utf-8"

                ) as f:


                    self.memory = json.load(

                        f

                    )



        except Exception:


            self.memory = {


                "analysis":[],

                "predictions":[],

                "decisions":[],

                "performance":[]

            }




    # =====================================================
    # SAVE MEMORY
    # =====================================================

    def save(
        self
    ):


        try:


            with open(

                self.memory_file,

                "w",

                encoding="utf-8"

            ) as f:


                json.dump(

                    self.memory,

                    f,

                    indent=2,

                    ensure_ascii=False,

                    default=str

                )


        except Exception:


            pass




    # =====================================================
    # STORE ANALYSIS
    # =====================================================

    def remember_analysis(
        self,
        data: Dict[str,Any]
    ):


        self.memory["analysis"].append(

            {

                "data":

                    data,


                "time":

                    datetime.utcnow().isoformat()

            }

        )


        self.save()




    # =====================================================
    # STORE PREDICTION
    # =====================================================

    def remember_prediction(
        self,
        data: Dict[str,Any]
    ):


        self.memory["predictions"].append(

            {

                "data":

                    data,


                "time":

                    datetime.utcnow().isoformat()

            }

        )


        self.save()




    # =====================================================
    # STORE DECISION
    # =====================================================

    def remember_decision(
        self,
        data: Dict[str,Any]
    ):


        self.memory["decisions"].append(

            {

                "data":

                    data,


                "time":

                    datetime.utcnow().isoformat()

            }

        )


        self.save()




    # =====================================================
    # PERFORMANCE MEMORY
    # =====================================================

    def remember_performance(
        self,
        data: Dict[str,Any]
    ):


        self.memory["performance"].append(

            {

                "data":

                    data,


                "time":

                    datetime.utcnow().isoformat()

            }

        )


        self.save()




    # =====================================================
    # SYMBOL HISTORY
    # =====================================================

    def symbol_history(
        self,
        symbol
    ):


        symbol = str(

            symbol

        ).upper()



        result = []



        for item in self.memory["analysis"]:


            data = item.get(

                "data",

                {}

            )


            if data.get(

                "symbol"

            ) == symbol:


                result.append(

                    item

                )



        return result




    # =====================================================
    # EXPERIENCE SEARCH
    # =====================================================

    def find_experience(
        self,
        symbol,
        limit=20
    ):


        history = self.symbol_history(

            symbol

        )


        return history[-limit:]




    # =====================================================
    # MEMORY SUMMARY
    # =====================================================

    def summary(
        self
    ):


        return {


            "analysis_count":

                len(

                    self.memory["analysis"]

                ),


            "prediction_count":

                len(

                    self.memory["predictions"]

                ),


            "decision_count":

                len(

                    self.memory["decisions"]

                ),


            "performance_count":

                len(

                    self.memory["performance"]

                ),


            "version":

                self.version

        }




    # =====================================================
    # CLEAR MEMORY
    # =====================================================

    def clear(
        self
    ):


        self.memory = {


            "analysis":[],

            "predictions":[],

            "decisions":[],

            "performance":[]

        }


        self.save()




    # =====================================================
    # HEALTH
    # =====================================================

    def health(
        self
    ):


        return {


            "service":

                "OMEGA Memory Brain",


            "version":

                self.version,


            "memory_file":

                self.memory_file,


            "status":

                "READY"

        }



__all__ = [

    "MemoryBrain"

]