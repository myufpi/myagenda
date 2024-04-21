import re

# re (Regular Expression)
# https://en.wikipedia.org/wiki/Regular_expression
# https://docs.python.org/3/library/re.html
# https://www.geeksforgeeks.org/python-regex

class ValidadorDados:
  def __init__(self):
    self.cpf = ""
    self.data_nascimento = ""
    self.email = ""
    self.cep = ""
    self.telefone = ""

  '''
    ^ e $ indicam o início e o fim da string, respectivamente.
    \d{11} representa exatamente 11 dígitos numéricos [0..9].
  '''
  def validar_cpf(self):
    pattern = r"^\d{11}$"
    if re.match(pattern, self.cpf):
      return True
    else:
      return False

  '''
    ^ e $ indicam o início e o fim da string, respectivamente.
    (0[1-9]|1[0-9]|2[0-9]|3[0-1]) representa o dia da data de nascimento, permitindo valores de 01 a 31.
    (0[1-9]|1[0-2]) representa o mês da data de nascimento, permitindo valores de 01 a 12.
    (19|20)\d{2} representa o ano da data de nascimento, permitindo valores de 1900 a 2099.
  '''
  def validar_data_nascimento(self):
    pattern = r"^(0[1-9]|1[0-9]|2[0-9]|3[0-1])/(0[1-9]|1[0-2])/(19|20)\d{2}$"
    if re.match(pattern, self.data_nascimento):
        return True
    else:
        return False

  '''
  ^: Corresponde ao início da string.
  [a-zA-Z0-9_.+-]+: Corresponde a um ou mais caracteres do conjunto (letras, números, sublinhado, ponto, sinal de adição, hífen).
  @: Corresponde ao símbolo "@".
  [a-zA-Z0-9-]+.: Corresponde a um ou mais caracteres do conjunto (letras, números, hífen) seguido por um ponto literal.
  [a-zA-Z0-9-.]+$: Corresponde a um ou mais caracteres do conjunto (letras, números, hífen, ponto) no final da string.
  '''
  def validar_email(self):
    pattern = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"  # Email regex pattern
    if re.match(pattern, self.email):
      return True
    else:
      return False

  '''
  \d{5}: Exactly five digits before the hyphen.
  -: A literal hyphen.
  \d{3}: Exactly three digits after the hyphen.
  '''
  def validar_cep(self):
    pattern = r"\d{5}-\d{3}"  # CEP regex pattern
    if re.match(pattern, self.cep):
      return True
    else:
      return False

  '''
  ^: Corresponde ao início da string.
  \(\d{2}\): Corresponde a parênteses de abertura, dois dígitos para o código de área e parênteses de fechamento
  (?:\s)?: Corresponde a um espaço opcional (grupo de captura não captura).
  \d{5}: Cinco dígitos para a primeira parte do número de telefone.
  (?:\s|-)?: Corresponde a outro espaço opcional (grupo de captura não captura).
  \d{4}: Quatro dígitos para a segunda parte do número de telefone.
  $: Corresponde ao final da string.
  '''
  def validar_telefone(self):
    pattern = r"^\(\d{2}\)(?:\s)?\d{5}(?:\s|-)?\d{4}$"
    if re.match(pattern, self.telefone):
      return True
    else:
      return False
