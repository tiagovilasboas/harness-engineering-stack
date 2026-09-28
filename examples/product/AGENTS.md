# AGENTS.md

Este arquivo é um template. Salve uma cópia como `AGENTS.md` na raiz do repositório de produto. A partir daqui, "este repositório" é o produto.

Instruções para qualquer LLM apontado a este repositório. Guia: entra antes da geração. O sensor (teste, lint, type check, log) volta depois e recusa o que quebrou.

## Visão

<Uma frase: o que este sistema faz e para quem.>

## Stack

<Substitua pela sua stack. A lista abaixo é placeholder, não recomendação.>

- Linguagem:
- Framework:
- Banco:
- Testes:

## Arquitetura

<Uma linha: o estilo que o time segue.>

## Estrutura

<As pastas reais do repo. Exemplo:>

- `src/domain/` — regras e entidades do domínio
- `src/application/` — casos de uso
- `src/infra/` — banco e serviços externos
- `src/presentation/` — controllers e rotas
- `tests/` — testes automatizados

## Regras de arquitetura

<As fronteiras que o time cobra no code review. Exemplos:>

- Controller sem regra de negócio. Regra de negócio em `domain`.
- `domain` não depende de `infra`.
- Banco só via repositories.
- Não criar camada ou padrão sem necessidade.

## Regras para escrever código

<As regras mecânicas do time. Exemplos:>

- Tipagem estrita ligada. Sem `any` implícito.
- Funções pequenas, uma responsabilidade.
- Nomenclatura já usada no projeto.
- Antes de criar função ou serviço, procurar implementação existente para reutilizar.

## O que este arquivo não é

- Não é a fonte da verdade do comportamento: o código é.
- Não substitui o sensor: teste, lint, type check e log recusam o que este guia não previu.
- Trocar o modelo não substitui este arquivo.
