# CoinSenseAI 💹

## 📌 Overview
The **AI Crypto Portfolio Assistant** is an intelligent crypto analysis tool that helps users make informed investment decisions.  
It uses **CrewAI/LangChain agents** to perform real-time **fundamental** and **technical** analysis on cryptocurrencies, powered by the **CoinGecko API**.  

This project was built as part of the **AI Bootcamp (atomcamp x NUST) Capstone Project**, demonstrating an end-to-end agentic application with:
- **Gradio UI** frontend
- **FastAPI backend**
- **CrewAI agent layer**
- **Live deployment** on Hugging Face Spaces / Replit
- **Secure secrets management** for API keys

---

## 🎯 Problem Statement
Cryptocurrency investors often struggle to:
- Track **real-time market trends**
- Understand **technical indicators** (RSI, MACD, Moving Averages)
- Filter out **fake news and hype-based speculation**

Our AI assistant solves this by providing **clear, data-backed insights** and **automated portfolio rebalancing suggestions**.

---

## 🚀 Features
- 📊 **Real-Time Crypto Data** – Fetches market prices, volume, and market cap from CoinGecko.
- 📈 **Technical Analysis** – Calculates RSI, MACD, and Moving Averages.
- 🤖 **AI Insights** – CrewAI agent explains market trends and suggests actions.
- 🔄 **Portfolio Rebalancing** – Automatically suggests allocation changes.
- 📅 **Historical Analysis** – Uses CoinGecko historical data for better trend prediction.
- 📰 **News Sentiment Analysis** – Detects FUD, hype, or neutral market news.

---

## 🛠️ Tech Stack
| Layer         | Tool/Framework |
|---------------|---------------|
| **Frontend**  | Gradio |
| **Backend**   | FastAPI |
| **Agent Layer** | CrewAI / LangChain |
| **Data API**  | CoinGecko API |
| **Deployment**| Hugging Face Spaces / Replit |
| **Secrets**   | `python-dotenv` |

---

## 🖥️ Architecture Diagram
```mermaid
flowchart LR
    U[User] -->|Inputs Coin/Portfolio| G[Gradio UI]
    G -->|Request| F[FastAPI Backend]
    F -->|Calls Agent| A[CrewAI/LangChain Agent]
    A -->|Fetch Data| C[CoinGecko API]
    A -->|Process Data| TA[Technical Indicators]
    A -->|Generate Response| F
    F -->|Output| G
    G -->|Displays| U
