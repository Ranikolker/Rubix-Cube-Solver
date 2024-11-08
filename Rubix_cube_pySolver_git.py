"""
R' = r
L' = l
F' = f
B' = b
D' = d
U' = u

R2 = A
L2 = C
F2 = E
B2 = G
U2 = H
D2 = J
"""

solution = []
solution_end = ""
solution_ROBOT = ""

switch = ""

switch02 = ""

switch03 = ""

switch04 = ""

switch05 = ""

print \
    ("Write every edge / corrner as his color (W, Y, B, R, G, O) when you are holdong the white side up and the green front")
AE = input("AE: ").upper()
BE = input("BE: ").upper()
CE = input("CE: ").upper()
DE = input("DE: ").upper()
EE = input("EE: ").upper()
FE = input("FE: ").upper()
GE = input("GE: ").upper()
HE = input("HE: ").upper()
IE = input("IE: ").upper()
JE = input("JE: ").upper()
KE = input("KE: ").upper()
LE = input("LE: ").upper()
ME = input("ME: ").upper()
NE = input("NE: ").upper()
OE = input("OE: ").upper()
PE = input("PE: ").upper()
QE = input("QE: ").upper()
RE = input("RE: ").upper()
SE = input("SE: ").upper()
TE = input("TE: ").upper()
UE = input("UE: ").upper()
VE = input("VE: ").upper()
WE = input("WE: ").upper()
XE = input("XE: ").upper()

# definding all corrners
AC = input("AC: ").upper()
BC = input("BC: ").upper()
CC = input("CC: ").upper()
DC = input("DC: ").upper()
EC = input("EC: ").upper()
FC = input("FC: ").upper()
GC = input("GC: ").upper()
HC = input("HC: ").upper()
IC = input("IC: ").upper()
JC = input("JC: ").upper()
KC = input("KC: ").upper()
LC = input("LC: ").upper()
MC = input("MC: ").upper()
NC = input("NC: ").upper()
OC = input("OC: ").upper()
PC = input("PC: ").upper()
QC = input("QC: ").upper()
RC = input("RC: ").upper()
SC = input("SC: ").upper()
TC = input("TC: ").upper()
UC = input("UC: ").upper()
VC = input("VC: ").upper()
WC = input("WC: ").upper()
XC = input("XC: ").upper()

# definding all edges
AQE = ""
BME_Buffer = ""
CIE = ""
DEE = ""
LFE = ""
GXE = ""
HRE = ""
JPE = ""
KUE = ""
NTE = ""
OVE = ""
SWE = ""

QAE = ""
MBE_Buffer = ""
ICE = ""
EDE = ""
FLE = ""
XGE = ""
RHE = ""
PJE = ""
UKE = ""
TNE = ""
VOE = ""
WSE = ""

# the cube edges

# AQE
AQE = AE + QE

# QAE
QAE = QE + AE

# BME_Buffer
BME_Buffer = BE + ME

# MBE_Buffer
MBE_Buffer = ME + BE

# CIE
CIE = CE + IE

# ICE
ICE = IE + CE

# DEE
DEE = DE + EE

# EDE
EDE = EE + DE

# LFE
LFE = LE + FE

# FLE
FLE = FE + LE

# GXE
GXE = GE + XE

# XGE
XGE = XE + GE

# HRE
HRE = HE + RE

# RHE
RHE = RE + HE

# JPE
JPE = JE + PE

# PJE
PJE = PE + JE

# KUE
KUE = KE + UE

# UKE
UKE = UE + KE

# NTE
NTE = NE + TE

# TNE
TNE = TE + NE

# OVE
OVE = OE + VE

# VOE
VOE = VE + OE

# SWE
SWE = SE + WE

# WSE
WSE = WE + SE

