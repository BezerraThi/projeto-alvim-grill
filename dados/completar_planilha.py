import openpyxl

wb = openpyxl.load_workbook('c:/Users/User/alvim_grill_ccos/dados/Palavras chave Alvim Grill.xlsx')
ws = wb.active

# Cada linha tem conteudo unico e especifico para a palavra-chave
# (keyword, avg, comp, min_bid, max_bid, titulo, descricao, sitelink, sitelink_desc, callout, snippet)
data = [
    ('churrasqueira', '100 mil - 1 mi', 'Alta', 0.23, 2.37,
     'Churrasqueira Gourmet Premium',
     'Carvao, gas ou eletrica: encontre o modelo ideal pra sua area. Parcele em 10x sem juros.',
     'Ver Catalogo Completo',
     'Carvao, gas, eletrica e kits',
     'Frete Gratis',
     'Tipos: Carvao, Gas, Eletrica, Coifa'),

    ('churrasqueira alvenaria', '1 mil - 10 mil', 'Alta', 0.52, 2.75,
     'Kit Churrasqueira Alvenaria',
     'Kit coifa e acessorios para churrasqueira de alvenaria. Encaixa perfeito. Parcele em 10x.',
     'Kits para Alvenaria',
     'Coifa, grelha e acessorios inclusos',
     'Parcele em 10x Sem Juros',
     'Inclui: Coifa, Grelha, Acessorios'),

    ('churrasqueira carvao apartamento', '1 mil - 10 mil', 'Alta', 0.26, 2.94,
     'Churrasqueira p/ Apartamento',
     'Churrasqueira carvao para apartamento. Cabe em qualquer varanda. Parcele em 10x sem juros.',
     'Modelos p/ Apartamento',
     'Compactas e sem reforma necessaria',
     'Pronta Entrega',
     'Tipos: Compacta, Embutir, Cooktop'),

    ('churrasqueira de tijolinho', '10 mil - 100 mil', 'Alta', 0.20, 1.43,
     'Churrasqueira de Tijolinho',
     'Kit completo para churrasqueira de tijolinho: coifa, grelha e suporte. Parcele em 10x.',
     'Kits para Alvenaria',
     'Coifa + grelha + suporte inclusos',
     'Garantia 2 Anos',
     'Inclui: Coifa, Grelha, Suporte'),

    ('churrasqueira gourmet a carvao', '100 - 1 mil', 'Alta', 0.85, 3.28,
     'Churrasqueira Gourmet Carvao',
     'Churrasqueira gourmet carvao inox 316L. Sabor autentico e design premium. Parcele em 10x.',
     'Churrasqueiras a Carvao',
     'Gourmet, inox, embutir e bancada',
     'Inox 316L Premium',
     'Tipos: Embutir, Bancada, com Coifa'),

    ('churrasqueira gourmet completa', '100 - 1 mil', 'Alta', 1.15, 4.48,
     'Churrasqueira Gourmet Completa',
     'Kit gourmet completo: churrasqueira + coifa + grelhas e acessorios. Pronta para instalar.',
     'Kit Gourmet Completo',
     'Churrasqueira + coifa + acessorios',
     'Parcele em 10x Sem Juros',
     'Inclui: Churrasqueira, Coifa, Grelha'),

    ('churrasqueira gourmet vidro', '100 - 1 mil', 'Alta', 1.36, 3.88,
     'Churrasqueira Gourmet Vidro',
     'Churrasqueira gourmet com vidro temperado. Visual moderno e limpeza facil. Parcele em 10x.',
     'Linha Vidro Temperado',
     'Design moderno para area gourmet',
     'Compra Segura',
     'Tipos: Embutir, Bancada, com Vidro'),

    ('churrasqueira para area gourmet', '1 mil - 10 mil', 'Alta', 0.76, 2.88,
     'Churrasqueira Area Gourmet',
     'Churrasqueiras de embutir para area gourmet. Eleva o visual da sua area. Frete gratis.',
     'Modelos de Embutir',
     'Para embutir em bancada gourmet',
     'Frete Gratis',
     'Tipos: Embutir, Bancada, Premium'),

    ('churrasqueira pequena', '10 mil - 100 mil', 'Alta', 0.14, 0.89,
     'Churrasqueira Pequena Premium',
     'Churrasqueiras compactas para varanda e apartamento. Sem abrir mao do churrasco. Parcele.',
     'Modelos p/ Apartamento',
     'Cabem em qualquer varanda',
     'Entrega Rapida',
     'Tipos: Compacta, Eletrica, Gas'),

    ('churrasqueira pre moldada preco', '100 mil - 1 mi', 'Alta', 0.20, 1.20,
     'Churrasqueira Pre-Moldada',
     'Churrasqueira pre-moldada com melhor custo-beneficio do mercado. Pronta entrega. Parcele.',
     'Precos e Condicoes',
     'Melhor preco e condicoes do mercado',
     'Melhor Preco',
     'Tipos: Carvao, Gas, Eletrica'),

    ('churrasqueiras para varanda gourmet', '100 - 1 mil', 'Alta', 1.07, 3.50,
     'Churrasqueira para Varanda',
     'Churrasqueira ideal para varanda gourmet. Modelos compactos e embutir. Parcele em 10x.',
     'Modelos p/ Varanda',
     'Compactas e de embutir para varanda',
     'Pronta Entrega',
     'Tipos: Embutir, Compacta, Gas'),

    ('churrasqueria gourmet vidro', '100 - 1 mil', 'Alta', 1.36, 3.88,
     'Churrasqueira Vidro Temperado',
     'Churrasqueira vidro temperado. Controle visual do fogo e design moderno. Parcele em 10x.',
     'Linha Vidro Temperado',
     'Vidro temperado e acabamento inox',
     'Compra Segura',
     'Tipos: com Vidro, Embutir, Bancada'),

    ('churrasquerias gourmet', '10 mil - 100 mil', 'Alta', 1.52, 5.66,
     'Churrasqueiras Gourmet',
     'Linha completa de churrasqueiras gourmet: varios modelos e tamanhos. Parcele em 10x.',
     'Ver Catalogo Completo',
     'Todos os modelos gourmet',
     'Frete Gratis',
     'Tipos: Carvao, Gas, Eletrica, Coifa'),

    ('comprar churrasqueira', '1 mil - 10 mil', 'Alta', 0.33, 2.75,
     'Compre Sua Churrasqueira',
     'Pronta entrega, frete gratis e parcele em 10x sem juros. Compre agora e receba em casa.',
     'Compre Agora',
     'Frete gratis e entrega rapida',
     'Frete Gratis',
     'Tipos: Carvao, Gas, Eletrica, Coifa'),

    ('comprar churrasqueira eletrica', '100 - 1 mil', 'Alta', 0.24, 1.68,
     'Churrasqueira Eletrica',
     'Churrasqueira eletrica: sem carvao, sem gas, so ligar na tomada. Parcele em 10x sem juros.',
     'Churrasqueiras Eletricas',
     'Sem carvao, sem gas, facil de usar',
     'Pronta Entrega',
     'Tipos: Cooktop, Embutir, Compacta'),

    ('kit churrasqueira', '1 mil - 10 mil', 'Alta', 0.28, 1.82,
     'Kit Churrasqueira Completo',
     'Kit churrasqueira com tudo que voce precisa: coifa, grelha e acessorios. Parcele em 10x.',
     'Kit Gourmet Completo',
     'Tudo incluido, so instalar',
     'Frete Gratis',
     'Inclui: Coifa, Grelha, Acessorios'),

    ('kit churrasqueira gourmet', '1 mil - 10 mil', 'Alta', 1.02, 5.40,
     'Kit Churrasqueira Gourmet',
     'Kit gourmet premium com churrasqueira, coifa inox e grelhas. Transforma sua area. Parcele.',
     'Kit Gourmet Completo',
     'Transforma sua area gourmet',
     'Parcele em 10x Sem Juros',
     'Inclui: Churrasqueira, Coifa, Grelha'),

    ('kit para churrasqueira de alvenaria', '100 - 1 mil', 'Alta', 0.19, 0.93,
     'Kit Churrasqueira Alvenaria',
     'Kit de acessorios para churrasqueira de alvenaria. Coifa, grelhas e acabamento em inox.',
     'Kits para Alvenaria',
     'Acessorios para churrasqueira',
     'Garantia 2 Anos',
     'Inclui: Coifa, Grelha, Acabamento'),

    ('lojas de churrasqueiras', '1 mil - 10 mil', 'Alta', 1.08, 2.84,
     'Loja Alvim Grill Oficial',
     'Mais de 10 anos especializados em churrasqueiras. Compre direto da loja oficial. Parcele.',
     'Sobre a Alvim Grill',
     'Especialistas ha mais de 10 anos',
     'Mais de 10 Anos',
     'Tipos: Carvao, Gas, Eletrica, Coifa'),

    ('churrasqueira de luxo', '100 - 1 mil', 'Alta', 1.08, 2.97,
     'Churrasqueira de Luxo Inox',
     'Churrasqueiras de luxo em inox 316L. Exclusividade e acabamento de alto padrao. Parcele.',
     'Linha Premium',
     'Exclusividade em inox 316L',
     'Garantia 2 Anos',
     'Tipos: Inox 316L, Embutir, Premium'),

    ('churrasqueira para apartamento', '10 mil - 100 mil', 'Alta', 0.23, 2.99,
     'Churrasqueira p/ Apartamento',
     'Churrasqueira para apartamento: modelos eletricos e a gas sem fumaca excessiva. Parcele.',
     'Modelos p/ Apartamento',
     'Gas e eletrica para espacos menores',
     'Pronta Entrega',
     'Tipos: Eletrica, Gas, Compacta'),

    ('churrasqueira a gas', '10 mil - 100 mil', 'Alta', 0.36, 2.42,
     'Churrasqueira a Gas Inox',
     'Churrasqueira a gas: acende em segundos, sem carvao e sem sujeira. Parcele em 10x.',
     'Churrasqueiras a Gas',
     'Acende rapido, sem carvao',
     'Frete Gratis',
     'Tipos: Embutir, Bancada, com Coifa'),

    ('comprar churrasqueira a gas', '10 - 100', 'Alta', 0.63, 4.86,
     'Compre Churrasqueira a Gas',
     'Compre churrasqueira a gas agora: frete gratis, parcele em 10x. Entrega em todo Brasil.',
     'Churrasqueiras a Gas',
     'Entrega rapida para todo o Brasil',
     'Frete Gratis',
     'Tipos: Embutir, Bancada, Premium'),

    ('churrasqueira comprar', '1 mil - 10 mil', 'Alta', 0.34, 2.79,
     'Compre Sua Churrasqueira',
     'Escolha seu modelo, parcele em 10x sem juros e receba em casa com frete gratis. Compre ja.',
     'Compre Agora',
     'Parcele sem juros, frete incluso',
     'Parcele em 10x Sem Juros',
     'Tipos: Carvao, Gas, Eletrica, Coifa'),

    ('comprar churrasqueira eletrica', '100 - 1 mil', 'Alta', 0.24, 1.70,
     'Churrasqueira Eletrica',
     'Churrasqueira eletrica p/ apartamento: sem fumaca, sem odor de gas. Parcele em 10x.',
     'Churrasqueiras Eletricas',
     'Ideal para apartamento e varanda',
     'Pronta Entrega',
     'Tipos: Cooktop, Embutir, Bancada'),

    ('churrasqueira eletrica de embutir', '1 mil - 10 mil', 'Alta', 0.73, 3.96,
     'Churrasqueira Eletrica Embutir',
     'Churrasqueira eletrica de embutir: design limpo, acabamento inox e facil de usar. Parcele.',
     'Modelos de Embutir',
     'Embutir em inox com design limpo',
     'Pronta Entrega',
     'Tipos: Embutir, Inox, Eletrica'),

    ('churrasqueira eletrica cooktop', '100 - 1 mil', 'Alta', 0.52, 2.28,
     'Churrasqueira Cooktop',
     'Churrasqueira cooktop: compacta, moderna e perfeita para apartamento. Parcele em 10x.',
     'Modelos Cooktop',
     'Compacta e moderna para apartamento',
     'Parcele em 10x Sem Juros',
     'Tipos: Cooktop, Eletrica, Compacta'),
]

