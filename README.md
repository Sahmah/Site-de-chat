Importação da Biblioteca
Importamos flet como ft, que permite criar interfaces gráficas para web e desktop de forma simples.
Criando a Função Principal (main)

A função main(pagina) define o que será mostrado na interface.
Título do Chat
Criamos um ft.Text("Chatzapp", size=40, color=ft.colors.CYAN_700) para exibir o nome do chat.

Criando a Estrutura do Chat
Criamos um ft.Column() chamado chat, onde as mensagens serão exibidas, uma abaixo da outra.
Criamos um campo de texto (ft.TextField) para o usuário digitar seu nome.

Função para Enviar Mensagens pelo "Túnel" (pubsub)
pagina.pubsub.subscribe(enviar_mensagem_tunel): O Flet usa um sistema de comunicação chamado pubsub, que permite enviar mensagens entre usuários conectados.
Quando uma mensagem é recebida, verificamos o tipo:
Se for "mensagem", adicionamos o nome do usuário e o texto ao chat.
Se for "entrada", mostramos que o usuário entrou no chat.
Chamamos pagina.update() para atualizar a interface automaticamente.

Função para Enviar uma Nova Mensagem
Pegamos o texto digitado com campo_mensagem.value.
Enviamos a mensagem para todos os usuários com pagina.pubsub.send_all().
Limpamos o campo de mensagem e atualizamos a tela.

Criando os Elementos da Interface
Criamos campo_mensagem (caixa de texto para mensagens) e botao_enviar_mensagem (botão de envio).
Função para Entrar no Chat

Quando o usuário entra no chat:
Enviamos uma mensagem avisando que ele entrou.
Adicionamos o chat à tela com pagina.add(chat).
Fechamos o popup (popup.open = False).
Removemos o botão inicial e o título.
Criamos a área de envio de mensagens (ft.Row([campo_mensagem, botao_enviar_mensagem])).

Criando o Popup de Entrada
Criamos um ft.AlertDialog para pedir o nome do usuário antes de entrar no chat.
O botão "Entrar" chama a função entrar_chat().

Criando o Botão para Abrir o Popup
Criamos um botão inicial (botao_iniciar), que ao ser clicado abre o popup de entrada.
Adicionando Elementos na Página
Adicionamos o título e o botão inicial ao layout.
Definimos o tema com pagina.theme_mode = ft.ThemeMode.SYSTEM (modo claro/escuro automático).

Rodando o Aplicativo
ft.app(target=main, view=ft.WEB_BROWSER, port=8000):
Rodamos o chat como um site no navegador.
O chat fica disponível na porta 8000.
Interrompendo a Execução
Para parar o servidor, usamos Ctrl + C no terminal.
