# Python program to read
# json file
 
import json
import matplotlib.pyplot as plt

# Loads json file and returns a json object
def read_data(filename):
    file = open('data/'+ filename)
    data = json.load(file)
    file.close()
    return data


# A simple matplot plotting of the data
def simple_graph():
    data = read_data("Exchange_1.json")
    X = []
    Y = []
    for i in data:
        if i["MessageType"] == "NewOrderRequest":
            X.append(int(i["TimeStampEpoch"]))
            Y.append(i["OrderPrice"])
            print(i["OrderID"])
    animated_plot = plt.plot(X, Y, 'ro')[0]

    for i in range(len(X)):
        animated_plot.set_xdata(X[0:i])
        animated_plot.set_ydata(Y[0:i])
        plt.draw()
    plt.show()

if __name__ == "__main__":
    simple_graph()