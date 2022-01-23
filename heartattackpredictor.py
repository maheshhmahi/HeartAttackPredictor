from sklearn import svm
from sklearn.model_selection import train_test_split
import pandas as pd
from tkinter import *
from tkinter import messagebox

root=Tk()
resData=[]

def predictor():
    data1=pd.read_csv('bpchart.csv')
    x1field=['Age','MinBP','AvgBP','MaxBP','TimeInCare']
    x2field=['Age','MinBP','AvgBP','MaxBP','TimeInCare','Chances']
    #print(data1)
    x1=data1.iloc[:,:-2] 
    y1=data1['Chances']   #Finding
    x2=data1.iloc[:,:-1] 
    y2=data1['TimeTillDeath']   #Finding
    #x1_train, x1_test, y1_train, y1_test=train_test_split(x1,y1,test_size=1/3)
    #x2_train, x2_test, y2_train, y2_test=train_test_split(x2,y2,test_size=1/3)

    #Training
    clf1=svm.SVC(kernel='linear')
    clf2=svm.SVC(kernel='linear')
    #print('\nTested Case:\n', x1_test)
    clf1.fit(x1[x1field],y1)
    clf2.fit(x2[x2field],y2)

    #Prediction
    #name=input('Enter Patient Name: ')
    #age=int(input('Enter age of the patient: '))
    #minbp=int(input('Enter the Minimum Recorded Blood Pressure: '))
    #maxbp=int(input('Enter the Maximum Recorded Blood Pressure: '))
    avgbp=int(int(Minbp.get())+int(Maxbp.get()))/2
    #tincare=int(input('Enter Time in care: '))
    if(Age.get()>0):
        x1_test=[[Age.get(),Minbp.get(),avgbp,Maxbp.get(),Tincare.get()]]
        pred_chance=clf1.predict(x1_test)
        x2_test=[[Age.get(),Minbp.get(),avgbp,Maxbp.get(),Tincare.get(),int(pred_chance)]]
        pred_timeOD=clf2.predict(x2_test)
        #Display
        #print('\nResults:')
        #print('\nName: ',name)
        #print('Age: ',age)
        #Store current log in bpchart.csv
        resData=[int(pred_chance), int(pred_timeOD)]
        result='Chances of Heart-attacks are High\nConsult Doctor as Soon as Possible\n\nNote:Within '+str(resData[1])+' day(s)'
        if(resData[0]==1):
            msg1=messagebox.showinfo('Results', result)
        else:
            msg1=messagebox.showinfo('Results','Chances of Heart-attacks are Low')
        fp=open('bpchart.csv','a')
        data='\n'+Name.get()+','+str(Age.get())+','+str(Minbp.get())+','+str(avgbp)+','+str(Maxbp.get())+','+str(Tincare.get())+','+str(int(pred_chance))+','+str(int(pred_timeOD[0]))
        fp.write(data)
        
C = Canvas(root, height = 250, width = 300)
w2 = Label(root, justify=LEFT, text="Heart Attack Predictor")
w2.config(font=("Candara", 16))
w2.grid(row=1, column=0, columnspan=2, padx=100)
Name=StringVar()
NameLb = Label(root, text="Name of the Patient")
NameLb.grid(row=6, column=0, pady=5, sticky=W, padx=15)
NameEn = Entry(root, textvariable=Name)
NameEn.grid(row=6, column=1, padx=15, pady=5)
Age=IntVar()
Minbp=IntVar()
Maxbp=IntVar()
Tincare=IntVar()
AgeLb = Label(root, text="Age of the Patient")
AgeLb.grid(row=7, column=0, pady=5, sticky=W, padx=15)
AgeEn = Entry(root, textvariable=Age)
AgeEn.grid(row=7, column=1, padx=15, pady=5)
MinbpLb = Label(root, text="Minimum Recorded Blood Pressure")
MinbpLb.grid(row=8, column=0, pady=5, sticky=W, padx=15)
MinbpEn = Entry(root, textvariable=Minbp)
MinbpEn.grid(row=8, column=1, padx=15, pady=5)
MaxbpLb = Label(root, text="Maximum Recorded Blood Pressure")
MaxbpLb.grid(row=9, column=0, pady=5, sticky=W, padx=15)
MaxbpEn = Entry(root, textvariable=Maxbp)
MaxbpEn.grid(row=9, column=1, padx=15, pady=5)
TincareLb = Label(root, text="Time in care")
TincareLb.grid(row=10, column=0, pady=5, sticky=W, padx=15)
TincareEn = Entry(root, textvariable=Tincare)
TincareEn.grid(row=10, column=1, padx=15, pady=5)
Res = Button(root, text="Predict Results", command=predictor)
Res.grid(row=11, column=1,padx=10, pady=15)
root.mainloop()   
