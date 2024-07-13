import openpyxl 
import pyperclip
import pyautogui
from time import sleep 

# Entrar na planilha
workbook = openpyxl.load_workbook('produtos_ficticios.xlsx')
sheet_produtos = workbook['Produtos']

for linha in sheet_produtos.iter_rows(min_row=2):
    nome_produto = linha[0].value
    pyperclip.copy(nome_produto)
    pyautogui.click(222, 342, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    descricao = linha[1].value
    pyperclip.copy(descricao)
    pyautogui.click(256, 433, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    categoria = linha[2].value
    pyperclip.copy(categoria)
    pyautogui.click(232, 553, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    codigo_produto = linha[3].value
    pyperclip.copy(codigo_produto)
    pyautogui.click(208, 644, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    peso = linha[4].value
    pyperclip.copy(peso)
    pyautogui.click(196, 738, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    dimensoes = linha[5].value
    pyperclip.copy(dimensoes)
    pyautogui.click(209, 817, duration=1)
    pyautogui.hotkey('ctrl', 'v')
    
    pyautogui.click(195, 886, duration=1)
    sleep(2)

    preco = linha[6].value
    pyperclip.copy(preco)
    pyautogui.click(175, 364, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    quantidade_em_estoque = linha[7].value
    pyperclip.copy(quantidade_em_estoque)
    pyautogui.click(171, 452, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    data_de_validade = linha[8].value
    pyperclip.copy(data_de_validade)
    pyautogui.click(177, 535, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    cor = linha[9].value
    pyperclip.copy(cor)
    pyautogui.click(178, 625, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    tamanho = linha[10].value 
    pyautogui.click(186, 707, duration=1)

    if tamanho == 'Pequeno':
        pyautogui.click(233, 741, duration=1)
    elif tamanho == 'Médio':
        pyautogui.click(170, 758, duration=1)
    else:
        pyautogui.click(265, 781, duration=1)

    material = linha[11].value
    pyperclip.copy(material)
    pyautogui.click(170, 790, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    pyautogui.click(198, 857, duration=1)
    sleep(2)

    fabricante = linha[12].value
    pyperclip.copy(fabricante)
    pyautogui.click(175,403, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    pais_origem = linha[13].value
    pyperclip.copy(pais_origem)
    pyautogui.click(175,488, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    observacoes = linha[14].value
    pyperclip.copy(observacoes)
    pyautogui.click(176,573, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    codigo_de_barras = linha[15].value
    pyperclip.copy(codigo_de_barras)
    pyautogui.click(185,709, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    localizacao_armazem = linha[16].value
    pyperclip.copy(localizacao_armazem)
    pyautogui.click(175,796, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    pyautogui.click(199,850,duration=1)
    pyautogui.click(686,171,duration=1)
    pyautogui.click(496,621,duration=1)
    sleep(2)
