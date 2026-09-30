# Brazil & LATAM OSINT Sources

> Prefer primary official sources. Aggregators are useful for discovery, but they are not magical truth dispensers.

## Brazil — core public data

| Source | Organization | Best use |
|---|---|---|
| [dados.gov.br](https://dados.gov.br/) | Governo Federal | federal open-data catalog |
| [Portal da Transparência](https://portaldatransparencia.gov.br/) | CGU | spending, sanctions, public programs and transparency |
| [Receita Federal — Dados Abertos CNPJ](https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/cadastros/cnpj/dados-abertos-cnpj) | Receita Federal | public CNPJ datasets |
| [IBGE](https://www.ibge.gov.br/) | IBGE | geography, statistics, municipalities, economic/demographic context |
| [IBGE APIs](https://servicodados.ibge.gov.br/api/docs/) | IBGE | programmatic geographic/statistical data |
| [Banco Central — Dados Abertos](https://dadosabertos.bcb.gov.br/) | BCB | financial/economic datasets |
| [CVM Dados Abertos](https://dados.cvm.gov.br/) | CVM | securities market/company filings |
| [TSE Dados Abertos](https://dadosabertos.tse.jus.br/) | TSE | election/candidate/party datasets |
| [Câmara Dados Abertos](https://dadosabertos.camara.leg.br/) | Câmara dos Deputados | legislative/member data |
| [Senado Dados Abertos](https://www12.senado.leg.br/dados-abertos) | Senado Federal | legislative data |
| [PNCP](https://www.gov.br/pncp/) | Governo Federal | public procurement and contracts |
| [Compras.gov.br](https://www.gov.br/compras/) | Governo Federal | federal procurement |
| [DataSUS](https://datasus.saude.gov.br/) | Ministério da Saúde | public health datasets |
| [CNES](https://cnes.datasus.gov.br/) | Ministério da Saúde | health establishments |
| [INEP Dados Abertos](https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos) | INEP | education datasets |
| [ANATEL Dados Abertos](https://dados.gov.br/dados/organizacoes/visualizar/agencia-nacional-de-telecomunicacoes-anatel) | ANATEL | telecom public datasets |
| [INPE TerraBrasilis](https://terrabrasilis.dpi.inpe.br/) | INPE | environmental/geospatial monitoring |
| [INPE Queimadas](https://terrabrasilis.dpi.inpe.br/queimadas/portal/) | INPE | fire/burn monitoring |
| [Registro.br](https://registro.br/) | NIC.br | .br domain/RDAP context |
| [CERT.br](https://www.cert.br/) | NIC.br | incident/security statistics and references |
| [NIC.br Medições](https://medicoes.nic.br/) | NIC.br | Brazilian internet measurement data |

## Brazil — civic, legal and journalism-oriented open data

| Source | Best use |
|---|---|
| [Querido Diário](https://queridodiario.ok.org.br/) | municipal official gazettes |
| [Brasil.IO](https://brasil.io/) | cleaned public Brazilian datasets |
| [Base dos Dados](https://basedosdados.org/) | harmonized public datasets |
| [MapBiomas](https://mapbiomas.org/) | land-use/environment data |
| [Open Knowledge Brasil](https://ok.org.br/) | civic/open-data projects |
| [CNJ DataJud](https://www.cnj.jus.br/sistemas/datajud/) | judiciary statistics/open datasets |
| [Diário Oficial da União](https://www.in.gov.br/) | federal official publications |
| [LexML](https://www.lexml.gov.br/) | legal and legislative documents |

## Brazil — geospatial and address context

| Source | Best use |
|---|---|
| [IBGE Cidades](https://cidades.ibge.gov.br/) | municipality context |
| [IBGE Malhas](https://www.ibge.gov.br/geociencias/organizacao-do-territorio/malhas-territoriais.html) | administrative boundaries |
| [OpenStreetMap Brasil](https://www.openstreetmap.org/) | open map features |
| [GeoSampa](https://geosampa.prefeitura.sp.gov.br/) | São Paulo geospatial public data |
| [BHGeo](https://bhmap.pbh.gov.br/) | Belo Horizonte municipal geodata |
| [Data.Rio](https://www.data.rio/) | Rio de Janeiro municipal datasets |

## Brazil — Ridd1kulusC0d3r tools

| Project | Focus |
|---|---|
| [F.I.O. Lab](https://github.com/Ridd1kulusC0d3r/FIO) | Brazilian identifiers and public datasets |
| [Mineiro Username Intelligence](https://github.com/Ridd1kulusC0d3r/Mineiro-OSINT-Extractor) | username/public-presence intelligence |
| [Tropeiro Intel](https://github.com/Ridd1kulusC0d3r/tropeiro-intel) | defensive phishing/fraud campaign intelligence |
| [T.O.C.A.I.A](https://github.com/Ridd1kulusC0d3r/tocaia-osint) | behavioral OSINT / absence analysis |
| [OSINT Checklist](https://github.com/Ridd1kulusC0d3r/osintchecklist) | investigation method and logbook |

## LATAM — national open-data portals

| Country | Portal |
|---|---|
| Argentina | [datos.gob.ar](https://datos.gob.ar/) |
| Chile | [datos.gob.cl](https://datos.gob.cl/) |
| Colombia | [datos.gov.co](https://www.datos.gov.co/) |
| Mexico | [datos.gob.mx](https://datos.gob.mx/) |
| Peru | [Datos Abiertos](https://www.datosabiertos.gob.pe/) |
| Uruguay | [Catálogo de Datos Abiertos](https://catalogodatos.gub.uy/) |
| Paraguay | [Datos Abiertos](https://www.datos.gov.py/) |
| Costa Rica | [Datos Abiertos](https://datosabiertos.go.cr/) |

## Regional / international sources useful in LATAM

| Source | Best use |
|---|---|
| [World Bank Data](https://data.worldbank.org/) | macroeconomic/development context |
| [IDB Data](https://data.iadb.org/) | regional development datasets |
| [CEPALSTAT](https://statistics.cepal.org/portal/cepalstat/) | Latin American socio-economic statistics |
| [OAS](https://www.oas.org/) | regional public documents and programs |
| [OpenCorporates](https://opencorporates.com/) | cross-border company discovery |
| [GLEIF](https://www.gleif.org/en/lei-search) | legal entity identifiers |
| [OCCRP Aleph](https://aleph.occrp.org/) | cross-border investigative records |
| [ICIJ Offshore Leaks](https://offshoreleaks.icij.org/) | offshore entity records |

## Regional workflow

```text
Official registry / open data
        ↓
Normalize identifiers
        ↓
Cross-check secondary databases
        ↓
Historical/archive verification
        ↓
Relationship/timeline analysis
        ↓
Document provenance + uncertainty
```

## Caveats

- availability and field definitions change;
- the same name may refer to different people or entities;
- Brazilian identifiers should be normalized before comparison;
- public records can contain stale or administratively inherited addresses;
- corporate addresses may represent accountants, coworking spaces or agents rather than operational premises;
- absence from a dataset can reflect coverage limits, not actual absence.

For general methodology, see [WORKFLOW.md](WORKFLOW.md).
