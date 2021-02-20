import math
queM=float(input("What is the probability of the event?\n"))
quen=float(input("What is the sample size?\n"))
SDs1=(1 - queM)
SDs2=(queM * SDs1)
SDs3=(SDs2 / quen)
SDsF=math.sqrt(SDs3)
print("Standard Deviation is " + str(SDsF))
