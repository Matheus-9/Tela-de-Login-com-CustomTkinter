import customtkinter

janela = customtkinter.CTk()
janela.geometry("500x500")
janela.title("HOSPITAL JOSÉ PINTO SARAIVA")

def entrar():
    print("Nome: ", nome.get(), "Senha: ", senha.get())



texto = customtkinter.CTkLabel(janela, text="Fazer Login", font=("Arial", 25))
texto.pack(padx=10, pady=10)

nome = customtkinter.CTkEntry(janela, width=200, placeholder_text="Email")
nome.pack(padx=10, pady=10)

senha = customtkinter.CTkEntry(janela, width=200, show="*", placeholder_text="Sua senha", )
senha.pack(padx=10, pady=10)

botao = customtkinter.CTkButton(janela, text="Entrar", width=200, command=entrar, fg_color="light blue")
botao.pack(padx=10, pady=10)
esuqcel_senha = customtkinter.CTkLabel(janela, text="Esqueceu sua senha?", font=("Arial", 10))
esuqcel_senha.pack(padx=10, pady=10)



janela.mainloop()