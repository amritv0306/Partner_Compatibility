import pandas as pd
import win32com.client as wincl

dataframe = pd.read_csv("datasets/data.csv")
# print(dataframe)
# print(dataframe.shape)
# print(dataframe[['boy', 'girl']])
# print(dataframe.boy, dataframe.girl)
dataframe['result'] = ~(dataframe['boy'] ^ dataframe['girl']) & 1 # using XNOR operator to find the final result, if they have same linkingss and disliking's, final result will be 1 and vice-versa.

# print(dataframe)
# filtered_dataframe = dataframe[dataframe['result'] == 0]
# print(filtered_dataframe['feature'])

result_sum = dataframe['result'].sum()
# print(result_sum)
r,c = dataframe.shape
final_compatibility = (result_sum/r)*100

speaker = wincl.Dispatch("SAPI.SpVoice")
speaker.Speak(f"Welcome to the compatibility test")

user_input = int(input("Are you doing this compatibility test for a friend or a partner\nPress 1 for friend and 2 for partner: "))
relation = {1:"Friend", 2:"Partner"}

print(f"Compatibility = {final_compatibility}%")
speaker.Speak(f"you both are {int(final_compatibility)}% compatibile")

if final_compatibility >= 65:
    print("Congratulations")    
    speaker.Speak(f"you guy's have great compatibility together, congratulations, she can be your {relation[user_input]}")
else:
    print("I am sorry")
    speaker.Speak(f"I am sorry to say but she can't be your {relation[user_input]}!")