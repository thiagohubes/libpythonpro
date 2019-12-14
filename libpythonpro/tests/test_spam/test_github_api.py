from unittest.mock import Mock

from libpythonpro import github_api


def test_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {
        'login': 'thiagohubes', 'id': 50760362, 'node_id': 'MDQ6VXNlcjUwNzYwMzYy',
        'avatar_url': 'https://avatars3.githubusercontent.com/u/50760362?v=4',
    }
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('thiagohubes')
    assert 'https://avatars3.githubusercontent.com/u/50760362?v=4' == url
