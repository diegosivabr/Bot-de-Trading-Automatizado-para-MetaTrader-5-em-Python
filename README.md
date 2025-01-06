# Bot de Trading Automatizado para MetaTrader 5 em Python

Este projeto é um bot de trading automatizado desenvolvido em **Python**, projetado para operar no MetaTrader 5. Ele utiliza a biblioteca oficial `MetaTrader5` para conectar-se à plataforma, abrir e fechar posições com base em configurações pré-definidas para diferentes ativos e horários.  

⚠️ **Nota:** O sufixo `xx` nos símbolos dos ativos é utilizado porque este exemplo foi configurado para a corretora **4XC**. Caso utilize outra corretora, será necessário remover o `xx` ou ajustar os nomes dos ativos conforme as especificações da corretora em uso.  

## 📋 Funcionalidades

- **Conexão ao MetaTrader 5:** Inicializa e verifica a conexão com a plataforma.
- **Gerenciamento de posições:**  
  - Abertura automática de posições (compra ou venda) em horários definidos.  
  - Fechamento automático de posições ao final dos períodos configurados.  
- **Agendamento personalizado:** Configurações de horários específicos para abertura e fechamento de ordens para cada ativo.  
- **Suporte a múltiplos ativos:** Inclui exemplos de operações em Forex, índices, commodities, criptomoedas e mais.  

## 🔧 Configurações

Os ativos e seus parâmetros podem ser personalizados no dicionário `ativos`, incluindo:

- **Símbolo do ativo** (ex.: `GBPUSDxx`, `BTCUSDxx`).  
- **Volume da ordem** (ex.: 0.01).  
- **Tipo de ordem** (compra ou venda).  
- **Horários de abertura e fechamento de ordens**.  

## 🚀 Como Usar

1. Certifique-se de que o MetaTrader 5 esteja instalado e configurado no seu computador.  
2. Instale as dependências do projeto:  
   ```bash
   pip install MetaTrader5 schedule
   ```  
3. Edite as configurações no dicionário `ativos` de acordo com suas preferências.  
4. Execute o script Python para iniciar o bot:  
   ```bash
   python mt5.py
   ```  

## ⚠️ Avisos

- Este projeto é apenas para fins educacionais e de desenvolvimento. Teste em uma conta demo antes de usar em uma conta real.  
- Certifique-se de configurar os horários e volumes de forma responsável para evitar perdas financeiras significativas.  
- Não nos responsabilizamos por quaisquer perdas decorrentes do uso deste software.  

## 🛠 Tecnologias Utilizadas

- **Linguagem:** Python  
- **Bibliotecas:**  
  - `MetaTrader5` para integração com a plataforma de trading  
  - `schedule` para agendamento de tarefas  

## 📩 Contato

Se tiver dúvidas ou sugestões, entre em contato pelo e-mail: diego02071988@gmail.com  
