---
name: campanha-google
description: Guia o processo completo de criação de campanha Google Ads para a Alvim Grill. Lê a persona salva, coleta dados de SpyFu e da biblioteca de anúncios, gera estrutura completa com keywords, anúncios e extensões, agrupa por tema e funil, e gera lista de negativos.
triggers:
  - /campanha-google
  - criar campanha google
  - nova campanha google
  - campanha google ads
---

# Skill: Criação de Campanha Google Ads — Alvim Grill

## Contexto

Ler antes de começar:
- `_contexto/empresa.md`
- `_contexto/preferencias.md`
- `dados/[iAzazelOfc] - Cap3_Aula4_Prompt para buscar ideias de palavra chave.docx` — prompt de pesquisa de keywords (usar na etapa de SpyFu para expandir ideias)
- `dados/Mod1_Cap5_Aula9_Ideias_do_que_Pesquisar.pdf` — 8 categorias de ideias de keyword (aplicar como checklist de cobertura antes de fechar a lista)
- `dados/[iAzazelOfc] - Mod3_Cap3_Aula4_Checklist para Criação de Anúncio_DOCX.docx` — checklist de criação de anúncio (seguir antes de gerar os RSAs)
- `dados/[iAzazelOfc] - Mod3_Cap3_Aula5_Frameworks para Criação de Anúncios_DOCX.docx` — 6 frameworks de copy (usar para montar títulos e descrições)

## Fluxo

### Passo 1 — Produto e persona

Perguntar:

> "Pra qual produto é essa campanha? (ex: churrasqueira a carvão, churrasqueira a gás, lareira, kit gourmet)"

Verificar se existe `campanhas/personas/[produto].md`. Se existir, ler e confirmar:

> "Encontrei a análise de persona pra esse produto. Vou usar ela como base. Pode seguir."

Se não existir:

> "Não tem análise de persona pra esse produto ainda. Recomendo rodar `/persona` primeiro — leva 5 minutos e alimenta toda a estrutura da campanha. Quer fazer agora ou continuar sem ela?"

### Passo 2 — Pesquisa de keywords (SpyFu + expansão)

> "Cola aqui os dados que você coletou no SpyFu. Quero: principais concorrentes identificados, keywords de tráfego pago que eles usam e keywords orgânicas relevantes que apareceram."

Aguardar. Se o usuário ainda não fez a pesquisa:

> "Acessa o spyfu.com, digita alvimgrill.com.br, e me traz: os principais concorrentes que aparecem + as keywords de paid e organic que eles destacam."

Com os dados do SpyFu em mãos, aplicar os dois frameworks de pesquisa:

**Framework 1 — Prompt Gianini** (`dados/[iAzazelOfc] - Cap3_Aula4_Prompt para buscar ideias de palavra chave.docx`):
- Entender o produto e os problemas que ele resolve
- Gerar até 50 ideias de como as pessoas pesquisam antes de comprar
- Organizar em tabela por relevância e tipo de relação (produto direto, solução de problema, desejo)
- Filtrar apenas keywords com alta intenção de compra

**Framework 2 — 8 Categorias de Ideias** (`dados/Mod1_Cap5_Aula9_Ideias_do_que_Pesquisar.pdf`):
Usar como checklist para garantir cobertura completa de keywords. Para cada categoria, levantar termos específicos da Alvim Grill:

1. **Marca própria** — "Alvim Grill", "alvimgrill"
2. **Solução própria** — nomes dos produtos (churrasqueira, lareira, kit gourmet, coifa)
3. **Marcas concorrentes** — nomes das marcas identificadas no SpyFu
4. **Solução dos concorrentes** — produtos e modelos que os concorrentes vendem
5. **Variações de busca do cliente** — formas diferentes que o cliente usa para pesquisar o mesmo produto (ex: "churrasqueira de chão", "fogão a lenha gourmet", "parrilla")
6. **Problemas que a persona quer resolver** — churrasquear em apartamento, fumaça, espaço pequeno, presente para o pai
7. **Desejos e metas** — área gourmet dos sonhos, reunir família, churrasco premium, casa nova
8. **Concorrentes por solução (não diretos)** — produtos que a persona compra no lugar do seu (ex: fogão a lenha, forno a lenha, grelha portátil)

Ao final, consolidar todas as keywords levantadas e filtrar as que têm baixíssima intenção de compra antes de avançar.

### Passo 3 — Análise competitiva de anúncios

> "Agora me passa o que você viu na biblioteca de anúncios do Google nos concorrentes: títulos que eles usam, gatilhos (parcelamento, garantia, entrega, etc.) e qualquer padrão de copy que apareceu mais de uma vez."

