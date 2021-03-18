<h2 align="center">Valitação BR :heavy_check_mark:</h2> 

---

**Objetivo:** Este projeto visa a realização da validação e formatação (vali + tação) de dados em padrão nacional, de maneira simples e rápida, utilizando a linguagem de programação Python 3, pacotes open source e APIs gratuitas. Os dados atualmente englobados pelo projeto para realização da validação e formatação são:
- **_CPF_**
- **_CNPJ_**
- **_CEP_**
- **_Data_**
- **_Número de Telefone_**


---

**Ferramentas utilizadas:** :hammer_and_wrench:
- [ViaCEP](https://viacep.com.br/ "ViaCEP"): API que retorna informações de endereço a partir do CEP (bairro, cidade, uf).
- [validate_docbr](https://pypi.org/project/validate-docbr/ "validate_docbr"): Pacote Python para validação de documentos brasileiros.
- [datetime](https://docs.python.org/3/library/datetime.html "datetime"): Módulo datetime fornece classes para manipulação de datas e horas.
- [re](https://docs.python.org/3/library/re.html "re"): Módulo re fornece uma interface para o mecanismo de expressão regular, permitindo compilar REs em objetos e, em seguida, executar comparações com eles.

---

**Exemplo do funcionamento:** :heart:

```python
from phone_number_br import Phone_number_br
from cpf_cnpj import Document
from date_br import Date_br
from search_address_cep import Search_address_cep

# ======== CPF & CNPJ ========

cpf = "95100647183"
cnpj = "35379838000112"
objeto_cpf = Document.create_document(cpf)
objeto_cnpj = Document.create_document(cnpj)

print(objeto_cpf)  # Saída: 951.006.471-83
print(objeto_cnpj)  # Saída: 35.379.838/0001-12

# ======== Número Telefone ========

telefone = "552126481234"
telefone_objeto = Phone_number_br(telefone)

print(telefone_objeto)  # Saída: +55 (21)2648-1234

# ======== Datas ========

cadastro = Date_br()
print(cadastro)    # Saída: 18/03/2021 10:14
print(cadastro.weekday_registration()) # Saída: quinta-feira
print(cadastro.month_registration())   # Saída: março

# ======== CEP ========

cep = "01001000"
objeto_cep = Search_address_cep(cep)
# enviando requisição para API via_cep, e retornando bairro, cidade e UF do CEP informado
bairro, cidade, uf = objeto_cep.send_request_via_cep()

print(objeto_cep)  # Saída: 01001-000
print(f"Bairro: {bairro} - Cidade: {cidade} - UF: {uf}") # Saída: Bairro: Sé - Cidade: São Paulo - UF: SP

```

---  

![](https://komarev.com/ghpvc/?username=tsffarias&color=blue&style=flat)
