"""
BIST AI LAB OMEGA
API Gateway v1.3 PRO

Production FastAPI Layer.

Architecture:

CLIENT
 |
FASTAPI
 |
OMEGA CONTAINER
 |
AI ORCHESTRATOR
 |
AGENTS
 |
INTELLIGENCE ENGINE

Features:

- Typed responses
- Production schemas
- Health monitoring
- Analysis endpoint
- Market endpoint
"""

from __future__ import annotations


from datetime import datetime


from fastapi import FastAPI, HTTPException



from core.omega_container import OmegaContainer



from api.schemas import (

    AnalysisResponse,

    SystemResponse,

    ErrorResponse,

    MarketRankingResponse

)




# =====================================================
# APPLICATION
# =====================================================


app = FastAPI(


    title="BIST AI LAB OMEGA",


    description=(

        "Multi Agent AI Investment Intelligence Platform"

    ),


    version="1.3.0"

)




# =====================================================
# OMEGA INSTANCE
# =====================================================


omega = OmegaContainer()




# =====================================================
# ROOT
# =====================================================


@app.get(

    "/",

    response_model=SystemResponse

)

def root():


    return {


        "system":

            "BIST AI LAB OMEGA",


        "version":

            "1.3.0",


        "status":

            "ONLINE",


        "services":

            omega.health().get(

                "services",

                []

            ),


        "generated_at":

            datetime.utcnow().isoformat()

    }




# =====================================================
# HEALTH
# =====================================================


@app.get(

    "/health"

)

def health():


    return {


        "api":

            "ONLINE",


        "omega":

            omega.health(),


        "timestamp":

            datetime.utcnow().isoformat()

    }




# =====================================================
# SYSTEM
# =====================================================


@app.get(

    "/system",

    response_model=SystemResponse

)

def system():


    data = omega.health()



    return {


        "system":

            "BIST AI LAB OMEGA",


        "version":

            data.get(

                "version",

                "1.3.0"

            ),


        "status":

            data.get(

                "status",

                "ONLINE"

            ),


        "services":

            data.get(

                "services",

                []

            ),


        "generated_at":

            datetime.utcnow().isoformat()

    }




# =====================================================
# SINGLE SYMBOL ANALYSIS
# =====================================================


@app.get(

    "/analysis/{symbol}",

    response_model=AnalysisResponse

)

def analysis(

    symbol: str

):


    try:


        result = omega.analyze(

            symbol

        )


        return result



    except Exception as e:


        raise HTTPException(

            status_code=500,

            detail=str(e)

        )

    # =====================================================
# MARKET ANALYSIS
# =====================================================


@app.post(

    "/market/analyze",

    response_model=MarketRankingResponse

)

def market_analysis(

    symbols: list[str]

):


    try:


        results = omega.analyze_market(

            symbols

        )



        return {


            "market":

                "BIST",


            "count":

                len(results),


            "rankings":

                results,


            "generated_at":

                datetime.utcnow().isoformat()

        }



    except Exception as e:


        raise HTTPException(

            status_code=500,

            detail=str(e)

        )




# =====================================================
# SERVICE STATUS
# =====================================================


@app.get(

    "/services"

)

def services():


    return {


        "container":

            omega.health(),


        "time":

            datetime.utcnow().isoformat()

    }




# =====================================================
# CONTAINER ANALYSIS DEBUG
# =====================================================


@app.get(

    "/debug/{symbol}"

)

def debug_analysis(

    symbol:str

):


    try:


        data = omega.get(

            "data_bridge"

        )



        features = data.create_features(

            symbol

        )



        return {


            "symbol":

                symbol.upper(),


            "feature_available":

                features is not None,


            "feature_columns":

                list(

                    features.columns

                )

                if hasattr(

                    features,

                    "columns"

                )

                else [],


            "generated_at":

                datetime.utcnow().isoformat()

        }



    except Exception as e:


        return {


            "error":

                str(e)

        }




# =====================================================
# GLOBAL ERROR FORMAT
# =====================================================


@app.exception_handler(

    Exception

)

async def global_exception_handler(

    request,

    exc

):


    return {


        "error":

            "OMEGA_API_ERROR",


        "message":

            str(exc),


        "timestamp":

            datetime.utcnow().isoformat()

    }