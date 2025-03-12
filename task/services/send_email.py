import smtplib
import email.message
from datetime import timedelta
from django.utils.timezone import now
from task.models import Commitment  # Importa do models.py do mesmo app

from appYoutube.settings import EMAIL_REMETENTE, EMAIL_SECRET_KEY

def enviar_email(destinatario, titulo, descricao):
    # Cria o conteúdo do e-mail em formato HTML
    corpo_email = f"""
    <p>Olá, você tem uma tarefa agendada para amanhã!</p>
    <p><strong>Título:</strong> {titulo}</p>
    <p><strong>Descrição:</strong> {descricao}</p>
    """

    # Configura os detalhes do e-mail
    msg = email.message.Message()
    msg['Subject'] = "Lembrete de Tarefa - Amanhã!"  # Assunto do e-mail
    msg['From'] = EMAIL_REMETENTE  # E-mail do remetente
    msg['To'] = destinatario  # E-mail do destinatário

    password = EMAIL_SECRET_KEY  # Senha do e-mail do remetente
    msg.add_header('Content-Type', 'text/html')  # Define o tipo de conteúdo como HTML
    msg.set_payload(corpo_email)  # Adiciona o corpo do e-mail

    try:
        # Conecta ao servidor SMTP do Gmail
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()  # Inicia a comunicação criptografada
        s.login(msg['From'], password)  # Faz login com o e-mail e a senha

        # Envia o e-mail
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
        s.quit()  # Encerra a conexão com o servidor

        print(f"E-mail enviado para {destinatario}")
    except Exception as e:
        # Trata e exibe qualquer erro que ocorra durante o envio
        print(f"Erro ao enviar e-mail: {e}")

def verificar_tarefas():
    # Calcula a data de amanhã
    amanha = now() + timedelta(days=1)

    # Busca todas as tarefas agendadas para amanhã
    tarefas = Commitment.objects.filter(date_commitmment__date=amanha.date())

    # Para cada tarefa encontrada, envia um e-mail para o usuário responsável
    for tarefa in tarefas:
        enviar_email(
            destinatario=tarefa.user.email,  # E-mail do usuário vinculado à tarefa
            titulo=tarefa.title,  # Título da tarefa
            descricao=tarefa.describe  # Descrição da tarefa
        )
