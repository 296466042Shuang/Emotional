# Author: Zhi Kai
# Time:  0:38
import pandas as pd

#open the file
import pandas.errors


#data =pd.read_csv('D:\My PhD\Burssa Project\TEST.csv', encoding='utf-8',header=None,sep = '\t')
data = pd.read_csv(open('D:\My PhD\Burssa Project\TEST.csv' , 'r', encoding='utf-8'))
data_list=[]
#get the number of rows
try:
    rows=data.shape[0]
    colums=data.shape[1]
except pandas.errors.ParserError as e:
    print("something failed")

print(rows)
print(colums)
#print(data.iloc[2,0])
for i in range(rows):
    if "Time" in data.iloc[i,0]:
        data_list.append(i+2)
size=len(data_list)
data_list.insert(0,1)
print(data_list)
print(size)
results=[]
for i in range(len(data_list) - 1):
    results.append(data_list[i:i + 2])
print(results)
print(len(results))
for i in range(len(results)):
    Temp_data=data.iloc[results[i+1][0]-1:results[i+1][1]-1,:]
    #print(type(Temp_data))
    Temp_data=pd.DataFrame(Temp_data)
    print(type(Temp_data))
    print(Temp_data)
    #print(Temp_data)
    #Save_data=Temp_data[["Time, HR, GSR"]].str.split(',')
    #print(Save_data)
    #Temp_data.to_excel("D:\My PhD\Burssa Project\\ " + str(i) + ".xlsx", sheet_name='Sheet1', index=False)
    # for j in range(3):
    #     print(j)
    #     Saved_data=Temp_data.iloc[:, j]
    #     #print(Saved_data)
    #     print(type(Saved_data))
    #     if j ==0:
    #         Saved_data.to_excel("D:\My PhD\Burssa Project\\"+str(i)+"-Time.xlsx",sheet_name='Sheet1', index=False)
    #     if j ==1:
    #         Saved_data.to_excel("D:\My PhD\Burssa Project\\"+str(i) + "-HR.xlsx", sheet_name='Sheet1', index=False)
    #     if j ==2:
    #         Saved_data.to_excel("D:\My PhD\Burssa Project\\"+str(i) + "-GSR.xlsx", sheet_name='Sheet1', index=False)
    Temp_data.to_excel("D:\My PhD\Burssa Project\Data after processing\\"+"record_"+str(i+1)+".xlsx",sheet_name="Sheets1",index=False)
    print("存入成功")