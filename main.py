import tkinter
import math


#Configure Window 1
window = tkinter.Tk()
window.title("Python Calculator")
window.configure(bg='#002421')

displayBuffer = ""
ansBuffer = ""
display = tkinter.Label(window, text="Python Calculator", bg='#424242', fg='#FFFFFF', pady=3, height="3", width="35", font=("Arial", 12))
display.grid(row = 0, column = 0, columnspan=5)

def calculate(expression):
    #Follow PEMDAS; in code the priority will be reversed cus it just works that way (can't really explain it lol)
    #I'm using recursion hehehehaw
    
    if "+" in expression:
        exprsnParts = expression.split("+")
        sum = 0
        for i in range(len(exprsnParts)):
            sum += calculate(exprsnParts[i])
        return sum
    elif "-" in expression:
        exprsnParts = expression.split("-")
        diff = float(exprsnParts[0])
        for i in range(len(exprsnParts)-1):
            diff -= calculate(exprsnParts[i+1])
        return diff
    elif "*" in expression: 
        exprsnParts = expression.split("*")
        prod = float(exprsnParts[len(exprsnParts)-1])
        for i in range(len(exprsnParts)-1):
            prod *= calculate(exprsnParts[i])
        return prod
    elif "/" in expression:
        exprsnParts = expression.split("/")
        quotnt = float(exprsnParts[0])
        for i in range(len(exprsnParts)-1):
            quotnt /= calculate(exprsnParts[i+1])
        return quotnt
    else:
        return float(expression)
        

def calculationHandler(displayBuffer):
    result = calculate(displayBuffer)
    global ansBuffer
    ansBuffer = result
    display = tkinter.Label(window, text=result, bg='#424242', fg='#FFFFFF', pady=3, height="3", width="35", font=("Arial", 12))
    display.grid(row = 0, column = 0, columnspan=5)


def displayHandler(elem):
    global displayBuffer
    txt = elem.cget("text")
    
    if txt == "<":
        displayBuffer = displayBuffer[:-1]
    elif txt == "+/-":
        #Code for the +/- funcitonality, need to be addressed
        """if not "-" in displayBuffer:
            displayBuffer = "-" + displayBuffer
        else:
            displayBuffer = displayBuffer[1:]
        """
    elif txt == "C":
        displayBuffer = ""
    else:
        displayBuffer += txt

    global display
    display = tkinter.Label(window, text=displayBuffer, bg='#424242', fg='#FFFFFF', pady=3, height="3", width="35", font=("Arial", 12))
    display.grid(row = 0, column = 0, columnspan=5)


def renderNumKeys(*render):    
    #Render Number Buttons 
    for i in range(len(render)-4):      
        for l in range(3):
            if(i*3 + l >= len(render)):
                break
            render[(i*3 + l)].grid(row=i+1, column=l, padx=3,pady=3)

def renderOperators(*render):
    #Render Operator Buttons
    for i in range(len(render)):
        render[i].grid(row=i+1, column = 4, padx=3, pady=3)


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
addition = tkinter.Button(window, text="+", width = btnWdth, command=lambda: [displayHandler(addition)], bg = '#0047AB', fg="#FFFFFF")
subtraction = tkinter.Button(window, text="-", width = btnWdth, command=lambda: [displayHandler(subtraction)], bg = '#0047AB', fg="#FFFFFF")
multiplication = tkinter.Button(window, text="*", width = btnWdth, command=lambda: [displayHandler(multiplication)], bg = '#0047AB', fg="#FFFFFF")
division = tkinter.Button(window, text="/", width = btnWdth, command=lambda: [displayHandler(division)], bg = '#0047AB', fg="#FFFFFF")

clear = tkinter.Button(window, width = btnWdth, text="C", command=lambda: [displayHandler(clear)])
equals = tkinter.Button(window, width = btnWdth, text="=", command=lambda: [calculationHandler(displayBuffer)], bg = '#78601D')
delete = tkinter.Button(window, width = btnWdth, text="<", command=lambda: [displayHandler(delete)])
ans = tkinter.Button(window, width=btnWdth, text="Ans", command=lambda: [displayHandler(ans)])

renderNumKeys(b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12, ans, clear, delete)
renderOperators(addition,subtraction,multiplication,division, equals)

window.mainloop()
