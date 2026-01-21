def solve(models: list, available: list, manufacturers: list):
    repair_count = 0  # количество дисков, которые купит сисадмин
    ssds = []  # модели дисков из списка models, которые купит сисадмин
    # код вашего решения ниже:
    ssds = [model for model, qty in zip(models, available) if model.split()[5] in manufacturers and qty != 0]
    repair_count = len(ssds)

    return ssds, repair_count  # Этот код менять не нужно


def reverse(string: str) -> str:
    return string[::-1].lower()


def check_email(email: str) -> bool:
    if ' ' not in email and '@' in email and '.' in email:
        return True
    else:
        return False
