import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\M2500457\OneDrive - Middlesbrough College\Documents\GitHub\DSD-Y1-Python\copy of task4a data.csv")

def task_1():

    print(df.head())
    print(df.info())
##task_1()
def task_2():
    #take hashes off beforing running 
    def daily_likes_average():
        daily_avg = df.groupby("Date")["Likes"].mean()
        overall_daily_average = daily_avg.mean()
        rounded_likes = overall_daily_average.round()
        print(rounded_likes)
    #daily_likes_average()
    def daily_shares_average():
        daily_avg = df.groupby("Date")["Shares"].mean()
        overall_daily_average = daily_avg.mean()
        rounded_shares = overall_daily_average.round()
        print(rounded_shares)
    #daily_shares_average()
    def daily_comments_average():
        daily_avg = df.groupby("Date")["Comments"].mean()
        overall_daily_average = daily_avg.mean()
        rounded_comments = overall_daily_average.round()
        print(rounded_comments)
    #daily_comments_average()
    def highest_interactions():
        df["Interactions"] = df["Likes"] + df["Shares"] + df["Comments"]
        interactions_by_type = (
        df.groupby("Post Type")["Interactions"]
        .sum()
        .sort_values(ascending=False)
        )
        top_post_type = interactions_by_type.idxmax()
        print(top_post_type)
    #highest_interactions()
    def time_of_day_impact(df):
        df["Interactions"] = df["Likes"] + df["Shares"] + df["Comments"]
        avg_by_time = df.groupby("Time")["Interactions"].mean()

        plt.figure()
        plt.bar(avg_by_time.index, avg_by_time.values)
        plt.xticks(rotation=45, ha="right")
        plt.xlabel("Time of Day")
        plt.ylabel("Average Interactions")
        plt.title("Average Interactions by Time of Day")
        plt.tight_layout()
        plt.show()
    #time_of_day_impact(df)
#task_2()


def task_3():
    def average_likes_per_day():
        # Convert Date column to datetime objects
        df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
        
        # Calculate the average likes for each unique date
        avg_likes_per_day = df.groupby('Date')['Likes'].mean()
        
        # Display the results
        print("Average Likes Per Day:")
        print(avg_likes_per_day)
        
        # Optional: Plotting the trend
        avg_likes_per_day.plot(kind='line', title='Likes Trend Over Time')
        plt.ylabel('Average Likes')
        plt.show()
    average_likes_per_day()
    def total_interactions_by_post_type():
            df["Interactions"] = df["Likes"] + df["Shares"] + df["Comments"]

            interactions_by_type = (
                df.groupby("Post Type")["Interactions"]
                .sum()
                .sort_values(ascending=False)
            )

            x = interactions_by_type.index      # Post Types
            y = interactions_by_type.values     # Total interactions

            plt.bar(x, y)
            plt.xlabel("Post Type")
            plt.ylabel("Total Interactions")
            plt.title("Total Interactions by Post Type")
            plt.show()
    total_interactions_by_post_type()
    def time_of_day_impact(df):
        df["Interactions"] = df["Likes"] + df["Shares"] + df["Comments"]
        avg_by_time = df.groupby("Time")["Interactions"].mean()

        plt.figure()
        plt.plot(avg_by_time.index, avg_by_time.values)
        plt.xticks(rotation=45, ha="right")
        plt.xlabel("Time of Day")
        plt.ylabel("Average Interactions")
        plt.title("Average Interactions by Time of Day")
        plt.tight_layout()
        plt.show()
    time_of_day_impact(df)
task_3()


def task_4():
    print("Hi")
    #Which type of post performs best overall?
    #A poll perfroms the bst overall.
    #What trend do you notice across the campaign dates?
    #I noticed that posts made on the 9th September perform the best.
    #At what time of day do posts get the most interaction?
    #Posts get the most interaction when posted between 2 and 4pm.


