from pyvirtualdisplay import Display


# Função que abre um display virtual para execução sem interface gráfica
def open_display():
    try:
        display = Display(visible=0, size=(800, 600))
        display.start()
    except Exception as e:
        print(e)
