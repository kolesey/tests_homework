import pytest

from main import solve, reverse, check_email


# Test solve
@pytest.fixture
def create_list_of_models():
    models = ['480 ГБ 2.5" SATA накопитель Kingston A400',
              '500 ГБ 2.5" SATA накопитель Samsung 870 EVO',
              '480 ГБ 2.5" SATA накопитель ADATA SU650',
              '240 ГБ 2.5" SATA накопитель ADATA SU650',
              '250 ГБ 2.5" SATA накопитель Samsung 870 EVO',
              '256 ГБ 2.5" SATA накопитель Apacer AS350 PANTHER',
              '480 ГБ 2.5" SATA накопитель WD Green',
              '500 ГБ 2.5" SATA накопитель WD Red SA500']
    return models


params = (
    ([1, 1, 1, 1, 0, 1, 1, 0], ['Intel', 'Samsung', 'WD'],
     (['500 ГБ 2.5" SATA накопитель Samsung 870 EVO', '480 ГБ 2.5" SATA накопитель WD Green'], 2)),
    ([0, 0, 0, 0, 0, 0, 0, 0], ['Intel', 'Samsung', 'WD'], ([], 0)),
    ([1, 1, 1, 1, 0, 1, 1, 0], ['Intel', 'Samsung'], (['500 ГБ 2.5" SATA накопитель Samsung 870 EVO'], 1))
)


@pytest.mark.parametrize(
    'available, manufacturers, expected',
    params
)
def test_solve_with_params(create_list_of_models, available, manufacturers, expected):
    assert solve(create_list_of_models, available, manufacturers) == expected


# Test reverse
params = (
    ('!dlroW olleH', 'hello world!'),
    ('AvadaKedavraaaaA!', '!aaaaarvadekadava'),
    ('', '')
)


@pytest.mark.parametrize(
    'test_string, expected',
    params
)
def test_reverse(test_string, expected):
    assert reverse(test_string) == expected


def test_reverse_int():
    with pytest.raises(TypeError):
        reverse(123)


# Test check_email
params = (
    ('Helloworld@.ru', True),
    ('мояпочта@нетология.ру', True),
    ('python@email@net', False),
    (' em@il.ru', False)
)


@pytest.mark.parametrize(
    'email, expected',
    params
)
def test_check_email(email, expected):
    assert check_email(email) is expected


def test_check_email_int():
    with pytest.raises(TypeError):
        check_email(123)
