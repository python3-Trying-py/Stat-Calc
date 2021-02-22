while True:
    que1=input("Welcome to Stat Calc. What function are you Calculating?\n1)Mean\n2)Standard Deviation\n3)Zscore and Percentile\n")
    queMean="1" or "Mean"
    queSD="2" or "Standard deviation" or "SD"
    queZ="3" or "Zscore and Percentile" or "Zscore" or "Z score" or "z" or "Z"
    if que1==queMean:
        exec(open('Data set to mean calc.py').read())
    elif que1==queSD:
        exec(open('SD calc.py').read())
    elif que1==queZ:
        exec(open('Zscore and Percentile calc.py').read())
    else:
        print("invalid function")
