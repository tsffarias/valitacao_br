from validate_docbr import CPF, CNPJ

# design pattern factory
class Document:

    @staticmethod
    def create_document(documento):
        if len(documento) == 11:
            return Doc_cpf(documento)
        elif len(documento) == 14:
            return Doc_cnpj(documento)
        else:
            raise ValueError("Quantidade de digitos inválida!!")

# classe validacao e formatacao de CPF
class Doc_cpf:
    
    def __init__(self, documento):
        if self.validate(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF Inválido!!")

    def __str__(self):
        return self.format()
       
    # realiza a validacao do documento cpf
    def validate(self, documento):
        validador = CPF()
        return validador.validate(documento)

    # aplica mascara de formatacao em cpf
    def format(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

# classe validacao e formatacao de CNPJ
class Doc_cnpj:
    
    def __init__(self, documento):
        if self.validate(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ Inválido!!")

    def __str__(self):
        return self.format()

    # realiza a validacao do documento cnpj
    def validate(self, documento):
        validador = CNPJ()
        return validador.validate(documento)

    # aplica mascara de formatacao em cnpj
    def format(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)
