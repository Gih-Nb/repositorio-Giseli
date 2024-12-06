import tkinter as tk
from tkinter import messagebox


class CadastroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Página de Cadastro")
        self.root.geometry("300x400")
        self.root.configure(bg="#EAF6FF")  # Fundo branco-azulado
        
        # Configurações da interface
        self.criar_widgets()
    
    def criar_widgets(self):
        # Título
        tk.Label(
            self.root, text="Cadastro", font=("Arial", 16, "bold"), 
            bg="#EAF6FF", fg="#003366"  # Azul escuro
        ).pack(pady=10)
        
        # Nome
        tk.Label(
            self.root, text="Nome:", bg="#EAF6FF", fg="#003366"
        ).pack(anchor="w", padx=10)
        self.entry_nome = tk.Entry(self.root, bg="#FFFFFF", fg="#003366")
        self.entry_nome.pack(fill="x", padx=10, pady=5)
        
        # Email
        tk.Label(
            self.root, text="Email:", bg="#EAF6FF", fg="#003366"
        ).pack(anchor="w", padx=10)
        self.entry_email = tk.Entry(self.root, bg="#FFFFFF", fg="#003366")
        self.entry_email.pack(fill="x", padx=10, pady=5)
        
        # Senha
        tk.Label(
            self.root, text="Senha:", bg="#EAF6FF", fg="#003366"
        ).pack(anchor="w", padx=10)
        self.entry_senha = tk.Entry(self.root, show="*", bg="#FFFFFF", fg="#003366")
        self.entry_senha.pack(fill="x", padx=10, pady=5)
        
        # Botão de Cadastro
        self.btn_cadastrar = tk.Button(
            self.root, text="Cadastrar", 
            command=self.registrar_usuario, 
            bg="#003366", fg="#FFFFFF", activebackground="#0059b3", activeforeground="#FFFFFF"
        )
        self.btn_cadastrar.pack(pady=20)
        
    def registrar_usuario(self):
        # Captura os dados do formulário
        nome = self.entry_nome.get()
        email = self.entry_email.get()
        senha = self.entry_senha.get()
        
        # Verifica se os campos estão preenchidos
        if not nome or not email or not senha:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
            return
        
        # Exibe uma mensagem de sucesso
        messagebox.showinfo("Sucesso", f"Usuário {nome} cadastrado com sucesso!")
        
        # Limpa os campos após o registro
        self.limpar_campos()
    
    def limpar_campos(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_senha.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = CadastroApp(root)
    root.mainloop()

