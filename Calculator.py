from tkinter import *
from math import *


# Variables  for calculation - Do not change name of variables
standard_history = []  # Ust to store history of Standard
isDot = False  # True on press dot or else false
isOperator = False  # True on press operator or else false
isOperatorEquals = False  # True on press equals or else false


# InIt graphics window
calc = Tk()  # InIt graphical window
calc.title("Calculator")  # Set title as calculator
calc.geometry("300x400")  # Set the size of calculator
calc.wm_maxsize(300, 400)  # Set max possible size of window
calc.wm_minsize(300, 400)  # Set min possible size of window
# All Basic foe graphical window are set


def onClickNumbers(num):
    """
    :param num: contain information of pressed button ( as a string )
    it also handel dot is pressed or not
    it display number on display and do certain operation on it
    """
    if answer["text"] == "ERROR":
        pass
    else:
        if globals()["isOperatorEquals"] == True:
            answer["text"] = "0"
            overall["text"] = ""
            globals()["isOperatorEquals"] = False
        if num == ".":
            if globals()["isOperator"]:
                answer["text"] = "0."
                globals()["isDot"] = True
                globals()["isOperator"] = False
            elif not globals()["isDot"]:
                globals()["isDot"] = True
                answer["text"] += num
        elif answer["text"] == "0" and num == 0:
            pass
        elif answer["text"] == "0" and num != 0:
                answer["text"] = str(num)
        elif answer["text"] != "0":
            if globals()["isOperator"]:
                answer["text"] = str(num)
                globals()["isOperator"] = False
            else:
                answer["text"] += str(num)


# 1 -> sqrt  2->squre  3->div by 1
def onClickOtherOperator(ope):
    """
    :param ope: contain information of pressed button ( as a string )
    there are only three possibility  either sqrt , sqre or div by 1 button are pressed they are operation done on single number
    so this are unary operator
    """
    if answer["text"] == "ERROR":
        pass
    elif ope == 1:
        answer["text"] = f"sqrt ({answer['text']})"
    elif ope == 2:
        answer["text"] = f"({answer['text']} ** 2)"
    elif ope == 3:
        answer["text"] = f"(1 / {answer['text']})"


def onClickOperator(ope):
    """
    :param ope: contain information of pressed button ( as a string )
    this are binary operations
    """
    if answer["text"] == "ERROR":
        pass
    else:
        if not globals()["isOperator"]:
            if ope == 1:  # 1 -> %
                overall["text"] += answer["text"] + " % "
            elif ope == 2:  # 2 -> /
                overall["text"] += answer["text"] + " / "
            elif ope == 3:  # 3 -> *
                overall["text"] += answer["text"] + " * "
            elif ope == 4:  # 4 -> -
                overall["text"] += answer["text"] + " - "
            elif ope == 5:  # 5 -> +
                overall["text"] += answer["text"] + " + "
            globals()["isOperator"] = True
        else:
            if ope == 1:  # 1 -> %
                overall["text"] = overall["text"][:-2:] + "% "
            elif ope == 2:  # 2 -> /
                overall["text"] = overall["text"][:-2:] + "/ "
            elif ope == 3:  # 3 -> *
                overall["text"] = overall["text"][:-2:] + "* "
            elif ope == 4:  # 4 -> -
                overall["text"] = overall["text"][:-2:] + "- "
            elif ope == 5:  # 5 -> +
                overall["text"] = overall["text"][:-2:] + "+ "


def equals():
    """
    on pressing equals
    """
    if answer["text"] == "ERROR" or globals()["isOperatorEquals"]:
        pass
    else:
        try:
            overall["text"] += answer["text"]
            answer["text"] = str(eval(overall["text"]))
            globals()["isOperatorEquals"]  = True
            standard_history.append(str(overall["text"] + " = " + answer["text"]))
        except:
            answer["text"] = "ERROR"


def onClickC():
    """
    On pressing C button
    """
    overall["text"] = ""
    answer["text"] = "0"
    globals()["isDot"] = False
    globals()["isOperator"] = False


def onClickCE():
    """
    On pressing CE button
    """
    if answer["text"] == "ERROR":
        pass
    else:
        answer["text"] = "0"