Aguardar. Extrair e listar internamente:
- Títulos recorrentes
- Gatilhos identificados
- Padrões de copy

### Passo 4 — Geração da estrutura

Com persona + SpyFu + análise competitiva, gerar a estrutura completa.

#### 4.1 — Separação por nível de funil (campanhas distintas)

Antes de agrupar por tema, classificar cada keyword pelo nível de intenção de compra. Isso define em qual campanha ela vai.

**Campanha 1 — Alta intenção** (sinal claro de compra: "comprar", "preço", "onde comprar", "loja de")
Exemplos: "comprar churrasqueira", "churrasqueira preço", "lojas de churrasqueiras", "churrasqueira onde comprar"
Lance: mais agressivo — são as pessoas mais próximas de fechar.

**Campanha 2 — Média intenção** (sabe o que quer, está pesquisando, mas ainda não sinalizou compra)
Exemplos: "churrasqueira a gás", "churrasqueira gourmet completa", "kit churrasqueira", "churrasqueira para apartamento"
Lance: moderado.

**Campanha 3 — Baixa intenção** (termo genérico, volume alto, intenção indefinida)
Exemplos: "churrasqueira", "lareiras", termos sem qualificador de produto ou ação
Lance: conservador — volume alto mas conversão mais difícil.

Regra prática para classificar:
- Tem "comprar", "preço", "loja", "onde comprar" → Campanha 1
- Tem qualificador de produto (modelo, material, uso) mas sem sinal de compra → Campanha 2
- Termo isolado, sem qualificador → Campanha 3

#### 4.2 — Agrupamento por tema (conjuntos de anúncios)

Dentro de cada campanha, agrupar keywords que descrevem o mesmo produto ou intenção. Cada conjunto deve ter keywords tão parecidas que o mesmo anúncio serve bem para todas.

**Critério de agrupamento:** keywords do mesmo conjunto devem compartilhar o tema central. Se a pessoa pesquisou "churrasqueira elétrica de embutir" ou "churrasqueira elétrica cooktop", as duas estão buscando churrasqueira elétrica — mesmo conjunto. Mas "churrasqueira gourmet" e "churrasqueira elétrica" são temas diferentes — conjuntos separados.

Exemplos de conjuntos para a Alvim Grill:
- **Churrasqueira Gourmet** → churrasqueira gourmet, churrasqueiras gourmet, churrasqueira gourmet completa, churrasqueira gourmet vidro, churrasqueira para área gourmet, churrasqueiras para varanda gourmet
- **Churrasqueira Elétrica** → churrasqueira elétrica de embutir, churrasqueira elétrica cooktop
- **Churrasqueira a Gás** → churrasqueira a gás, churrasqueira gás inox
- **Churrasqueira para Apartamento** → churrasqueira para apartamento, churrasqueira carvão apartamento, churrasqueira pequena
- **Kit Churrasqueira** → kit churrasqueira, kit churrasqueira gourmet, kit para churrasqueira de alvenaria
- **Alvenaria e Tijolinho** → churrasqueira alvenaria, churrasqueira de tijolinho

Usar tipos de correspondência:
- Correspondência de frase: "churrasqueira a gás"
- Correspondência exata: [comprar churrasqueira a gás]

Apresentar a estrutura completa antes de criar os anúncios:

> "Aqui a estrutura que montei:
>
> **Campanha 1 — Alta Intenção**
> - Conjunto: [nome] → [keywords]
> - Conjunto: [nome] → [keywords]
>
> **Campanha 2 — Média Intenção**
> - Conjunto: [nome] → [keywords]
> - ...
>
> **Campanha 3 — Baixa Intenção**
> - Conjunto: [nome] → [keywords]
>
> Confirma essa estrutura ou quer ajustar algum conjunto antes de criar os anúncios?"

Aguardar confirmação antes de avançar para os anúncios.

#### 4.3 — Checklist antes de criar os anúncios

Antes de gerar qualquer título ou descrição, preencher o checklist do arquivo `dados/[iAzazelOfc] - Mod3_Cap3_Aula4_Checklist para Criação de Anúncio_DOCX.docx`:

1. Para qual keyword (ou grupo temático) será criado esse anúncio?
2. Quais argumentos/gatilhos os anúncios nas primeiras posições estão usando? (ordem de empilhamento)
3. Quais gatilhos os sites dos anúncios usam na primeira dobra?
4. Quais gatilhos são mais importantes para a Alvim Grill usar?
5. Qual o empilhamento de gatilhos mais poderoso para esse grupo?

Só depois de responder o checklist, gerar os anúncios.

#### 4.4 — Anúncios responsivos de pesquisa (RSA)

