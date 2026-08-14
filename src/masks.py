def get_mask_card_number(card_number: str) -> str:
    """
    Принимает номер карты и шифрует его
    :param card_number: 7000792289606361
    :return: 7000 79** **** 6361
    """
    # Проверяем, что номер карты состоит из цифр и имеет правильную длину
    if not card_number.isdigit() or len(card_number) != 16:
        print("Проверьте ввод, Номер карты должен состоять из 16 цифр.")
        raise ValueError("Номер карты должен состоять из 16 цифр.")
    masked_number = (
        card_number[0:4] + " " + card_number[4:6] + "** **** " + card_number[12:]
    )
    return masked_number


def get_mask_account(account_number: str) -> str:
    """
    Принимает аккаунт и шифрует его
    :param account_number: 73654108430135874305
    :return: **4305
    """
    if not account_number.isdigit() or len(account_number) != 20:
        print("Проверьте ввод. Аккаунт должен состоять из 20 цифр.")
        raise ValueError("Номер аккаунта должен состоять из 20 цифр.")
    mask_account = "**" + account_number[16:]
    return mask_account

