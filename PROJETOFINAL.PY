import sqlite3
import tkinter as tk
from tkinter import messagebox #funções que criam mensagens na tela
from tkinter import ttk #widgets

#conectar ou criar o banco de dados
def conectar():
    return sqlite3.connect('xyzcomercio.db')

#criar uma tabela(caso ela não exista)
def criar_tabela():
    conn = conectar()
    c = conn.cursor()
    c.execute('''
              CREATE TABLE IF NOT EXISTS clientes(
              id INTEGER PRIMARY KEY ,
              nome TEXT,
              datanascimento DATE,
              email TEXT UNIQUE,
              telefone TEXT, 
              endereco TEXT
              )
              ''')

    conn.commit()
    conn.close()

#inserindo dados no banco de dados
def agregar_clientes():
    nome = entry_nome.get()
    datanascimento = entry_datanascimento.get()
    email = entry_email.get()
    telefone = entry_telefone.get()
    endereco = entry_endereco.get()

    if nome and datanascimento and email and telefone and endereco: #se ambos existirem
        conn = conectar()
        c = conn.cursor()
        c.execute('INSERT INTO clientes(nome,datanascimento,email,telefone,endereco) VALUES(?,?,?,?,?)',
                  (nome,datanascimento,email,telefone,endereco))
        conn.commit()
        conn.close()
        messagebox.showinfo('Inseridos.','Os dados estão no banco de dados.')
        mostrar_clientes()
    else: 
        messagebox.showerror('Erro.', 'Ocorreu um erro: os dados não foram inseridos.')

#mostrar dados
def mostrar_clientes():
    for row in tree.get_children():
        tree.delete(row)
    conn = conectar()
    c = conn.cursor()
    c.execute('SELECT * from clientes')
    clientes = c.fetchall()
    for cliente in clientes:
        tree.insert("", "end", values=(cliente[0],cliente[1],cliente[2],cliente[3],cliente[4],cliente[5]))
    conn.close()

#deletar dados
def eliminar_clientes():
    selected = tree.selection()
    if selected:
        client_id = tree.item(selected)['values'][0]
        conn = conectar()
        c = conn.cursor()
        c.execute('DELETE FROM clientes WHERE id = ?', (client_id,))
        conn.commit()
        conn.close()
        messagebox.showinfo('Êxito.','Dados deletados.')
        mostrar_clientes()
    else:
        messagebox.showerror('Erro.','Dados não deletados.')

def atualizar_clientes():
    selected = tree.selection()
    if selected:
        client_id = tree.item(selected)['values'][0]
        novo_nome = entry_nome.get()
        nova_datanascimento = entry_datanascimento.get()
        novo_email = entry_email.get()
        novo_telefone = entry_telefone.get()
        novo_endereco = entry_endereco.get()

        if novo_nome and nova_datanascimento and novo_endereco and novo_telefone:
            conn = conectar()
            c = conn.cursor()
            # c.execute('UPDATE clientes SET nome = ?, datanascimento = ?, WHERE id = ?, email = ?, telefone = ?, endereco = ?',
            #           (novo_nome, nova_datanascimento, id, novo_telefone, novo_endereco))
            c.execute('UPDATE clientes SET nome = ?, datanascimento = ?, email = ?, telefone = ?, endereco = ? WHERE id = ?',
            (novo_nome, nova_datanascimento, novo_email, novo_telefone, novo_endereco, client_id))
            conn.commit()
            conn.close()
            messagebox.showinfo('Êxito.', 'Dados alterados.')
            mostrar_clientes()
        else:
            messagebox.showinfo('Erro.', 'Dados não alterados.')

janela = tk.Tk()
janela.title('CLIENTES XYZ COMÉRCIO')

label_nome = tk.Label(janela, text = 'NOME')
label_nome.grid(row=1, column=0, padx=10, pady=10)
entry_nome = tk.Entry(janela)
entry_nome.grid(row=1, column=1, padx=10, pady=10)

label_datanascimento = tk.Label(janela, text='DATA DE NASCIMENTO')
label_datanascimento.grid(row = 2, column = 0, padx = 10, pady = 10)
entry_datanascimento = tk.Entry(janela)
entry_datanascimento.grid(row=2, column=1, padx=10, pady=10)

label_email = tk.Label(janela, text='E-MAIL')
label_email.grid(row = 3, column = 0, padx = 10, pady = 10)
entry_email = tk.Entry(janela)
entry_email.grid(row=3, column=1, padx=10, pady=10)

label_telefone = tk.Label(janela, text='TELEFONE')
label_telefone.grid(row = 4, column = 0, padx = 10, pady = 10)
entry_telefone = tk.Entry(janela)
entry_telefone.grid(row=4, column=1, padx=10, pady=10)

label_endereco = tk.Label(janela, text='ENDEREÇO')
label_endereco.grid(row = 5, column = 0, padx = 10, pady = 10)
entry_endereco = tk.Entry(janela)
entry_endereco.grid(row= 5, column=1, padx=10, pady=10)

btn_agregar = tk.Button(janela, text = 'INSERIR DADOS', command=agregar_clientes)
btn_agregar.grid(row = 4, column = 0, columnspan=2, padx=10, pady=10)

# btn_agregar = tk.Button(janela, text = 'INSERIR DADOS', command=agregar_clientes)
# btn_agregar.grid(row = 1, column = 0, columnspan=2, padx=10, pady=10)

# btn_agregar = tk.Button(janela, text = 'INSERIR DADOS', command=agregar_clientes)
# btn_agregar.grid(row = 2, column = 0, columnspan=2, padx=10, pady=10)

# btn_agregar = tk.Button(janela, text = 'INSERIR DADOS', command=agregar_clientes)
# btn_agregar.grid(row = 3, column = 0, columnspan=2, padx=10, pady=10)

# btn_agregar = tk.Button(janela, text = 'INSERIR DADOS', command=agregar_clientes)
# btn_agregar.grid(row = 4, column = 0, columnspan=2, padx=10, pady=10)

btn_atualizar = tk.Button(janela, text = 'ATUALIZAR OS DADOS', command=atualizar_clientes)
btn_atualizar.grid(row = 5, column=0, columnspan=2,padx=10,pady=10)

btn_deletar = tk.Button(janela, text = 'DELETAR OS DADOS', command=eliminar_clientes)
btn_deletar.grid(row = 6, column=0, columnspan=2,padx=10,pady=10)

columns = ('ID','NOME', 'DATA DE NASCIMENTO', 'E-MAIL', 'TELEFONE', 'ENDEREÇO')
tree = ttk.Treeview(janela,columns=columns, show='headings')
tree.grid(row=7,column=0, columnspan=2, padx=10, pady=10)

for col in columns:
    tree.heading(col, text=col)

criar_tabela()
mostrar_clientes()

janela.mainloop()
