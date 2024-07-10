import tkinter
from tkinter import *
from tkinter import ttk,messagebox


def reg():
    win.destroy()
    base = Tk()
    base.geometry("600x600")  
    base.title('Register to get started')  
  
    lbl_0 = Label(base, text="Registration form", width=20,font=("bold",20))  
    lbl_0.place(x=90,y=60)  
  
    lbl_1 =Label (base, text= "FullName:*", width=20,font=("bold",10))  
    lbl_1.place(x=80,y=130)  
  
    enter_1= Entry(base)  
    enter_1.place(x=240,y=130)

    lbl_2 =Label(base, text= "Age:*", width=20,font=("bold",10))  
    lbl_2.place(x=65,y=180)  
  
    
    enter_2 = Entry(base)  
    enter_2.place(x=240,y=180)

   
    lbl_3 = Label(base, text="Email:*", width=20,font=("bold",10))  
    lbl_3.place(x=68,y=230)  
      
    enter_3 = Entry(base)  
    enter_3.place(x=240,y=230)


    lbl_4 = Label(base, text="Gender:*", width=20,font=("bold",10))  
    lbl_4.place(x=70,y=280)


    enter_4=ttk.Combobox(base,values=["Male","Female","Pregnant women"])
    enter_4.place(x=240,y=280)


    def onclick_save():
        if enter_1.get()!='':
            print("Name:",enter_1.get())
        else:
            print('Fill your name')
        if enter_2.get()!='':
            print("Age:",enter_2.get())
        else:
            print('Enter your age')
        if enter_3.get()!='':
            print("Mail ID:",enter_3.get())
        else:
            print('Enter your mail ID')
        if enter_4.get()!='':
            global Gender
            Gender=enter_4.get()
            print("Gender:",enter_4.get())
        else:
            print('Enter your gender')
        if enter_1.get()!='' and enter_2.get()!='' and enter_3.get()!='' and enter_4.get()!='':
            print('Registration done successfully')
        else:
            print('Fill in the mandatory details to move to the next page')

        
    

    def ac_lvl():
        base.destroy()
        data = Tk()  
        data.geometry("650x650")  
        data.title('Daily routine')  
                  
        label1 = Label(data, text="Let's know your routine:)", width=20,font=("bold",20))  
        label1.place(x=90,y=60)

        label2 = Label(data, text="Activity Level:", width=20,font=("bold",10))  
        label2.place(x=40,y=150)  

        def val(value):
            global a
            a = value

        activity=StringVar(data, 'No activity')
                
        Radiobutton(data, text="No activity",variable=activity,value="No activity",command=val("No activity")).place(x=230, y=150)  
        Radiobutton(data, text="Light activity",variable=activity,value="Light activity",command=val("Light activity")).place(x=230,y=180)
        Radiobutton(data, text="Moderate activity",variable=activity,value="Moderate activity",command=val("Moderate activity")).place(x=230,y=210)
        Radiobutton(data, text="Hard activity",variable=activity,value="Hard activity",command=val("Hard activity")).place(x=230,y=240)
        Radiobutton(data, text="Very hard activity",variable=activity,value="Very hard activity",command=val("Very hard activity")).place(x=230,y=270)
        Radiobutton(data, text="Extreme activity",variable=activity,value="Extreme activity",command=val("Extreme activity")).place(x=230,y=300)

     

        label4= Label(data,text = "Wake-up time:",width=20,font=("bold",10)) 
        label4.place(x=40,y=360)

        entry5=ttk.Combobox(data, state="readonly",values=["0","1","2","3","4","5","6","7","8","9","10","11","12"],width=5,font=("bold",10))
        entry5.place(x=230, y=360)

        entry6=ttk.Combobox(data, state="readonly",values=["00","15","30","45"],width=5,font=("bold",10))
        entry6.place(x=340, y=360)

        entry7=ttk.Combobox(data, state="readonly",values=["AM","PM"],width=5,font=("bold",10))
        entry7.place(x=450, y=360)

        label5= Label(data,text = "Bed time:",width=20,font=("bold",10)) 
        label5.place(x=25,y=420)

        entry8=ttk.Combobox(data, state="readonly",values=["0","1","2","3","4","5","6","7","8","9","10","11","12"],width=5,font=("bold",10))
        entry8.place(x=230, y=420)

        entry9=ttk.Combobox(data, state="readonly",values=["00","15","30","45"],width=5,font=("bold",10))
        entry9.place(x=340, y=420)

        entry10=ttk.Combobox(data, state="readonly",values=["AM","PM"],width=5,font=("bold",10))
        entry10.place(x=450, y=420)

        def onclick_submit():
            global Activity_Level
            Activity_Level=activity.get()
            print('Activity level:',Activity_Level)
            global Hours
            Hours=entry5.get()
            global Mins
            Mins=entry6.get()
            global Meridian
            Meridian=entry7.get()
            print("Wake up time:",Hours,':',Mins,':',Meridian)
            global hours
            hours=entry8.get()
            global mins
            mins=entry9.get()
            global meridian
            meridian=entry10.get()
            print("Bed time:",hours,':',mins,':',meridian)
            data.destroy()   
                


        button = Button(data, text="Done...",command=onclick_submit) 
        button.place(x=325, y=500)
        data.mainloop()
        

    Button(base, text='Save' , width=20, bg="grey",fg='white',command=onclick_save).place(x=120,y=380)

    Button(base, text='Submit' , width=20, bg="grey",fg='white',command=ac_lvl).place(x=290,y=380)  
    base.mainloop()        
    


