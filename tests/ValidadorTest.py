import sys
import os

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(project_root, 'src'))

from Validador import validar_cpf # pyright: ignore[reportMissingImports]

def run_test(name, cpf_input, expected_result):
    cpf_input_str = str(cpf_input) if cpf_input is not None else 'None'
    
    result = validar_cpf(cpf_input)
    status = "PASSOU" if result == expected_result else "FALHOU"
    
    print(f"Teste: {name:<25} | Entrada: '{cpf_input_str:<20}' | Esperado: {expected_result:<5} | Resultado: {result:<5} | Status: {status}")
print("   ")
print("   ")
print("--- Testes de Cenários Válidos ---")
run_test("CPF válido (com máscara)", "529.982.247-25", True)
run_test("CPF válido (sem máscara)", "52998224725", True)
run_test("CPF com espaços externos", " 529.982.247-25 ", True)
print("   ")
print("\n--- Testes de Cenários Inválidos ---")
run_test("Entrada nula", None, False)
run_test("Entrada vazia", "", False)
run_test("Tamanho menor", "935.411.347-8", False)
run_test("Tamanho maior", "935.411.347-800", False)
run_test("Caractere inválido", "529.982.247-2X", False)
run_test("Sequência repetida", "000.000.000-00", False)
run_test("DV incorreto", "529.982.247-24", False)
run_test("DV incorreto (genérico)", "123.456.789-00", False)
print("   ")
print("   ")
