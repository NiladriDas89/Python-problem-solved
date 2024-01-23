'''
Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black"]
'''
print("----------------------------------------------\ncommon concept \n")
color_list = ["Red","Green","White" ,"Black"]
print(color_list[0],color_list[3])#common concept 
print("----------------------------------------------\nstart,stop,step concept \n")
print(color_list[0::3])#start,stop,step concept 
print("----------------------------------------------\nDelete method using in this list \n")
#Delete method using in this list 
del(color_list[0::3])
print(color_list)