def delVal():
    """
    Help us to remove last value
    """
    if answer["text"] == "ERROR":
        pass
    else:
        if len(answer["text"]) == 1:
            answer["text"] = "0"
        else:
            answer["text"] = answer["text"][0:len(answer["text"])-1]


def plusminus():
    """
    Help us to change the sign of number
    """
    if answer["text"] == "ERROR":
        pass
    else:
        if int(answer["text"]) == 0:
            pass
        elif int(answer["text"]) > 0:
            answer["text"] = "-" + answer["text"]
        else:
            answer["text"] = answer["text"][1:]


def selfInfo():
    """
    Display Information of developer by clicking on About button
    """
    import  tkinter.messagebox
    tkinter.messagebox.showinfo("Created by", "Akshar Patel")


def showHistory():
    """
    Display history of developer by clicking on History button
    """
    history = Tk()
    history.title("History")
    history.geometry("200x200")
    historyList = Listbox(history, width=20000)
    historyList.pack(side=LEFT, fill=Y)
    for index, element in enumerate(standard_history):
        historyList.insert(END, f"({str(index+1)}) {element}")

    history.mainloop()


# Top label
top_frame = Frame(calc, bg="lightblue", height=25)
top_frame.pack(side=TOP, fill=X)
modeLable = Label(top_frame, bg="lightblue", text="Standard", font=("Comic Sans MS", 12))
modeLable.pack(side=LEFT, padx=5)
historyButton = Button(top_frame, text="History", bg="lightpink", font=("Comic Sans MS", 8), command=showHistory)
historyButton.pack(side=RIGHT, padx=5)


# Create Main Screen For calculator Visible Points -> x=4 and y=110
overallFrame = Frame(calc, bg="gray")
overallFrame.pack(fill=X)
overall = Label(overallFrame, text="", fg="white", bg="gray", font=("Comic Sans MS", 9))
overall.pack(side=LEFT, padx=10, pady=15)
answerFrame = Frame(calc, bg="gray")
answerFrame.pack(fill=X)
# overall.place(x=4, y=50)
equal = Label(answerFrame, text="= ", fg="white", bg="gray", font=("Comic Sans MS", 15))
equal.pack(side=LEFT, padx=5, pady=5)
# equal.place(x=4, y=90)
answer = Label(answerFrame, text="0", fg="white", bg="gray", font=("Comic Sans MS", 15))
answer.pack(side=LEFT, padx=5, pady=5)
# answer.place(x=30, y=90)


