def _sanitizar_cpf(cpf):
    """
    Sanitiza a string do CPF, removendo máscara e espaços.
    """
    if not isinstance(cpf, str):
        return None
    
    cpf_limpo = ''.join(filter(str.isdigit, cpf))
    
    if not cpf_limpo.isdigit():
        return None
        
    return cpf_limpo

def _calcular_dv(digitos, peso_inicial):
    """
    Calcula um dígito verificador usando soma ponderada e módulo 11.
    """
    soma = 0
    peso = peso_inicial
    for digito in digitos:
        soma += int(digito) * peso
        peso -= 1
    
    resto = soma % 11
    
    # Aplica a regra especial: se o resto for menor que 2, o DV é 0
    if resto < 2:
        return 0
    else:
        return 11 - resto

def validar_cpf(cpf):
    """
    Valida um CPF brasileiro de acordo com as regras estabelecidas.
    """
    # 1. Sanitiza a entrada, removendo espaços, pontos e traços.
    cpf_limpo = _sanitizar_cpf(cpf)
    
    # 2. Checa se a sanitização foi bem-sucedida e se a entrada não é nula ou vazia.
    if cpf_limpo is None or not cpf_limpo:
        return False
        
    # 3. Checa o tamanho: deve ter exatamente 11 dígitos.
    if len(cpf_limpo) != 11:
        return False
    
    # 4. Rejeita sequências com todos os dígitos iguais.
    if len(set(cpf_limpo)) == 1:
        return False
        
    # 5. Separa os 9 primeiros dígitos e os 2 verificadores para o cálculo.
    nove_digitos = cpf_limpo[:9]
    dv1_original = int(cpf_limpo[9])
    dv2_original = int(cpf_limpo[10])

    # 6. Calcula e valida o primeiro dígito verificador (DV1).
    dv1_calculado = _calcular_dv(nove_digitos, 10)
    if dv1_calculado != dv1_original:
        return False
        
    # 7. Calcula e valida o segundo dígito verificador (DV2).
    dez_digitos = nove_digitos + str(dv1_calculado)
    dv2_calculado = _calcular_dv(dez_digitos, 11)
    if dv2_calculado != dv2_original:
        return False
        
    # 8. Se todas as verificações passarem, o CPF é válido.
    return True