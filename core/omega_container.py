"""
BIST AI LAB OMEGA
Omega Container v1.2 PRO

Regime Engine integrated.
"""

from __future__ import annotations


import logging



from data.multi_symbol_downloader import (
    MultiSymbolDownloader
)


from data.multi_symbol_feature_pipeline import (
    MultiSymbolFeaturePipeline
)



from core.data_bridge import DataBridge


from core.ai_orchestrator import AIOrchestrator



from agents import (

    TechnicalAgent,

    PredictionAgent,

    NewsAgent,

    KAPAgent,

    RiskAgent,

    MacroAgent

)



from intelligence import (

    FusionEngine,

    ConfidenceEngine,

    ExplainEngine,

    RegimeEngine

)



logger = logging.getLogger(__name__)




class OmegaContainer:



    def __init__(self):


        self.version = "1.2.0"


        self.services = {}


        self.initialize()




    # =====================================================
    # INITIALIZE
    # =====================================================

    def initialize(self):


        self.create_data_layer()


        self.create_intelligence()


        self.create_agents()


        self.create_brain()




    # =====================================================
    # DATA LAYER
    # =====================================================

    def create_data_layer(self):


        downloader = MultiSymbolDownloader(

            period="5y",

            interval="1d"

        )


        feature_pipeline = MultiSymbolFeaturePipeline()



        self.services["downloader"] = downloader


        self.services["feature_pipeline"] = feature_pipeline



        self.services["data_bridge"] = DataBridge(

            downloader=downloader,

            feature_pipeline=feature_pipeline

        )




    # =====================================================
    # INTELLIGENCE
    # =====================================================

    def create_intelligence(self):


        self.services["fusion"] = FusionEngine()


        self.services["confidence"] = ConfidenceEngine()


        self.services["explain"] = ExplainEngine()


        self.services["regime"] = RegimeEngine()




    # =====================================================
    # AGENTS
    # =====================================================

    def create_agents(self):


        self.services["technical_agent"] = TechnicalAgent()


        self.services["prediction_agent"] = PredictionAgent()


        self.services["news_agent"] = NewsAgent()


        self.services["kap_agent"] = KAPAgent()


        self.services["risk_agent"] = RiskAgent()


        self.services["macro_agent"] = MacroAgent()




    # =====================================================
    # BRAIN
    # =====================================================

    def create_brain(self):


        self.services["orchestrator"] = AIOrchestrator(


            technical_agent=

                self.services["technical_agent"],


            prediction_agent=

                self.services["prediction_agent"],


            news_agent=

                self.services["news_agent"],


            kap_agent=

                self.services["kap_agent"],


            risk_agent=

                self.services["risk_agent"],


            macro_agent=

                self.services["macro_agent"],



            fusion_engine=

                self.services["fusion"],



            confidence_engine=

                self.services["confidence"],



            explain_engine=

                self.services["explain"],



            regime_engine=

                self.services["regime"]

        )




    # =====================================================
    # ACCESS
    # =====================================================

    def get(
        self,
        name
    ):


        return self.services.get(

            name

        )




    # =====================================================
    # ANALYSIS
    # =====================================================

    def analyze(
        self,
        symbol
    ):


        bridge = self.services["data_bridge"]


        data = bridge.create_features(

            symbol

        )



        return self.services["orchestrator"].analyze(

            symbol,

            data

        )




    # =====================================================
    # MARKET
    # =====================================================

    def analyze_market(
        self,
        symbols
    ):


        bridge = self.services["data_bridge"]


        market_data = bridge.fetch_market(

            symbols

        )



        return self.services["orchestrator"].analyze_market(

            symbols,

            market_data

        )




    # =====================================================
    # HEALTH
    # =====================================================

    def health(
        self
    ):


        return {


            "service":

                "OMEGA Container",


            "version":

                self.version,


            "services":

                list(

                    self.services.keys()

                ),


            "status":

                "READY"

        }




__all__ = [

    "OmegaContainer"

]