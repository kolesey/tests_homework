import pytest

from main import solve


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
    ([1, 1, 1, 1, 0, 1, 1, 0], ['Intel', 'Samsung', 'WD'], (['500 ГБ 2.5" SATA накопитель Samsung 870 EVO', '480 ГБ 2.5" SATA накопитель WD Green'], 2)),
    ([0, 0, 0, 0, 0, 0, 0, 0], ['Intel', 'Samsung', 'WD'], ([], 0)),
    ([1, 1, 1, 1, 0, 1, 1, 0], ['Intel', 'Samsung'], (['500 ГБ 2.5" SATA накопитель Samsung 870 EVO'], 1))
)
@pytest.mark.parametrize(
    'available, manufacturers, expected',
    params
)


def test_solve_with_params(create_list_of_models, available, manufacturers, expected):
    assert solve(create_list_of_models, available, manufacturers) == expected