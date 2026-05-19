---
name: persona
description: Analisa a persona ideal para uma campanha de tráfego pago. Faz as 4 perguntas estruturadas, extrai dores, termos de busca, argumentos de venda e negativos. Salva o documento em campanhas/personas/.
triggers:
  - /persona
  - analisar persona
  - análise de persona
  - persona ideal
---

# Skill: Análise de Persona — Alvim Grill

## Contexto

Ler antes de começar:
- `_contexto/empresa.md` — produtos, mercado, foco atual
- `_contexto/preferencias.md` — tom de voz

## Fluxo

### Passo 1 — Produto ou segmento

Perguntar:

> "Pra qual produto ou linha você quer fazer a análise de persona? (ex: churrasqueira a carvão, churrasqueira a gás, lareira, kit gourmet)"

Aguardar resposta. Usar como nome do arquivo gerado.

### Passo 2 — As 4 perguntas

Fazer uma por vez. Aguardar resposta completa antes de ir pra próxima.

**Pergunta 1:**
> "Qual problema esse produto resolve? Se resolve mais de um, cita todos."

**Pergunta 2:**
> "Como uma pessoa que tem esse problema pesquisaria no Google antes de comprar? Pensa nos termos que ela digitaria."

**Pergunta 3:**
> "Quais argumentos são mais fortes pra convencer essa pessoa de que a Alvim Grill é a melhor escolha? (ex: parcelamento, garantia, entrega, preço, qualidade, exclusividade)"

**Pergunta 4:**
> "Quais formas de pesquisar seriam ruins para esse produto — termos que trazem pessoas que não vão comprar? (ex: 'aluguel de', 'conserto de', 'como fazer')"

### Passo 3 — Análise dos sites dos concorrentes

Perguntar:

> "Me passa os sites dos principais concorrentes que você quer analisar."

Aguardar os URLs. Para cada site informado, fazer WebFetch e extrair:
- Como eles se posicionam (proposta de valor, tagline, diferencial principal)
- Quais argumentos de venda usam em destaque (parcelamento, garantia, entrega, preço, qualidade)
- Quais produtos têm em evidência e como descrevem
- Tom de voz e linguagem usada com o cliente
- Qualquer elemento de urgência ou escassez (estoque limitado, oferta por tempo, frete grátis condicionado)

Consolidar o que foi encontrado em uma análise comparativa antes de avançar:

> "Analisei os concorrentes. Aqui o que encontrei:
>
> **[Concorrente 1]:** [resumo em 2-3 linhas]
> **[Concorrente 2]:** [resumo em 2-3 linhas]
>
> Os argumentos mais usados por eles são: [lista]. Isso vai alimentar os argumentos de venda da persona."

### Passo 4 — Análise e geração do documento

Com as 4 respostas + análise dos concorrentes, processar e estruturar:

**Dores:** extrair os problemas reais por trás das respostas da Pergunta 1. Ir além do literal — identificar o desejo subjacente (status, praticidade, reunir família, etc.).

**Termos de busca:** organizar os termos da Pergunta 2 em dois grupos:
- Alta intenção de compra (ex: "comprar churrasqueira a gás", "churrasqueira gourmet preço")
- Média/baixa intenção (ex: "churrasqueira a gás", "tipos de churrasqueira")

**Argumentos de venda / gatilhos:** listar os argumentos da Pergunta 3, priorizando os mais fortes pra copy de anúncio.

**Palavras-chave negativas:** consolidar a lista da Pergunta 4 + adicionar negativos padrão do mercado:
- de graça, grátis, gratis, gratuito
- como fazer, como montar, como instalar, faça você mesmo, DIY
- aluguel, alugar
- conserto, manutenção, reparo, assistência técnica
- usado, segunda mão, seminovo
- planta, projeto, planta baixa

### Passo 5 — Salvar

Salvar o documento em `campanhas/personas/[nome-do-produto].md` com o seguinte formato:

```markdown
# Persona — [Produto]

**Data:** [data atual]

## Dores identificadas

[lista das dores reais, além do literal]

## Nível de consciência

[descrever em 2-3 linhas onde essa persona provavelmente está no funil — já conhece o produto? Só conhece o problema? Está comparando opções?]

## Termos de busca

### Alta intenção de compra
[lista]

### Média / baixa intenção
[lista]

## Argumentos de venda

[lista priorizada — os mais fortes primeiro]

## Palavras-chave negativas

### Padrão (aplicar em toda campanha)
- de graça, grátis, gratis, gratuito
- como fazer, como montar, faça você mesmo, DIY
- aluguel, alugar
- conserto, manutenção, reparo, assistência técnica
- usado, segunda mão, seminovo
- planta, projeto, planta baixa

### Específicas desse produto
[lista vinda da Pergunta 4]

## Análise competitiva dos sites

[para cada concorrente analisado: proposta de valor, argumentos em destaque, tom de voz, diferenciais]

## O que fazer diferente

[com base na análise dos concorrentes, quais argumentos a Alvim Grill pode usar que eles não estão usando ou estão usando mal]

## Observações para copy

[2-3 pontos práticos sobre o que ressaltar nos anúncios com base na análise]
```

Depois de salvar, confirmar:

> "Persona salva em `campanhas/personas/[nome-do-produto].md`. Quer usar ela agora pra montar a estrutura da campanha Google Ads?"

## Regras

- Uma pergunta por vez. Não listar as 4 de uma vez.
- Se a resposta for vaga, fazer uma pergunta de acompanhamento antes de continuar.
- Não inventar dores ou argumentos. Usar apenas o que o usuário informou.
- O documento deve ser acionável — alguém deve conseguir montar uma campanha lendo só ele.
