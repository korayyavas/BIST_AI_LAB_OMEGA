"""
BIST AI LAB OMEGA
API Schemas v1.0 PRO

Production response models.

Compatible with:

- FastAPI
- Omega Container
- AI Orchestrator
- Dashboard
- Mobile Client
- External API

"""

from __future__ import annotations


from typing import List, Dict, Any, Optional


from datetime import datetime


from pydantic import BaseModel, Field




# =====================================================
# AGENT RESPONSE
# =====================================================


class AgentResponse(BaseModel):


    agent: str = Field(

        default=""

    )


    symbol: str = Field(

        default=""

    )


    score: Optional[float] = Field(

        default=50

    )


    data: Dict[str, Any] = Field(

        default_factory=dict

    )


    generated_at: Optional[str] = None




# =====================================================
# TECHNICAL RESPONSE
# =====================================================


class TechnicalResponse(BaseModel):


    agent: str = "Technical Agent"


    symbol: str


    technical_score: float = 50


    trend: str = "NEUTRAL"


    signals: List[str] = Field(

        default_factory=list

    )


    generated_at: Optional[str] = None




# =====================================================
# PREDICTION RESPONSE
# =====================================================


class PredictionResponse(BaseModel):


    agent: str = "Prediction Agent"


    symbol: str


    prediction: float = 0


    prediction_score: float = 50


    confidence: float = 50


    signal: str = "HOLD"


    generated_at: Optional[str] = None




# =====================================================
# NEWS RESPONSE
# =====================================================


class NewsResponse(BaseModel):


    agent: str = "News Agent"


    symbol: str


    news_score: float = 50


    sentiment: str = "NEUTRAL"


    news_count: int = 0


    impact: str = "LOW"


    generated_at: Optional[str] = None




# =====================================================
# KAP RESPONSE
# =====================================================


class KAPResponse(BaseModel):


    agent: str = "KAP Agent"


    symbol: str


    kap_score: float = 50


    disclosure_count: int = 0


    impact: str = "LOW"


    important_events: List[Any] = Field(

        default_factory=list

    )


    generated_at: Optional[str] = None




# =====================================================
# RISK RESPONSE
# =====================================================


class RiskResponse(BaseModel):


    agent: str = "Risk Agent"


    symbol: str


    risk_score: float = 50


    risk_level: str = "MEDIUM"


    warnings: List[str] = Field(

        default_factory=list

    )



# =====================================================
# MACRO RESPONSE
# =====================================================


class MacroResponse(BaseModel):


    agent: str = "Macro Agent"


    symbol: str


    macro_score: float = 50


    environment: str = "NEUTRAL"


    signals: List[str] = Field(

        default_factory=list

    )


    generated_at: Optional[str] = None

    # =====================================================
# CONFIDENCE RESPONSE
# =====================================================


class ConfidenceResponse(BaseModel):


    confidence: float = 50


    agreement: float = 50


    signal_consensus: float = 50


    level: str = "LOW"


    generated_at: Optional[str] = None


    version: str = "1.0.0"




# =====================================================
# REGIME RESPONSE
# =====================================================


class RegimeResponse(BaseModel):


    regime: str = "NEUTRAL"


    score: float = 50


    signals: List[str] = Field(

        default_factory=list

    )


    generated_at: Optional[str] = None




# =====================================================
# EXPLANATION RESPONSE
# =====================================================


class ExplanationResponse(BaseModel):


    decision: str = "HOLD"


    summary: str = ""


    strengths: List[str] = Field(

        default_factory=list

    )


    weaknesses: List[str] = Field(

        default_factory=list

    )


    risk_message: str = ""


    score: float = 50


    generated_at: Optional[str] = None




# =====================================================
# FINAL ANALYSIS RESPONSE
# =====================================================


class AnalysisResponse(BaseModel):


    symbol: str


    agents: List[Dict[str, Any]] = Field(

        default_factory=list

    )


    scores: Dict[str, Any] = Field(

        default_factory=dict

    )


    final_score: float = 50


    signal: str = "HOLD"


    confidence: Optional[Dict[str, Any]] = None


    regime: Optional[Dict[str, Any]] = None


    explanation: Optional[Dict[str, Any]] = None


    generated_at: Optional[str] = None


    version: str = "1.0.0"




# =====================================================
# MARKET RANKING RESPONSE
# =====================================================


class MarketRankingItem(BaseModel):


    symbol: str


    final_score: float = 50


    signal: str = "HOLD"


    confidence: float = 50


    regime: str = "NEUTRAL"




class MarketRankingResponse(BaseModel):


    market: str = "BIST"


    count: int = 0


    rankings: List[MarketRankingItem] = Field(

        default_factory=list

    )


    generated_at: Optional[str] = None




# =====================================================
# SYSTEM RESPONSE
# =====================================================


class SystemResponse(BaseModel):


    system: str = "BIST AI LAB OMEGA"


    version: str = "1.0.0"


    status: str = "ONLINE"


    services: List[str] = Field(

        default_factory=list

    )


    generated_at: Optional[str] = None




# =====================================================
# ERROR RESPONSE
# =====================================================


class ErrorResponse(BaseModel):


    error: str


    message: str


    timestamp: str = Field(

        default_factory=lambda:

        datetime.utcnow().isoformat()

    )




# =====================================================
# EXPORTS
# =====================================================


__all__ = [


    "AgentResponse",


    "TechnicalResponse",


    "PredictionResponse",


    "NewsResponse",


    "KAPResponse",


    "RiskResponse",


    "MacroResponse",


    "ConfidenceResponse",


    "RegimeResponse",


    "ExplanationResponse",


    "AnalysisResponse",


    "MarketRankingResponse",


    "MarketRankingItem",


    "SystemResponse",


    "ErrorResponse"

]