# Chatzapp
# botao de iniciar chat
# popup para entrar no chat
# quando entrar no chat: (aparece para todo mundo)
    # a mensagem que você entrou no chat
    # o campo e o botão de enviar mensagem
# a cada mensagem que você envia (aparece para todo mundo)
    # Nome: Texto da Mensagem

# Flet->Usado pra criar sites e apps tanto no Frontend e Backend

import flet as ft

# Criar uma função principal para rodar o site
def main(pagina):
    texto = ft.Text("Chatzapp", 
                    size=40, color=ft.colors.CYAN_700)

# ft.Column() = As irformação ficam uma em baixo da outra por isso -> coluna
    chat = ft.Column()
# label = orientação pra o usuario do que digitar quando se abre o chat
# TextField = Caixa que abre para digitar a mensagem
    nome_usuario = ft.TextField(label="Escreva seu nome")

# Tunel seria o tunel de comunicação entre os usuarios
    def enviar_mensagem_tunel(mensagem):
        tipo = mensagem["tipo"]
        if tipo == "mensagem":
            texto_mensagem = mensagem["texto"]
            usuario_mensagem = mensagem["usuario"]
            # Ao adicionar a mensagem no chat parece o usuario e a mensagem
            chat.controls.append(ft.Text(f"{usuario_mensagem}: {texto_mensagem}"))
        else:
            usuario_mensagem = mensagem["usuario"]
            chat.controls.append(ft.Text(f"{usuario_mensagem} entrou no chat", 
                                         size=12, italic=True, color=ft.colors.ORANGE_500))
        # Pagina.update atualiza a pagina do usuario automaticamente, quando se muda visualmente a pagina
        pagina.update()
# pubsub = é o tunel de comunicação do flet
    pagina.pubsub.subscribe(enviar_mensagem_tunel)

# Para pegar o texto que o usuario escreveu deve-se pegar nesse caso campo_mensagem.value -> valor
# pubsub.send_all= enviar a mensagem pra todos os usuarios conectados
    def enviar_mensagem(evento):
        pagina.pubsub.send_all({"texto": campo_mensagem.value, "usuario": nome_usuario.value,
                                "tipo": "mensagem"})
        # limpar o campo de mensagem ao mandar uma mensagem
        campo_mensagem.value = ""
        pagina.update()
# on_submit = como se fosse o onclick, quando o usuario enviar a mensagem ele vai excutar a função enviar_mensagem
    campo_mensagem = ft.TextField(label="Digite uma mensagem", on_submit=enviar_mensagem)
    botao_enviar_mensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

# Função de entrar no chat
# Ao entrar no chat deve-se fechar o popup, sumir com o titulo e com o botão de iniciar chat
    def entrar_chat(evento):
        pagina.pubsub.send_all({"usuario": nome_usuario.value, "tipo": "entrada"})
        # adicionar o chat
        pagina.add(chat)
        # fechar o popup
        popup.open = False
        # remover o botao iniciar chat
        pagina.remove(botao_iniciar)
        pagina.remove(texto)
        # criar o campo de mensagem do usuario
        # criar o botao de enviar mensagem do usuario
        #ft.Row = as informações aparecem em uma linha, um do lado do outro
        pagina.add(ft.Row(
            [campo_mensagem, botao_enviar_mensagem]
        ))
        pagina.update()

# Criar o popup que no flet é chamado de AlertDialog
# Dentro do popup se coloca título, texto, entre outras coisas
# Content é o conteúdo do popup, nesse caso seria a caixa de texto com o nome do usuario
# Actions = ações que o popup vai ter e tem que ser em formato de lista -> []
    popup = ft.AlertDialog(
        open=False, 
        modal=True,
        title=ft.Text("Bem vindo ao Chatzapp"),
        content=nome_usuario,
        actions=[ft.ElevatedButton("Entrar", on_click=entrar_chat)],
        )

# Função de clicar no botão e abrir o popup
# Sempre que uma função esta relacionada ao clique ou algo parecido sempre deve receber como parametro uma variavel evento
    def entrar_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

# Quando o usuario clicar no botão ele vai entrar no chat
# ElevateButton é uma das variações da aparencia do botão
    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=entrar_popup)

    pagina.add(texto)
    pagina.add(botao_iniciar)
    pagina.theme_mode = ft.ThemeMode.SYSTEM
# Para abrir como um site colocar view=ft.WEBROWSER
ft.app(target=main, view=ft.WEB_BROWSER, port=8000)
# Para interromper a execução do código vá no terminal e de um ctrl C
# deploy