# Verificar limites
print('=== VERIFICACAO DE LIMITES ===')
errors_found = False
for row in data:
    kw = row[0]
    title, desc, sitelink, sitelink_desc, callout = row[5], row[6], row[7], row[8], row[9]
    errs = []
    if len(title) > 30: errs.append(f'TITULO ({len(title)}): {title}')
    if len(desc) > 90: errs.append(f'DESC ({len(desc)}): {desc}')
    if len(sitelink) > 25: errs.append(f'SITELINK ({len(sitelink)}): {sitelink}')
    if len(sitelink_desc) > 35: errs.append(f'SITELINK_DESC ({len(sitelink_desc)}): {sitelink_desc}')
    if len(callout) > 25: errs.append(f'CALLOUT ({len(callout)}): {callout}')
    if errs:
        errors_found = True
        print(f'KW: {kw}')
        for e in errs: print(f'  !! {e}')

if not errors_found:
    print('Nenhum erro encontrado!')

# Escrever na planilha
print('\n=== ESCREVENDO NA PLANILHA ===')
for i, row_data in enumerate(data, start=2):
    kw, avg, comp, min_b, max_b, title, desc, sitelink, sitelink_desc, callout, snippet = row_data
    ws.cell(row=i, column=1, value=kw)
    ws.cell(row=i, column=2, value=avg)
    ws.cell(row=i, column=3, value=comp)
    ws.cell(row=i, column=4, value=min_b)
    ws.cell(row=i, column=5, value=max_b)
    ws.cell(row=i, column=6, value=f'=(D{i}+E{i})/2')
    ws.cell(row=i, column=7, value=title)
    ws.cell(row=i, column=8, value=desc)
    ws.cell(row=i, column=9, value=sitelink)
    ws.cell(row=i, column=10, value=sitelink_desc)
    ws.cell(row=i, column=11, value=callout)
    ws.cell(row=i, column=12, value=snippet)

wb.save('c:/Users/User/alvim_grill_ccos/dados/Palavras chave Alvim Grill.xlsx')
print(f'Salvo. {len(data)} linhas preenchidas.')
