def bar_graph():
    
    import matplotlib.pylab as plt 

    #Sample data
    Names = ["Dave", "Lilly", "Louise", "Dylan",]
    Amount = [10, 20, 40, 50,]
    
    #Creating a bar chart
    plt.bar(Names,Amount)
    plt.title("Testing")
    plt.xlabel("Categories")
    plt.ylabel("Amount")

    plt.style.use

    #The 2 lines below are used to label the values of the bars on the chart.
    bar_container = plt.bar(Names, Amount)
    plt.bar_label(bar_container, fmt='{:,.0f}')

    plt.show()

import matplotlib.pylab as plt
print(plt.style.available)