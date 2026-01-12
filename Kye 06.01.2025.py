def line_graph():

    import matplotlib.pylab as plt 

    #Sample data
    x = [89 , 27, 39, 48, 19.5,]
    y = [27, 49, 6, 88, 97.9]

    #Creating a line graph 
    plt.plot(x,y)

    plt.show()

def bar_graph():
    
    import matplotlib.pylab as plt 

    #Sample data
    x = [5, 10, 15, 20, 25,]
    y = [10, 20, 30, 40, 50,]
    
    #Creating a bar chart
    plt.bar(x,y)
    plt.title("Testing")
    plt.xlabel("Categories")
    plt.ylabel("Amount")
    plt.show()

def pie_chart():

    import matplotlib.pylab as plt

    #Sample data
    labels = ["Apples", "Bannanas", "Cherries", "Dates"]
    data = [30,25,20,10]

    #This creates the pie chart with labels
    plt.pie(data, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.axis('equal') # Ensures the pie is drawn as a circle
    plt.title("Favorite Fruits")
    plt.show()

bar_graph()