from typing import Final

ECOTOUCH: Final = "ECOTOUCH"
EASYCON: Final = "EASYCON"
HEATING_MODES: Final = {
    0: "hm0",
    1: "hm1",
    2: "hm2",
    3: "hm3",
    4: "hm4",
    5: "hm5"
}
SERIES: Final = [
    "Custom",
    "Ai1",
    "Ai1+",
    "AiQE",
    "DS 5023",
    "DS 5027Ai",
    "DS 5051",
    "DS 5050T",
    "DS 5110T",
    "DS 5240",
    "DS 6500",
    "DS 502xAi",
    "DS 505x",
    "DS 505xT",
    "DS 51xxT",
    "DS 509x",
    "DS 51xx",
    "EcoTouch Ai1 Geo",
    "EcoTouch DS 5027 Ai",
    "EnergyDock",
    "Basic Line Ai1 Geo",
    "EcoTouch DS 5018 Ai",
    "EcoTouch DS 5050T",
    "EcoTouch DS 5112.5 DT",
    "EcoTouch 5029 Ai",
    "DS 6500 D (Duo)",
    "ET 6900 Q",
    "EcoTouch Geo Inverter",
    "EcoTouch 5110TWR",
    "EcoTouch 5240TWR",
    "EcoTouch 5240T",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "Ai QL / WP QL",
    "WPQL-K",
    "EcoTouch Ai1 Air",
    "EcoTouch Ai1 Air",
    "EcoTouch MB 7010",
    "EcoTouch DA 5018 Ai",
    "EcoTouch Air LCI",
    "EcoTouch Ai1 Air K1.1",
    "EcoTouch DA 5018 Ai K1.1",
    "EcoTouch Ai1 Air K2",
    "EcoTouch DA 5018 Ai K2",
    "EcoTouch Ai1 Air 2018",
    "Basic Line Ai1 Air",
    "Basic Line Split",
    "Basic Line Split W",
    "EcoTouch Ai1 Air LC S",
    "EcoTouch Air Kaskade",
    "EcoTouch Ai1 Air K1.2",
    "EcoTouch DA 5018 Ai K1.2",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
]
SYSTEM_IDS: Final = [
    "Ai1 5005.4",
    "Ai1 5006.4",
    "Ai1 5007.4",
    "Ai1 5008.4",
    "Ai1+ 5006.3",
    "Ai1+ 5007.3",
    "Ai1+ 5009.3",
    "Ai1+ 5011.3",
    "Ai1+ 5006.3 (1x230V)",
    "Ai1+ 5007.3 (1x230V)",
    "Ai1+ 5009.3 (1x230V)",
    "Ai1+ 5011.3 (1x230V)",
    "DS 5006.3",
    "DS 5008.3",
    "DS 5009.3",
    "DS 5011.3",
    "DS 5014.3",
    "DS 5017.3",
    "DS 5020.3",
    "DS 5023.3",
    "DS 5006.3 (1x230V)",
    "DS 5008.3 (1x230V)",
    "DS 5009.3 (1x230V)",
    "DS 5011.3 (1x230V)",
    "DS 5014.3 (1x230V)",
    "DS 5017.3 (1x230V)",
    "DS 5006.4",
    "DS 5008.4",
    "DS 5009.4",
    "DS 5011.4",
    "DS 5014.4",
    "DS 5017.4",
    "DS 5020.4",
    "DS 5023.4",
    "DS 5007.3 Ai",
    "DS 5009.3 Ai",
    "DS 5010.3 Ai",
    "DS 5012.3 Ai",
    "DS 5015.3 Ai",
    "DS 5019.3 Ai",
    "DS 5022.3 Ai",
    "DS 5025.3 Ai",
    "DS 5007.3 Ai (1x230V)",
    "DS 5009.3 Ai (1x230V)",
    "DS 5010.3 Ai (1x230V)",
    "DS 5012.3 Ai (1x230V)",
    "DS 5015.3 Ai (1x230V)",
    "DS 5019.3 Ai (1x230V)",
    "DS 5007.4 Ai",
    "DS 5009.4 Ai",
    "DS 5010.4 Ai",
    "DS 5012.4 Ai",
    "DS 5015.4 Ai",
    "DS 5019.4 Ai",
    "DS 5022.4 Ai",
    "DS 5025.4 Ai",
    "DS 5007.4 Ai (1x230V)",
    "DS 5009.4 Ai (1x230V)",
    "DS 5010.4 Ai (1x230V)",
    "DS 5012.4 Ai (1x230V)",
    "DS 5015.4 Ai (1x230V)",
    "DS 5030.3",
    "DS 5034.3",
    "DS 5043.3",
    "DS 5051.3",
    "DS 5030.4",
    "DS 5034.4",
    "DS 5043.4",
    "DS 5051.4",
    "DS 5030.3 T",
    "DS 5037.3 T",
    "DS 5044.3 T",
    "DS 5050.3 T",
    "DS 5030.4 T",
    "DS 5037.4 T",
    "DS 5044.4 T",
    "DS 5050.4 T",
    "DS 5062.3 T",
    "DS 5072.3 T",
    "DS 5089.3 T",
    "DS 5109.3 T",
    "DS 5062.4 T",
    "DS 5072.4 T",
    "DS 5089.4 T",
    "DS 5109.4 T",
    "DS 5118.3",
    "DS 5136.3",
    "DS 5161.3",
    "DS 5162.3",
    "DS 5193.3",
    "DS 5194.3",
    "DS 5231.3",
    "DS 5118.4",
    "DS 5136.4",
    "DS 5161.4",
    "DS 5162.4",
    "DS 5194.4",
    "DS 6237.3",
    "DS 6271.3",
    "DS 6299.3",
    "DS 6388.3",
    "DS 6438.3",
    "DS 6485.3",
    "DS 6237.4",
    "DS 6271.4",
    "DS 6299.4",
    "DS 6388.4",
    "DS 6438.4",
    "DS 6485.4",
    "Ai1QE 5006.5",
    "Ai1QE 5007.5",
    "Ai1QE 5009.5",
    "Ai1QE 5010.5",
    "Ai1QE 5006.5 (1x230V)",
    "Ai1QE 5007.5 (1x230V)",
    "Ai1QE 5009.5 (1x230V)",
    "Ai1QE 5010.5 (1x230V)",
    "DS 5008.5AI",
    "DS 5009.5AI",
    "DS 5012.5AI",
    "DS 5014.5AI",
    "DS 5017.5AI",
    "DS 5020.5AI",
    "DS 5023.5AI",
    "DS 5026.5AI",
    "DS 5008.5AI (1x230V)",
    "DS 5009.5AI (1x230V)",
    "DS 5012.5AI (1x230V)",
    "DS 5014.5AI (1x230V)",
    "DS 5017.5AI (1x230V)",
    "DS 5029.5",
    "DS 5033.5",
    "DS 5040.5",
    "DS 5045.5",
    "DS 5050.5",
    "DS 5059.5",
    "DS 5028.5 T",
    "DS 5034.5 T",
    "DS 5040.5 T",
    "DS 5046.5 T",
    "DS 5052.5 T",
    "DS 5058.5 T",
    "DS 5063.5 T",
    "DS 5075.5 T",
    "DS 5085.5 T",
    "DS 5095.5 T",
    "DS 5112.5 T",
    "DS 5076.5",
    "DS 5095.5",
    "DS 5123.5",
    "DS 5158.5",
    "Ai QL",
    "Ai QL Kaskade",
    "DS 5013.5AI",
    "DS 5013.5AI (1x230V)",
    "DS 5036.4T",
    "DS 5049.4T",
    "DS 5063.4T",
    "DS 5077.4T",
    "DS 5007.5AI HT",
    "DS 5008.5AI HT",
    "DS 5010.5AI HT",
    "DS 5014.5AI HT",
    "DS 5018.5AI HT",
    "DS 5023.5AI HT",
    "DS 5007.5AI HT (1x230V)",
    "DS 5008.5AI HT (1x230V)",
    "DS 5010.5AI HT (1x230V)",
    "DS 5014.5AI HT (1x230V)",
    "DS 5018.5AI HT (1x230V)",
    "DS 5005.4Ai HT",
    "DS 5007.4Ai HT",
    "DS 5009.4Ai HT",
    "DS 5010.4Ai HT",
    "DS 5012.4Ai HT",
    "DS 5015.4Ai HT",
    "DS 5005.4Ai HT (1x230V)",
    "DS 5007.4Ai HT (1x230V)",
    "DS 5009.4Ai HT (1x230V)",
    "DS 5010.4Ai HT (1x230V)",
    "5006.5",
    "5008.5",
    "5010.5",
    "5013.5",
    "5006.5(1x230V)",
    "5008.5(1x230V)",
    "5010.5(1x230V)",
    "5013.5(1x230V)",
    "EcoTouch Ai1 QL ",
    "5018.5",
    "5010.5",
    "5010.5",
    "DS 5008.5AI",
    "DS 5010.5AI",
    "DS 5012.5AI",
    "DS 5014.5AI",
    "DS 5017.5AI",
    "DS 5020.5AI",
    "DS 5023.5AI",
    "DS 5027.5AI",
    "DS 5008.5AI (1x230V)",
    "DS 5010.5AI (1x230V)",
    "DS 5012.5AI (1x230V)",
    "DS 5014.5AI (1x230V)",
    "DS 5017.5AI (1x230V)",
    "Power+",
    "DS 5145.5 Tandem",
    "DS 5150.5",
    "DS 5182.5 Tandem",
    "DS 5226.5",
    "DS 5235.5 Tandem",
    "DS 6272.5 Trio",
    "DS 6300.5 Tandem",
    "DS 6352.5 Trio",
    "DS 6450.5 Trio",
    "5005.5",
    "5006.5",
    "5007.5",
    "5008.5",
    "5010.5",
    "5005.5 (1x230V)",
    "5006.5 (1x230V)",
    "5008.5 (1x230V)",
    "5010.5 (1x230V)",
    "DS 5006.5Ai Split",
    "DS 5007.5Ai Split",
    "DS 5009.5Ai Split",
    "DS 5012.5Ai Split",
    "DS 5015.5Ai Split",
    "DS 5020.5Ai Split",
    "DS 5025.5Ai Split",
    "DS 5006.3Ai Split",
    "DS 5007.3Ai Split",
    "DS 5008.3Ai Split",
    "DS 5010.3Ai Split",
    "DS 5012.3Ai Split",
    "DS 5015.3Ai Split",
    "DS 5018.3Ai Split",
    "DS 5020.3Ai Split",
    "5008.5",
    "5011.5",
    "5014.5",
    "5018.5",
    "5008.5 (230V)",
    "5011.5 (230V)",
    "5014.5 (230V)",
    "5018.5 (230V)",
    "5018.5",
    "5010.5",
    "5034.5T",
    "5045.5T",
    "5056.5T",
    "5009.3",
    "5068.5 DT",
    "5090.5 DT",
    "5112.5 DT",
    "5007.3",
    "5011.3",
    "EcoTouch 5007.5Ai",
    "EcoTouch 5008.5Ai",
    "EcoTouch 5010.5Ai",
    "EcoTouch 5014.5Ai",
    "EcoTouch 5018.5Ai",
    "EcoTouch 5023.5Ai",
    "EcoTouch 5029.5Ai",
    "EcoTouch 5007.5Ai",
    "EcoTouch 5008.5Ai",
    "EcoTouch 5010.5Ai",
    "EcoTouch 5014.5Ai",
    "EcoTouch 5018.5Ai",
    "DS 5028.4T HT",
    "EcoTouch compact 5004.5",
    "5010.5",
    "5010.5",
    "DS 6450.5 D",
    "5028.5T",
    "ET 6600.5 Q",
    "ET 6750.5 Q",
    "ET 6900.5 Q",
    "5015.5 Ai",
    "5010.5 Ai",
    "5010.5",
    "5018.5",
    "5010.5(1x230V)",
    "5018.5(1x230V)",
    "5010.5",
    "5018.5",
    "5010.5(1x230V)",
    "5018.5(1x230V)",
    "50xx.5",
    "5003.5 Ai",
    "5004.5(1x230V)",
    "",
    "5008.5(1x230V)",
    "5011.5(1x230V)",
    "5012.5(1x230V)",
    "",
    "5011.5",
    "5012.5",
    "5015.5",
    "5003.5 Ai NX",
    "5004.5(1x230V)",
    "",
    "5008.5(1x230V)",
    "5011.5(1x230V)",
    "5012.5(1x230V)",
    "",
    "5011.5",
    "5012.5",
    "5015.5",
    "5004.5(1x230V)",
    "",
    "5008.5(1x230V)",
    "5011.5(1x230V)",
    "5012.5(1x230V)",
    "",
    "5011.5",
    "5012.5",
    "5015.5",
    "5004.5(1x230V)",
    "",
    "5008.5(1x230V)",
    "5011.5(1x230V)",
    "5012.5(1x230V)",
    "",
    "5011.5",
    "5012.5",
    "5015.5",
    "EcoTouch Air Kaskade",
    "5003.6 Ai NX",
    "5003.5 Ai SNB",
    "5003.6 Ai SVB",
    "5010.5-18 (230V)",
    "5010.5-18 (230V)",
    "5018.5",
    "5018.5(1x230V)",
    "5018.5",
    "5018.5(1x230V)",
    "EcoTouch 5007.5Ai Split",
    "EcoTouch 5008.5Ai Split",
    "EcoTouch 5010.5Ai Split",
    "EcoTouch 5014.5Ai Split",
    "EcoTouch 5018.5Ai Split",
    "EcoTouch 5023.5Ai Split",
    "EcoTouch 5029.5Ai Split",
    "ET 5063.4 Tandem WR",
    "ET 5072.4 Tandem WR",
    "ET 5090.4 Tandem WR",
    "ET 5108.4 Tandem WR",
    "ET 5144.4 Tandem WR",
    "ET 5179.4 Tandem WR",
    "ET 5222.4 Tandem WR",
    "ET 5144.4 Tandem",
    "ET 5179.4 Tandem",
    "ET 5222.4 Tandem",
    None,
]

