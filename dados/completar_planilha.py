import openpyxl

wb = openpyxl.load_workbook('c:/Users/User/alvim_grill_ccos/dados/Palavras chave Alvim Grill.xlsx')
ws = wb.active

# Dados completos para cada keyword
# Formato: (keyword, avg_searches, competition, min_bid, max_bid, title, description, sitelink, sitelink_desc, callout, snippet)
data = [
    ('churrasqueira', '100 mil - 1 mi', 'Alta', 0.23, 2.37,
     'Churrasqueira Gourmet Premium',
     'Modelos a carvao, gas e eletrico. Parcele em 10x sem juros. Frete gratis.',
     'Ver Catalogo Completo', 'Veja todos os modelos disponiveis',
     'Frete Gratis', 'Tipos: Carvao, Gas, Eletrica, Coifa'),

    ('churrasqueira alvenaria', '1 mil - 10 mil', 'Alta', 0.52, 2.75,
     'Kit Churrasqueira Alvenaria',
     'Kits de alvenaria completos com coifa. Mais de 10 anos no mercado. Parcele sem juros.',
     'Kit Gourmet Completo', 'Churrasqueira + coifa + acessorios',
     'Parcele em 10x Sem Juros', 'Tipos: Carvao, Gas, Eletrica, Coifa'),

    ('churrasqueira carvao apartamento', '1 mil - 10 mil', 'Alta', 0.26, 2.94,
     'Churrasqueira p/ Apartamento',
     'Churrasqueiras compactas para apartamento. Sem fumaca. Pronta entrega. Parcele sem juros.',
     'Modelos para Apartamento', 'Churrasqueiras compactas sem fumaca',
     'Pronta Entrega', 'Tipos: Carvao, Gas, Eletrica, Coifa'),

    ('churrasqueira de tijolinho', '10 mil - 100 mil', 'Alta', 0.20, 1.43,
     'Churrasqueira de Tijolinho',
     'Kits de churrasqueira de tijolinho com coifa. Qualidade e durabilidade. Parcele em 10x.',
     'Kit Gourmet Completo', 'Tudo que voce precisa incluido',
     'Garantia 2 Anos', 'Tipos: Carvao, Gas, Eletrica, Coifa'),

    ('churrasqueira gourmet a carvao', '100 - 1 mil', 'Alta', 0.85, 3.28,
     'Churrasqueira Gourmet Carvao',
     'Churrasqueiras gourmet a carvao premium. Parcele em 10x sem juros. Frete gratis.',
     'Churrasqueiras Gourmet', 'Modelos premium para area gourmet',
     'Frete Gratis', 'Tipos: Carvao, Gas, Eletrica, Coifa'),

    ('churrasqueira gourmet completa', '100 - 1 mil', 'Alta', 1.15, 4.48,
     'Churrasqueira Gourmet Completa',
     'Kit gourmet completo: churrasqueira, coifa e acessorios. Parcele em 10x sem juros.',
     'Kit Gourmet Completo', 'Churrasqueira + coifa + acessorios',
     'Parcele em 10x Sem Juros', 'Tipos: Carvao, Gas, Eletrica, Coifa'),

    ('churrasqueira gourmet vidro', '100 - 1 mil', 'Alta', 1.36, 3.88,
     'Churrasqueira Gourmet Vidro',
     'Churrasqueiras gourmet com vidro temperado. Design moderno. Parcele em 10x sem juros.',
     'Ver Catalogo Completo', 'Todos os modelos disponiveis',
     'Compra Segura', 'Tipos: Carvao, Gas, Eletrica, Coifa'),

    ('churrasqueira para area gourmet', '1 mil - 10 mil', 'Alta', 0.76, 2.88,
     'Churrasqueira Area Gourmet',
     'Churrasqueiras premium para area gourmet. Modelos embutidos e de bancada. Pronta entrega.',
     'Modelos de Embutir', 'Para embutir na bancada gourmet',
     'Pronta Entrega', 'Tipos: Carvao, Gas, Eletrica, Coifa'),

    ('churrasqueira pequena', '10 mil - 100 mil', 'Alta', 0.14, 0.89,
     'Churrasqueira Pequena Premium',
     'Churrasqueiras compactas para apartamento e varanda. Parcele em 10x sem juros.',
     'Modelos para Apartamento', 'Churrasqueiras compactas sem fumaca',
     'Frete Gratis', 'Tipos: Carvao, Gas, Eletrica, Coifa'),

    ('churrasqueira pre moldada preco', '100 mil - 1 mi', 'Alta', 0.20, 1.20,
     'Churrasqueira Pre-Moldada',
     'Churrasqueiras pre-moldadas com melhor preco do mercado. Parcele em 10x sem juros.',
     'Ver Catalogo Completo', 'Todos os modelos disponiveis',
     'Melhor Preco', 'Tipos: Carvao, Gas, Eletrica, Coifa'),

    ('churrasqueiras para varanda gourmet', '100 - 1 mil', 'Alta', 1.07, 3.50,
     'Churrasqueira para Varanda',
     'Churrasqueiras p/ varanda gourmet. Modelos sob medida. Pronta entrega. Parcele sem juros.',
     'Churrasqueiras Gourmet', 'Modelos premium para area gourmet',
     'Pronta Entrega', 'Tipos: Carvao, Gas, Eletrica, Coifa'),

    ('churrasqueria gourmet vidro', '100 - 1 mil', 'Alta', 1.36, 3.88,
     'Churrasqueira Gourmet Vidro',
     'Churrasqueiras gourmet com vidro temperado. Design moderno. Parcele em 10x sem juros.',
     'Ver Catalogo Completo', 'Todos os modelos disponiveis',
     'Compra Segura', 'Tipos: Carvao, Gas, Eletrica, Coifa'),

    ('churrasquerias gourmet', '10 mil - 100 mil', 'Alta', 1.52, 5.66,
     'Churrasqueiras Gourmet',
     'Churrasqueiras gourmet premium. Parcele em 10x sem juros. Frete gratis para todo Brasil.',
     'Ver Catalogo Completo', 'Todos os modelos disponiveis',
     'Frete Gratis', 'Tipos: Carvao, Gas, Eletrica, Coifa'),

    ('comprar churrasqueira', '1 mil - 10 mil', 'Alta', 0.33, 2.75,
     'Compre Sua Churrasqueira',
     'Compre agora com frete gratis. Parcele em 10x sem juros. Pronta entrega para todo Brasil.',
     'Frete Gratis Brasil', 'Entrega rapida para todo o Brasil',
     'Frete Gratis', 'Tipos: Carvao, Gas, Eletrica, Coifa'),

    ('comprar churrasqueira eletrica', '100 - 1 mil', 'Alta', 0.24, 1.68,
     'Churrasqueira Eletrica',
     'Compre sua churrasqueira eletrica. Modelos embutir e cooktop. Parcele em 10x sem juros.',
     'Churrasqueiras Eletricas', 'Modelos de embutir e cooktop',
     'Pronta Entrega', 'Tipos: Carvao, Gas, Eletrica, Coifa'),

    ('kit churrasqueira', '1 mil - 10 mil', 'Alta', 0.28, 1.82,
     'Kit Churrasqueira Completo',
     'Kit churrasqueira completo com tudo incluso. Parcele em 10x sem juros. Frete gratis.',
     'Kit Gourmet Completo', 'Churrasqueira + coifa + acessorios',
     'Frete Gratis', 'Tipos: Carvao, Gas, Eletrica, Coifa'),

    ('kit churrasqueira gourmet', '1 mil - 10 mil', 'Alta', 1.02, 5.40,
     'Kit Churrasqueira Gourmet',
     'Kit gourmet para sua area. Churrasqueira + coifa + acessorios. Parcele em 10x sem juros.',
     'Kit Gourmet Completo', 'Churrasqueira + coifa + acessorios',
     'Parcele em 10x Sem Juros', 'Tipos: Carvao, Gas, Eletrica, Coifa'),

    ('kit para churrasqueira de alvenaria', '100 - 1 mil', 'Alta', 0.19, 0.93,
     'Kit Churrasqueira Alvenaria',
     'Kit para churrasqueira de alvenaria com coifa e acessorios. Parcele em 10x sem juros.',
     'Kit Gourmet Completo', 'Tudo que voce precisa incluido',
     'Garantia 2 Anos', 'Tipos: Carvao, Gas, Eletrica, Coifa'),

    ('lojas de churrasqueiras', '1 mil - 10 mil', 'Alta', 1.08, 2.84,
     'Loja Alvim Grill Oficial',
     'Loja especializada em churrasqueiras ha mais de 10 anos. Parcele em 10x sem juros.',
     'Ver Catalogo Completo', 'Todos os modelos disponiveis',
     'Mais de 10 Anos', 'Tipos: Carvao, Gas, Eletrica, Coifa'),

    ('churrasqueira de luxo', '100 - 1 mil', 'Alta', 1.08, 2.97,
     'Churrasqueira de Luxo Inox',
     'Churrasqueiras de luxo em inox 316L. Modelos exclusivos. Parcele em 10x sem juros.',
     'Churrasqueiras Premium', 'Modelos exclusivos Inox 316L',
     'Garantia 2 Anos', 'Tipos: Carvao, Gas, Eletrica, Coifa'),

    ('churrasqueira para apartamento', '10 mil - 100 mil', 'Alta', 0.23, 2.99,
     'Churrasqueira p/ Apartamento',
     'Churrasqueiras compactas para apartamento. Sem fumaca. Pronta entrega. Parcele sem juros.',
     'Modelos para Apartamento', 'Churrasqueiras compactas sem fumaca',
     'Pronta Entrega', 'Tipos: Carvao, Gas, Eletrica, Coifa'),

    ('churrasqueira a gas', '10 mil - 100 mil', 'Alta', 0.36, 2.42,
     'Churrasqueira a Gas Inox',
     'Churrasqueiras a gas premium em inox. Praticidade e eficiencia. Parcele em 10x sem juros.',
     'Churrasqueiras a Gas', 'Modelos premium em inox',
     'Frete Gratis', 'Tipos: Carvao, Gas, Eletrica, Coifa'),

    ('comprar churrasqueira a gas', '10 - 100', 'Alta', 0.63, 4.86,
     'Compre Churrasqueira a Gas',
     'Compre sua churrasqueira a gas agora. Frete gratis. Parcele em 10x sem juros.',
     'Churrasqueiras a Gas', 'Modelos premium em inox',
     'Frete Gratis', 'Tipos: Carvao, Gas, Eletrica, Coifa'),

    ('churrasqueira comprar', '1 mil - 10 mil', 'Alta', 0.34, 2.79,
     'Compre Sua Churrasqueira',
     'Compre sua churrasqueira com frete gratis. Parcele em 10x sem juros. Pronta entrega.',
     'Frete Gratis Brasil', 'Entrega rapida para todo o Brasil',
     'Frete Gratis', 'Tipos: Carvao, Gas, Eletrica, Coifa'),

    ('comprar churrasqueira eletrica', '100 - 1 mil', 'Alta', 0.24, 1.70,
     'Churrasqueira Eletrica',
     'Compre sua churrasqueira eletrica. Modelos embutir e cooktop. Parcele em 10x sem juros.',
     'Churrasqueiras Eletricas', 'Modelos de embutir e cooktop',
     'Pronta Entrega', 'Tipos: Carvao, Gas, Eletrica, Coifa'),

    ('churrasqueira eletrica de embutir', '1 mil - 10 mil', 'Alta', 0.73, 3.96,
     'Churrasqueira Eletrica Embutir',
     'Churrasqueiras eletricas para embutir. Design elegante. Parcele em 10x sem juros.',
     'Churrasqueiras Eletricas', 'Modelos de embutir e cooktop',
     'Pronta Entrega', 'Tipos: Carvao, Gas, Eletrica, Coifa'),

    ('churrasqueira eletrica cooktop', '100 - 1 mil', 'Alta', 0.52, 2.28,
     'Churrasqueira Cooktop',
     'Churrasqueiras eletricas cooktop. Compactas para apartamento. Parcele em 10x sem juros.',
     'Churrasqueiras Eletricas', 'Modelos de embutir e cooktop',
     'Parcele em 10x Sem Juros', 'Tipos: Carvao, Gas, Eletrica, Coifa'),
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
    print('Nenhum erro de limite encontrado!')

# Escrever dados na planilha
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

# Salvar
output_path = 'c:/Users/User/alvim_grill_ccos/dados/Palavras chave Alvim Grill.xlsx'
wb.save(output_path)
print(f'Planilha salva em: {output_path}')
print(f'Total de linhas preenchidas: {len(data)}')
