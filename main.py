
# Python program to read
# json file
 
import json
import matplotlib.pyplot as plt

def simple_graph():
    # Opening JSON file
    e1 = open('data/Exchange_1.json')
    # returns JSON object as 
    # a dictionary
    data = json.load(e1)
    
    # Iterating through the json
    # list

    X = []
    Y = []

    for i in data:
        if i["MessageType"] == "NewOrderAcknowledged":
            X.append(int(i["TimeStampEpoch"]))
            Y.append(i["OrderPrice"])
            print(i["OrderID"])

    plt.ion() # turn interactive mode on
    animated_plot = plt.plot(X, Y, 'ro')[0]

    for i in range(len(X)):
        animated_plot.set_xdata(X[0:i])
        animated_plot.set_ydata(Y[0:i])
        plt.draw()
        plt.pause(0.1)
        
    #Closing file
    e1.close()

if __name__ == "__main__":
    simple_graph()