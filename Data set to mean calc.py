queDS=input("Input sample data set.\n")
#finds commas
comma=(queDS.count(","))
if comma>=1:
    #purges commas
    queDS.replace(" ", "")
    DataSet = queDS.split(",")
else:
    DataSet=queDS.split(" ")
#puts the floats into an array
floats=[]
for i in DataSet:
    floats.append(float(i))
#adds all data values together
DataSetSum=sum(floats)
#finds number of data values
DataSetTotal=len(floats)
#divides sum by number
MeanDS=(DataSetSum / DataSetTotal)
print("Mean = " + str(MeanDS))