Para cada grupo, escolher o framework mais adequado do arquivo `dados/[iAzazelOfc] - Mod3_Cap3_Aula5_Frameworks para Criação de Anúncios_DOCX.docx`:

- **Framework 3 (Dor):** para keywords onde a persona compra movida por uma dor clara (ex: não consegue churrasquear no apartamento)
- **Framework 4 (Desejo):** para keywords onde o desejo/sonho é o motor (ex: churrasqueira gourmet, área premium)
- **Framework 5 (Benefícios):** para keywords onde os ganhos práticos vencem (ex: kit completo, praticidade)
- **Framework 6 (Urgência):** para keywords de alta intenção de compra (ex: comprar churrasqueira, churrasqueira preço)

Aplicar o framework escolhido na estrutura:

**Títulos (até 15, máx 30 caracteres cada):**
- Pelo menos 2 títulos com a keyword principal ou variante aproximada
- Gatilhos em ordem de prioridade definida no checklist
- CTA em pelo menos 1 título (Compre Agora, Peça o Seu, Confira)
- Informar o número de caracteres de cada título gerado

**Descrições (até 4, máx 90 caracteres cada):**
- Aprofundar os gatilhos dos títulos, do mais forte para o mais fraco
- Uma descrição focada em dor/desejo da persona
- Uma focada em argumentos racionais (parcelamento, garantia, frete)
- Informar o número de caracteres de cada descrição gerada

#### 4.5 — Extensões

**Sitelinks (mínimo 4):**
Cada sitelink: título (máx 25 chars) + 2 descrições (máx 35 chars cada)
Sugestões base: Ver Catálogo Completo, Frete para Todo Brasil, Parcele em Até 10x, Fale com Especialista

**Snippets estruturados:**
Cabeçalho: Tipos → listar os produtos da linha (ex: A Carvão, A Gás, Elétrica, Gourmet)

**Mensagens (callouts):**
Frases curtas de até 25 caracteres destacando diferenciais. Exemplos: Frete Grátis, Garantia 2 Anos, Entrega Rápida, Compra Segura

### Passo 5 — Validação com Keyword Planner

Se o Google Ads Ratos estiver instalado (`~/.claude/skills/google-ads-ratos`), usar o subcomando de Keyword Planner pra buscar volume, concorrência e lances estimados de cada grupo. Adicionar os dados à estrutura.

Se não estiver instalado:

> "Pra automatizar a etapa do Keyword Planner (volume de busca, CPC estimado, lances), instale o Google Ads Ratos:
> `git clone https://github.com/duduesh/google-ads-ratos ~/.claude/skills/google-ads-ratos`
> Por enquanto, preencha manualmente no Google Ads → Ferramentas → Planejador de palavras-chave."

### Passo 6 — Lista de negativos

Consolidar a lista de negativos padrão + específicos do produto (vindos da persona ou da análise competitiva):

**Padrão:**
de graça, grátis, gratis, gratuito, como fazer, como montar, faça você mesmo, DIY, aluguel, alugar, conserto, manutenção, reparo, assistência técnica, usado, segunda mão, seminovo, planta, projeto, planta baixa, curso, aula

**Específicos do produto:**
[extrair da persona salva ou perguntar ao usuário]

### Passo 7 — Salvar

Salvar em `campanhas/google/[produto]-[data]/estrutura.md` com o seguinte formato:

```markdown
# Campanha Google Ads — [Produto]
**Data:** [data]
**Baseada na persona:** [sim/não — arquivo usado]

---

## Campanha 1 — Alta Intenção

### Grupo: [Nome do Grupo]
**Keywords:**
- [correspondência de frase]
- [correspondência exata]

**Títulos:**
1. [título]
...

**Descrições:**
1. [descrição]
...

---

## Campanha 2 — Média Intenção

[mesma estrutura]

---

## Extensões

### Sitelinks
[lista]

### Snippets estruturados
[lista]

### Mensagens (callouts)
[lista]

---

## Palavras-chave negativas

### Padrão
[lista]

### Específicas
[lista]

---

## Notas para configuração na plataforma

[observações práticas sobre lances, orçamento inicial sugerido, configurações recomendadas com base no que foi analisado]
```

Depois de salvar, confirmar:

> "Estrutura salva em `campanhas/google/[produto]-[data]/estrutura.md`. Quer criar agora a campanha do Meta Ads com base nessa mesma análise?"

## Regras

- Não inventar keywords, títulos ou gatilhos. Usar só o que veio da persona, SpyFu e análise competitiva.
- Títulos devem ter no máximo 30 caracteres. Descriptions no máximo 90. Avisar se estiver próximo do limite.
- Sempre separar em Campanha 1 (alta intenção) e Campanha 2 (média intenção).
- Sempre gerar a lista de negativos completa antes de finalizar.
