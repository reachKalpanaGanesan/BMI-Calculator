import tkinter
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as graph
import csv
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

result=""

def showResult():
    name=nameData.get()
    age=ageData.get()
    height=heightData.get()
    weight=weightData.get()
    if name!="" and name!=" " and age!="" and height!="" and weight!="" and height!=" " and weight!=" ": # need to ensure the dataype is int for height age and weight
        # convert height and weight to required standard.
        name=name.title()
        age = int(age)
        height=float(height)
        weight=float(weight)
        if age>0 and height>0 and weight>0:
            bmi = round(weight / (height ** 2),2)
            if bmi >= 30:
                result='Obese'
            elif bmi >= 25 and bmi <= 29.9:
                result='Overweight'
            elif bmi >= 18.5 and bmi <= 24.9:
                result='Normal'
            else:
                result='Underweight'
            with open('bmiData.txt','a') as fileObject:
                fileObject.write(name+","+str(age)+","+str(height)+","+str(weight)+","+str(bmi)+","+result+"\n")
            print("Saved data to file.")

            frame1 = tkinter.Frame(window)
            frame1.pack()

            resultFrame = tkinter.LabelFrame(frame1, text="BMI Result")
            resultFrame.grid(row=2, column=0)
            resultLabel = tkinter.Label(resultFrame, text="Your BMI Result: ")
            resultLabel.grid(row=2, column=0)
            resultValue=tkinter.StringVar()
            resultValue.set(result)
            resultData = tkinter.Entry(resultFrame,textvariable=resultValue,state='disabled')
            resultData.grid(row=2, column=1)
            graphButton= tkinter.Button(frame1,text="Show Graph",command=showGraph)
            graphButton.grid(row=3,column=0)

        else:
            tkinter.messagebox.showwarning(title="Warning",message="Age/Weight/Height cannot be zero")
    else:
        tkinter.messagebox.showwarning(title="Warning",message="All inputs are mandatory.")

def readFile():
    bmiData = {'Underweight': 0, 'Overweight': 0, 'Obese': 0, 'Normal': 0}
    with open("bmiData.txt",'r') as readObject:
        reader=csv.reader(readObject)
        for data in reader:
            name,age,height,weight,bmi,bmiStatus=data
            bmiData[bmiStatus]+=1
    print(bmiData)
    return bmiData

def showGraph():
    bmiGraph=readFile()
    fig, axs = graph.subplots()
    axs.pie(bmiGraph.values(), labels=bmiGraph.keys(), autopct='%1.1f%%')
    frame2 = tkinter.Frame(window)
    frame2.pack()
    graphFrame = tkinter.LabelFrame(frame2, text="Overall BMI Percentage")
    graphFrame.grid(row=3, column=0)
    canvas = FigureCanvasTkAgg(fig, master=graphFrame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)

window=tkinter.Tk()
window.title("BMI Calculator")
frame=tkinter.Frame(window)
frame.pack()

userInfoFrame=tkinter.LabelFrame(frame,text="User Information")
userInfoFrame.grid(row=0,column=0)

namelabel=tkinter.Label(userInfoFrame,text="Name: ")
namelabel.grid(row=0,column=0)
nameData=tkinter.Entry(userInfoFrame)
nameData.grid(row=0,column=1)

ageLabel=tkinter.Label(userInfoFrame,text="Age: ")
ageLabel.grid(row=1,column=0)
ageData=tkinter.Spinbox(userInfoFrame,from_=10,to=100,width=5)
ageData.grid(row=1,column=1)

heightLabel=tkinter.Label(userInfoFrame,text="Height (in meter): ")
heightLabel.grid(row=2,column=0)
#heightType=ttk.Combobox(userInfoFrame,values=['meter','feet'])
#heightType.grid(row=2,column=1)
heightData=tkinter.Entry(userInfoFrame,width=5)
heightData.grid(row=2,column=1)

weightLabel=tkinter.Label(userInfoFrame,text="Weight (in Kilogram): ")
weightLabel.grid(row=3,column=0)
weightData=tkinter.Entry(userInfoFrame,width=5)
weightData.grid(row=3,column=1)

bmiResultButton=tkinter.Button(frame,text="Show Result",command=showResult)
bmiResultButton.grid(row=1,column=0)

window.mainloop()
