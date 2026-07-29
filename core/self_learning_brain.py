"""
BIST AI LAB OMEGA
Self Learning Brain v0.1

Adaptive AI improvement layer.

Responsibilities:

- Track AI predictions
- Compare prediction vs reality
- Calculate agent performance
- Update intelligence weights
- Learn from mistakes
- Improve future decisions

Compatible with:

- AI Orchestrator
- Fusion Engine
- Confidence Engine
- Backtest Brain
"""

from __future__ import annotations


from datetime import datetime

from typing import Dict, Any, List




class SelfLearningBrain:


    def __init__(self):


        self.version = (

            "0.1.0"

        )


        self.history = []


        self.agent_scores = {



            "Technical Agent":

                1.0,


            "Prediction Agent":

                1.0,


            "News Agent":

                1.0,


            "KAP Agent":

                1.0,


            "Risk Agent":

                1.0,


            "Macro Agent":

                1.0


        }




    # =====================================================
    # REGISTER PREDICTION
    # =====================================================

    def register(
        self,
        prediction
    ):


        self.history.append(


            {

                "prediction":

                    prediction,


                "date":

                    datetime.utcnow().isoformat()


            }

        )



    # =====================================================
    # LEARNING FROM RESULT
    # =====================================================

    def learn(
        self,
        prediction,
        actual_return
    ):


        predicted = float(

            prediction.get(

                "prediction",

                0

            )

        )


        actual = float(

            actual_return

        )



        error = abs(

            predicted -

            actual

        )



        accuracy = self._accuracy(

            error

        )



        self.history.append(

            {

                "predicted":

                    predicted,


                "actual":

                    actual,


                "accuracy":

                    accuracy,


                "date":

                    datetime.utcnow().isoformat()

            }

        )



        return {


            "accuracy":

                accuracy,


            "error":

                round(

                    error,

                    4

                ),


            "learning_status":

                "UPDATED"

        }




    # =====================================================
    # AGENT PERFORMANCE UPDATE
    # =====================================================

    def update_agent(
        self,
        agent,
        success
    ):


        if agent not in self.agent_scores:


            self.agent_scores[agent] = 1.0



        current = self.agent_scores[agent]



        if success:


            current += 0.05



        else:


            current -= 0.05



        self.agent_scores[agent] = max(

            0.1,

            min(

                2.0,

                current

            )

        )



        return self.agent_scores[agent]




    # =====================================================
    # DYNAMIC WEIGHTS
    # =====================================================

    def intelligence_weights(
        self
    ):


        total = sum(

            self.agent_scores.values()

        )



        if total == 0:


            return self.agent_scores



        return {


            key:

                round(

                    value /

                    total,

                    4

                )


            for key,value

            in self.agent_scores.items()

        }




    # =====================================================
    # ACCURACY
    # =====================================================

    def _accuracy(
        self,
        error
    ):


        accuracy = 100 - (

            error *

            10

        )



        return round(

            max(

                0,

                min(

                    100,

                    accuracy

                )

            ),

            2

        )




    # =====================================================
    # LEARNING REPORT
    # =====================================================

    def report(
        self
    ):


        return {


            "learning_cycles":

                len(

                    self.history

                ),


            "agent_performance":

                self.agent_scores,


            "dynamic_weights":

                self.intelligence_weights(),


            "version":

                self.version,


            "status":

                "SELF_LEARNING_ACTIVE"

        }




    # =====================================================
    # HEALTH
    # =====================================================

    def health(
        self
    ):


        return {


            "service":

                "OMEGA Self Learning Brain",


            "version":

                self.version,


            "status":

                "READY"

        }



__all__ = [

    "SelfLearningBrain"

]