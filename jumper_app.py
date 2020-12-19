from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog
from tkinter import ttk
from tkinter import *
import threading

import jumper
import os

class VentanaContador:

    def __init__(self):
        self.html_table = ""
        self.cabecera = ('N','Verso', 'Etiquetado', "Sílabas", "Acentos", 'Sin extrarrítmicos', 'Tipo', 'Coincidencia')
        self.dibujar()



    def dibujar(self):
        self.root = Tk()
        self.root.title("Jumper: Contador de sílabas y acentos en tiempo real")

        # Group0 Frame ----------------------------------------------------
        group0 = LabelFrame(self.root, text="Tendencia versal", padx=2, pady=2)
        group0.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky=N + E + W + S)

        group0.rowconfigure(0, weight=1)
        group0.columnconfigure(0, weight=1)

        # Create the textbox
        self.trend = Entry(group0, width=50, font=("Verdana", 11))
        self.trend.grid(row=0, column=0, sticky=E + W + N + S)

        # Group1 Frame ----------------------------------------------------
        group1 = LabelFrame(self.root, text="Poema", padx=2, pady=2)
        group1.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky=N + E + W + S)

        group1.rowconfigure(0, weight=1)
        group1.columnconfigure(0, weight=1)

        # Create the textbox
        self.txt_origen = ScrolledText(group1, width=80, height=10, font=("Times New Roman", 12))
        self.txt_origen.grid(row=0, column=0, sticky=E + W + N + S)

        # Group2 Frame ----------------------------------------------------
        group2 = LabelFrame(self.root, text="Análisis", padx=2, pady=2)
        group2.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky=N + E + W + S)

        group2.rowconfigure(1, weight=1)
        group2.columnconfigure(0, weight=1)

        # Create the textbox
        self.txt_destino = ttk.Treeview(group2, height=25, columns=self.cabecera, show='headings')
        vsb = ttk.Scrollbar(group2, orient="vertical", command=self.txt_destino.yview)
        vsb.configure(command=self.txt_destino.yview)
        self.txt_destino.configure(yscrollcommand=vsb.set)
        
        # set column headings
        tamanios = (50, 400, 400, 80, 180, 180, 350, 100)
        for i,col in enumerate(self.cabecera):
            self.txt_destino.heading(col, text=col)
            self.txt_destino.column(col, minwidth = 0, width = tamanios[i], stretch = NO)
        self.txt_destino.tag_configure('green', foreground='green')
        self.txt_destino.tag_configure('red', foreground='red')
        self.txt_destino.tag_configure('black', foreground='black')
        
        
        vsb.grid(row=1, column=3, sticky=N+S)
        self.txt_destino.grid(row=1, column=0, sticky=E + W + N + S)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)

        # Menu
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar, tearoff=0)

        filemenu.add_command(label="Guardar análisis", command=self.onSave)
        filemenu.add_command(label="Limpiar texto", command=self.clearText)
        filemenu.add_separator()
        filemenu.add_command(label="Salir", command=self.root.quit)

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Cómo se usa", command=self.popupmsgHelp)
        helpmenu.add_separator()
        helpmenu.add_command(label="Acerca de...", command=self.popupmsgAbout)
        
        analisismenu = Menu(menubar, tearoff=0)
        analisismenu.add_command(label="Analizar poema", command=self.put_text_in_txt_destino_menu)


        menubar.add_cascade(label="Archivo", menu=filemenu)
        menubar.add_cascade(label="Análisis", menu=analisismenu)
        menubar.add_cascade(label="Ayuda", menu=helpmenu)
        
        self.txt_origen.bind('<Button-3>',self.rClicker, add='')
        self.txt_origen.bind('<KeyPress>', self.put_text_in_txt_destino_on_key)
        self.txt_origen.focus()
        
        self.statusbar = Label(self.root, text="", bd=1, relief=SUNKEN, anchor='e', justify=LEFT)
        self.statusbar.grid(row=3, column=0, columnspan=2)
    
    # https://stackoverflow.com/questions/4266566/stardand-context-menu-in-python-tkinter-text-widget-when-mouse-right-button-is-p
    def rClicker(self, e):


        try:
            def rClick_Copy(e, apnd=0):
                e.widget.event_generate('<Control-c>')

            def rClick_Cut(e):
                e.widget.event_generate('<Control-x>')

            def rClick_Paste(e):
                e.widget.event_generate('<Control-v>')

            e.widget.focus()

            nclst=[
                   (' Cortar', lambda e=e: rClick_Cut(e)),
                   (' Copiar', lambda e=e: rClick_Copy(e)),
                   (' Pegar', lambda e=e: rClick_Paste(e)),
                   ]

            rmenu = Menu(None, tearoff=0, takefocus=0)

            for (txt, cmd) in nclst:
                rmenu.add_command(label=txt, command=cmd)

            rmenu.tk_popup(e.x_root+40, e.y_root+10,entry="0")

        except TclError:
            print (' - rClick menu, something wrong')
            pass

        return "break"
    
    def show(self,x, colores):
        self.txt_destino.delete(*self.txt_destino.get_children())

        for i, (v, v_etiquetado, v_silabas, v_acentos, v_extra, v_tipo, v_coin) in enumerate(x):
            self.txt_destino.insert("", "end", values=(i+1, v, v_etiquetado, v_silabas, str(v_acentos), str(v_extra), v_tipo, v_coin),tags=(colores[i],))

    def put_text_in_txt_destino_on_key(self,event):
        t = threading.Thread(target=self.put_text_in_txt_destino(), args=(self,))
        del(t)

    def put_text_in_txt_destino_menu(self):
        t = threading.Thread(target=self.put_text_in_txt_destino(), args=(self,))
        del(t)

    def put_text_in_txt_destino(self):
        fetched_content = self.txt_origen.get('1.0', 'end-1c')

        try:
            x = jumper.escandir_texto(fetched_content)
            columna_silabas_v = list(map(list, zip(*x)))[2]
            versos_frecuentes = jumper.most_frequent(columna_silabas_v)
        except:
            return None
        tendencia_versal = self.trend.get().strip().strip(',').split(',')
        # si hay tendencia versal operamos con ella
        if tendencia_versal[0] != '' and tendencia_versal[0].find('Auto') == -1:
            tendencia_versal = [int(i) for i in tendencia_versal] if len(tendencia_versal) > 0 and self.RepresentsInt(tendencia_versal[0]) else []
        else:
            tendencia_versal = list(versos_frecuentes.keys())
            self.trend.delete(0, END)
            self.trend.insert(0, 'Auto: '+str(tendencia_versal).replace(']','').replace('[',''))


        precision = 0
        colores = []

        self.html_table = '<table width="100%" style="margin: 0px;font-size: 11pt;font-family: Courier;">'
        self.html_table += '<tr>'
        for item in self.cabecera:
            self.html_table += '<th style="text-align: left;">' + item + '</th>'
        self.html_table += '</tr>'

        for v in x:
            silabas_v = v[2]

            # se convierte a porcetaje
            v[-1] = int(v[-1]*100)

            if len(tendencia_versal) > 0:
                if silabas_v in tendencia_versal and v[-1] == 100:
                    precision += 1
                    color = 'green'
                elif silabas_v in tendencia_versal:
                    precision += 1
                    color = 'black'
                else:
                    color = 'red'
            colores.append(color)
            self.html_table += '<tr style="color:' + color + '">'
            for item in v:
                self.html_table += '<td>' + str(item) + '</td>'
            self.html_table += '</tr>'
        self.html_table += '</table><br>'
        self.html_table += 'Tendencia versal:'+str(tendencia_versal)

        calidad, regularidad = self.calcular_calidad_precision(x, versos_frecuentes)

        #imprimimos regularidad y precision

        resumen_precision = f"Precisión de los acentos:  {calidad:.1f}% Regularidad con los versos más frecuentes: {regularidad:.1f}%"
        self.statusbar['text'] = resumen_precision

        self.show(x,colores)
        #self.txt_destino.set_content(self.html_table)

    def calcular_calidad_precision(self, analisis, versos_frecuentes):
        calidad = 0
        regularidad = 0
        for verso_analizado in analisis:
            ratio = verso_analizado[-1]
            silabas = verso_analizado[2]
            if ratio == 100:
                calidad += 1
            if silabas in versos_frecuentes:
                regularidad += 1
        return (calidad/len(analisis))*100, (regularidad/len(analisis))*100


    def popupgen(self, title, msg):
        popup = Tk()
        popup.wm_title(title)
        label = Label(popup, text=msg)
        label.pack(side="top", fill="x", pady=15)
        B1 = Button(popup, text="Ok", command=popup.destroy)
        B1.pack()
        popup.mainloop()

    def popupmsgAbout(self):
        msg = 'Analizador automático de métrica por Guillermo Marco Remón.\n nlp.uned.es, Research Group in NLP & IR, UNED, Madrid, Spain.\n Las tipologías de verso empleadas se han extraído de Pou, P. J. (2020). Métrica española. Ediciones Cátedra. \n Si detecta cualquier error escriba a gmarco@lsi.uned.es'
        title = "Acerca de... Versión 21122020"
        self.popupgen(title, msg)

    def popupmsgHelp(self):
        msg = 'Pegue o escriba el poema en la sección "Poema",\nel análisis métrico se hará automáticamente. \nLa tendencia versal se calculará también automáticamente.\n Si lo desea, puede establecerla manualmente separada por comas en la caja de texto: ej.: 14, 11, 7'
        title = 'Modo de empleo'
        self.popupgen(title, msg)

    def clearText(self):
        self.txt_origen.delete('1.0', END)

    def onSave(self):
        home = os.path.expanduser('~')
        path = filedialog.asksaveasfilename(initialdir=home, title="Guardar como",
                                            filetypes=(("html", "*.html"), ("All files", "*.*")))
        textFile = open(path+'.html', 'w')
        textFile.write(self.html_table)
        textFile.close()

    def RepresentsInt(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def lanzar(self):
        self.root.mainloop()


def main():
    ventana = VentanaContador()
    ventana.lanzar()


if __name__ == "__main__":
    main()
