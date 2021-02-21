import scipy.stats as st
#acquires values
queEV=float(input("What is the expected value?\n"))
queM=float(input("What is the mean of the distribution?\n"))
queSD=float(input("What is the standard deviation of the distribution?\n"))
#calculates Z score
Zs1=(queEV - queM)
Zscore=(Zs1 / queSD)
#calculates percentile
Prob=st.norm.cdf(Zscore)
ProbInv=(1 - Prob)
Per=(Prob * 100)
PerInv=(ProbInv * 100)
print("Z score = " + str(Zscore))
print("Percentile = " + str(Per) + "%")
print("Percentile compliment = " + str(PerInv) + "%")
#big thanks to urlordjames for telling me about scipy
    
