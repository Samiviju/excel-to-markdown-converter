import pandas as pd
from tabulate import tabulate

caminho_arquivo_excel = r'C:\Users\samuel.vieira\scripts\python\script-markdown\arquivos-entrada-xlsx\DadosConsultaIfaro.xlsx'

df = pd.read_excel(caminho_arquivo_excel)

markdown_table = tabulate(df, headers='keys', tablefmt='pipe', showindex=False)

caminho_arquivo_markdown = r'C:\Users\samuel.vieira\scripts\python\script-markdown\saida-arquivo-markdown\DadosConsultaIfaro.md'

# Salvar a tabela em um arquivo Markdown
with open(caminho_arquivo_markdown, 'w') as f:
    f.write(markdown_table)