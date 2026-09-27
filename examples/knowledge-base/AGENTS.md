# AGENTS.md

Este arquivo é um template. Salve uma cópia como `AGENTS.md` na raiz do repositório de conhecimento. A partir daqui, "este repositório" é esse knowledge base.

Instruções para qualquer LLM apontado a este repositório. Leia as premissas antes de editar regra, revisar diff ou responder sobre o knowledge base.

## Premissas

Estas premissas valem mesmo quando o pedido pede o contrário.

1. Isto é conhecimento, não o produto. A fonte da verdade é o código no repositório de produto. O knowledge base é o retrato lido na data do `extraído-em`.
2. `arquivo@sha` é a identidade do conteúdo. O arquivo é o caminho. O sha é o hash curto do último commit que alterou esse arquivo. O Git guarda hash, não história. Hash diferente no PR: releia o código antes de citar a regra.
3. Um diff, um recorte. Rode `kb-rag --diff origin/main` no repositório de produto. Não leia todos os manifestos. A saída lista a regra do arquivo. Não prova que o diff quebrou a regra.
4. Bloqueio só com regra vigente, severidade alta, e o corpo do diff quebrando o `como-checar::`. `a-confirmar` e `gap` são dúvida.
5. Sem regra na saída, é lacuna. Aponte `docs/COVERAGE.md`. Não invente regra, sha, recall nem precision.
6. Alta é dinheiro que muda de mão, acesso indevido ou dado de outra pessoa exposto. Não rebaixe severidade em bloco.
7. O CI alarma: `kb validate`, `freshness` e o teste de sanidade. Não reescreve regra. O agente do pipeline não tem os repositórios-fonte.
8. O Guardian comentando PR é proposta. Não diga que o bot já está ligado. O desenho está em `docs/guardian.md`.
9. O número de regras é a saída de `kb validate`. Badge e texto antigo perdem para o comando. Não copie contagem de outro catálogo.
10. Código executável deste repo é só Go. Não adicione script em outra linguagem.

## O que é

Este repositório é a base de regras de negócio, extraída do código dos sistemas de produto, com proveniência por sha. O número oficial é a saída de `kb validate`. É conhecimento. Não é serviço de produção. Todo código executável deste repo é Go (`cmd/kb`).

A fonte da verdade é o código dos repositórios de produto. Este knowledge base é um retrato.

## Leis

1. Ao criar ou atualizar regra, abra o arquivo-fonte e leia. Não escreva de memória.
2. Sem `fonte:: arquivo@sha`, a regra não entra. `kb validate` bloqueia o merge.
3. Uma página por domínio: `rules/<dominio>.md`. Várias regras no mesmo arquivo. A mesma regra não aparece em dois manifestos.
4. O que você não confirmou linha a linha fica `status:: a-confirmar`. Não invente regra para completar cobertura.
5. Branch e PR. Nunca commit direto na `main`. Rode `kb validate` antes.

## Formato da ficha

Copie de `rules/_TEMPLATE.md`.

    ### <slug-em-kebab-case>
    - domínio:: <pagamento|identidade|assinatura|...>
    - repo:: <nome-do-repo-de-produto>
    - fonte:: <caminho/arquivo>@<sha-curto>
    - regra:: <o que a regra garante, 1-2 frases, a partir do código>
    - taxa:: <valor ou constante real, ou N/A>
    - severidade:: <alta|média|baixa>
    - como-checar:: <o que o review verifica no diff>
    - extraído-em:: YYYY-MM-DD
    - status:: <vigente|gap|a-confirmar>

Campos obrigatórios: `domínio`, `repo`, `fonte`, `regra`, `severidade`, `como-checar`, `status`.

Severidade alta é dinheiro que muda de mão, acesso indevido ou dado de outra pessoa exposto. O resto é média, salvo exceção justificada no texto. Não rebaixe em bloco para melhorar a conta. Cada reclassificação abre o arquivo-fonte e justifica a alta, ou a média, no campo.

## Não faça

