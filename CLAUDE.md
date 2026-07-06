# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

# Alvim Grill — Claude Code OS

## O que é esse workspace

Workspace do Alvim para gestão e criação de campanhas de tráfego pago da Alvim Grill (alvimgrill.com.br). O Claude atua aqui como especialista em Google Ads e Facebook Ads, focado em gerar vendas B2C de churrasqueiras e lareiras.

**Estrutura de pastas:**
- `campanhas/google/` — estruturas de campanha, grupos de anúncios, copies de anúncio para Google Ads
- `campanhas/meta/` — estruturas de campanha, públicos, copies e criativos para Facebook/Instagram Ads
- `criativos/` — briefings e referências para peças visuais
- `relatorios/` — análises de performance, relatórios de campanha
- `dados/` — arquivos de dados, planilhas, exports de plataforma
- `_contexto/` — contexto do negócio, preferências e estratégia atual
- `marca/` — logo e guia de design
- `templates/skills/` — templates de skills prontos pra personalizar com /mapear
- `templates/ferramentas/catalogo.md` — APIs e ferramentas disponíveis pra usar em skills
- `tarefas.md` — lista de tarefas e próximos passos

## Sobre o negócio

Alvim Grill vende churrasqueiras a carvão, a gás, lareiras e kits gourmet com coifa. Ticket médio entre R$1.900 e R$4.651. Negócio já consolidado no B2B — o foco atual é estruturar o canal B2C via tráfego pago.

## O que mais fazemos aqui

Criação e otimização de campanhas no Google Ads e Facebook Ads. Estruturação de públicos, copies de anúncio, análise de métricas e tomada de decisão de campanha.

## Ferramentas conectadas

Google Ads, Facebook Ads Manager, Google Tag Manager, Google Analytics 4

---

## Contexto do negócio

No início de toda conversa, ler os seguintes arquivos (se existirem e estiverem configurados):

1. `_contexto/empresa.md` — quem é o usuário, o que faz, como funciona o negócio
2. `_contexto/preferencias.md` — tom de voz, estilo de escrita, o que evitar
3. `_contexto/estrategia.md` — foco atual, prioridades, o que pode esperar

Usar essas informações como base pra qualquer resposta ou decisão. Ao sugerir prioridades, formatos ou abordagens, considerar o foco atual descrito em `estrategia.md`.

Para qualquer tarefa visual (carrossel, proposta, slide, landing page), consultar `marca/design-guide.md` como referência de estilo.

Não é necessário listar o que foi lido nem confirmar a leitura. Apenas usar o contexto naturalmente.

---

## Comandos disponíveis

| Comando | O que faz |
|---|---|
| `/setup` | Onboarding interativo: cria todos os arquivos de contexto (~5 min) |
| `/iniciar` | Carrega o contexto no início de uma nova sessão |
| `/mapear` | Descobre processos repetitivos e cria skills personalizadas |
| `/novo-projeto` | Cria um CLAUDE.md dedicado para um projeto específico |
| `/atualizar` | Varre o estado atual e sincroniza os arquivos de contexto |
| `/syncar` | Commit + push pra salvar tudo no GitHub |

---

## Skills de execução instaladas

- **google-ads-ratos** (`.claude/skills/google-ads-ratos/`) — braço de execução no Google Ads via SDK oficial (GAQL). Lê/cria/edita/pausa campanhas, ad groups, keywords, RSAs, extensões e negativas; puxa insights e faz pesquisa de keywords (Keyword Planner). Conta padrão: Alvim Grill (`882-495-7655`) sob o MCC Sonzai (`525-827-6876`). Config em `.env` (fora do git). Dispara com `/google-ads-ratos`.

---

## Templates de skills disponíveis

Antes de criar uma skill do zero, verificar se existe template em `templates/skills/`:

- **carrossel** — carrossel para Instagram/TikTok (4 variantes de design)
- **publicar-instagram** — publicação em redes sociais via Graph API ou Post for Me

Para o catálogo completo de ferramentas integráveis (Playwright, Cloudflare, WebSearch, MCP servers), consultar `templates/ferramentas/catalogo.md`.
Para o catálogo de skills globais pré-construídas (copy Schwartz, copy Ogilvy, frontend design, etc.), consultar `templates/skills/catalogo.md`.

