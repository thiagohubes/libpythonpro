class Enviador:
    def enviar(self, remetente, destinatario, assunto, corpo):
        if '@' not in remetente:
            raise EmailInvalido('Email de remetente inválido: {remetente}')
        return remetente


class EmailInvalido(Exception):
    pass
