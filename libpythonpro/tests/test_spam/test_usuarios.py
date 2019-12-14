from libpythonpro.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Thiago', email="thiago.hubes@gmail.com")
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [
        Usuario(nome='Thiago', email="thiago.hubes@gmail.com"),
        Usuario(nome='Hubes', email="thiago.hubes@gmail.com")
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
