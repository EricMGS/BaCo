#############################################################################################################
#                           Desenvolvedores: EricMGS, FabioHF, LCapalbo, OsmarV, DivanPS                    #
#                                              Data: Março de 2018                                          #
#                                                                                                           #
#   Programa que converte bases numéricas, da base 2 até 62. Tem como valor de saída máximo 100 dígitos     #
#############################################################################################################

#Interface gráfica

from BaCo import *
from tkinter import Tk, Label, Spinbox, Entry, messagebox, ttk, CENTER

#colors
bg_color = 'lightblue'
bg_box = 'gray95'

#window
window = Tk()
window.wm_iconbitmap('BaCo.ico') 
window.title("BaCo - BaseConverter")
window.geometry ('700x400')
window.resizable (0, 0)
window.configure (bg = bg_color)

#style
style=ttk.Style()
style.theme_use('vista')
style.configure ('TButton')

#labels
lblbase = Label (window, text = 'Base:', bg = bg_color, font = ('Arial', 12))
lblbase.place (relx = 0.5, rely = 0.1, anchor = CENTER)

lblfor = Label (window, text = 'para', bg = bg_color)
lblfor.place (relx = 0.5, rely = 0.2, anchor = CENTER)

lblvalue = Label (window, bg = bg_color, text = 'Valor: (0 - 1)', font = ('Arial', 12))
lblvalue.place (relx = 0.5, rely = 0.4, anchor = CENTER)

result = Label (window, bg = bg_color, text = 'Resultado:', font = ('Arial', 12))
result.place (relx = 0.5, rely = 0.6, anchor = CENTER)

final_result = Label (window, bg = bg_color)
final_result.place (relx = 0.5, rely = 0.7, anchor = CENTER)

#spinbox
def clicked (): #quando a spinbox mudar de valor o texto que identifica o intervalo de dígitos de entrada muda
    lblvalue.configure (text = 'Valor: (0 - ' +  digitos[int(base1.get()) - 1] + ')')

base1 = Spinbox(window, from_ = 2, to = 62, width = 5, bg = bg_box, state = 'readonly', command = clicked)
base1.place (relx = 0.4, rely= 0.2, anchor = CENTER)

base2 = Spinbox (window, from_ = 2, to = 62, width = 5, bg = bg_box, state = 'readonly')
base2.place (relx = 0.6, rely = 0.2, anchor = CENTER)

#entry
value = Entry (window, width = 110, bg = bg_box, justify = 'center')
value.place (relx = 0.5, rely = 0.5, anchor = CENTER)

#buttons
def convert(): #quando o botão de conversão é clicado verifica-se erros de conversão e de limite de dígitos
    if Converte (value.get(), int(base1.get()), int(base2.get())) == 'Erro':
        return messagebox.showerror ('Erro 1', 'Valor inválido')
        
    res = Converte (value.get(), int(base1.get()), int(base2.get()))
    final_result.configure (text = res + '\n')
    
    if len(res) > 100:
        final_result.configure (text = '')
        return messagebox.showerror ('Erro 2', 'O resultado é muito grande\nMáximo: 100 dígitos')

convert_btn = ttk.Button (window, text = 'Converter', command = convert, style = 'TButton')
convert_btn.place (relx = 0.3, rely = 0.9, anchor = CENTER)


def out ():
    if messagebox.askyesno ('Sair', 'Deseja mesmo sair?') == 1:
        import sys
        sys.exit()

out_btn = ttk.Button (window, text = 'Sair', command = out, style = 'TButton')
out_btn.place(relx = 0.7, rely = 0.9, anchor = CENTER)

window.mainloop () #executa a janela