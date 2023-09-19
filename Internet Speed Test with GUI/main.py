from tkinter import *
#pip3 install speedtest-cli
import speedtest

#speedtest

def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    download = str(round(sp.download()/(10**6),1)) + " Mbps"
    upload = str(round(sp.upload()/(10**6),1)) + " Mbps"
    label2.config(text=download)
    label4.config(text=upload)

# graphics

sp = Tk()
sp.title("Internet Speed Test")
sp.geometry("600x500")
sp.config(bg="LightGreen")

label1 = Label(sp,text="Internet Speed Test",font=("Time New Roman",40,"bold"),bg="LightGreen")
label1.place(y=40,x=60)

# downloading speed

label2 = Label(sp,text="00",font=("Time New Roman",30,"bold"),bg="LightGreen")
label2.place(y=160,x=80)
label3 = Label(sp,text="Download Speed ",font=("Time New Roman",18,"bold"),bg="LightGreen")
label3.place(y=250,x=70)

# uploading speed

label4 = Label(sp,text="00",font=("Time New Roman",30,"bold"),bg="LightGreen")
label4.place(y=160,x=330)
label5 = Label(sp,text="Uploading Speed",font=("Time New Roman",18,"bold"),bg="LightGreen")
label5.place(y=250,x=330)

#button

but = Button(sp,text="CHECK SPEED",font=("Time New Roman",30,"bold"),relief=RAISED, command=speedcheck)
but.place(y=350,x=130)


sp.mainloop()
