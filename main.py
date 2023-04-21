def get_hidden_card(karta, num=4):

    result = f'{"*" * num} {karta.replace(" ", "")[-4:]}'
    return result


get_hidden_card('2034399002121100')

