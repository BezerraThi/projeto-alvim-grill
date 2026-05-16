---
name: campanha-meta
description: Guia a criação de campanha Meta Ads para a Alvim Grill. Analisa os criativos dos concorrentes na biblioteca do Meta, gera brief de criativos baseado nos que estão performando e cria títulos e descrições com as dores e gatilhos mapeados.
triggers:
  - /campanha-meta
  - criar campanha meta
  - nova campanha meta
  - campanha facebook
  - campanha instagram
---

# Skill: Criação de Campanha Meta Ads — Alvim Grill

## Contexto

Ler antes de começar:
- `_contexto/empresa.md`
- `_contexto/preferencias.md`

## Fluxo

### Passo 1 — Produto e persona

Perguntar:

> "Pra qual produto é essa campanha Meta?"

Verificar se existe `campanhas/personas/[produto].md`. Se existir, ler e confirmar:

> "Vou usar a análise de persona salva pra esse produto como base pros textos."

Se não existir, sugerir:

> "Não tem persona pra esse produto. Recomendo rodar `/persona` primeiro. Quer fazer agora ou continuar sem ela?"

Verificar também se existe `campanhas/google/[produto]*/estrutura.md`. Se existir, ler — os gatilhos e argumentos de venda já mapeados ali servem diretamente pro Meta.

### Passo 2 — Análise de criativos dos concorrentes

> "Me passa o que você viu na Biblioteca de Anúncios do Meta nos concorrentes. Pra cada criativo relevante, me diz:
> - O que aparece no criativo (imagem, vídeo, o que está sendo mostrado)
> - Quanto tempo está no ar (data de publicação)
> - Em quantos conjuntos de anúncios esse criativo está sendo usado
> - Qualquer texto, headline ou CTA que aparece no anúncio"

Aguardar. Se o usuário ainda não fez a pesquisa:

> "Acessa facebook.com/ads/library, filtra por 'Todos os anúncios' e busca pelos concorrentes que você identificou no SpyFu. Usa o filtro de 'mais visualizações' pra ver o que está performando. Traz aqui o que encontrar."

Com os dados, extrair e listar internamente:
- Criativos com maior tempo no ar (indicam que estão funcionando)
- Criativos em mais conjuntos de anúncios (indicam escala)
- Padrões visuais recorrentes (produto isolado, produto em uso, comparativo, depoimento)
- Gatilhos de copy mais usados

### Passo 3 — Brief de criativos

Com base na análise, gerar o brief dos criativos a replicar. Para cada tipo de criativo identificado:

```
## Criativo [N] — [Tipo]

**Por que funciona:** [o que indica que esse formato está performando — tempo no ar, escala]
**Formato:** [imagem estática / vídeo / carrossel]
**O que mostrar:** [descrição visual objetiva do que colocar no criativo]
**Referência:** [qual concorrente usou e o que exatamente eles fizeram]
**Texto sobreposto (se houver):** [copy que aparece na imagem/vídeo]
```

Gerar no mínimo 3 briefs de criativos diferentes, em ordem de prioridade (o que tem mais evidência de performance primeiro).

### Passo 4 — Textos dos anúncios

Para cada brief de criativo, gerar os textos do anúncio:

**Texto principal (até 125 caracteres recomendados, máx 500):**
- Começar com a dor ou desejo da persona
- Conectar com o produto
- Fechar com CTA ou argumento de urgência

**Título (até 40 caracteres):**
- Direto, com benefício ou gatilho principal
- Testar pelo menos 2 variações por criativo

**Descrição (até 30 caracteres):**
- Reforço do argumento principal ou CTA secundário

Usar os gatilhos identificados na persona e na análise competitiva. Priorizar os que apareceram mais de uma vez nos concorrentes.

### Passo 5 — Estrutura da campanha

Definir a estrutura básica:

**Objetivo:** Vendas (otimização para compra no site)

**Público:**
- Interesses relacionados: churrasqueira, churrasco, área gourmet, decoração, casa e jardim
- Faixa etária sugerida com base no produto: [ajustar conforme produto]
- Excluir: pessoas que já compraram (remarketing separado)

**Conjuntos de anúncios sugeridos:**
1. Público frio — interesses amplos
2. Público frio — interesses específicos (churrasqueira, gourmet)
3. Lookalike de compradores (quando houver base)

### Passo 6 — Salvar

Salvar em `campanhas/meta/[produto]-[data]/estrutura.md` com o seguinte formato:

```markdown
# Campanha Meta Ads — [Produto]
**Data:** [data]
**Baseada na persona:** [sim/não]

---

## Análise competitiva

### Padrões de criativo identificados
[lista dos padrões e por que indicam performance]

### Gatilhos de copy mais usados pelos concorrentes
[lista]

---

## Brief de Criativos

### Criativo 1 — [Tipo] (Prioridade Alta)
[brief completo]

### Criativo 2 — [Tipo]
[brief completo]

### Criativo 3 — [Tipo]
[brief completo]

---

## Textos dos Anúncios

### Para o Criativo 1
**Texto principal:** [texto]
**Título A:** [título]
**Título B:** [título]
**Descrição:** [descrição]

[repetir para cada criativo]

---

## Estrutura da Campanha

### Conjuntos de anúncios
[lista]

### Público
[detalhamento]

---

## Notas para configuração

[observações práticas: orçamento inicial sugerido, tipo de lance recomendado, período de aprendizado esperado]
```

Depois de salvar, confirmar:

> "Estrutura salva em `campanhas/meta/[produto]-[data]/estrutura.md`. Os criativos do brief você produz no Canva ou em outra ferramenta — o documento já tem tudo que o designer (ou você) precisa pra executar."

## Regras

- Não inventar criativos sem base na análise competitiva. O brief deve ser ancorado no que os concorrentes estão fazendo.
- Tempo no ar e número de conjuntos são os principais indicadores de performance. Priorizar o que tem os dois altos.
- Textos devem respeitar os limites de caracteres do Meta. Avisar se estiver acima.
- Sempre gerar no mínimo 2 variações de título por criativo pra teste A/B.