# Creating Standard Frame
standard_frame = Frame(calc, bg="gray")
standard_frame.pack(fill=X)
# Create Buttons For Standard Calculator
standardRow1 = Frame(standard_frame, bg="gray")
standardRow1.pack()
Button(standardRow1, width=3, height=1, text="%", font=("Comic Sans MS", 15), bg="#dfdfdf", command=lambda ope=1: onClickOperator(ope)).pack(side=LEFT, padx=3, pady=3)
Button(standardRow1, width=3, height=1, text="\u221Ax", font=("Comic Sans MS", 15), bg="#dfdfdf", command=lambda ope=1: onClickOtherOperator(ope)).pack(side=LEFT, padx=3, pady=3)
Button(standardRow1, width=3, height=1, text="x\u00b2", font=("Comic Sans MS", 15), bg="#dfdfdf", command=lambda ope=2: onClickOtherOperator(ope)).pack(side=LEFT, padx=3, pady=3)
Button(standardRow1, width=3, height=1, text="1/x", font=("Comic Sans MS", 15), bg="#dfdfdf", command=lambda ope=3: onClickOtherOperator(ope)).pack(side=LEFT, padx=3, pady=3)
# row 2
standardRow2 = Frame(standard_frame, bg="gray")
standardRow2.pack()
Button(standardRow2, width=3, height=1,  text="CE", font=("Comic Sans MS", 15), bg="#dfdfdf", command=onClickCE).pack(side=LEFT, padx=3, pady=3)
Button(standardRow2, width=3, height=1, text="C", font=("Comic Sans MS", 15), bg="#dfdfdf", command=onClickC).pack(side=LEFT, padx=3, pady=3)
Button(standardRow2, width=3, height=1, text="DEL", font=("Comic Sans MS", 15), bg="#dfdfdf", command=delVal).pack(side=LEFT, padx=3, pady=3)
Button(standardRow2, width=3, text="\u00F7", font=("Comic Sans MS", 15), bg="#dfdfdf", command=lambda ope=2: onClickOperator(ope)).pack(side=LEFT, padx=3, pady=3)
# row 3
standardRow3 = Frame(standard_frame, bg="gray")
standardRow3.pack()
Button(standardRow3, width=3, height=1, text="7", font=("Comic Sans MS", 15), bg="white", command=lambda a=7: onClickNumbers(a)).pack(side=LEFT, padx=3, pady=3)
Button(standardRow3, width=3, height=1, text="8", font=("Comic Sans MS", 15), bg="white", command=lambda a=8: onClickNumbers(a)).pack(side=LEFT, padx=3, pady=3)
Button(standardRow3, width=3, height=1, text="9", font=("Comic Sans MS", 15), bg="white", command=lambda a=9: onClickNumbers(a)).pack(side=LEFT, padx=3, pady=3)
Button(standardRow3, width=3, height=1, text="X", font=("Comic Sans MS", 15), bg="#dfdfdf", command=lambda ope=3: onClickOperator(ope)).pack(side=LEFT, padx=3, pady=3)
# row 4
standardRow4 = Frame(standard_frame, bg="gray")
standardRow4.pack()
Button(standardRow4, width=3, height=1, text="4", font=("Comic Sans MS", 15), bg="white", command=lambda a=4: onClickNumbers(a)).pack(side=LEFT, padx=3, pady=3)
Button(standardRow4, width=3, height=1, text="5", font=("Comic Sans MS", 15), bg="white", command=lambda a=5: onClickNumbers(a)).pack(side=LEFT, padx=3, pady=3)
Button(standardRow4, width=3, height=1, text="6", font=("Comic Sans MS", 15), bg="white", command=lambda a=6: onClickNumbers(a)).pack(side=LEFT, padx=3, pady=3)
Button(standardRow4, width=3, height=1, text="-", font=("Comic Sans MS", 15), bg="#dfdfdf", command=lambda ope=4: onClickOperator(ope)).pack(side=LEFT, padx=3, pady=3)
# row 5
standardRow5 = Frame(standard_frame, bg="gray")
standardRow5.pack()
Button(standardRow5, width=3, height=1, text="1", font=("Comic Sans MS", 15), bg="white", command=lambda a=1: onClickNumbers(a)).pack(side=LEFT, padx=3, pady=3)
Button(standardRow5, width=3, height=1, text="2", font=("Comic Sans MS", 15), bg="white", command=lambda a=2: onClickNumbers(a)).pack(side=LEFT, padx=3, pady=3)
Button(standardRow5, width=3, height=1, text="3", font=("Comic Sans MS", 15), bg="white", command=lambda a=3: onClickNumbers(a)).pack(side=LEFT, padx=3, pady=3)
Button(standardRow5, width=3, height=1, text="+", font=("Comic Sans MS", 15), bg="#dfdfdf", command=lambda ope=5: onClickOperator(ope)).pack(side=LEFT, padx=3, pady=3)
# row 6
standardRow6 = Frame(standard_frame, bg="gray")
standardRow6.pack()
Button(standardRow6, width=3, height=1, text="+/-", font=("Comic Sans MS", 15), bg="#dfdfdf", command=plusminus).pack(side=LEFT, padx=3, pady=3)
Button(standardRow6, width=3, height=1, text="0", font=("Comic Sans MS", 15), bg="white", command=lambda a=0: onClickNumbers(a)).pack(side=LEFT, padx=3, pady=3)
Button(standardRow6, width=3, height=1, text=".", font=("Comic Sans MS", 15), bg="#dfdfdf", command=lambda a=".": onClickNumbers(a)).pack(side=LEFT, padx=3, pady=3)
Button(standardRow6, width=3, height=1, text="=", font=("Comic Sans MS", 15), bg="#dfdfdf", command=equals).pack(side=LEFT, padx=3, pady=3)


# Status Bar
statusBar = Frame(calc, bg="lightblue", height=25)
statusBar.pack(side=BOTTOM, fill=X)
Button(statusBar, text="About", bg="lightpink", font=("Comic Sans MS", 8), command=selfInfo).pack(side=LEFT, padx=5)


calc.mainloop()
