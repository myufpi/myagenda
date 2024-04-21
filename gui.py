import tkinter as tk
import tkinter.messagebox as msgbox
import tkinter.simpledialog as simpledialog
import entidades

class Window(tk.Tk):
  def __init__(self, minha_agenda):
    super().__init__()

    self.geometry("300x400")
    self.resizable(False, False)
    self.title('Mini Agenda')

    self.conteudo_list_box = dict()
    
    # armazena cpf, nome e data_nascimento
    self.cpf = tk.StringVar()
    self.nome = tk.StringVar()
    self.data_nascimento = tk.StringVar()    
    # Agenda in frame
    self.agenda = tk.Frame()
    self.agenda.pack(padx=10, pady=10, fill='x', expand=True)
    # label do cpf
    cpf_label = tk.Label(self.agenda, text="CPF:")
    cpf_label.pack(fill='x', expand=True)
    # input do cpf
    self.cpf_entry = tk.Entry(self.agenda, textvariable=self.cpf)
    self.cpf_entry.pack(fill='x', expand=True)
    self.cpf_entry.focus()
    # label do nome
    nome_label = tk.Label(self.agenda, text="Nome:")
    nome_label.pack(fill='x', expand=True)
    # input do nome
    self.nome_entry = tk.Entry(self.agenda, textvariable=self.nome)
    self.nome_entry.pack(fill='x', expand=True)
    # label da data_nascimento
    self.data_nascimento_label = tk.Label(self.agenda, text="Data nascimento:")
    self.data_nascimento_label.pack(fill='x', expand=True)
    # input da data_nascimento
    self.data_nascimento_entry = tk.Entry(self.agenda, textvariable=self.data_nascimento)
    self.data_nascimento_entry.pack(fill='x', expand=True)
    # insere button
    self.insere_button = tk.Button(self, text="Inserir", command=self.insere_clicked)
    self.insere_button.pack(fill='x', expand=True, pady=1)
    # pesquisar button
    self.pesquisa_button = tk.Button(self, text="Pesquisa", command=self.pesquisa_clicked)
    self.pesquisa_button.pack(fill='x', expand=True, pady=1)
    # remove button
    self.remove_button = tk.Button(self, text="Remover", command=self.remove_clicked)
    self.remove_button.pack(fill='x', expand=True, pady=1)
    # clear button
    self.limpa_button = tk.Button(self, text="Limpar", command=self.limpa_clicked)
    self.limpa_button.pack(fill='x', expand=True, pady=1)

    # frame do listbox
    self.meu_list_box = tk.Frame()
    self.meu_list_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    self.listbox = tk.Listbox(self.meu_list_box)
    self.listbox.pack(side = tk.LEFT, fill = tk.BOTH, expand=True)
    scrollbar = tk.Scrollbar(self.meu_list_box)
    scrollbar.pack(side = tk.RIGHT,  fill = tk.BOTH)
    self.listbox.config(yscrollcommand = scrollbar.set)
    scrollbar.config(command = self.listbox.yview)
    self.minha_agenda = minha_agenda
    self.atualiza_list_box_contato()

    # captura eventos dos componentes e teclas
    self.listbox.bind("<<ListboxSelect>>", self.show_item)
    self.insere_button.bind('<Return>', self.key_return)
    self.remove_button.bind('<Return>', self.key_return2)
    self.limpa_button.bind('<Return>', self.key_return3)

  def key_return(self,event):
    self.insere_clicked()

  def key_return2(self, event):
    self.remove_clicked()

  def key_return3(self, event):
    self.clear_entries()

  def clear_entries(self):
    self.cpf_entry.delete(0, tk.END)
    self.nome_entry.delete(0, tk.END)
    self.data_nascimento_entry.delete(0, tk.END)
    self.cpf_entry.focus()

  def update_entries(self, cpf, nome, data_nascimento):
    self.cpf.set(cpf)
    self.nome.set(nome)
    self.data_nascimento.set(data_nascimento)

  def atualiza_list_box_contato(self):
    self.conteudo_list_box
    self.listbox.delete(0,tk.END)
    meus_contatos = self.minha_agenda.listar_conteudo()
    indice_elemento = 0
    for values in meus_contatos:
      # remove o enter da linha
      elemento = values[:-1]
      conteudo = elemento.split(';')
      self.conteudo_list_box[conteudo[0]] = indice_elemento
      indice_elemento += 1
      self.listbox.insert(tk.END, elemento)

  def show_item(self, event=' '):
    selected_indices = self.listbox.curselection()
    if not selected_indices: 
        return 
    selected_index = selected_indices[0]
    selected_item = self.listbox.get(selected_index)
    print("Selected item:", selected_item)
    my_item = selected_item.strip().split(";")
    self.update_entries(cpf=my_item[0], nome=my_item[1], data_nascimento=my_item[2])

  def limpa_clicked(self):
    self.clear_entries()
    self.atualiza_list_box_contato()

  def insere_clicked(self):
    try:
        novo_contato = entidades.PessoaValida(self.cpf.get(), self.nome.get(), self.data_nascimento.get())
        if (len(self.cpf.get())==0 or len(self.nome.get())==0): 
          msgbox.showwarning(title='Atenção', message="CPF e Nome obrigatório")
        else:
          try: 
            self.minha_agenda.insere_contato(novo_contato)
            msg = f'Seu CPF: {self.cpf.get()}, nome: {self.nome.get()} e data_nascimento: {self.data_nascimento.get()}'
            msgbox.showinfo(title='Informação', message=msg)
            self.clear_entries()
            self.atualiza_list_box_contato()
          except Exception as ex: 
            msgbox.showwarning(title='Atenção', message=f'{str(ex)}')
    except Exception as ex:
      msgbox.showwarning(title='Atenção', message=f'{str(ex)}') 

  def remove_clicked(self):
    try:
      contato = entidades.PessoaValida(self.cpf.get(), self.nome.get(), self.data_nascimento.get())
      if (len(self.cpf.get())==0 or len(self.nome.get())==0): 
          msgbox.showwarning(title='Atenção', message="CPF e Nome obrigatório")
      else:
          try: 
              self.minha_agenda.remove_contato(contato)
              msg = f"O contato {self.nome.get()} será removido."
              msgbox.showinfo(title='Informação', message=msg)
              self.limpa_clicked()
          except Exception as ex:
              msgbox.showwarning(title='Atenção', message=f"{str(ex)}") 
    except Exception as ex:
      msgbox.showwarning(title='Atenção', message=f"{str(ex)}")

  def pesquisa_clicked(self):
    cpf = simpledialog.askstring(title="Pesquisa contato", prompt="Qual o CPF?")   
    contato = self.minha_agenda.pesquisa_contato(cpf)
    if contato:
        nome, data_nascimento = contato
        self.update_entries(cpf, nome, data_nascimento)
        #atualiza o indice do listbox
        self.atualiza_list_box_contato()
        self.listbox.activate(self.conteudo_list_box[cpf])
    else:
      msgbox.showwarning(title='Atenção', message="Contato não encontrado!")  