win=Tk()

win.geometry('325x200')
win.title('Welcome:)')


button=Button(win, text='Let\'s Go' , width=20, bg="black",fg='white',command=reg).place(x=80,y=80)
win.mainloop()




weight = float(input("Enter your weight in kg: "))

if Gender=='Male' and Activity_Level=='No activity':
    wi=weight*0.032
    print("Your daily water intake quantity is ",wi,'ltrs')
elif Gender=='Male' and Activity_Level=='Light activity':
    wi=weight*(0.032+0.002)
    print("Your daily water intake quantity is ",wi,'ltrs')
elif Gender=='Male' and Activity_Level=='Moderate activity':
    wi=weight*(0.032+0.004)
    print("Your daily water intake quantity is ",wi,'ltrs')
elif Gender=='Male' and Activity_Level=='Hard activity':
    wi=weight*(0.032+0.006)
    print("Your daily water intake quantity is ",wi,'ltrs')
elif Gender=='Male' and Activity_Level=='Very hard activity':
    wi=weight*(0.032+0.008)
    print("Your daily water intake quantity is ",wi,'ltrs')
elif Gender=='Male' and Activity_Level=='Extreme activity':
    wi=weight*(0.032+0.009)
    print("Your daily water intake quantity is ",wi,'ltrs')
else:
    print('   ')




if Gender=='Female' and Activity_Level=='No activity':
    wi=weight*0.03
    print("Your daily water intake quantity is ",wi,'ltrs')
elif Gender=='Female' and Activity_Level=='Light activity':
    wi=weight*(0.03+0.002)
    print("Your daily water intake quantity is ",wi,'ltrs')
elif Gender=='Female' and Activity_Level=='Moderate activity':
    wi=weight*(0.03+0.004)
    print("Your daily water intake quantity is ",wi,'ltrs')
elif Gender=='Female' and Activity_Level=='Hard activity':
    wi=weight*(0.03+0.006)
    print("Your daily water intake quantity is ",wi,'ltrs')
elif Gender=='Female' and Activity_Level=='Very hard activity':
    wi=weight*(0.03+0.008)
    print("Your daily water intake quantity is ",wi,'ltrs')
elif Gender=='Female' and Activity_Level=='Extreme activity':
    wi=weight*(0.03+0.009)
    print("Your daily water intake quantity is ",wi,'ltrs')
else:
    print('  ')



if Gender=='Pregnant women' and Activity_Level=='No activity':
    wi=weight*0.031
    print("Your daily water intake quantity is ",wi,'ltrs')
elif Gender=='Pregnant women' and Activity_Level=='Light activity':
    wi=weight*(0.031+0.002)
    print("Your daily water intake quantity is ",wi,'ltrs')
elif Gender=='Pregnant women' and Activity_Level=='Moderate activity':
    wi=weight*(0.031+0.004)
    print("Your daily water intake quantity is ",wi,'ltrs')
elif Gender=='Pregnant women' and Activity_Level=='Hard activity':
    wi=weight*(0.031+0.006)
    print("Your daily water intake quantity is ",wi,'ltrs')
elif Gender=='Pregnant women' and Activity_Level=='Very hard activity':
    wi=weight*(0.031+0.008)
    print("Your daily water intake quantity is ",wi,'ltrs')
elif Gender=='Pregnant women' and Activity_Level=='Extreme activity':
    wi=weight*(0.031+0.009)
    print("Your daily water intake quantity is ",wi,'ltrs')
else:
    print('  ')































    