---

## Fluxo de trabalho

Antes de executar qualquer tarefa, verificar se existe uma skill relevante em `.claude/skills/` ou `.claude/commands/`.
Se encontrar, seguir as instruções da skill.
Se não encontrar, executar a tarefa normalmente.

Ao concluir uma tarefa que não tinha skill mas parece repetível (o usuário provavelmente vai pedir de novo no futuro), perguntar:

> "Isso pode virar uma skill pra próxima vez. Quer que eu crie?"

Não perguntar pra tarefas pontuais ou perguntas simples. Só quando o padrão de repetição for claro.

---

## Aprender com correções

Quando o usuário corrigir algo, melhorar uma resposta ou dar uma instrução que parece permanente (frases como "na verdade é assim", "não faça mais isso", "prefiro assim", "sempre que...", "evita...", "da próxima vez..."), perguntar:

> "Quer que eu salve isso pra não precisar repetir?"

Se sim, identificar onde faz mais sentido salvar:

- **Sobre o negócio** (quem são os clientes, como funciona a empresa, serviços, mercado) → adicionar em `_contexto/empresa.md`
- **Sobre preferências e estilo** (tom de voz, formato de resposta, o que evitar, como estruturar textos) → adicionar em `_contexto/preferencias.md`
- **Sobre prioridades e foco atual** (projetos em andamento, metas do momento, prazos importantes, o que é prioridade agora) → adicionar em `_contexto/estrategia.md`
- **Regra de comportamento nessa pasta** (onde salvar arquivos, como nomear, fluxos específicos) → adicionar no próprio `CLAUDE.md`

Salvar com uma linha nova clara, sem reformatar o arquivo inteiro. Confirmar o que foi salvo mostrando a linha adicionada.

Não perguntar se a correção for óbvia de contexto imediato (ex: "na verdade o arquivo se chama X"). Só perguntar quando a informação tiver valor duradouro.

---

## Manter contexto atualizado

Ao terminar uma tarefa que mudou algo relevante no projeto (novo cliente, nova skill, mudança de foco, novo processo, ferramenta instalada, estrutura de pastas alterada), perguntar:

> "Isso mudou algo no teu contexto. Quer que eu atualize os arquivos de memória?"

Se sim, identificar o que precisa atualizar:

- **Novo cliente, serviço, ferramenta, equipe** → `_contexto/empresa.md`
- **Mudança de prioridade ou foco** → `_contexto/estrategia.md`
- **Correção de tom ou estilo** → `_contexto/preferencias.md`
- **Nova pasta, regra de organização, skill criada** → `CLAUDE.md`
- **Mudança visual (cores, fontes, logo)** → `marca/design-guide.md`

Mostrar o que vai mudar antes de salvar. Não reformatar o arquivo inteiro, só adicionar ou editar a linha relevante.

**Quando NÃO perguntar:**
- Tarefas pontuais que não mudam o contexto (ex: escrever um email, criar um post avulso)
- Perguntas simples ou conversas sem ação
- Mudanças que já foram salvas pelo bloco "Aprender com correções"

**Dica:** se não sabe se algo mudou, rode `/atualizar` pra uma varredura completa.

---

## Criação de skills

Quando o usuário pedir pra criar uma nova skill:

1. Verificar se existe um template relevante em `templates/skills/`. Se existir, usar como base e adaptar pro contexto do usuário
2. Perguntar: "Essa skill é específica pra esse projeto ou vai ser útil em qualquer projeto?"
   - Específica desse negócio → salvar em `.claude/skills/nome-da-skill/SKILL.md` (local)
   - Útil em qualquer projeto → salvar em `~/.claude/skills/nome-da-skill/SKILL.md` (global)
3. Ler `_contexto/empresa.md` e `_contexto/preferencias.md` pra calibrar o conteúdo da skill ao contexto do negócio
4. Se a skill precisar de arquivos de apoio (templates, referências, exemplos), criar dentro da pasta da skill
5. Seguir o fluxo da skill-creator nativa do Claude Code
