from tkinter import Tk  
from tkhtmlview import HTMLLabel  

# Crear la ventana principal  
root = Tk()  
root.title("Mi Aplicación de Escritorio")  

# Leer el archivo HTML  
with open("pagina.html", "r", encoding="utf-8") as html_file:  
    html_content = html_file.read()  





# Crear un label que muestre el HTML  
html_label = HTMLLabel(root, html=html_content)  
html_label.pack(fill="both", expand=True)  




# Iniciar el bucle principal  
root.mainloop()