# The Pensieve OSINT

> **O segundo cérebro do analista de Inteligência de Fontes Abertas.**  
> Arsenal pesquisável · playbooks orientados por evidência · memória analítica · knowledge graph · Brasil/LATAM · conhecimento estruturado para agentes de IA.

[Web Explorer / Pages](docs/PAGES.md) · [English](README.md) · [Arsenal](docs/ARSENAL.md) · [Roteador “Eu tenho…”](docs/ROUTER.md) · [Second Brain](docs/SECOND-BRAIN.md) · [Descoberta por IA](docs/AI-DISCOVERY.md)

## A proposta

O Pensieve não é só uma lista de links. Ele precisa lembrar **como o analista pensa**:

~~~text
O QUE EU TENHO
      ↓
NORMALIZAR → PLANEJAR → DESCOBRIR → COLETAR → VERIFICAR → CORRELACIONAR → ANALISAR → RELATAR
      │                                  │
      └── semântica do input             └── caveats + memória + confiança
~~~

Ele registra ferramentas e fontes, inputs e outputs, playbooks, limitações, verificações, padrões de falso positivo, relações entre recursos, projetos especializados e mudanças de disponibilidade.

## Comece por aqui

| Objetivo | Caminho |
|---|---|
| Pesquisar e filtrar o arsenal | [Web Explorer / Pages](docs/PAGES.md) |
| Começar pelo dado que você já possui | [Roteador “I Have…”](docs/ROUTER.md) |
| Navegar no arsenal | [Arsenal OSINT](docs/ARSENAL.md) |
| Seguir método investigativo | [Workflow](docs/WORKFLOW.md) |
| Entender a arquitetura | [Second Brain](docs/SECOND-BRAIN.md) |
| Ver relações | [Knowledge Graph](docs/KNOWLEDGE-GRAPH.md) |
| Consultar lições reutilizáveis | [Memória do Analista](memory/README.md) |
| Trabalhar com Brasil/LATAM | [Brasil & LATAM](docs/BRAZIL-LATAM.md) |
| Consumir dados estruturados | [knowledge/](knowledge/) |
| Dar contexto a agentes de IA | [llms.txt](llms.txt) · [ai-index.json](ai-index.json) · [AGENTS.md](AGENTS.md) |

## Camadas do Second Brain

| Memória | Conteúdo |
|---|---|
| **Declarativa** | ferramentas, fontes, inputs, outputs, taxonomia |
| **Procedural** | playbooks de investigação |
| **Analítica** | erros recorrentes e lições aprendidas |
| **Relacional** | knowledge graph |
| **Temporal** | health/diff das fontes |
| **Recuperação** | busca, filtros e “I Have…” |
| **IA** | llms.txt, JSON canônico, JSON-LD e índice de agentes |

## Conhecimento canônico

A verdade estruturada vive em knowledge/*.json. O CSV é apenas uma exportação.

Agentes devem ler primeiro:

1. llms.txt;
2. ai-index.json;
3. knowledge/README.md;
4. o JSON relacionado à pergunta;
5. documentação e padrões em memory/.

O modelo explicita regras que listas comuns deixam perigosamente vagas:

**username igual ≠ identidade**  
**infraestrutura compartilhada ≠ propriedade**  
**label de reputação ≠ atribuição**  
**nenhum resultado ≠ evidência de ausência**

## Ecossistema

- [Mineiro Username Intelligence](https://github.com/Ridd1kulusC0d3r/Mineiro-OSINT-Extractor)
- [T.O.C.A.I.A](https://github.com/Ridd1kulusC0d3r/tocaia-osint)
- [OSINT Checklist](https://github.com/Ridd1kulusC0d3r/osintchecklist)
- [F.I.O. Lab](https://github.com/Ridd1kulusC0d3r/FIO)
- [Tropeiro Intel](https://github.com/Ridd1kulusC0d3r/tropeiro-intel)
- [OSINT](https://github.com/Ridd1kulusC0d3r/OSINT)
- [OSINT Uai](https://github.com/Ridd1kulusC0d3r/OsintUAI)
- [T4lks](https://github.com/Ridd1kulusC0d3r/T4lks)

## Regra de ouro

**Achado não é conclusão. Correlação não é identidade. Coincidência não é atribuição. Ausência não é evidência sem cobertura de coleta.**

Dados de casos sensíveis não pertencem ao repositório público.

---

**Estado: v0.3 Second Brain foundation** — knowledge base estruturada, interface pesquisável, roteamento por input, playbooks, memória analítica, grafo, descoberta por IA e monitoramento temporal.
