from command import voicebox,brain
from tkinter import *




if __name__ == "__main__":
    voicebox().wishMe()
    while True:

        query = voicebox().takeCommand().lower()

        if 'and' in query:
            second_execution = query.split("and")
            #print(second_execution)
            count_and = query.count("and")
            for c in range(0,count_and+1):
                brain().execute(second_execution[c])
            
        else:
            brain().execute(query)
