import numpy as np

def calculate(list):

    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")

    else:
        numArray = np.array(list).reshape(3,3)

        meanY = np.mean(numArray, axis = 0).tolist()
        meanX = np.mean(numArray, axis = 1).tolist()
        meanR = float(np.mean(numArray))

        varinaceY = np.var(numArray, axis = 0).tolist()
        varianceX = np.var(numArray, axis = 1).tolist()
        varinaceR = float(np.var(numArray))

        stdY = np.std(numArray, axis = 0).tolist()
        stdX = np.std(numArray, axis = 1).tolist()
        stdR = float(np.std(numArray))

        maxY = np.max(numArray, axis = 0).tolist()
        maxX = np.max(numArray, axis = 1).tolist()
        maxR = int(np.max(numArray))


        minY = np.min(numArray, axis = 0).tolist()
        minX = np.min(numArray, axis = 1).tolist()
        minR = int(np.min(numArray))


        sumY = np.sum(numArray, axis = 0).tolist()
        sumX = np.sum(numArray, axis = 1).tolist()
        sumR = int(np.sum(numArray))


        calculations = {
            "mean":[meanY,meanX,meanR],
            "variance":[varinaceY,varianceX,varinaceR],
            "standard deviation":[stdY,stdX,stdR],
            "max":[maxY,maxX,maxR],
            "min":[minY,minX,minR],
            "sum":[sumY,sumX,sumR]
        
        }

        return calculations