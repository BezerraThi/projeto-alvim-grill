# E-mails transacionais Nuvemshop — Alvim Grill

Templates para os e-mails automáticos da loja (Configurações > E-mails no painel da Nuvemshop). Cada e-mail tem duas versões:

- `.html` — versão principal, cola no editor HTML
- `.txt` — versão em texto puro (backup exibido quando o cliente de e-mail não carrega HTML), cola no campo de texto do mesmo editor

## Identidade aplicada

- Header escuro (#1A1A1A) com a logo Alvim Grill (hospedada no CDN da Nuvemshop, mesma imagem usada no site)
- Cor de destaque e botões: laranja #E8610A com texto branco
- Card branco com cantos arredondados 8px, fundo cinza claro #F5F5F5
- Barra superior laranja de 4px
- Tipografia sans-serif (Roboto com fallback de sistema)

## Como aplicar

1. No painel da Nuvemshop: **Configurações > E-mails**
2. Clique em **Editar conteúdo** no e-mail desejado
3. Abra o modo HTML do editor, apague o conteúdo atual e cole o `.html` correspondente
4. No campo de versão em texto do mesmo editor, cole o `.txt` correspondente
5. **Antes de salvar**, compare as variáveis do template com o painel **"Explicação do código"** na lateral do editor. Se alguma variável do painel tiver grafia diferente, ajuste nos dois arquivos
6. Salve e envie um e-mail de teste (quando disponível) ou faça um pedido de teste

## Status de cada template

| Arquivo | E-mail | Variáveis |
|---|---|---|
| 01-carrinho-abandonado | Carrinhos abandonados | OK, confirmadas no painel da loja |
| 02-ativacao-conta | Ativação da conta | OK, confirmadas no painel da loja |
| 03-mudanca-senha | Mudança de senha | OK, confirmadas no painel da loja |
| 04-boas-vindas | Boas-vindas | OK, confirmadas no painel da loja |
| 05-confirmacao-compra | Confirmação de compra | OK, confirmadas no painel da loja |
| 06-confirmacao-pagamento | Confirmação de pagamento | OK, confirmadas no painel da loja |
| 07-pronto-para-retirada | Pronto para retirada | **PENDENTE. Conferir painel "Explicação do código" antes de salvar** |
| 08-confirmacao-envio | Confirmação de envio | OK, confirmadas no painel da loja |
| 09-confirmacao-entrega | Confirmação de entrega | OK, confirmadas no painel da loja |
| 10-cancelamento-compra | Cancelamento de compra | OK, confirmadas no painel da loja |
| 11-nota-fiscal | Nota fiscal | OK, confirmadas no painel da loja |

Fonte da doc oficial (HTML original + variáveis): https://docs.nuvemshop.com.br/help/e-mails-automaticos

Só o **Pronto para retirada** ainda usa variáveis não confirmadas ({{ contact_name }}, {{ order.id }}); o arquivo tem um comentário `<!-- ATENCAO -->` no topo. Uma foto do painel "Explicação do código" dele resolve.

Notas de formatação aprendidas no preview:
- `order.discountCouponFormat`, `order.discountGatewayFormat` e `order.shippingDiscountFormat` já vêm com sinal negativo. Não adicionar "-" antes.
- `promotion.total_discount_amount_short` vem SEM sinal. Manter o "- " antes.

Limitações descobertas na validação de salvamento (testado em 2026-07):
- `product.is_kit` e `product.components` NÃO passam na validação dos e-mails de pedido (confirmação de compra e de pagamento). A Nuvemshop rejeita o salvamento com erro genérico. Kits aparecem como uma linha única de produto, sem listar os componentes. Essas variáveis só funcionam no carrinho abandonado.
- `order.shippingDiscount` / `order.shippingDiscountFormat` passam na validação normalmente.

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

## Logo no header

O header de todos os templates usa a logo oficial da loja hospedada no CDN da Nuvemshop (a mesma imagem que o site alvimgrill.com.br carrega):

`https://dcdn-us.mitiendanube.com/stores/007/797/591/themes/common/logo-7026286291621255565-1781473397-22b2a674a591f2f34fe1b9c422ef3ed31781473397.png`

Atenção: se a logo do site for trocada no futuro, essa URL pode mudar. Nesse caso, pegue a nova URL no código-fonte da home da loja (img do header) e substitua nos 11 arquivos `.html`.
