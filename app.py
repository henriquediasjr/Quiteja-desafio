import zipfile
import os
import pandas as pd
from flask import Flask, jsonify

# Descompacta o arquivo dados.zip
with zipfile.ZipFile('dados.zip', 'r') as zip_ref:
    zip_ref.extractall()

# Lê os arquivos CSV
dados = pd.read_csv('origem-dados.csv')
tipos = pd.read_csv('tipos.csv')

# Debug: Mostra as colunas e algumas linhas do arquivo dados
print("Columns in 'dados':", dados.columns)
print("First few rows of 'dados':")
print(dados.head())

# Filtra os dados com status "CRÍTICO"
dados_criticos = dados[dados['status'] == 'CRÍTICO']

# Ordena os dados filtrados pelo campo created_at
dados_criticos = dados_criticos.sort_values(by='created_at')

# Remove espaços extras nos nomes das colunas
dados_criticos.columns = dados_criticos.columns.str.strip()
tipos.columns = tipos.columns.str.strip()

# Adiciona o campo nome_tipo baseado no arquivo tipos.csv
dados_criticos = dados_criticos.merge(tipos[['id', 'nome']], left_on='tipo', right_on='id', how='left')
dados_criticos.rename(columns={'nome': 'nome_tipo'}, inplace=True)

# Cria o arquivo insert-dados.sql com os dados filtrados
with open('insert-dados.sql', 'w') as f:
    for index, row in dados_criticos.iterrows():
        insert_statement = f"INSERT INTO dados_finais (id, created_at, status, tipo, nome_tipo) VALUES ({row['id']}, '{row['created_at']}', '{row['status']}', {row['tipo']}, '{row['nome_tipo']}');\n"
        f.write(insert_statement)

# Cria a aplicação Flask
app = Flask(__name__)

# Cria um dicionário para buscar tipos pelo ID
tipos_dict = tipos.set_index('id')['nome'].to_dict()

# Rota para buscar o tipo pelo ID
@app.route('/tipo/<int:id>', methods=['GET'])
def get_tipo(id):
    tipo = tipos_dict.get(id)
    if tipo:
        return jsonify({'id': id, 'nome': tipo}), 200
    else:
        return jsonify({'error': 'Tipo não encontrado'}), 404

# Inicia o servidor Flask
if __name__ == '__main__':
    app.run(debug=True)