# solving edges
while True:

    # statments
    switch = BME_Buffer
    switch02 = MBE_Buffer

    # if solved
    if AQE == "WB" and BME_Buffer == "WR" and CIE == "WG" and DEE == "WO" and FLE == "OG" and GXE == "OY" and HRE == "OB" and JPE == "GR" and KUE == "GY" and NTE == "RB" and SWE == "BY" and OVE == "RY" and QAE == "BW" and MBE_Buffer == "RW" and ICE == "GW" and EDE == "OW" and LFE == "GO" and XGE == "YO" and RHE == "BO" and PJE == "RG" and UKE == "YG" and TNE == "BR" and WSE == "YB" and VOE == "YR":
        print("edges has been solved")
        break

    # if not solved
    else:
        if BME_Buffer == "WG":
            solution.append("AUCRDrdrBAdrdRDrbCuA")
            BME_Buffer = CIE
            MBE_Buffer = ICE
            CIE = switch
            ICE = switch02

        elif BME_Buffer == "WB":
            solution.append("AuCRDrdrBAdrdRDrbCUA")
            BME_Buffer = AQE
            MBE_Buffer = QAE
            AQE = switch
            QAE = switch02

        elif BME_Buffer == "WO":
            solution.append("RUrurFAuruRUrf")
            BME_Buffer = DEE
            MBE_Buffer = EDE
            DEE = switch
            EDE = switch02

        elif BME_Buffer == "YG":
            solution.append("dCRUrurFAuruRUrfCD")
            BME_Buffer = UKE
            MBE_Buffer = KUE
            UKE = switch
            KUE = switch02

        elif BME_Buffer == "YR":
            solution.append("JCRUrurFAuruRUrfCJ")
            BME_Buffer = VOE
            MBE_Buffer = OVE
            VOE = switch
            OVE = switch02

        elif BME_Buffer == "YB":
            solution.append("DCRUrurFAuruRUrfCd")
            BME_Buffer = WSE
            MBE_Buffer = SWE
            WSE = switch
            SWE = switch02

        elif BME_Buffer == "YO":
            solution.append("CRUrurFAuruRUrfC")
            BME_Buffer = XGE
            MBE_Buffer = GXE
            XGE = switch
            GXE = switch02

        elif BME_Buffer == "RG":
            solution.append("ufBUbubRGubuBUbrFU")
            BME_Buffer = PJE
            MBE_Buffer = JPE
            PJE = switch
            JPE = switch02

        elif BME_Buffer == "RB":
            solution.append("UBFUfufLEufuFUflbu")
            BME_Buffer = NTE
            MBE_Buffer = TNE
            NTE = switch
            TNE = switch02

        elif BME_Buffer == "BO":
            solution.append("LRUrurFAuruRUrfl")
            BME_Buffer = RHE
            MBE_Buffer = HRE
            RHE = switch
            HRE = switch02

        elif BME_Buffer == "OG":
            solution.append("uFBUbubRGubuBUbrfU")
            BME_Buffer = FLE
            MBE_Buffer = LFE
            FLE = switch
            LFE = switch02

        # --
        elif BME_Buffer == "GW":
            solution.append("RfCRBrbrUAbrbRBruCFr")
            BME_Buffer = ICE
            MBE_Buffer = CIE
            ICE = switch
            CIE = switch02

        elif BME_Buffer == "BW":
            solution.append("rBCRFrfrDAfrfRFrdCbR")
            BME_Buffer = QAE
            MBE_Buffer = AQE
            QAE = switch
            AQE = switch02

        elif BME_Buffer == "OW":
            solution.append("LuFBUbubRGubuBUbrfUl")
            BME_Buffer = EDE
            MBE_Buffer = DEE
            EDE = switch
            DEE = switch02


        elif BME_Buffer == "GY":
            solution.append("FlfRUrurFAuruRUrLf")
            BME_Buffer = KUE
            MBE_Buffer = UKE
            KUE = switch
            UKE = switch02


        elif BME_Buffer == "RY":
            solution.append("JluFBUbubRGubuBUbrfULJ")
            BME_Buffer = OVE
            MBE_Buffer = VOE
            OVE = switch
            VOE = switch02


        elif BME_Buffer == "BY":
            solution.append("rbCRFrfrDAfrfRFrdCBR")
            BME_Buffer = SWE
            MBE_Buffer = WSE
            SWE = switch
            WSE = switch02


        elif BME_Buffer == "OY":
            solution.append("luFBUbubRGubuBUbrfUL")
            BME_Buffer = GXE
            MBE_Buffer = XGE
            GXE = switch
            XGE = switch02


        elif BME_Buffer == "GR":
            solution.append("HRLUlulBCuluLUlbrH")
            BME_Buffer = JPE
            MBE_Buffer = PJE
            JPE = switch
            PJE = switch02


        elif BME_Buffer == "BR":
            solution.append("HrluLULfCULUluLFRH")
            BME_Buffer = TNE
            MBE_Buffer = NTE
            TNE = switch
            NTE = switch02


        elif BME_Buffer == "OB":
            solution.append("UbFUfufLEufuFUflBu")
            BME_Buffer = HRE
            MBE_Buffer = RHE
            HRE = switch
            RHE = switch02


        elif BME_Buffer == "GO":
            solution.append("lRUrurFAuruRUrfL")
            BME_Buffer = LFE
            MBE_Buffer = FLE
            LFE = switch
            FLE = switch02

        # cycle
        elif BME_Buffer == "WR" or BME_Buffer == "RW":

            if AQE != "WB":
                solution.append("AuCRDrdrBAdrdRDrbCUA")
                BME_Buffer = AQE
                MBE_Buffer = QAE
                AQE = switch
                QAE = switch02

            elif QAE != "BW":
                solution.append("rBCRFrfrDAfrfRFrdCbR")
                BME_Buffer = QAE
                MBE_Buffer = AQE
                QAE = switch
                AQE = switch02

            elif CIE != "WG":
                solution.append("AUCRDrdrBAdrdRDrbCuA")
                BME_Buffer = CIE
                MBE_Buffer = ICE
                CIE = switch
                ICE = switch02

            elif ICE != "GW":
                solution.append("RfCRBrbrUAbrbRBruCFr")
                BME_Buffer = ICE
                MBE_Buffer = CIE
                ICE = switch
                CIE = switch02

            elif DEE != "WO":
                solution.append("RUrurFAuruRUrf")
                BME_Buffer = DEE
                MBE_Buffer = EDE
                DEE = switch
                EDE = switch02

            elif EDE != "OW":
                solution.append("LuFBUbubRGubuBUbrfUl")
                BME_Buffer = EDE
                MBE_Buffer = DEE
                EDE = switch
                DEE = switch02

            elif LFE != "GO":
                solution.append("lRUrurFAuruRUrfL")
                BME_Buffer = LFE
                MBE_Buffer = FLE
                LFE = switch
                FLE = switch02

            elif FLE != "OG":
                solution.append("uFBUbubRGubuBUbrfU")
                BME_Buffer = FLE
                MBE_Buffer = LFE
                FLE = switch
                LFE = switch02

            elif GXE != "OY":
                solution.append("luFBUbubRGubuBUbrfUL")
                BME_Buffer = GXE
                MBE_Buffer = XGE
                GXE = switch
                XGE = switch02

            elif XGE != "YO":
                solution.append("CRUrurFAuruRUrfC")
                BME_Buffer = XGE
                MBE_Buffer = GXE
                XGE = switch
                GXE = switch02

            elif HRE != "OB":
                solution.append("UbFUfufLEufuFUflBu")
                BME_Buffer = HRE
                MBE_Buffer = RHE
                HRE = switch
                RHE = switch02

            elif RHE != "BO":
                solution.append("LRUrurFAuruRUrfl")
                BME_Buffer = RHE
                MBE_Buffer = HRE
                RHE = switch
                HRE = switch02

            elif JPE != "GR":
                solution.append("HRLUlulBCuluLUlbrH")
                BME_Buffer = JPE
                MBE_Buffer = PJE
                JPE = switch
                PJE = switch02

            elif PJE != "RG":
                solution.append("ufBUbubRGubuBUbrFU")
                BME_Buffer = PJE
                MBE_Buffer = JPE
                PJE = switch
                JPE = switch02

            elif KUE != "GY":
                solution.append("FlfRUrurFAuruRUrLf")
                BME_Buffer = KUE
                MBE_Buffer = UKE
                KUE = switch
                UKE = switch02

            elif UKE != "YG":
                solution.append("dCRUrurFAuruRUrfCD")
                BME_Buffer = UKE
                MBE_Buffer = KUE
                UKE = switch
                KUE = switch02

            elif NTE != "RB":
                solution.append("UBFUfufLEufuFUflbu")
                BME_Buffer = NTE
                MBE_Buffer = TNE
                NTE = switch
                TNE = switch02

            elif TNE != "BR":
                solution.append("HrluLULfCULUluLFRH")
                BME_Buffer = TNE
                MBE_Buffer = NTE
                TNE = switch
                NTE = switch02

            elif OVE != "RY":
                solution.append("JluFBUbubRGubuBUbrfULJ")
                BME_Buffer = OVE
                MBE_Buffer = VOE
                OVE = switch
                VOE = switch02

            elif VOE != "YR":
                solution.append("JCRUrurFAuruRUrfCJ")
                BME_Buffer = VOE
                MBE_Buffer = OVE
                VOE = switch
                OVE = switch02

            elif SWE != "BY":
                solution.append("rbCRFrfrDAfrfRFrdCBR")
                BME_Buffer = SWE
                MBE_Buffer = WSE
                SWE = switch
                WSE = switch02

            elif WSE != "YB":
                solution.append("DCRUrurFAuruRUrfCd")
                BME_Buffer = WSE
                MBE_Buffer = SWE
                WSE = switch
                SWE = switch02

