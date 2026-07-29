"""
BIST AI LAB OMEGA
Core Configuration

Central configuration layer.
"""

from __future__ import annotations

import os
from pathlib import Path


# =====================================================
# PROJECT ROOT
# =====================================================

BASE_DIR = Path(
    __file__
).resolve().parent.parent



# =====================================================
# DATA PATHS
# =====================================================

DATA_DIR = BASE_DIR / "data"

MODEL_DIR = BASE_DIR / "models"

MEMORY_DIR = BASE_DIR / "memory"

REPORT_DIR = BASE_DIR / "reports"



for directory in [
    DATA_DIR,
    MODEL_DIR,
    MEMORY_DIR,
    REPORT_DIR,
]:
    directory.mkdir(
        exist_ok=True
    )



# =====================================================
# SYSTEM INFO
# =====================================================

PROJECT_NAME = (
    "BIST AI LAB OMEGA"
)


VERSION = (
    "0.1.0"
)


ENVIRONMENT = os.getenv(
    "ENVIRONMENT",
    "development"
)



# =====================================================
# MARKET SETTINGS
# =====================================================

DEFAULT_MARKET = (
    "BIST"
)


DEFAULT_SYMBOL_COUNT = 30


DEFAULT_PERIOD = (
    "5y"
)



# =====================================================
# AI SETTINGS
# =====================================================

AI_CONFIG = {

    "prediction_weight": 0.30,

    "technical_weight": 0.20,

    "news_weight": 0.15,

    "kap_weight": 0.10,

    "risk_weight": 0.15,

    "learning_weight": 0.10,

}



# =====================================================
# MEMORY SETTINGS
# =====================================================

MEMORY_CONFIG = {

    "enabled": True,

    "max_history_days": 3650,

}



# =====================================================
# MCP SETTINGS
# =====================================================

MCP_CONFIG = {

    "enabled": True,

    "server_name":
        "BIST_AI_LAB_OMEGA_MCP",

}



# =====================================================
# PORTFOLIO SETTINGS
# =====================================================

PORTFOLIO_CONFIG = {

    "initial_capital": 100000,

    "max_position_ratio": 0.35,

    "default_stop_loss": 0.07,

}



# =====================================================
# GLOBAL CONFIG
# =====================================================

OMEGA_CONFIG = {

    "project":
        PROJECT_NAME,

    "version":
        VERSION,

    "environment":
        ENVIRONMENT,

    "market":
        DEFAULT_MARKET,

    "ai":
        AI_CONFIG,

    "memory":
        MEMORY_CONFIG,

    "mcp":
        MCP_CONFIG,

    "portfolio":
        PORTFOLIO_CONFIG,

}



def get_config():

    return OMEGA_CONFIG



__all__ = [

    "BASE_DIR",

    "DATA_DIR",

    "MODEL_DIR",

    "MEMORY_DIR",

    "REPORT_DIR",

    "OMEGA_CONFIG",

    "get_config",

]