from tkinter import *
from tkinter import ttk
 
co0 = "#444466"  # Preto
co1 = "#feffff"  # branco
co2 = "#4065a1"  # azul
 
janela = Tk()
janela.title('')
janela.geometry('295x230')
janela.configure(bg=co1)

frame_cima = Frame(janela, width=295, height=50, bg=co1, pady=0, padx=0, relief='flat')
frame_cima.grid(row=0, column=0, sticky=NSEW)

frame_baixo = Frame(janela, width=295, height=180, bg=co1, pady=0, padx=0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW)

#cabecalho>>>

app_name = Label(frame_cima, text='Calculadora de IMC', width=23, height=1, padx=0, relief='flat', anchor='center', font=('Ivy, 16 bold'), bg=co1, fg=co0)
app_name.place(x=0, y=0) 

app_linha = Label(frame_cima, text='', width=400, height=1, padx=0, relief='flat', anchor='center', font=('Ivy, 1'), bg=co2, fg=co2)
app_linha.place(x=0, y=35) 

#abaixo da linha>>>

l_peso = Label(frame_baixo, text='Insira seu Peso', height=1, padx=0, relief='flat', anchor='center', font=('Ivy, 10 bold'), bg=co1, fg=co0)
l_peso.grid(row=0, column=0, sticky=NSEW, pady=10, padx=3) 

e_peso = Entry(frame_baixo, width=5, relief='solid', font=('Ivy, 10 bold'), justify='center')
e_peso.grid(row=0, column=1, sticky=NSEW, pady=10, padx=3) 

l_altura = Label(frame_baixo, text='Insira sua altura', height=1, padx=0, relief='flat', anchor='center', font=('Ivy, 10 bold'), bg=co1, fg=co0)
l_altura.grid(row=1, column=0, sticky=NSEW, pady=10, padx=3) 

e_altura = Entry(frame_baixo, width=5, relief='solid', font=('Ivy, 10 bold'), justify='center')
e_altura.grid(row=1, column=1, sticky=NSEW, pady=10, padx=3) 

l_resultado = Label(frame_baixo, text='---', width=5, height=1, padx=6, pady=12, relief='flat', anchor='center', font=('Ivy, 24 bold'), bg=co2, fg=co1)
l_resultado.place(x=175, y=10)

l_resultado_texto = Label(frame_baixo, text='O seu IMC é: abaixo do peso', width=37, height=1, padx=0, pady=11, relief='flat', anchor='center', font=('Ivy, 10 bold'), bg=co1, fg=co0)
l_resultado_texto.place(x=0, y=90)

b_calcular = Button(frame_baixo, text='Calcular', width=34, height=1, overrelief=SOLID, relief='raised', anchor='center', font=('Ivy, 10 bold'), bg=co2, fg=co1)
b_calcular.grid(row=4, column=0, sticky=NSEW, pady=60, padx=5, columnspan=30) 

janela.mainloop()
 