# solving corrners
while True:

    # statments
    switch03 = EC
    switch04 = AC
    switch05 = RC

    # if the cube is solved
    if AC == "W" and BC == "W" and CC == "W" and DC == "W" and EC == "O" and FC == "O" and GC == "O" and HC == "O" and IC == "G" and JC == "G" and KC == "G" and LC == "G" and MC == "R" and NC == "R" and OC == "R" and PC == "R" and QC == "B" and RC == "B" and SC == "B" and TC == "B" and UC == "Y" and VC == "Y" and WC == "Y" and XC == "Y":
        print("corrners has been solved")
        break

    # if cube is not solved
    else:

        # cycle
        if EC + AC + RC == "OWB" or EC + AC + RC == "BOW" or EC + AC + RC == "WBO":

            if BC + NC + QC != "WRB":
                solution.append("ruruRUrfRUrurFr")
                EC = BC
                AC = NC
                RC = QC
                BC = switch03
                NC = switch04
                QC = switch05

            elif HC + SC + XC != "OBY":
                solution.append("dAuruRUrfRUrurFD")
                EC = HC
                AC = SC
                RC = XC
                HC = switch03
                SC = switch04
                XC = switch05


            elif MC + CC + JC != "RWG":
                solution.append("FRuruRUrfRUrurFRf")
                EC = MC
                AC = CC
                RC = JC
                MC = switch03
                JC = switch05
                CC = switch04

            elif IC + DC + FC != "GWO":
                solution.append("FuruRUrfRUrurFAf")
                EC = IC
                AC = DC
                RC = FC
                IC = switch03
                FC = switch05
                DC = switch04

            elif LC + GC + UC != "GOY":
                solution.append("EuruRUrfRUrurFAE")
                EC = LC
                AC = GC
                RC = UC
                LC = switch03
                UC = switch05
                GC = switch04

            elif PC + KC + VC != "RGY":
                solution.append("FDRuruRUrfRUrurFRdf")
                EC = PC
                AC = KC
                RC = VC
                PC = switch03
                VC = switch05
                KC = switch04

            elif TC + OC + WC != "BRY":
                solution.append("AuruRUrfRUrurF")
                EC = TC
                AC = OC
                RC = WC
                TC = switch03
                WC = switch05
                OC = switch04

            elif JC + MC + CC != "GRW":
                solution.append("uruRUrfRUrurFA")
                EC = JC
                AC = MC
                RC = CC
                JC = switch03
                CC = switch05
                MC = switch04

            elif FC + IC + DC != "OGW":
                solution.append("fDRuruRUrfRUrurFRdF")
                EC = FC
                AC = IC
                RC = DC
                FC = switch03
                DC = switch05
                IC = switch04

            elif UC + LC + GC != "YGO":
                solution.append("DRuruRUrfRUrurFRd")
                EC = UC
                AC = LC
                RC = GC
                UC = switch03
                GC = switch05
                LC = switch04

            elif VC + PC + KC != "YRG":
                solution.append("RuruRUrfRUrurFR")
                EC = VC
                AC = PC
                RC = KC
                VC = switch03
                PC = switch04
                KC = switch05

            elif WC + TC + OC != "YBR":
                solution.append("dRuruRUrfRUrurFRD")
                EC = WC
                AC = TC
                RC = OC
                WC = switch03
                TC = switch04
                OC = switch05

            elif GC + UC + LC != "OYG":
                solution.append("fRuruRUrfRUrurFRF")
                EC = GC
                AC = UC
                RC = LC
                GC = switch03
                UC = switch04
                LC = switch05

            elif NC + QC + BC != "RBW":
                solution.append("rFRuruRUrfRUrurFRfR")
                EC = NC
                AC = QC
                RC = BC
                NC = switch03
                BC = switch05
                QC = switch04

            elif QC + BC + NC != "BWR":
                solution.append("RdRuruRUrfRUrurFRDr")
                EC = QC
                AC = BC
                RC = NC
                QC = switch03
                NC = switch05
                BC = switch04

            elif CC + JC + MC != "WGR":
                solution.append("EDRuruRUrfRUrurFRdE")
                EC = CC
                AC = JC
                RC = MC
                CC = switch03
                MC = switch05
                JC = switch04

            elif DC + FC + IC != "WOG":
                solution.append("ERuruRUrfRUrurFRE")
                EC = DC
                AC = FC
                RC = IC
                DC = switch03
                FC = switch04
                IC = switch05

            elif KC + VC + PC != "GYR":
                solution.append("furuRUrfRUrurFAF")
                EC = KC
                AC = VC
                RC = PC
                KC = switch03
                VC = switch04
                PC = switch05

            elif OC + WC + TC != "RYB":
                solution.append("AFRuruRUrfRUrurFRfA")
                EC = OC
                AC = WC
                RC = TC
                OC = switch03
                TC = switch05
                WC = switch04

            elif XC + HC + SC != "YOB":
                solution.append("JRuruRUrfRUrurFRJ")
                EC = XC
                AC = HC
                RC = SC
                XC = switch03
                SC = switch05
                HC = switch04

            elif SC + XC + HC != "BYO":
                solution.append("DfRuruRUrfRUrurFRFd")
                EC = SC
                AC = XC
                RC = HC
                SC = switch03
                HC = switch05
                XC = switch04


        else:
            # white color (3) one in cycle
            if EC == "W" and AC == "R" and RC == "B":
                solution.append("ruruRUrfRUrurFr")
                EC = BC
                AC = NC
                RC = QC
                BC = switch03
                NC = switch04
                QC = switch05

            elif EC == "W" and AC == "G" and RC == "R":
                solution.append("EDRuruRUrfRUrurFRdE")
                EC = CC
                AC = JC
                RC = MC
                CC = switch03
                MC = switch05
                JC = switch04

            elif EC == "W" and AC == "O" and RC == "G":
                solution.append("ERuruRUrfRUrurFRE")
                EC = DC
                AC = FC
                RC = IC
                DC = switch03
                FC = switch04
                IC = switch05

            # orange color (3) one in cycle
            elif EC == "O" and AC == "Y" and RC == "G":
                solution.append("fRuruRUrfRUrurFRF")
                EC = GC
                AC = UC
                RC = LC
                GC = switch03
                UC = switch04
                LC = switch05

            elif EC == "O" and AC == "B" and RC == "Y":
                solution.append("dAuruRUrfRUrurFD")
                EC = HC
                AC = SC
                RC = XC
                HC = switch03
                SC = switch04
                XC = switch05

            elif EC == "O" and AC == "G" and RC == "W":
                solution.append("fDRuruRUrfRUrurFRdF")
                EC = FC
                AC = IC
                RC = DC
                FC = switch03
                DC = switch05
                IC = switch04


            # green color (4)
            elif EC == "G" and AC == "Y" and RC == "R":
                solution.append("furuRUrfRUrurFAF")
                EC = KC
                AC = VC
                RC = PC
                KC = switch03
                VC = switch04
                PC = switch05

            elif EC == "G" and AC == "W" and RC == "O":
                solution.append("FuruRUrfRUrurFAf")
                EC = IC
                AC = DC
                RC = FC
                IC = switch03
                FC = switch05
                DC = switch04

            elif EC == "G" and AC == "O" and RC == "Y":
                solution.append("EuruRUrfRUrurFAE")
                EC = LC
                AC = GC
                RC = UC
                LC = switch03
                UC = switch05
                GC = switch04

            elif EC == "G" and AC == "R" and RC == "W":
                solution.append("uruRUrfRUrurFA")
                EC = JC
                AC = MC
                RC = CC
                JC = switch03
                CC = switch05
                MC = switch04


            # red color (4)
            elif EC == "R" and AC == "Y" and RC == "B":
                solution.append("AFRuruRUrfRUrurFRfA")
                EC = OC
                AC = WC
                RC = TC
                OC = switch03
                TC = switch05
                WC = switch04

            elif EC == "R" and AC == "W" and RC == "G":
                solution.append("FRuruRUrfRUrurFRf")
                EC = MC
                AC = CC
                RC = JC
                MC = switch03
                JC = switch05
                CC = switch04

            elif EC == "R" and AC == "G" and RC == "Y":
                solution.append("FDRuruRUrfRUrurFRdf")
                EC = PC
                AC = KC
                RC = VC
                PC = switch03
                VC = switch05
                KC = switch04

            elif EC == "R" and AC == "B" and RC == "W":
                solution.append("rFRuruRUrfRUrurFRfR")
                EC = NC
                AC = QC
                RC = BC
                NC = switch03
                BC = switch05
                QC = switch04


            # yellow color (4)
            elif EC == "Y" and AC == "G" and RC == "O":
                solution.append("DRuruRUrfRUrurFRd")
                EC = UC
                AC = LC
                RC = GC
                UC = switch03
                GC = switch05
                LC = switch04

            elif EC == "Y" and AC == "O" and RC == "B":
                solution.append("JRuruRUrfRUrurFRJ")
                EC = XC
                AC = HC
                RC = SC
                XC = switch03
                SC = switch05
                HC = switch04

            elif EC == "Y" and AC == "R" and RC == "G":
                solution.append("RuruRUrfRUrurFR")
                EC = VC
                AC = PC
                RC = KC
                VC = switch03
                PC = switch04
                KC = switch05

            elif EC == "Y" and AC == "B" and RC == "R":
                solution.append("dRuruRUrfRUrurFRD")
                EC = WC
                AC = TC
                RC = OC
                WC = switch03
                TC = switch04
                OC = switch05



            # blue color (3) one cycle
            elif EC == "B" and AC == "Y" and RC == "O":
                solution.append("DfRuruRUrfRUrurFRFd")
                EC = SC
                AC = XC
                RC = HC
                SC = switch03
                HC = switch05
                XC = switch04

            elif EC == "B" and AC == "R" and RC == "Y":
                solution.append("AuruRUrfRUrurF")
                EC = TC
                AC = OC
                RC = WC
                TC = switch03
                WC = switch05
                OC = switch04


            elif EC == "B" and AC == "W" and RC == "R":
                solution.append("RdRuruRUrfRUrurFRDr")
                EC = QC
                AC = BC
                RC = NC
                QC = switch03
                NC = switch05
                BC = switch04

