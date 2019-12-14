class Enviador:
    def __init__(self):
        self.qde_de_emails_enviados = 0

    def enviar(self, remetente, destinatario, assunto, corpo):
        if '@' not in remetente:
            raise EmailInvalido('Email de remetente inválido: {remetente}')
        self.qde_de_emails_enviados += 1
        return remetente


class EmailInvalido(Exception):
    pass
