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

## Fluxo

### Passo 1 — Produto e persona

Perguntar:

> "Pra qual produto é essa campanha? (ex: churrasqueira a carvão, churrasqueira a gás, lareira, kit gourmet)"

Verificar se existe `campanhas/personas/[produto].md`. Se existir, ler e confirmar:

> "Encontrei a análise de persona pra esse produto. Vou usar ela como base. Pode seguir."

Se não existir:

> "Não tem análise de persona pra esse produto ainda. Recomendo rodar `/persona` primeiro — leva 5 minutos e alimenta toda a estrutura da campanha. Quer fazer agora ou continuar sem ela?"

### Passo 2 — Dados do SpyFu

> "Cola aqui os dados que você coletou no SpyFu. Quero: principais concorrentes identificados, keywords de tráfego pago que eles usam e keywords orgânicas relevantes que apareceram."

Aguardar. Se o usuário ainda não fez a pesquisa:

> "Acessa o spyfu.com, digita alvimgrill.com.br, e me traz: os principais concorrentes que aparecem + as keywords de paid e organic que eles destacam."

### Passo 3 — Análise competitiva de anúncios

> "Agora me passa o que você viu na biblioteca de anúncios do Google nos concorrentes: títulos que eles usam, gatilhos (parcelamento, garantia, entrega, etc.) e qualquer padrão de copy que apareceu mais de uma vez."

Aguardar. Extrair e listar internamente:
- Títulos recorrentes
- Gatilhos identificados
- Padrões de copy

### Passo 4 — Geração da estrutura

Com persona + SpyFu + análise competitiva, gerar a estrutura completa.

#### 4.1 — Keywords por grupo de anúncio (mesmo tema)

Agrupar as keywords em conjuntos temáticos. Cada grupo deve ter keywords que descrevem o mesmo produto/intenção. Exemplo:

- **Grupo: Churrasqueira a Gás** → churrasqueira a gás, churrasqueira gás, churrasqueira a gás inox, churrasqueira a gás embutir
- **Grupo: Churrasqueira Gourmet** → churrasqueira gourmet, churrasqueira gourmet embutir, kit churrasqueira gourmet

Usar tipos de correspondência:
- Correspondência de frase: "churrasqueira a gás"
- Correspondência exata: [comprar churrasqueira a gás]

#### 4.2 — Separação por funil (campanhas distintas)

Separar os grupos em duas campanhas:

**Campanha 1 — Alta intenção** (termos com intenção de compra clara)
Exemplos: "comprar churrasqueira", "churrasqueira preço", "churrasqueira onde comprar", "melhor churrasqueira"

**Campanha 2 — Média intenção** (termos mais genéricos, ainda relevantes)
Exemplos: "churrasqueira a gás", "churrasqueira gourmet", "tipos de churrasqueira"

#### 4.3 — Anúncios responsivos de pesquisa (RSA)

Para cada grupo, gerar:

**Títulos (até 15, máx 30 caracteres cada):**
- Incluir a keyword principal do grupo em pelo menos 2 títulos
- Incluir os gatilhos identificados (parcelamento, frete, garantia)
- Incluir CTA (Compre Agora, Peça o Seu, Confira)
- Variar entre benefício, urgência e credencial

**Descrições (até 4, máx 90 caracteres cada):**
- Desenvolver as dores + argumentos de venda da persona
- Uma descrição focada em benefício emocional
- Uma focada em argumentos racionais (parcelamento, garantia, frete)

#### 4.4 — Extensões

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
