# Daily Coding Problem: Problem #1781
# 2024-08-11
# Author: Spencer Trumbore

'''
The United States uses the imperial system of weights and measures,
which means that there are many different, seemingly arbitrary units
to measure distance. There are 12 inches in a foot, 3 feet in a yard,
22 yards in a chain, and so on.

Create a data structure that can efficiently convert a certain quantity
of one unit to the correct amount of any other unit. You should also
allow for additional units to be added to the system.
'''

class ImpUnit:
    def __init__(self, u: str,v: float):
        self.unit = u
        self.value = float(v)

    def __repr__(self):
         return "{%s, %s}" % (self.unit, self.value)

    dims = {
        "in": 1, "inch": 1, "inches": 1,
        "hh": 4, "hand": 4, "hands": 4,
        "ft": 12, "foot": 12, "feet": 12,
        "yd": 36, "yard": 36, "yards": 36,
        "chn": 792, "chain": 792, "chains": 792,
        "fur": 7920, "furlong": 7920, "furlongs": 7920,
        "mi": 63360, "mile": 63360, "miles": 63360,
        "lea": 190080, "league": 190080, "leagues": 190080
    }


def main():
    inU = input('type input imperial unit:\t')
    inV = input('type the value of the input unit:\t')
    outStr = input('type output imperial unit:\t')

    inUnit = ImpUnit(inU,inV)

    outUnit = ConvertImps(inUnit, outStr)
    print(outUnit)


def ConvertImps(inu: ImpUnit, outu: str) -> (ImpUnit | None):
   
    if (ImpUnit.dims.get(outu)): # if output unit exists
        if (ImpUnit.dims.get(inu.unit)): # if input unit exists
            inVal = ImpUnit.dims.get(inu.unit) # inVal is value of input unit
            outVal = ImpUnit.dims.get(outu) # outVal is value of output unit
            fac = inVal/outVal # conversion factor
            return ImpUnit(outu,inu.value*fac)
        else:
            print("Unknown input unit. Conversion canceled.")
    else:
            print("Unknown output unit. Conversion canceled.")
    return None

if __name__ == '__main__':
    main()