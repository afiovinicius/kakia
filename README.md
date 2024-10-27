# Assistente Kakía

O Assistente Kakía é um assistente virtual desenvolvido em Python que permite interações por voz ou texto. Ele utiliza reconhecimento de voz, síntese de voz, e integração com um modelo de linguagem para responder a comandos.

## Funcionalidades

- **Reconhecimento de Voz:** Interaja com o assistente usando comandos de voz.
- **Pesquisa na Web:** Abra pesquisas no Google ou no YouTube.
- **Interação por Texto:** Insira comandos manualmente.
- **Integração com Modelos de Linguagem:** Utilize um modelo de linguagem para respostas a perguntas.
- **Varredura de dados:** Executa um web scraping para fazer uma coleta de dados simples com tópico e url específica.
- **Gera Imagens** Gera imagens em base de uma descrição objetiva e simples.

## Estrutura

```
|—— kakia/
|———— kak_ia/
|—————— components/
|———————— gtts.py
|———————— ptts.py
|———————— savescraped.py
|—————— core/
|———————— assistant.py
|———————— config.py
|———————— database.py
|—————— models/
|———————— scraped.py
|—————— modules/
|———————— caching.py
|———————— commands.py
|———————— logging.py
|———————— voicer.py
|———————— webscraping.py
|—————— schemas/
|———————— scraped.py
|—————— main.py
|———— .env-example
|———— .gitignore
|———— alembic.ini
|———— pyproject.toml
|———— README.md

```
