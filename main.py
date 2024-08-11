import tkinter
import math


#Configure Window 1
window = tkinter.Tk()
window.title("Input Window")
window.configure(bg='#002421')

def renderElems(*render):    
    #Render Elements 
    for i in range(len(render)):      
        for l in range(3):
            if(i*3 + l >= len(render)):
                break
            render[(i*3 + l)].grid(row=i, column=l, padx=3,pady=3)

#Buttons
b1 = tkinter.Button(window, text="1")
b2 = tkinter.Button(window, text="2")
b3 = tkinter.Button(window, text="3")
b4 = tkinter.Button(window, text="4")
b5 = tkinter.Button(window, text="5")
b6 = tkinter.Button(window, text="6")
b7 = tkinter.Button(window, text="7")
b8 = tkinter.Button(window, text="8")
b9 = tkinter.Button(window, text="9")
b10 = tkinter.Button(window, text="0")
b11 = tkinter.Button(window, text="+/-")
b12 = tkinter.Button(window, text=".")
equals = tkinter.Button(window, text="=")

renderElems(b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,equals)




#enter_URL = tkinter.Label(window, text="Enter Game URL:", bg='#424242', fg='#FFFFFF', pady=3, padx=3)
#entry_URL = tkinter.Entry(window)
#loading = tkinter.Label(window, text="Give it about 10 seconds, and your results should appear.", bg='#424242', fg='#FFFFFF', pady=3, padx=3)
#invalid = tkinter.Label(window, text="Invalid URL Entered! Only enter the URLs of Roblox Game Pages!", bg='#424242', fg='#FFFFFF', pady=3, padx=3)
#button_calculate = tkinter.Button(window, text="Calculate", command=begin)

#Render the elements (Window 1)



window.mainloop()
