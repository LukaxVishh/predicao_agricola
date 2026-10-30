"""
Validador não-bloqueante de execução do Notebook Oficial do Projeto
"""
import json
import sys
from pathlib import Path
import matplotlib
matplotlib.use("Agg")  # Impede abertura de janelas bloqueantes durante testes headless
import matplotlib.pyplot as plt
plt.show = lambda: None  # Mock show para rodar continuamente

nb_path = Path(r"C:\Users\kinha\predicao_agricola\Projeto\notebooks\02_projeto_principal\projeto_agrodata_pipeline_completo.ipynb")

with open(nb_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

print(f"Executando validação de {len(nb['cells'])} células em: {nb_path.name}...")

global_env = {}

for idx, cell in enumerate(nb["cells"]):
    if cell["cell_type"] == "code":
        code_src = "".join(cell["source"])
        print(f"--- Executando Célula {idx} ---")
        try:
            exec(code_src, global_env)
            print(f"[OK] Célula {idx} executou sem erros.")
        except Exception as e:
            print(f"[ERRO] Falha na célula {idx}: {e}")
            sys.exit(1)

print("\n[SUCESSO ABSOLUTO] TODAS AS CELULAS DO NOTEBOOK EXECUTARAM COM SUCESSO E ZERO ERROS!")