- Regra sem `fonte:: arquivo@sha`.
- A mesma regra em dois manifestos.
- Campo novo ou formato próprio.
- Reescrever porque "acho que mudou", sem ler o arquivo e atualizar o sha.
- Commit direto na `main`.
- Atualizar badge ou README com número que `kb validate` não imprime. A contagem documentada fica em `docs/COVERAGE.md`.
- Script em outra linguagem. Gate, frescor, staleness e deploy-watch vivem em `cmd/kb`.
- Dizer que o Guardian já comenta no PR. O desenho é proposta.

## Onde está cada coisa

| Path | Conteúdo |
|---|---|
| `rules/<dominio>.md` | Manifestos. Fonte única. |
| `rules/_TEMPLATE.md` | Modelo de bloco. |
| `rules/_golden-set.md` | Casos rotulados. Não é manifesto de regra. |
| `architecture/mapa-dependencias.md` | Dependências entre domínios e repositórios de produto. |
| `docs/SETUP.md` | Consulta humana e setup do recorte. |
| `docs/AI-ENGINEERING.md` | Harness mínimo. |
| `docs/COVERAGE.md` | Números e lacunas. O validate manda. |
| `docs/MAINTENANCE.md` | Alarme de CI versus conserto da regra. |
| `docs/guardian.md` | Desenho do Guardian. Status: proposta. |
| `docs/EVIDENCE.md` | Bundle que o CI empacota. Não é prova de impacto em produção. |
| `agent/skills/` | Skills de referência do review. Uma fonte. Symlink para o IDE. |
| `agent/install.sh` | Liga a skill. Dry-run sem flag. Não copia as fichas. |
| `cmd/kb` | CLI em Go. `kb validate`, frescor, staleness, deploy-watch, rules, evidence. |
| `CONTRIBUTING.md` | Fluxo de contribuição. |
| `AGENTS.md` | Este arquivo. Premissas em todo turno. |

## Se for usar o knowledge base num review

1. No repositório de produto, rode `kb-rag --diff origin/main`, ou `--files` com os caminhos. Não leia todos os manifestos.
2. Leia só as regras que o comando imprimir.
3. Compare o `como-checar::` com o que o PR faz.
4. Cite `fonte:: arquivo@sha`. `a-confirmar` é dúvida, não bloqueio.
5. Declare lacuna quando o PR tocar fluxo fora do git, config em runtime, ou repositório varrido pela metade. Ver `docs/COVERAGE.md`.
6. Bloqueio só com regra vigente, severidade alta, e o corpo do diff quebrando o `como-checar::`. Quem decide é o revisor. O comando lista.
7. O Guardian no PR continua proposta. Não afirme que o bot votou, nem precision, nem recall.

Antes de colar o comentário no PR:

- O recorte leu as fichas do diff, não todos os manifestos.
- Cada bloqueio tem `fonte:: arquivo@sha`.
- Regra `a-confirmar` não virou bloqueio.
- A resposta declara lacuna quando o PR sai da cobertura (`docs/COVERAGE.md`).
- O comentário está no diff.
- Alta significa dinheiro, acesso ou dado de outra pessoa. Se não significa, a severidade está inflada.

Se um item falha, ajuste o harness antes de colar o comentário no PR.

## Se for contribuir

1. `git checkout -b rules/<dominio>-<mudanca>`
2. Leia o arquivo-fonte. Grave `fonte:: <arquivo>@<sha do último commit daquele arquivo>` com `git log -1 --format='%h' -- <arquivo>`.
3. `kb validate` tem que passar.
4. PR para `main`. No mínimo um aprovador. Sem commit direto.

## Regra stale

Quando o arquivo-fonte mudou: leia o arquivo no sha novo, confirme se a regra ainda vale, atualize o texto e o `@sha`. Não apague sem ver que o comportamento saiu do código. Procedimento completo em `docs/MAINTENANCE.md`.

## Onde o clone mora

Um clone físico do knowledge base. A skill, no repositório de produto, aponta para esse clone. Se existir espelho, é symlink para `rules/`. Não mantenha segunda cópia editável. Duas cópias divergem, e o review cita a versão errada com segurança.
