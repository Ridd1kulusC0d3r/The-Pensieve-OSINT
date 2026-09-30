# OSINT Arsenal

> Curated by **investigative function**, not by how many bookmarks can be accumulated before a browser begs for mercy.

Legend: **OS** open source · **F** free · **FM** freemium · **P** paid/commercial · **O** official/public source.

## 0. Meta indexes and source discovery

| Resource | Access | Best use |
|---|---:|---|
| [Bellingcat Online Investigation Toolkit](https://bellingcat.gitbook.io/toolkit) | F | Curated investigation tools with use cases and limitations |
| [OSINT Framework](https://osintframework.com/) | F | Tree-style discovery by investigative surface |
| [Awesome OSINT](https://github.com/jivoi/awesome-osint) | OS | Large community-maintained catalog |
| [Awesome OSINT Repositories](https://github.com/osintshifu/awesome-osint-repos) | OS | Repository-first catalog, including newer agentic tools |
| [OSINT.dev](https://osint.dev/) | F | Searchable OSINT source/tool catalog |
| [IntelTechniques Search Tools](https://inteltechniques.com/tools/) | F | Search forms and pivot helpers |
| [OSINT Combine](https://www.osintcombine.com/free-osint-tools) | F/FM | Practical tool directory and training ecosystem |
| [Bellingcat GitHub](https://github.com/bellingcat) | OS | Open-source investigation utilities |

## 1. Search, discovery and web research

| Resource | Access | Pivot |
|---|---:|---|
| [Google](https://www.google.com/) | F | keywords, exact strings, files, domains |
| [Bing](https://www.bing.com/) | F | web, image and alternative indexing |
| [Brave Search](https://search.brave.com/) | F | independent web search |
| [DuckDuckGo](https://duckduckgo.com/) | F | general search with alternative result mix |
| [Mojeek](https://www.mojeek.com/) | F | independent crawler/index |
| [Yandex](https://yandex.com/) | F | multilingual web and image discovery |
| [Google Programmable Search](https://programmablesearchengine.google.com/) | F/FM | targeted source collections |
| [Google Dataset Search](https://datasetsearch.research.google.com/) | F | datasets |
| [Google News](https://news.google.com/) | F | news discovery |
| [GDELT](https://gdeltproject.org/) | F | global news/event datasets |
| [Media Cloud](https://www.mediacloud.org/) | F | media-source research |

## 2. Archives and historical web

| Resource | Access | Best use |
|---|---:|---|
| [Internet Archive Wayback Machine](https://web.archive.org/) | F | historical pages and snapshots |
| [Common Crawl](https://commoncrawl.org/) | F | large-scale historical web corpus |
| [Arquivo.pt](https://arquivo.pt/) | F/O | searchable archived web content |
| [Memento Time Travel](https://timetravel.mementoweb.org/) | F | federated web archive lookup |
| [UK Web Archive](https://www.webarchive.org.uk/) | F/O | UK-focused preserved web content |
| [Library of Congress Web Archives](https://www.loc.gov/web-archives/) | F/O | curated historical web collections |

## 3. Usernames, public identity and account discovery

> Treat account matches as **leads**, never automatic proof of identity.

| Resource | Access | Input |
|---|---:|---|
| [Mineiro Username Intelligence](https://github.com/Ridd1kulusC0d3r/Mineiro-OSINT-Extractor) | OS | username |
| [Sherlock](https://github.com/sherlock-project/sherlock) | OS | username |
| [Maigret](https://github.com/soxoj/maigret) | OS | username |
| [WhatsMyName](https://github.com/WebBreacher/WhatsMyName) | OS | username |
| [Blackbird](https://github.com/antoniaci/blackbird) | OS | username/e-mail |
| [GHunt](https://github.com/mxrch/GHunt) | OS | Google-account-related public signals |
| [Holehe](https://github.com/megadose/holehe) | OS | e-mail registration signals |
| [Epieos](https://epieos.com/) | FM | e-mail/phone public-source pivots |
| [Gravatar](https://gravatar.com/) | F | public avatar/profile relationships |

## 4. Social and platform research

| Resource | Access | Best use |
|---|---:|---|
| [Bellingcat social-media tools](https://bellingcat.gitbook.io/toolkit/more/all-tools) | F | curated platform-specific discovery |
| [Instaloader](https://github.com/instaloader/instaloader) | OS | public Instagram content collection |
| [YouTube Data API](https://developers.google.com/youtube/v3) | F/FM | channels, videos, metadata |
| [YouTube Transcript API](https://github.com/jdepoix/youtube-transcript-api) | OS | transcript extraction where available |
| [yt-dlp](https://github.com/yt-dlp/yt-dlp) | OS | public media metadata/download workflows |
| [Social Searcher](https://www.social-searcher.com/) | FM | public social/web mentions |
| [Fediverse Observer](https://fediverse.observer/) | F | Fediverse instance discovery |
| [Mastodon instances](https://instances.social/) | F | instance discovery |

## 5. Domains, DNS, IPs and internet infrastructure

| Resource | Access | Pivot |
|---|---:|---|
| [ICANN Lookup](https://lookup.icann.org/) | F/O | registration data |
| [RDAP.org](https://rdap.org/) | F | domain/IP registration |
| [crt.sh](https://crt.sh/) | F | certificate transparency |
| [Censys](https://search.censys.io/) | FM | hosts, certificates, services |
| [Shodan](https://www.shodan.io/) | FM/P | internet-exposed services |
| [Netlas](https://netlas.io/) | FM/P | infrastructure search |
| [SecurityTrails](https://securitytrails.com/) | FM/P | DNS/domain history |
| [DNSDumpster](https://dnsdumpster.com/) | F | DNS mapping |
| [ViewDNS.info](https://viewdns.info/) | F/FM | DNS/IP/domain utilities |
| [urlscan.io](https://urlscan.io/) | F/FM | URL/page scans and infrastructure |
| [BuiltWith](https://builtwith.com/) | FM/P | web technology profiling |
| [Wappalyzer](https://www.wappalyzer.com/) | FM/P | web technology identification |
| [RIPEstat](https://stat.ripe.net/) | F/O | IP/ASN/network context |
| [BGPView](https://bgpview.io/) | F | ASN/prefix relationships |
| [Hurricane Electric BGP Toolkit](https://bgp.he.net/) | F | ASN/BGP research |
| [AlienVault OTX](https://otx.alienvault.com/) | F | IOC and infrastructure context |

## 6. Cyber threat intelligence and defensive IOC enrichment

| Resource | Access | Best use |
|---|---:|---|
| [VirusTotal](https://www.virustotal.com/) | FM/P | domains, URLs, IPs, hashes |
| [GreyNoise](https://www.greynoise.io/) | FM/P | internet scanner/noise context |
| [AbuseIPDB](https://www.abuseipdb.com/) | FM | IP reputation |
| [ThreatFox](https://threatfox.abuse.ch/) | F | malware IOCs |
| [URLhaus](https://urlhaus.abuse.ch/) | F | malicious URL intelligence |
| [MalwareBazaar](https://bazaar.abuse.ch/) | F | malware sample metadata/hashes |
| [Feodo Tracker](https://feodotracker.abuse.ch/) | F | botnet C2 intelligence |
| [Pulsedive](https://pulsedive.com/) | FM | IOC enrichment |
| [MISP](https://www.misp-project.org/) | OS | threat-intelligence sharing |
| [OpenCTI](https://github.com/OpenCTI-Platform/opencti) | OS | CTI knowledge graph/platform |
| [IntelOwl](https://github.com/intelowlproject/IntelOwl) | OS | enrichment orchestration |
| [MITRE ATT&CK](https://attack.mitre.org/) | F | adversary behavior context |
| [MITRE D3FEND](https://d3fend.mitre.org/) | F | defensive technique context |
| [CIRCL](https://www.circl.lu/) | F/O | threat-intelligence services/resources |
| [FIRST EPSS](https://www.first.org/epss/) | F | vulnerability exploitation probability context |

## 7. Images, video and visual verification

| Resource | Access | Best use |
|---|---:|---|
| [Google Lens](https://search.google/ways-to-search/lens/) | F | reverse/visual search |
| [Bing Visual Search](https://www.microsoft.com/bing/visual-search) | F | reverse/visual search |
| [Yandex Images](https://yandex.com/images/) | F | reverse/visual search |
| [TinEye](https://tineye.com/) | FM | reverse image search/history |
| [ExifTool](https://exiftool.org/) | OS/F | metadata extraction |
| [InVID Verification Plugin](https://weverify.eu/verification-plugin/) | F | image/video verification |
| [Forensically](https://29a.ch/photo-forensics/) | F | image inspection |
| [FotoForensics](https://fotoforensics.com/) | F | image artifact inspection |
| [FFmpeg](https://ffmpeg.org/) | OS | frame/audio/video extraction |
| [MediaInfo](https://mediaarea.net/en/MediaInfo) | OS | media metadata |
| [Bellingcat Shadow Finder](https://github.com/bellingcat/ShadowFinder) | OS | shadow/geolocation assistance |

## 8. Maps, geolocation and geospatial analysis

| Resource | Access | Best use |
|---|---:|---|
| [Google Maps](https://maps.google.com/) | F | places, roads, imagery |
| [Google Earth](https://earth.google.com/web/) | F | 3D/historical geospatial research |
| [OpenStreetMap](https://www.openstreetmap.org/) | F/OS | open map data |
| [Overpass Turbo](https://overpass-turbo.eu/) | F/OS | query OpenStreetMap features |
| [Mapillary](https://www.mapillary.com/) | F | street-level imagery |
| [KartaView](https://kartaview.org/) | F/OS | open street imagery |
| [Wikimapia](https://wikimapia.org/) | F | community map annotations |
| [GeoNames](https://www.geonames.org/) | F | geographic names/features |
| [SunCalc](https://www.suncalc.org/) | F | sun/shadow position |
| [PeakVisor](https://peakvisor.com/) | FM | terrain/mountain identification |
| [Geohack](https://geohack.toolforge.org/) | F | coordinate pivot hub |
| [What3words](https://what3words.com/) | FM | coordinate/location representation |

## 9. Satellite, earth observation and environment

| Resource | Access | Best use |
|---|---:|---|
| [Copernicus Data Space](https://dataspace.copernicus.eu/) | F/O | Sentinel imagery and EO data |
| [Sentinel Hub EO Browser](https://apps.sentinel-hub.com/eo-browser/) | FM | satellite imagery exploration |
| [NASA Worldview](https://worldview.earthdata.nasa.gov/) | F/O | global satellite layers |
| [USGS EarthExplorer](https://earthexplorer.usgs.gov/) | F/O | satellite/aerial datasets |
| [Google Earth Engine](https://earthengine.google.com/) | FM | planetary-scale geospatial analysis |
| [OpenTopography](https://opentopography.org/) | F | terrain/elevation |
| [Global Forest Watch](https://globalnaturewatch.org/) | F | forest/environment monitoring |
| [FIRMS](https://firms.modaps.eosdis.nasa.gov/) | F/O | active fire data |

## 10. Companies, organizations and public records

| Resource | Access | Best use |
|---|---:|---|
| [OpenCorporates](https://opencorporates.com/) | FM | company records across jurisdictions |
| [GLEIF LEI Search](https://www.gleif.org/en/lei-data/lei-search/about-lei-search/) | F/O | legal entity identifiers |
| [SEC EDGAR](https://www.sec.gov/edgar/search/) | F/O | US filings |
| [Companies House](https://find-and-update.company-information.service.gov.uk/) | F/O | UK companies |
| [OCCRP Aleph](https://aleph.occrp.org/) | F/FM | investigative records/entities |
| [ICIJ Offshore Leaks](https://offshoreleaks.icij.org/) | F | offshore entity records |
| [OpenSanctions](https://www.opensanctions.org/) | OS/FM | sanctions/PEP/entity datasets |
| [OpenOwnership](https://www.openownership.org/) | F/OS | beneficial ownership data |
| [World Bank Projects](https://projects.worldbank.org/en/projects-operations/projects-home) | F/O | project/procurement context |
| [EU TED](https://ted.europa.eu/) | F/O | European public procurement |

## 11. Aviation and maritime

| Resource | Access | Best use |
|---|---:|---|
| [ADS-B Exchange](https://www.adsbexchange.com/) | FM | aircraft tracking |
| [OpenSky Network](https://opensky-network.org/) | F/FM | air traffic research/API |
| [FlightRadar24](https://www.flightradar24.com/) | FM/P | aircraft tracking/history |
| [FlightAware](https://www.flightaware.com/) | FM/P | flights and airport data |
| [FAA Registry](https://registry.faa.gov/aircraftinquiry/) | F/O | US aircraft registration |
| [MarineTraffic](https://www.marinetraffic.com/) | FM/P | vessel tracking |
| [VesselFinder](https://www.vesselfinder.com/) | FM | vessel tracking |
| [Equasis](https://www.equasis.org/) | F/O | ship/company safety information |
| [Global Fishing Watch](https://globalfishingwatch.org/) | F | vessel activity and maritime analysis |

## 12. Documents, metadata and public files

| Resource | Access | Best use |
|---|---:|---|
| [ExifTool](https://exiftool.org/) | OS/F | metadata |
| [Apache Tika](https://tika.apache.org/) | OS | text/metadata extraction |
| [OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF) | OS | searchable PDFs |
| [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) | OS | OCR |
| [DocumentCloud](https://www.documentcloud.org/) | OS/FM | document publication/search |
| [Tabula](https://tabula.technology/) | OS | extract tables from PDFs |
| [pdfinfo / Poppler](https://poppler.freedesktop.org/) | OS | PDF metadata and structure |
| [CyberChef](https://gchq.github.io/CyberChef/) | OS/F | data decoding/transformation |

## 13. Academic, scientific and citation research

| Resource | Access | Best use |
|---|---:|---|
| [Google Scholar](https://scholar.google.com/) | F | scholarly discovery |
| [OpenAlex](https://openalex.org/) | F/OS | works/authors/institutions graph |
| [Semantic Scholar](https://www.semanticscholar.org/) | F | scholarly search |
| [Crossref](https://search.crossref.org/) | F/O | DOI/publication metadata |
| [CORE](https://core.ac.uk/) | F | open-access research |
| [PubMed](https://pubmed.ncbi.nlm.nih.gov/) | F/O | biomedical literature |
| [arXiv](https://arxiv.org/) | F | preprints |
| [ORCID](https://orcid.org/) | F/O | researcher identifiers |
| [OpenCitations](https://opencitations.net/) | F/OS | citation data |

## 14. Blockchain and public ledger research

| Resource | Access | Best use |
|---|---:|---|
| [Etherscan](https://etherscan.io/) | FM | Ethereum transactions/contracts |
| [Blockchair](https://blockchair.com/) | FM | multi-chain explorer |
| [Blockchain.com Explorer](https://www.blockchain.com/explorer) | F | Bitcoin and chain data |
| [mempool.space](https://mempool.space/) | OS/F | Bitcoin blocks/transactions |
| [Blockstream Explorer](https://blockstream.info/) | OS/F | Bitcoin explorer |
| [GraphSense](https://graphsense.info/) | OS | cryptocurrency analytics research stack |

## 15. Automation, frameworks and orchestration

| Resource | Access | Best use |
|---|---:|---|
| [SpiderFoot](https://github.com/smicallef/spiderfoot) | OS | automated OSINT modules |
| [Recon-ng](https://github.com/lanmaster53/recon-ng) | OS | modular reconnaissance framework |
| [sn0int](https://github.com/kpcyrd/sn0int) | OS | semi-automatic OSINT framework |
| [Maltego](https://www.maltego.com/) | FM/P | transforms and link analysis |
| [IntelOwl](https://github.com/intelowlproject/IntelOwl) | OS | multi-provider enrichment |
| [OpenCTI](https://github.com/OpenCTI-Platform/opencti) | OS | knowledge graph and CTI workflows |
| [MISP](https://github.com/MISP/MISP) | OS | structured threat-intelligence sharing |
| [Amass](https://github.com/owasp-amass/amass) | OS | attack-surface/domain mapping |
| [theHarvester](https://github.com/laramies/theHarvester) | OS | public-source domain/e-mail discovery |
| [subfinder](https://github.com/projectdiscovery/subfinder) | OS | passive subdomain discovery |

## 16. Graphs, timelines and analytical workspaces

| Resource | Access | Best use |
|---|---:|---|
| [Gephi](https://gephi.org/) | OS | graph analysis |
| [Cytoscape](https://cytoscape.org/) | OS | network visualization |
| [Neo4j](https://neo4j.com/) | FM/OS | graph database |
| [Obsidian](https://obsidian.md/) | FM | local research notes/links |
| [TimelineJS](https://timeline.knightlab.com/) | F/OS | narrative timelines |
| [Kumu](https://kumu.io/) | FM | relationship mapping |
| [OpenRefine](https://openrefine.org/) | OS | data cleaning/reconciliation |
| [Jupyter](https://jupyter.org/) | OS | reproducible analysis notebooks |

## 17. Monitoring, feeds and change detection

| Resource | Access | Best use |
|---|---:|---|
| [RSSHub](https://github.com/DIYgod/RSSHub) | OS | generate RSS from many sources |
| [Huginn](https://github.com/huginn/huginn) | OS | event/source monitoring workflows |
| [changedetection.io](https://github.com/dgtlmoon/changedetection.io) | OS | webpage change monitoring |
| [Visualping](https://visualping.io/) | FM/P | visual/page change alerts |
| [Google Alerts](https://www.google.com/alerts) | F | keyword/web monitoring |
| [Distill](https://distill.io/) | FM | webpage monitoring |

## 18. AI-assisted and agentic OSINT

This category changes quickly. Treat model output as **analysis assistance**, not source evidence.

| Resource | Access | Best use |
|---|---:|---|
| [Bellingcat OSINT tools](https://github.com/bellingcat) | OS | source-grounded utilities that can be composed into assisted workflows |
| [Awesome OSINT Repositories – Agentic AI](https://github.com/osintshifu/awesome-osint-repos) | OS | tracking newer agentic/MCP OSINT projects |
| [Data Commons](https://datacommons.org/) | F/O | structured public knowledge graph |
| [OpenAlex API](https://help.openalex.org/) | F | research graph for assisted literature/entity work |
| [Wikidata](https://www.wikidata.org/) | F/OS | structured entity graph |
| [OpenAI-independent MCP specification](https://modelcontextprotocol.io/) | F/OS | integration pattern for tool-aware research agents |

## 19. Regional packs

- [Brazil & LATAM](BRAZIL-LATAM.md)
- Future: Europe, MENA, APAC and Africa packs.
- Region-specific sources should prioritize official registries and public-data portals over scraped mirrors.

## 20. Ridd1kulusC0d3r projects

See [ECOSYSTEM.md](ECOSYSTEM.md) for the complete internal map.

### Fast routing

| You have... | Start with... |
|---|---|
| username | Mineiro → Sherlock/Maigret → platform-native verification |
| domain | RDAP/ICANN → crt.sh → Censys/Shodan/urlscan → archive |
| URL | urlscan → archive → VirusTotal/OTX → page/source verification |
| IP | RDAP/RIPEstat → ASN/BGP → Censys/Shodan → CTI sources |
| image | metadata → Lens/TinEye/Yandex → geolocation tools |
| company | official registry → OpenCorporates/GLEIF → filings/procurement |
| IOC | VirusTotal/OTX/ThreatFox → passive DNS/infrastructure → ATT&CK context |
| document | hash → metadata → OCR/text extraction → source provenance |
| location | OSM/Maps → street imagery → satellite → sun/terrain validation |

## Maintenance rule

A resource may be removed even if it is famous.

Reasons:

- dead/unreachable;
- abandoned with a better maintained replacement;
- unclear provenance;
- misleading results;
- no meaningful OSINT use;
- primarily duplicates another entry;
- creates more analyst risk than value.

The machine-readable subset lives in [../data/tools.csv](../data/tools.csv).
