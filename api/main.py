"""
BIST AI LAB OMEGA
API Gateway v1.0 PRO

Production API Layer

Architecture:

Client
 |
 API
 |
 Omega Container
 |
 AI Orchestrator
 |
 Agents
 |
 Intelligence Engine
"""

from __future__ import annotations


from fastapi import FastAPI


from datetime import datetime


from core.omega_container import OmegaContainer




app = FastAPI(

    title="BIST AI LAB OMEGA",

    description="Multi Agent AI Investment Intelligence Platform",

    version="1.0.0"

)




# =====================================================
# OMEGA INSTANCE
# =====================================================


omega = OmegaContainer()




# =====================================================
# ROOT
# =====================================================


@app.get("/")
def root():


    return {


        "system":

            "BIST AI LAB OMEGA",


        "version":

            "1.0.0",


        "status":

            "ONLINE",


        "time":

            datetime.utcnow().isoformat()

    }




# =====================================================
# HEALTH
# =====================================================


@app.get("/health")
def health():


    return {


        "api":

            "ONLINE",


        "omega":

            omega.health(),


        "time":

            datetime.utcnow().isoformat()

    }




# =====================================================
# SINGLE STOCK ANALYSIS
# =====================================================


@app.get("/analysis/{symbol}")
def analysis(
    symbol:str
):


    return omega.analyze(

        symbol

    )




# =====================================================
# MARKET ANALYSIS
# =====================================================


@app.post("/market/analyze")
def market_analysis(
    symbols:list[str]
):


    return omega.analyze_market(

        symbols

    )




# =====================================================
# SYSTEM
# =====================================================


@app.get("/system")
def system():


    return {


        "architecture":

            "OMEGA MULTI AGENT AI",


        "layers":

            [


                "Data Bridge",


                "Omega Container",


                "AI Orchestrator",


                "Agent Layer",


                "Fusion Engine",


                "Confidence Engine",


                "Explain Engine"


            ],


        "status":

            "PRODUCTION_READY"

    }




# =====================================================
# SERVICE LIST
# =====================================================


@app.get("/services")
def services():


    return {


        "services":

            omega.health()

    }