import tkinter
import math


#Configure Window 1
window = tkinter.Tk()
window.title("Python Calculator")
window.configure(bg='#002421')

displayBuffer = ""
display = tkinter.Label(window, text="", bg='#424242', fg='#FFFFFF', padx=3, pady=3, width="20")
display.grid(row = 0, column = 0, columnspan=3)

def displayHandler(elem):
    global displayBuffer
    txt = elem.cget("text")
    
    if txt == "<":
        displayBuffer = displayBuffer[:-1]
    elif txt == "+/-":
        if not "-" in displayBuffer:
            displayBuffer = "-" + displayBuffer
        else:
            displayBuffer = displayBuffer[1:]
    elif txt == ".":
        if not "." in displayBuffer:
            displayBuffer += txt
    else:
        displayBuffer += txt

    global display
    display = tkinter.Label(window, text=displayBuffer, bg='#424242', fg='#FFFFFF', padx=3, pady=3, width="20")
    display.grid(row = 0, column = 0, columnspan=3)


def renderElems(*render):    
    #Render Number Buttons 
    for i in range(len(render)):      
        for l in range(3):
            if(i*3 + l >= len(render)):
                break
            render[(i*3 + l)].grid(row=i+1, column=l, padx=3,pady=3)



#Number Buttons
btnWdth = 6
b1 = tkinter.Button(window, text="1", width = btnWdth, command=lambda: [displayHandler(b1)])
b2 = tkinter.Button(window, text="2", width = btnWdth, command=lambda: [displayHandler(b2)])
b3 = tkinter.Button(window, text="3", width = btnWdth, command=lambda: [displayHandler(b3)])
b4 = tkinter.Button(window, text="4", width = btnWdth, command=lambda: [displayHandler(b4)])
b5 = tkinter.Button(window, text="5", width = btnWdth, command=lambda: [displayHandler(b5)])
b6 = tkinter.Button(window, text="6", width = btnWdth, command=lambda: [displayHandler(b6)])
b7 = tkinter.Button(window, text="7", width = btnWdth, command=lambda: [displayHandler(b7)])
b8 = tkinter.Button(window, text="8", width = btnWdth, command=lambda: [displayHandler(b8)])
b9 = tkinter.Button(window, text="9", width = btnWdth, command=lambda: [displayHandler(b9)])
b10 = tkinter.Button(window, text="+/-", width = btnWdth, command=lambda: [displayHandler(b10)])
b11 = tkinter.Button(window, text="0", width = btnWdth, command=lambda: [displayHandler(b11)])
b12 = tkinter.Button(window, text=".", width = btnWdth, command=lambda: [displayHandler(b12)])

#Operators and Functions

equals = tkinter.Button(window, width = btnWdth, text="=")
delete = tkinter.Button(window, width = btnWdth, text="<", command=lambda: [displayHandler(delete)])

renderElems(b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,equals,delete)




#enter_URL = tkinter.Label(window, text="Enter Game URL:", bg='#424242', fg='#FFFFFF', pady=3, padx=3)
#entry_URL = tkinter.Entry(window)
#loading = tkinter.Label(window, text="Give it about 10 seconds, and your results should appear.", bg='#424242', fg='#FFFFFF', pady=3, padx=3)
#invalid = tkinter.Label(window, text="Invalid URL Entered! Only enter the URLs of Roblox Game Pages!", bg='#424242', fg='#FFFFFF', pady=3, padx=3)
#button_calculate = tkinter.Button(window, text="Calculate", command=begin)

#Render the elements (Window 1)



window.mainloop()
