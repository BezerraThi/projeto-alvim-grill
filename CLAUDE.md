# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

# Claude Code OS — Kit Ratos de IA

Este repositório é o kit de boas-vindas do curso Claude Code OS, feito pelo [Ratos de IA](https://ratosdeia.com.br). Não é um projeto de software tradicional — é um sistema de workspace com contexto persistente e skills (slash commands) que automatizam processos do negócio do usuário.

Se você acabou de clonar esse repositório:
1. Rode `/setup` pra configurar o sistema pro seu negócio (uns 5 minutos)
2. Depois rode `/mapear` pra criar skills personalizadas pro que você faz no dia a dia

---

## Slash commands disponíveis

Ficam em `.claude/commands/` e são invocados com `/nome`:

| Comando | O que faz |
|---|---|
| `/setup` | Onboarding completo: entrevista o usuário, preenche contexto e configura git |
| `/iniciar` | Carrega contexto do negócio no início de cada sessão |
| `/mapear` | Descobre processos repetíveis e cria skills personalizadas |
| `/syncar` | Commit + push pro GitHub (configura na primeira vez) |
| `/atualizar` | Varre o projeto e atualiza arquivos de contexto desatualizados |
| `/novo-projeto` | Cria pasta de projeto com CLAUDE.md dedicado |

Skills adicionais criadas pelo `/mapear` ficam em `.claude/skills/nome-da-skill/SKILL.md` (locais ao projeto) ou `~/.claude/skills/` (globais).

---

## Arquitetura

O sistema é **context-first**: em toda sessão Claude lê os arquivos de contexto antes de qualquer tarefa. Fluxo de leitura:

```
CLAUDE.md
    ↓
_contexto/empresa.md       ← quem é o usuário, negócio, clientes, equipe, ferramentas
_contexto/preferencias.md  ← tom de voz, estilo, o que evitar
_contexto/estrategia.md    ← foco atual, prioridades, prazos
    ↓
marca/design-guide.md      ← identidade visual — só para tasks visuais
    ↓
.claude/commands/*.md      ← slash commands invocados pelo usuário
.claude/skills/*/SKILL.md  ← skills personalizadas criadas pelo /mapear
```

**`templates/`** contém referências, nunca editadas diretamente:
- `templates/perfis/` — modelos de CLAUDE.md pra diferentes perfis (solopreneur, freelancer, agência, empresa)
- `templates/skills/` — templates de skills prontas (carrossel, proposta, slide, analisar-dados, etc.)
- `templates/ferramentas/catalogo.md` — catálogo de APIs, CLIs e MCPs disponíveis pra usar em skills

**`dados/`** é drop zone pra arquivos do usuário analisar (CSV, XLSX, PDF). Usar com `/analisar-dados dados/arquivo`.

O hook em `.claude/settings.json` faz commit + push automático ao fim de cada sessão.

---

## Dependências externas

Algumas skills precisam de ferramentas instaladas separadamente:

- **Playwright** (renderização HTML → PNG para carrossel, proposta, slide): `npx playwright install chromium`
- **MCPs** (Notion, Gmail, Canva, etc.): instalados via `claude mcp add [nome]` durante `/setup`
- **APIs externas** (Cloudflare, Gemini, DALL-E, etc.): configuradas em `.env` — este arquivo é ignorado pelo git

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
