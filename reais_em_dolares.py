import api_cotacoes # importa biblioteca

try:
  carteira = float(input('Quanto tem na carteira? R$ '))

  reais_em_dolares = api_cotacoes.converter_reais_em_dolares(carteira)
  print(f'A quantidade de R$ {carteira:,.2f}, em Dólares é: USD {reais_em_dolares:,.2f}')
except ValueError:
  print('Valor informado foi inválido. \nEsperava um valor em unidade monetária.