TRANSLATIONS:Final = {
    "de": {
        "I52": {
            0: "F100: Motorschutzschalter 1",
            1: "F101: Motorschutzschalter 2",
            2: "F102: Phasenfolgeüberwachung",
            3: "F103: Störung Wärmequelle",
            4: "F110: HD-Pressostat",
            5: "F120: ND-Pressostat",
            6: "F121: Drucküberwachung Verdampfer",
            7: "F122: Temperaturüberwachung Verdampfer",
            8: "F123: Nasslauf",
            9: "F111: Verflüssigungstemperatur zu niedrig",
            10: "F130: Ausfall 4-Wege Ventil",
            11: "F200: Steuergerät Kommunikationsüberwachung Ausfall",
            12: "F201: Das Gerät pCOe oder EVD ist nicht vorhanden oder funktioniert nicht richtig",
            13: "F301: Ventilmotorfehler",
            14: "F600: Störung Außeneinheit"
        },
        "I53": {
            0: "I011: T Quelle Aus < OK",
            1: "I012: p Kondensator > OK",
            2: "I013: Ext Abschaltung",
            3: "I014: Schalthäufigkeit Verdichter 1",
            4: "I014: Schalthäufigkeit Verdichter 2",
            5: "I014: Schalthäufigkeit ext. Wärmeerzeuger",
            6: "I015: T Quelle Aus ERR"
        }
    },
    "en": {
        "I52": {
            0: "F100: Motor protection switch 1",
            1: "F101: Motor protection awitch 2",
            2: "F102: Phase sequence monitoring",
            3: "F103: Primary Source",
            4: "F110: HP-Pressostat",
            5: "F120: LP-Pressostat",
            6: "F121: Pressure monitoring evaporator",
            7: "F122: Temperature monitoring evaporator",
            8: "F123: Wet run",
            9: "F111: Condensing temperature too low",
            10: "F130: Failure 4-way valve",
            11: "F200: Failure control unit communication monitoring",
            12: "F201: Device pCOe or EVD is not available or does not function properly",
            13: "F301: Valve motor error",
            14: "F600: Failure outdoor unit"
        },
        "I53": {
            0: "I011: T Quelle Aus < OK",
            1: "I012: p Kondensator > OK",
            2: "I013: Ext Abschaltung",
            3: "I014: Schalthäufigkeit Verdichter 1",
            4: "I014: Schalthäufigkeit Verdichter 2",
            5: "I014: Schalthäufigkeit ext. Wärmeerzeuger",
            6: "I015: T Quelle Aus ERR"
        }
    }
}
