# E-mails transacionais Nuvemshop — Alvim Grill

Templates HTML personalizados para os e-mails automáticos da loja (Configurações > E-mails no painel da Nuvemshop).

## Identidade aplicada

- Header escuro (#1A1A1A) com wordmark ALVIM GRILL (GRILL em laranja)
- Cor de destaque e botões: laranja #E8610A com texto branco
- Card branco com cantos arredondados 8px, fundo cinza claro #F5F5F5
- Barra superior laranja de 4px
- Tipografia sans-serif (Roboto com fallback de sistema)

## Como aplicar

1. No painel da Nuvemshop: **Configurações > E-mails**
2. Clique em **Editar conteúdo** no e-mail desejado
3. Abra o modo HTML do editor
4. Apague o conteúdo atual e cole o HTML do arquivo correspondente
5. **Antes de salvar**, compare as variáveis do template com o painel **"Explicação do código"** na lateral do editor. Se alguma variável do painel tiver grafia diferente, ajuste no HTML
6. Salve e envie um e-mail de teste (quando disponível) ou faça um pedido de teste

## Status de cada template

| Arquivo | E-mail | Variáveis |
|---|---|---|
| 01-carrinho-abandonado.html | Carrinhos abandonados | OK, confirmadas no painel da loja |
| 02-ativacao-conta.html | Ativação da conta | OK, baseadas no template atual da loja |
| 03-mudanca-senha.html | Mudança de senha | Baseadas na doc oficial, conferir painel |
| 04-boas-vindas.html | Boas-vindas | Baseadas na doc oficial, conferir painel |
| 05-confirmacao-compra.html | Confirmação de compra | Baseadas na doc oficial, conferir painel |
| 06-confirmacao-pagamento.html | Confirmação de pagamento | Baseadas na doc oficial, conferir painel |
| 07-pronto-para-retirada.html | Pronto para retirada | **SEM doc pública. Conferir painel antes de salvar** |
| 08-confirmacao-envio.html | Confirmação de envio | Baseadas na doc oficial, conferir painel |
| 09-confirmacao-entrega.html | Confirmação de entrega | **SEM doc pública. Conferir painel antes de salvar** |
| 10-cancelamento-compra.html | Cancelamento de compra | Baseadas na doc oficial, conferir painel |
| 11-nota-fiscal.html | Nota fiscal | **SEM doc pública. Conferir painel antes de salvar** |

Fonte da doc oficial (HTML original + variáveis): https://docs.nuvemshop.com.br/help/e-mails-automaticos

Os 3 templates sem doc pública têm um comentário `<!-- ATENCAO -->` no topo do arquivo dizendo o que conferir. Uma foto do painel "Explicação do código" de cada um resolve: com ela dá pra ajustar as variáveis com precisão.

## Assuntos sugeridos

| E-mail | Assunto |
|---|---|
| Carrinho abandonado | Seu carrinho na Alvim Grill está esperando por você |
| Ativação da conta | Ative sua conta na Alvim Grill |
| Mudança de senha | Redefina sua senha na Alvim Grill |
| Boas-vindas | Bem-vindo à Alvim Grill! |
| Confirmação de compra | Recebemos seu pedido #{{ order.id }} |
| Confirmação de pagamento | Pagamento aprovado! Pedido #{{ order.id }} |
| Pronto para retirada | Seu pedido está pronto para retirada |
| Confirmação de envio | Seu pedido está a caminho |
| Confirmação de entrega | Seu pedido foi entregue |
| Cancelamento de compra | Seu pedido #{{ order.id }} foi cancelado |
| Nota fiscal | Sua nota fiscal foi emitida |

Obs: só use variável no assunto se o campo de assunto do editor aceitar (o painel "Explicação do código" indica).

## Trocar o wordmark de texto pela logo

O header usa o texto "ALVIM GRILL" para funcionar sem depender de imagem hospedada. Para usar a logo (marca/logo-alvimgrill-laranja-branca.png, que já é laranja e branca e combina com o fundo escuro do header):

1. Hospede a imagem em uma URL pública (ex: suba como imagem em uma página da própria Nuvemshop e copie a URL do CDN)
2. Em cada template, substitua o `<span>` dentro do header por:
   `<img src="URL_DA_LOGO" alt="Alvim Grill" width="160" style="display:block; margin:0 auto; height:auto;" />`
