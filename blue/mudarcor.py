import os
import xml.etree.ElementTree as ET

# --- Configurações ---
pasta_originais = 'svgs_originais'
pasta_modificados = 'svgs_modificados'
cor_antiga = '#3FBDF1'  # Substitua pela cor alvo
cor_nova = '#00ced1'    # Substitua pela cor desejada

# Certifique-se de que a pasta de modificados existe
if not os.path.exists(pasta_modificados):
    os.makedirs(pasta_modificados)

def mudar_cor_svg(arquivo_entrada, arquivo_saida, cor_antiga, cor_nova):
    try:
        tree = ET.parse(arquivo_entrada)
        root = tree.getroot()

        # Namespace dos SVGs (pode variar)
        namespace = {'svg': 'http://www.w3.org/2000/svg'}

        # Busca por atributos 'fill' e 'stroke' e substitui a cor
        for elem in root.findall('.//*[@fill]'):
            if elem.get('fill') == cor_antiga:
                elem.set('fill', cor_nova)
        for elem in root.findall('.//*[@stroke]'):
            if elem.get('stroke') == cor_antiga:
                elem.set('stroke', cor_nova)

        # Salva o arquivo modificado
        tree.write(arquivo_saida)
        print(f"Cor substituída em: {arquivo_entrada} -> {arquivo_saida}")

    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado: {arquivo_entrada}")
    except ET.ParseError:
        print(f"Erro: Falha ao analisar XML em: {arquivo_entrada}")

# Percorre todos os arquivos na pasta de originais
for nome_arquivo in os.listdir(pasta_originais):
    if nome_arquivo.endswith(".svg"):
        caminho_entrada = os.path.join(pasta_originais, nome_arquivo)
        caminho_saida = os.path.join(pasta_modificados, nome_arquivo)
        mudar_cor_svg(caminho_entrada, caminho_saida, cor_antiga, cor_nova)

print("Processo de substituição de cores concluído.")