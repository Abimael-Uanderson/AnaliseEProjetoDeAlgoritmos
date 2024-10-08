import ast

class AnalizadorCodigoPython(ast.NodeVisitor):
    
    def __init__(self):
        self.contagem_operacoes = {
            'Assign': 0,
            'AugAssign': 0,
            'BinOp': 0,
            'UnaryOp': 0,
            'Compare': 0,
            'Call': 0
        }
        self.contagem_loops = {
            'For': 0,
            'For Aninhado': 0,
            'While': 0,
            'While Aninhado': 0
        }
        self.contagem_recursao = 0
        self.funcao_ativa = None
        self.funcoes_recursivas = set()

    def visit(self, node):
        
        if isinstance(node, ast.FunctionDef):
            self.funcao_ativa = node.name
            self.generic_visit(node)
            self.funcao_ativa = None  
        elif isinstance(node, ast.For):
            self.contagem_loops['For'] += 1
            nivel_aninhado = contar_loops_aninhados(node)
            if nivel_aninhado > self.contagem_loops['For Aninhado']:
                self.contagem_loops['For Aninhado'] = nivel_aninhado
            self.generic_visit(node)
        elif isinstance(node, ast.While):
            self.contagem_loops['While'] += 1
            nivel_aninhado = contar_loops_aninhados(node)
            if nivel_aninhado > self.contagem_loops['While Aninhado']:
                self.contagem_loops['While Aninhado'] = nivel_aninhado
            self.generic_visit(node)
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            if node.func.id == self.funcao_ativa:
                # Olha a recursão
                self.contagem_recursao += 1
                self.funcoes_recursivas.add(self.funcao_ativa)
        else:
            tipo_node = type(node).__name__
            if tipo_node in self.contagem_operacoes:
                self.contagem_operacoes[tipo_node] += 1
            self.generic_visit(node)

def contar_loops_aninhados(node, profundidade=1):
    ## profundidade dos loops
    max_profundidade = profundidade
    for child in ast.iter_child_nodes(node):
        if isinstance(child, (ast.For, ast.While)):
            max_profundidade = max(max_profundidade, contar_loops_aninhados(child, profundidade + 1))
    return max_profundidade

def analisar_arquivo_codigo(caminho_arquivo):
    # realização da análise
    with open(caminho_arquivo, 'r') as file:
        codigo = file.read()
    arvore = ast.parse(codigo)
    analisador = AnalizadorCodigoPython()
    analisador.visit(arvore)
    return analisador.contagem_operacoes, analisador.contagem_loops, analisador.contagem_recursao, analisador.funcoes_recursivas

def exibir_notacao_assintotica(contagem_loops, contagem_recursao, funcoes_recursivas):
    max_for_aninhado = contagem_loops.get('For Aninhado', 0)
    max_while_aninhado = contagem_loops.get('While Aninhado', 0)

    if contagem_recursao > 0 and len(funcoes_recursivas) > 0:
        # Identificação de casos
        print("O(n log n) devido à recursão")
    elif max_for_aninhado == 0 and max_while_aninhado == 0:
        
        print("O(1)")
    elif max_for_aninhado == 0:
        print(f"O(n^{max_while_aninhado})")
    elif max_while_aninhado == 0:
        print(f"O(n^{max_for_aninhado})")
    else:
        print(f"O(n^{max_for_aninhado + max_while_aninhado})")

if __name__ == "__main__":
    caminho_arquivo = "copaAmerica.py"  # caminho do arquivo
    operacoes, loops, contagem_recursao, funcoes_recursivas = analisar_arquivo_codigo(caminho_arquivo)

    print("Contagem de Operações:")
    for operacao, contagem in operacoes.items():
        print(f"{operacao}: {contagem}")

    print("\nContagem de Loops:")
    for tipo_loop, contagem in loops.items():
        print(f"{tipo_loop}: {contagem}")

    print("\nTotal de Chamadas Recursivas:")
    print(f"Recursivas: {contagem_recursao} (funções recursivas: {', '.join(funcoes_recursivas)})")

    print("\nNotação Assintótica:")
    exibir_notacao_assintotica(loops, contagem_recursao, funcoes_recursivas)
