from phone_number_br import Phone_number_br
from cpf_cnpj import Document
from date_br import Date_br
from search_address_cep import Search_address_cep

# ======== CPF & CNPJ ========

cpf = "95100647183"
cnpj = "35379838000112"
objeto_cpf = Document.create_document(cpf)
objeto_cnpj = Document.create_document(cnpj)

print(objeto_cpf)   # Saída: 951.006.471-83
print(objeto_cnpj)  # Saída: 35.379.838/0001-12

# ======== Número Telefone ========

telefone = "552126481234"
telefone_objeto = Phone_number_br(telefone)

print(telefone_objeto)  # Saída: +55 (21)2648-1234

# ======== Datas ========

cadastro = Date_br()
print(cadastro)    # Saída: 15/03/2021 18:20
print(cadastro.weekday_registration())  # Saída: segunda-feira
print(cadastro.month_registration())   # Saída: março

# ======== CEP ========

cep = "01001000"
objeto_cep = Search_address_cep(cep)
# enviando requisição para API via_cep, e retornando bairro, cidade e UF do CEP informado
bairro, cidade, uf = objeto_cep.send_request_via_cep()

print(objeto_cep)  # Saída: 01001-000
# Saída: Bairro: Sé - Cidade: São Paulo - UF: SP
print(f"Bairro: {bairro} - Cidade: {cidade} - UF: {uf}")
