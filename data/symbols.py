"""
BIST AI LAB OMEGA
Symbol Registry v0.1

Market universe management layer.

Responsibilities:

- BIST symbol registry
- BIST30 support
- BIST100 ready structure
- Sector mapping
- Symbol normalization
- AI universe management

Compatible with:

- Data Engine
- Market Brain
- AI Orchestrator
- MCP
"""

from __future__ import annotations

from typing import Dict, List



class SymbolRegistry:


    def __init__(self):


        self.version = (
            "0.1.0"
        )


        self.symbols = {

            "BIST30":

                self._bist30(),


            "BIST100":

                self._bist100()

        }



    # =====================================================
    # BIST30
    # =====================================================

    def _bist30(
        self
    ):


        return [

            "AEFES",
            "AKBNK",
            "ASELS",
            "ASTOR",
            "BIMAS",
            "DOHOL",
            "EKGYO",
            "ENKAI",
            "EREGL",
            "FROTO",
            "GARAN",
            "GUBRF",
            "HALKB",
            "ISCTR",
            "KCHOL",
            "ASTOR",
            "PEKGY",
            "KRDMD",
            "MGROS",
            "ODAS",
            "OYAKC",
            "PETKM",
            "PGSUS",
            "SAHOL",
            "SASA",
            "SISE",
            "TCELL",
            "THYAO",
            "TOASO",
            "TUPRS"

        ]



    # =====================================================
    # BIST100 PLACEHOLDER
    # =====================================================

    def _bist100(
        self
    ):


        return []




    # =====================================================
    # GET MARKET
    # =====================================================

    def get(
        self,
        market="BIST30"
    ):


        return self.symbols.get(

            market.upper(),

            []

        )




    # =====================================================
    # NORMALIZE
    # =====================================================

    def normalize(
        self,
        symbol
    ):


        if not symbol:

            return None



        symbol = str(

            symbol

        ).upper()



        return symbol.replace(

            ".IS",

            ""

        )




    # =====================================================
    # VALIDATE
    # =====================================================

    def exists(
        self,
        symbol
    ):


        symbol = self.normalize(

            symbol

        )


        for market in self.symbols.values():


            if symbol in market:

                return True



        return False




    # =====================================================
    # ADD SYMBOL
    # =====================================================

    def add(
        self,
        symbol,
        market="CUSTOM"
    ):


        symbol = self.normalize(

            symbol

        )


        if market not in self.symbols:

            self.symbols[market] = []



        if symbol not in self.symbols[market]:

            self.symbols[market].append(

                symbol

            )



    # =====================================================
    # REMOVE
    # =====================================================

    def remove(
        self,
        symbol,
        market="CUSTOM"
    ):


        symbol = self.normalize(

            symbol

        )


        if market in self.symbols:


            if symbol in self.symbols[market]:

                self.symbols[market].remove(

                    symbol

                )




    # =====================================================
    # SECTOR MAP
    # =====================================================

    def sector_map(
        self
    ) -> Dict[str,str]:


        return {


            "ASELS":

                "DEFENSE",


            "THYAO":

                "TRANSPORT",


            "TUPRS":

                "ENERGY",


            "EREGL":

                "STEEL",


            "AKBNK":

                "BANKING",


            "GARAN":

                "BANKING",


            "KCHOL":

                "HOLDING",


            "SAHOL":

                "HOLDING",


            "SISE":

                "INDUSTRY"


        }




    # =====================================================
    # HEALTH
    # =====================================================

    def health(
        self
    ):


        return {


            "service":

                "OMEGA Symbol Registry",


            "version":

                self.version,


            "markets":

                list(

                    self.symbols.keys()

                ),


            "status":

                "READY"

        }




__all__ = [

    "SymbolRegistry"

]