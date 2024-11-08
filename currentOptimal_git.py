import itertools
solution_cross = ""
change_list2 = ""


letters = ["R", "r", "L", "l", "F", "f", "B", "b", "U", "u", "D", "d", "A", "S", "G", "H", "J", "K"]


#defind all edges
print("Write every edge / corrner as his color (W, Y, B, R, G, O) when you are holding the white side up and the green front")
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


r = 1


# function
def change(moves, aE, bE, cE, dE, eE, fE, gE, hE, iE, jE, kE, lE, mE, nE, oE, pE, qE, rE, sE, tE, uE, vE, wE, xE, aC,
          bC, cC, dC, eC, fC, gC, hC, iC, jC, kC, lC, mC, nC, oC, pC, qC, rC, sC, tC, uC, vC, wC, xC):
   moves = moves + "!"
   change_list = ""
   for i in range(len(moves)):
       switchE01 = aE
       switchE02 = bE
       switchE03 = cE
       switchE04 = dE
       switchE05 = eE
       switchE06 = fE
       switchE07 = gE
       switchE08 = hE
       switchE09 = iE
       switchE010 = jE
       switchE011 = kE
       switchE012 = lE
       switchE013 = mE
       switchE014 = nE
       switchE015 = oE
       switchE016 = pE
       switchE017 = qE
       switchE018 = rE
       switchE019 = sE
       switchE020 = tE
       switchE021 = uE
       switchE022 = vE
       switchE023 = wE
       switchE024 = xE


       switchC01 = aC
       switchC02 = bC
       switchC03 = cC
       switchC04 = dC
       switchC05 = eC
       switchC06 = fC
       switchC07 = gC
       switchC08 = hC
       switchC09 = iC
       switchC010 = jC
       switchC011 = kC
       switchC012 = lC
       switchC013 = mC
       switchC014 = nC
       switchC015 = oC
       switchC016 = pC
       switchC017 = qC
       switchC018 = rC
       switchC019 = sC
       switchC020 = tC
       switchC021 = uC
       switchC022 = vC
       switchC023 = wC
       switchC024 = xC


       if moves[i] != "!":
           if moves[i] == "R" and moves[i + 1] == "r" or moves[i] == "r" and moves[i + 1] == "R" or moves[i] == "L" and moves[i + 1] == "l" or moves[i] == "l" and moves[i + 1] == "L" or moves[i] == "F" and moves[i + 1] == "f" or moves[i] == "f" and moves[i + 1] == "F" or moves[i] == "B" and moves[i + 1] == "b" or moves[i] == "b" and moves[i + 1] == "B" or moves[i] == "U" and moves[i + 1] == "u" or moves[i] == "u" and moves[i + 1] == "U" or moves[i] == "D" and moves[i + 1] == "d" or moves[i] == "d" and moves[i + 1] == "D" or moves[i] == "A" and moves[i + 1] == "A" or moves[i] == "S" and moves[i + 1] == "S" or moves[i] == "G" and moves[i + 1] == "G" or moves[i] == "H" and moves[i + 1] == "H" or moves[i] == "J" and moves[i + 1] == "J" or moves[i] == "K" and moves[i + 1] == "K":
               continue


           else:


                   # R
                   if moves[i] == "R":
                       bC = jC
                       bE = jE
                       cC = kC


                       qC = switchC03
                       tE = switchE02
                       tC = switchC02


                       wC = switchC017
                       vE = switchE020
                       vC = switchC020


                       jC = switchC022
                       jE = switchE022
                       kC = switchC023


                       mC = switchC016
                       mE = switchE016
                       nC = switchC013
                       nE = switchE013
                       oC = switchC014
                       oE = switchE014
                       pC = switchC015
                       pE = switchE015


                   # L
                   elif moves[i] == "L":
                       aC = sC
                       dE = rE
                       dC = rC


                       rC = switchC024
                       rE = switchE024
                       sC = switchC021


                       uC = switchC09
                       xE = switchE012
                       xC = switchC012


                       iC = switchC01
                       lE = switchE04
                       lC = switchC04


                       fC = switchC05
                       fE = switchE05
                       gC = switchC06
                       gE = switchE06
                       hC = switchC07
                       hE = switchE07
                       eC = switchC08
                       eE = switchE08


                       # F--
                   elif moves[i] == "F":
                       dC = gC
                       cE = fE
                       cC = fC


                       mC = switchC04
                       pE = switchE03
                       pC = switchC03


                       uC = switchC016
                       uE = switchE016
                       vC = switchC013


                       fC = switchC021
                       fE = switchE021
                       gC = switchC022


                       jC = switchC09
                       jE = switchE09
                       kC = switchC010
                       kE = switchE010
                       lC = switchC011
                       lE = switchE011
                       iC = switchC012
                       iE = switchE012


                       # B--
                   elif moves[i] == "B":
                       aC = nC
                       aE = nE
                       bC = oC


                       eC = switchC02
                       hE = switchE01
                       hC = switchC01


                       xC = switchC05
                       wE = switchE08
                       wC = switchC08


                       oC = switchC024
                       nE = switchE023
                       nC = switchC023


                       rC = switchC017
                       rE = switchE017
                       sC = switchC018
                       sE = switchE018
                       tC = switchC019
                       tE = switchE019
                       qC = switchC020
                       qE = switchE020


                       # U--
                   elif moves[i] == "U":
                       jC = nC
                       iE = mE
                       iC = mC


                       fC = switchC010
                       eE = switchE09
                       eC = switchC09


                       rC = switchC06
                       qE = switchE05
                       qC = switchC05


                       nC = switchC018
                       mE = switchE017
                       mC = switchC017


                       bC = switchC01
                       bE = switchE01
                       cC = switchC02
                       cE = switchE02
                       dC = switchC03
                       dE = switchE03
                       aC = switchC04
                       aE = switchE04


                       # D--
                   elif moves[i] == "D":
                       lC = hC
                       kE = gE
                       kC = gC


                       hC = switchC020
                       gE = switchE019
                       gC = switchC019


                       tC = switchC016
                       sE = switchE015
                       sC = switchC015


                       pC = switchC012
                       oE = switchE011
                       oC = switchC011


                       vC = switchC021
                       vE = switchE021
                       wC = switchC022
                       wE = switchE022
                       xC = switchC023
                       xE = switchE023
                       uC = switchC024
                       uE = switchE024


                       # R'
                   elif moves[i] == "r":
                       bC = tC
                       bE = tE
                       cC = qC


                       qC = switchC023
                       tE = switchE022
                       tC = switchC022


                       wC = switchC011
                       vE = switchE010
                       vC = switchC010


                       jC = switchC02
                       jE = switchE02
                       kC = switchC03


                       pC = switchC013
                       pE = switchE013
                       oC = switchC016
                       oE = switchE016
                       nC = switchC015
                       nE = switchE015
                       mC = switchC014
                       mE = switchE014


                       # L'
                   elif moves[i] == "l":
                       uC = sC
                       xE = rE
                       xC = rC


                       rC = switchC04
                       rE = switchE04
                       sC = switchC01


                       aC = switchC09
                       dE = switchE012
                       dC = switchC012


                       iC = switchC021
                       lE = switchE024
                       lC = switchC024


                       hC = switchC05
                       hE = switchE05
                       gC = switchC08
                       gE = switchE08
                       fC = switchC07
                       fE = switchE07
                       eC = switchC06
                       eE = switchE06


                       # F'
                   elif moves[i] == "f":
                       dC = switchC013
                       cE = switchE016
                       cC = switchC016


                       mC = switchC022
                       pE = switchE021
                       pC = switchC021


                       vC = switchC07
                       uE = switchE06
                       uC = switchC06


                       fC = switchC03
                       fE = switchE03
                       gC = switchC04


                       lC = switchC09
                       lE = switchE09
                       kC = switchC012
                       kE = switchE012
                       jC = switchC011
                       jE = switchE011
                       iC = switchC010
                       iE = switchE010


                   # B'
                   elif moves[i] == "b":
                       xC = oC
                       wE = nE
                       wC = nC


                       aC = switchC08
                       aE = switchE08
                       bC = switchC05


                       eC = switchC024
                       hE = switchE023
                       hC = switchC023


                       oC = switchC02
                       nE = switchE01
                       nC = switchC01


                       tC = switchC017
                       tE = switchE017
                       sC = switchC020
                       sE = switchE020
                       rC = switchC019
                       rE = switchE019
                       qC = switchC018
                       qE = switchE018


                       # U'
                   elif moves[i] == "u":
                       rC = nC
                       qE = mE
                       qC = mC


                       jC = switchC06
                       iE = switchE05
                       iC = switchC05


                       fC = switchC018
                       eE = switchE017
                       eC = switchC017


                       nC = switchC010
                       mE = switchE09
                       mC = switchC09


                       dC = switchC01
                       dE = switchE01
                       cC = switchC04
                       cE = switchE04
                       bC = switchC03
                       bE = switchE03
                       aC = switchC02
                       aE = switchE02


                       # D'
                   elif moves[i] == "d":
                       tC = hC
                       sE = gE
                       sC = gC


                       lC = switchC016
                       kE = switchE015
                       kC = switchC015


                       hC = switchC012
                       gE = switchE011
                       gC = switchC011


                       pC = switchC020
                       oE = switchE019
                       oC = switchC019


                       xC = switchC021
                       xE = switchE021
                       wC = switchC024
                       wE = switchE024
                       vC = switchC023
                       vE = switchE023
                       uC = switchC022
                       uE = switchE022


                       # R2
                   elif moves[i] == "A":
                       jC = tC
                       jE = tE
                       kC = qC


                       bC = switchC022
                       bE = switchE022
                       cC = switchC023


                       qC = switchC011
                       tE = switchE010
                       tC = switchC010


                       wC = switchC03
                       vE = switchE02
                       vC = switchC02


                       oC = switchC013
                       oE = switchE013
                       nC = switchC016
                       nE = switchE016
                       mC = switchC015
                       mE = switchE015
                       pC = switchC014
                       pE = switchE014


                       # L2
                   elif moves[i] == "S":
                       iC = sC
                       lE = rE
                       lC = rC


                       aC = switchC021
                       dE = switchE024
                       dC = switchC024


                       rC = switchC012
                       rE = switchE012
                       sC = switchC09


                       uC = switchC01
                       xE = switchE04
                       xC = switchC04


                       gC = switchC05
                       gE = switchE05
                       fC = switchC08
                       fE = switchE08
                       eC = switchC07
                       eE = switchE07
                       hC = switchC06
                       hE = switchE06


                       # F2
                   elif moves[i] == "G":
                       mC = gC
                       pE = fE
                       pC = fC


                       dC = switchC022
                       cE = switchE021
                       cC = switchC021


                       uC = switchC03
                       uE = switchE03
                       vC = switchC04


                       fC = switchC016
                       fE = switchE016
                       gC = switchC013


                       kC = switchC09
                       kE = switchE09
                       jC = switchC012
                       jE = switchE012
                       iC = switchC011
                       iE = switchE011
                       lC = switchC010
                       lE = switchE010


                       # B2
                   elif moves[i] == "H":
                       eC = oC
                       hE = nE
                       hC = nC


                       aC = switchC023
                       aE = switchE023
                       bC = switchC024


                       xC = switchC02
                       wE = switchE01
                       wC = switchC01


                       oC = switchC05
                       nE = switchE08
                       nC = switchC08


                       sC = switchC017
                       sE = switchE017
                       rC = switchC020
                       rE = switchE020
                       qC = switchC019
                       qE = switchE019
                       tC = switchC018
                       tE = switchE018


                       # U2
                   elif moves[i] == "J":
                       fC = nC
                       eE = mE
                       eC = mC


                       jC = switchC018
                       iE = switchE017
                       iC = switchC017


                       rC = switchC010
                       qE = switchE09
                       qC = switchC09


                       nC = switchC06
                       mE = switchE05
                       mC = switchC05


                       cC = switchC01
                       cE = switchE01
                       bC = switchC04
                       bE = switchE04
                       aC = switchC03
                       aE = switchE03
                       dC = switchC02
                       dE = switchE02


                       # D2
                   elif moves[i] == "K":
                       pC = hC
                       oE = gE
                       oC = gC


                       lC = switchC020
                       kE = switchE019
                       kC = switchC019


                       hC = switchC016
                       gE = switchE015
                       gC = switchC015


                       tC = switchC012
                       sE = switchE011
                       sC = switchC011


                       wC = switchC021
                       wE = switchE021
                       vC = switchC024
                       vE = switchE024
                       uC = switchC023
                       uE = switchE023
                       xC = switchC022
                       xE = switchE022


       else:
           change_list = (
                       aE + bE + cE + dE + eE + fE + gE + hE + iE + jE + kE + lE + mE + nE + oE + pE + qE + rE + sE + tE + uE + vE + wE + xE +
                       aC + bC + cC + dC + eC + fC + gC + hC + iC + jC + kC + lC + mC + nC + oC + pC + qC + rC + sC + tC + uC + vC + wC + xC)


           list_change = [(aE + bE + cE + dE + eE + iE + mE + qE), (eE + fE + gE + hE + dE + lE + xE + rE), (iE + jE + kE + lE + cE + fE + uE + pE), (mE + nE + oE + pE + bE + jE + vE + tE), (qE + rE + sE + tE + aE + nE + wE + hE), (uE + vE + wE + xE + kE + oE + sE + gE), (aE + bE + cE + dE + eE + fE + gE + hE + iE + jE + kE + lE + mE + nE + oE + pE + qE + rE + sE + tE + uE + vE + wE + xE + aC + bC + cC + dC + eC + fC + gC + hC + iC + jC + kC + lC + mC + nC + oC + pC + qC + rC + sC + tC + uC + vC + wC + xC), (dC + iC + lE + fC + fE), (cC + jC + jE + mC + pE), (aC + rC + rE + eC + hE), (bC + qC + tE + nC + nE)]


           return list_change