for i in range(len(solution)):
    solution_end = solution_end + solution[i]

solution_end = solution_end + " "

for i in range(len(solution_end)):

    if solution_end[i] != " ":

        # R - R'
        if solution_end[i] == "R" and solution_end[i + 1] == "r" or solution_end[i] == "r" and solution_end[
            i + 1] == "R" or solution_end[i] == "R" and solution_end[i - 1] == "r" or solution_end[i] == "r" and \
                solution_end[i - 1] == "R":
            continue

        # L - L'
        elif solution_end[i] == "L" and solution_end[i + 1] == "l" or solution_end[i] == "l" and solution_end[
            i + 1] == "L" or solution_end[i] == "L" and solution_end[i - 1] == "l" or solution_end[i] == "l" and \
                solution_end[i - 1] == "L":
            continue

        # F - F'
        elif solution_end[i] == "F" and solution_end[i + 1] == "f" or solution_end[i] == "f" and solution_end[
            i + 1] == "F" or solution_end[i] == "F" and solution_end[i - 1] == "f" or solution_end[i] == "f" and \
                solution_end[i - 1] == "F":
            continue

        # B - B'
        elif solution_end[i] == "B" and solution_end[i + 1] == "b" or solution_end[i] == "b" and solution_end[
            i + 1] == "B" or solution_end[i] == "B" and solution_end[i - 1] == "b" or solution_end[i] == "b" and \
                solution_end[i - 1] == "B":
            continue

        # D - D'
        elif solution_end[i] == "D" and solution_end[i + 1] == "d" or solution_end[i] == "d" and solution_end[
            i + 1] == "D" or solution_end[i] == "D" and solution_end[i - 1] == "d" or solution_end[i] == "d" and \
                solution_end[i - 1] == "D":
            continue

        # U - U'
        elif solution_end[i] == "U" and solution_end[i + 1] == "u" or solution_end[i] == "u" and solution_end[
            i + 1] == "U" or solution_end[i] == "U" and solution_end[i - 1] == "u" or solution_end[i] == "u" and \
                solution_end[i - 1] == "U":
            continue


        # R2 - R2
        elif solution_end[i] == "A" and solution_end[i + 1] == "A" or solution_end[i] == "A" and solution_end[
            i - 1] == "A":
            continue

        # L2 - L2
        elif solution_end[i] == "C" and solution_end[i + 1] == "C" or solution_end[i] == "C" and solution_end[
            i - 1] == "C":
            continue

        # F2 - F2
        elif solution_end[i] == "E" and solution_end[i + 1] == "E" or solution_end[i] == "E" and solution_end[
            i - 1] == "E":
            continue

        # B2 - B2
        elif solution_end[i] == "G" and solution_end[i + 1] == "G" or solution_end[i] == "G" and solution_end[
            i - 1] == "G":
            continue

        # U2 - U2
        elif solution_end[i] == "H" and solution_end[i + 1] == "H" or solution_end[i] == "H" and solution_end[
            i - 1] == "H":
            continue

        # D2 - D2
        elif solution_end[i] == "J" and solution_end[i + 1] == "J" or solution_end[i] == "J" and solution_end[
            i - 1] == "J":
            continue

        else:
            solution_ROBOT = solution_ROBOT + solution_end[i]

    else:
        break

# motors moves
for i in range(len(solution_ROBOT)):
    # R - R'
    if solution_ROBOT[i] == "R":
        pass

    elif solution_ROBOT[i] == "r":
        pass

    # L - L'
    elif solution_ROBOT[i] == "L":
        pass

    elif solution_ROBOT[i] == "l":
        pass

    # F - F'
    elif solution_ROBOT[i] == "F":
        pass

    elif solution_ROBOT[i] == "f":
        pass

    # B - B'
    elif solution_ROBOT[i] == "B":
        pass

    elif solution_ROBOT[i] == "b":
        pass

    # D - D'
    elif solution_ROBOT[i] == "D":
        pass

    elif solution_ROBOT[i] == "d":
        pass

    # U - U'
    elif solution_ROBOT[i] == "U":
        pass

    elif solution_ROBOT[i] == "u":
        pass


    # R2
    elif solution_ROBOT[i] == "A":
        pass

    # L2
    elif solution_ROBOT[i] == "C":
        pass

    # F2
    elif solution_ROBOT[i] == "E":
        pass

    # B2
    elif solution_ROBOT[i] == "G":
        pass

    # U2
    elif solution_ROBOT[i] == "H":
        pass

    # D2
    elif solution_ROBOT[i] == "J":
        pass

