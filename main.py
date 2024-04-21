import gui
import entidades

def show_window():
  try: 
    minha_agenda = entidades.MyAgenda() 
    agenda = gui.Window(minha_agenda)
    agenda.mainloop()
  except Exception as ex: 
    print(f'Erro: {str(ex)}')

show_window()