def cross():
   r = 0
   while True:
       permutations = itertools.permutations(letters, r)
       for combo in permutations:
           solution_cross = ''.join(combo)
           print(solution_cross)
           # change
           change_list2 = change(solution_cross, AE, BE, CE, DE, EE, FE, GE, HE, IE, JE, KE, LE, ME, NE, OE, PE, QE, RE, SE,
                                        TE, UE,
                                        VE, WE, XE, AC, BC, CC, DC, EC, FC, GC, HC, IC, JC, KC, LC, MC, NC, OC, PC, QC, RC, SC, TC,
                                        UC, VC,
                                        WC, XC)


           print(change_list2)
           #print(" -> THIS DOESN'T WORK LOL")
           if change_list2[0] == "WWWWOGRB" or change_list2[1] == "OOOOWGYB" or change_list2[2] == "GGGGWOYR" or change_list2[3] == "RRRRWGYB" or change_list2[4] == "BBBBWRYO" or change_list2[5] == "YYYYGRBO":
               print("breakkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
               break
       if change_list2[0] == "WWWWOGRB" or change_list2[1] == "OOOOWGYB" or change_list2[2] == "GGGGWOYR" or change_list2[3] == "RRRRWGYB" or change_list2[4] == "BBBBWRYO" or change_list2[5] == "YYYYGRBO":
           print("breakkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk")
           break
       r += 1




   print(solution_cross)
   return change_list2


cross1 = cross()


AE = cross1[6][0]
BE = cross1[6][1]
CE = cross1[6][2]
DE = cross1[6][3]
EE = cross1[6][4]
FE = cross1[6][5]
GE = cross1[6][6]
HE = cross1[6][7]
IE = cross1[6][8]
JE = cross1[6][9]
KE = cross1[6][10]
LE = cross1[6][11]
ME = cross1[6][12]
NE = cross1[6][13]
OE = cross1[6][14]
PE = cross1[6][15]
QE = cross1[6][16]
RE = cross1[6][17]
SE = cross1[6][18]
TE = cross1[6][19]
UE = cross1[6][20]
VE = cross1[6][21]
WE = cross1[6][22]
XE = cross1[6][23]


AC = cross1[6][24]
BC = cross1[6][25]
CC = cross1[6][26]
DC = cross1[6][27]
EC = cross1[6][28]
FC = cross1[6][29]
GC = cross1[6][30]
HC = cross1[6][31]
IC = cross1[6][32]
JC = cross1[6][33]
KC = cross1[6][34]
LC = cross1[6][35]
MC = cross1[6][36]
NC = cross1[6][37]
OC = cross1[6][38]
PC = cross1[6][39]
QC = cross1[6][40]
RC = cross1[6][41]
SC = cross1[6][42]
TC = cross1[6][43]
UC = cross1[6][44]
VC = cross1[6][45]
WC = cross1[6][46]
XC = cross1[6][47]

def F2L():
    r = 1
    while True:
        permutations = itertools.permutations(letters, r)
        for combo in permutations:
            solution_f2l = ''.join(combo)
            print(solution_f2l)
            # change
            change_list2 = change(solution_f2l, AE, BE, CE, DE, EE, FE, GE, HE, IE, JE, KE, LE, ME, NE, OE, PE, QE,
                                  RE, SE,
                                  TE, UE,
                                  VE, WE, XE, AC, BC, CC, DC, EC, FC, GC, HC, IC, JC, KC, LC, MC, NC, OC, PC, QC, RC,
                                  SC, TC,
                                  UC, VC,
                                  WC, XC)

            #print("IT WORKS!")
            print(change_list2)

            #white
            if cross1[0] == "WWWWOGRB" and (cross1[7] == "WGGOO" or cross1[8] == "WGGRR" or cross1[9] == "WBBOO" or cross1[10] == "WBBRR"):
                    break

        if cross1[0] == "WWWWOGRB" and (cross1[7] == "WGGOO" or cross1[8] == "WGGRR" or cross1[9] == "WBBOO" or cross1[10] == "WBBRR"):
            break
        r += 1

    print(solution_f2l)
    return change_list2

F2L()




