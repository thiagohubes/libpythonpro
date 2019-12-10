import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['thiago.hubes@gmail.com', 'foo@bar.com.br'],

)
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        'thiago.hubes@outlook.com',
        'Cursos Python Pro',
        'Primeira turma Guido von Rossum aberta.')
    assert destinatario in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'foo'],
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'thiago.hubes@outlook.com',
            'Cursos Python Pro',
            'Primeira turma Guido von Rossum aberta.')
