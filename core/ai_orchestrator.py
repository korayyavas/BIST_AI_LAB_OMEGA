"""
BIST AI LAB OMEGA
AI Orchestrator v1.1 PRO

Central intelligence controller.

Pipeline:

DATA
 |
AGENTS
 |
FUSION
 |
CONFIDENCE
 |
REGIME
 |
EXPLAIN
 |
FINAL AI REPORT


Compatible with:

- Omega Container
- API Gateway
- Dashboard
- Portfolio Brain
"""

from __future__ import annotations


from datetime import datetime


import logging



logger = logging.getLogger(__name__)




class AIOrchestrator:



    def __init__(
        self,
        technical_agent=None,
        prediction_agent=None,
        news_agent=None,
        kap_agent=None,
        risk_agent=None,
        macro_agent=None,
        fusion_engine=None,
        confidence_engine=None,
        explain_engine=None,
        regime_engine=None
    ):


        self.technical_agent = technical_agent

        self.prediction_agent = prediction_agent

        self.news_agent = news_agent

        self.kap_agent = kap_agent

        self.risk_agent = risk_agent

        self.macro_agent = macro_agent


        self.fusion_engine = fusion_engine

        self.confidence_engine = confidence_engine

        self.explain_engine = explain_engine

        self.regime_engine = regime_engine



        self.version = "1.1.0"




    # =====================================================
    # SINGLE SYMBOL ANALYSIS
    # =====================================================

    def analyze(
        self,
        symbol,
        market_data=None
    ):


        symbol = str(

            symbol

        ).upper()



        agents = []



        agents.extend(

            self.run_agents(

                symbol,

                market_data

            )

        )



        intelligence = self.run_fusion(

            symbol,

            agents

        )



        confidence = self.run_confidence(

            agents

        )


        intelligence["confidence"] = confidence



        regime = self.run_regime(

            [

                intelligence

            ]

        )


        intelligence["regime"] = regime




        explanation = self.run_explain(

            intelligence

        )


        intelligence["explanation"] = explanation




        intelligence.update(


            {


                "agents":

                    agents,


                "orchestrator_version":

                    self.version,


                "generated_at":

                    datetime.utcnow().isoformat()


            }

        )



        return intelligence




    # =====================================================
    # AGENT EXECUTION
    # =====================================================

    def run_agents(
        self,
        symbol,
        market_data
    ):


        results = []



        agent_list = [


            self.technical_agent,

            self.prediction_agent,

            self.news_agent,

            self.kap_agent,

            self.risk_agent,

            self.macro_agent

        ]



        for agent in agent_list:


            if agent is None:


                continue



            try:


                result = agent.analyze(

                    symbol,

                    market_data

                )


                results.append(

                    result

                )


            except Exception:


                logger.exception(

                    "Agent failed"

                )



        return results




    # =====================================================
    # FUSION
    # =====================================================

    def run_fusion(
        self,
        symbol,
        agents
    ):


        if self.fusion_engine:


            return self.fusion_engine.fuse(

                symbol,

                agents

            )



        return {


            "symbol":

                symbol,


            "final_score":

                50,


            "signal":

                "HOLD"

        }




    # =====================================================
    # CONFIDENCE
    # =====================================================

    def run_confidence(
        self,
        agents
    ):


        if self.confidence_engine:


            result = self.confidence_engine.calculate(

                agents

            )



            # Fake confidence protection

            if self.is_empty_data(

                agents

            ):


                result["confidence"] = min(

                    result.get(

                        "confidence",

                        50

                    ),

                    55

                )


                result["level"] = "LOW"



            return result



        return {


            "confidence":

                50,


            "level":

                "LOW"

        }




    # =====================================================
    # REGIME
    # =====================================================

    def run_regime(
        self,
        reports
    ):


        if self.regime_engine:


            return self.regime_engine.analyze(

                reports

            )



        return {


            "regime":

                "NEUTRAL"

        }




    # =====================================================
    # EXPLAIN
    # =====================================================

    def run_explain(
        self,
        intelligence
    ):


        if self.explain_engine:


            return self.explain_engine.explain(

                intelligence

            )



        return {}




    # =====================================================
    # DATA CHECK
    # =====================================================

    def is_empty_data(
        self,
        agents
    ):


        if not agents:


            return True



        defaults = 0



        for agent in agents:


            values = str(

                agent

            )



            if (

                "50"

                in values

                and

                "0"

                in values

            ):


                defaults += 1




        return defaults >= len(

            agents

        )




    # =====================================================
    # MARKET ANALYSIS
    # =====================================================

    def analyze_market(
        self,
        symbols,
        market_data=None
    ):


        results = []



        for symbol in symbols:


            data = None



            if isinstance(

                market_data,

                dict

            ):


                data = market_data.get(

                    symbol

                )



            results.append(

                self.analyze(

                    symbol,

                    data

                )

            )



        return sorted(

            results,

            key=lambda x:

            x.get(

                "final_score",

                0

            ),

            reverse=True

        )




    # =====================================================
    # HEALTH
    # =====================================================

    def health(
        self
    ):


        return {


            "service":

                "OMEGA AI Orchestrator",


            "version":

                self.version,


            "status":

                "READY"

        }




__all__ = [

    "AIOrchestrator"

]