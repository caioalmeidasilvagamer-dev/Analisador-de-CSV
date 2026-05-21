# 📊 LeadScan — Analisador Inteligente de Leads

Aplicação web desenvolvida em Python para analisar arquivos CSV exportados do Apify Google Places Scraper e categorizar automaticamente a presença digital dos leads.

O sistema identifica padrões de links, classifica os tipos de presença online e organiza os dados para facilitar processos de prospecção, automação e análise comercial.

---

## 🚀 Funcionalidades

- Upload de arquivos CSV
- Processamento automático de leads
- Classificação inteligente de links
- Identificação de presença digital
- Interface web simples e rápida
- Análise automatizada de dados exportados do Google Maps
- Tratamento automático de valores ausentes
- Organização dos dados processados

---

## 🔍 Categorias identificadas

### 🌐 Site Próprio

Domínios personalizados:

```text
empresa.com
empresa.com.br
```

### 📱 Redes Sociais

- Instagram
- Facebook
- LinkedIn
- TikTok
- X / Twitter

### 🛠️ Sites Gratuitos

- Wix
- WordPress
- Canva
- Webflow
- Notion
- Carrd

### 🔗 Encurtadores

- Linktree
- Bitly
- Linkr.bio
- Beacons

### 📺 Plataformas

- YouTube
- Spotify
- Twitch

### ❌ Sem Link

Leads sem presença online detectada.

---

## ⚙️ Tecnologias utilizadas

- Python 3
- Flask
- Pandas
- HTML
- CSS
- JavaScript

---

## 📦 Instalação

### Clonando o repositório

```bash
git clone https://github.com/caioalmeidasilvagamer-dev/LeadScan.git
```

Entre na pasta:

```bash
cd LeadScan
```

---

## 📥 Instalando dependências

### Windows CMD

```cmd
pip install flask pandas
```

### Windows PowerShell

```powershell
pip install flask pandas
```

### Linux

```bash
pip install flask pandas
```

### macOS

```zsh
pip install flask pandas
```

---

## ▶️ Executando a aplicação

### Windows CMD

```cmd
python app.py
```

### Windows PowerShell

```powershell
python app.py
```

### Linux

```bash
python3 app.py
```

### macOS

```zsh
python3 app.py
```

---

## 🌐 Acesso local

Abra no navegador:

```text
http://localhost:5000
```

Faça upload do CSV exportado do Apify e clique em:

```text
Analisar
```

---

## 📁 Estrutura do projeto

```bash
.
├── app.py
├── templates/
├── static/
├── uploads/
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🔄 Fluxo da aplicação

```text
CSV exportado do Apify
↓
Upload do arquivo
↓
Leitura dos dados
↓
Análise dos links
↓
Classificação automática
↓
Exibição dos resultados
```

---

## 🧠 Funcionalidades técnicas

- Identificação automática de padrões de URL
- Classificação baseada em regras
- Processamento de dados tabulares
- Manipulação de arquivos CSV
- Estrutura backend com Flask
- Upload e processamento de arquivos
- Organização modular da aplicação
- Tratamento de dados inconsistentes

---

## 🎯 Objetivo do projeto

O projeto foi criado para automatizar a análise de presença digital de empresas e facilitar processos de prospecção, qualificação de leads e automação comercial.

---

## 📚 Conceitos aplicados

- Manipulação de arquivos
- Processamento de dados
- Estruturação backend
- Desenvolvimento web
- Automação de processos
- Tratamento de strings
- Classificação de padrões
- Organização de código
- Integração entre frontend e backend
