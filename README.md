# 📊 LeadScan — Analisador de Leads

Aplicação web que analisa arquivos CSV exportados do Apify (Google Places Scraper) e categoriza automaticamente os leads por tipo de presença online.

## 🔍 Categorias

- **Site Próprio** — domínio próprio (.com, .com.br, etc.)
- **Redes Sociais** — Instagram, Facebook, LinkedIn, TikTok
- **Site Grátis** — Wix, WordPress, Canva, Webflow, etc.
- **Encurtadores** — Linktree, Bitly, Linkr.bio, etc.
- **Sem Link** — nenhuma presença online encontrada
- **Plataformas** — YouTube, Spotify, Twitch, etc.

## 🚀 Como usar

1. Clone o repositório
2. Instale as dependências:
```bash
   pip install flask pandas
```
3. Rode a aplicação:
```bash
   python app.py
```
4. Acesse `http://localhost:5000`, carregue seu CSV e clique em **Analisar**

## 🛠️ Tecnologias

- Python 3
- Flask
- Pandas
- HTML/CSS/JavaScript