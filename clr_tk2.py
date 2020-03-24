from tkinter import *
from tkinter import colorchooser

#theme_text = open('config-highlight.txt, r+)

def normal_backround():
    #open( , a+
   # title = "Select Backround"
    clr = colorchooser.askcolor(title="select color")
    #hex=colorchooser.askcolor[]
    (clr[1])
    #pyfile.txt append  new color
    #Should use a simple theme with 3 or 4 colors reuse colors
    txt_f = open('test_config_highlight.txt', 'w')
    txt_f.write('TESTING NUMNUTS!')
    txt_f.write(clr[1])

 '''   [r]  #name
normal-foreground = #22c2ff
normal-background = #252132
keyword-foreground = #acfe63
keyword-background = #231d2c
builtin-foreground = #85fe34
builtin-background = #231d2c
comment-foreground = #2967da
comment-background = #32313c
string-foreground = #808040
string-background = #2e3536
definition-foreground = #f3d765
definition-background = #2f2035
hilite-foreground = #00caa2
hilite-background = #5e4437
break-foreground = #4ffbf7
break-background = #252738
hit-foreground = #8edde6
hit-background = #483849
error-foreground = #252059
error-background = #ff7777
context-foreground = #f16738
context-background = #4e3a4e
linenumber-foreground = #1cf04b
linenumber-background = #473d50
cursor-foreground = #00d9d9
stdout-foreground = #0cfcd8
stdout-background = #231d2c
stderr-foreground = #f5b065
stderr-background = #373e3d
console-foreground = #770000
console-background = #231d2c'''


#confif_py = open()


'''def normal_backround():
    clr = colorchooser.askcolor(title="select color")
    (clr[1])
    txt_f = open('config-highlight.txt', 'w')
    txt_f.write('TESTING NUMNUTS!/n')
    txt_f.write(clr[1])

    ("normal-foreground ="(clr[1]))  ''' 



root = Tk()




button = Button(root, text="change color", command=call_me)




button.grid(row = 2, column = 1,)
root.geometry("400x89")
root.mainloop()
