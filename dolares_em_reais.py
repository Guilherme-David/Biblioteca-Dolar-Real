import api_cotacoes # importa biblioteca

carteira = float(input('Quanto tem na carteira? USD '))

dolares_em_reais = api_cotacoes.converter_dolares_em_reais(carteira)
print(f'A quantidade de USD {carteira:,.2f}, em Reais é: R$ {dolares_em_reais:,.2f}')
