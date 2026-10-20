"""
App mínima de exemplo para o CP05.

PROVA 2 (Semgrep): a função abaixo usa eval() sobre entrada do usuário,
um padrão inseguro que o Semgrep aponta
(regra: python.lang.security.audit.eval-detected).

Para a entrega, deixe este eval presente no código enviado ao repositório:
é ele que o job do Semgrep vai sinalizar na aba Actions (Prova 2).
"""


def calcular(expressao: str):
    # VULNERÁVEL DE PROPÓSITO (Prova 2 do Semgrep):
    # eval() executa qualquer código Python contido em `expressao`.
    return eval(expressao)


if __name__ == "__main__":
    entrada = input("Digite uma expressão matemática: ")
    print("Resultado:", calcular(entrada))
