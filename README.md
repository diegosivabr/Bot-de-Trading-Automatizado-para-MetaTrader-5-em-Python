# Bot de Trading Automatizado para MetaTrader 5 em Python  

Este projeto é um bot de trading automatizado desenvolvido em **Python**, projetado para operar no MetaTrader 5. Ele utiliza a biblioteca oficial `MetaTrader5` para conectar-se à plataforma, abrir e fechar posições com base em configurações pré-definidas para diferentes ativos e horários.  

⚠️ **Nota:** O sufixo `xx` nos símbolos dos ativos é utilizado porque este exemplo foi configurado para a corretora **4XC**. Caso utilize outra corretora, será necessário remover o `xx` ou ajustar os nomes dos ativos conforme as especificações da corretora em uso.  

## 📋 Funcionalidades  

- **Conexão ao MetaTrader 5:** Inicializa e verifica a conexão com a plataforma.  
- **Gerenciamento de posições:**  
  - Abertura automática de posições (compra ou venda) em horários definidos.  
  - Fechamento automático de posições ao final dos períodos configurados.  
- **Regras personalizadas para abertura de posições:** Configuração baseada em sessões de mercado globais (asiática, europeia e americana) e comportamento histórico dos ativos.  
- **Suporte a múltiplos ativos:** Inclui exemplos de operações em Forex, índices, commodities, criptomoedas e mais.  

## 🔍 Regras de Abertura de Posições  

As posições são abertas com base nas características e horários das sessões globais de mercado, bem como no comportamento típico de cada ativo. Alguns exemplos:  

- **Forex:**  
  - `GBPUSDxx` (Venda): Operado durante a sessão europeia, aproveitando a alta volatilidade e oportunidades de venda entre 05:30 e 10:00.  
  - `USDJPYxx` (Compra): Configurado para a abertura da sessão asiática, de 00:00 a 03:00.  
  - `AUDUSDxx` (Venda): Venda programada durante o início da sessão asiática, de 22:00 a 02:00.  

- **Índices:**  
  - `DAX40xx` e `FTSE100xx` (Venda): Operações configuradas para aproveitar o movimento de venda durante a manhã europeia (07:00 a 10:30).  
  - `SP500xx` e `NASDAQxx` (Compra): Entrada no início ou meio da sessão americana (13:30 a 17:00), onde a volatilidade aumenta.  

- **Commodities:**  
  - `XAUUSDxx` (Ouro) e `XAGUSDxx` (Prata): Ordens de compra alinhadas com a transição entre as sessões europeia e americana (11:00 a 16:00).  
  - `USOILxx` (Petróleo): Venda programada para o início da sessão americana (13:00 a 16:00).  

- **Criptomoedas:**  
  - `BTCUSDxx`, `ETHUSDxx` e `LTCUSDxx` (Compra): Operações configuradas para a madrugada (00:00 a 05:00), período caracterizado por maior volatilidade no mercado cripto.  

Essas regras são definidas no dicionário `ativos`, onde você pode personalizar os horários, volumes e tipos de ordens conforme sua estratégia ou preferências.  

## 🔧 Configurações  

Os ativos e seus parâmetros podem ser personalizados no dicionário `ativos`, incluindo:  

- **Símbolo do ativo** (ex.: `GBPUSDxx`, `BTCUSDxx`).  
- **Volume da ordem** (ex.: 0.01).  
- **Tipo de ordem** (compra ou venda).  
- **Horários de abertura e fechamento de ordens**.  

⚠️ **Importante:** O bot utiliza o horário local do computador para operar. Certifique-se de que o relógio do sistema está sincronizado corretamente. O horário de Brasília está configurado como **GMT-3**. Se você estiver em outro fuso horário, ajuste os horários das ordens no dicionário `ativos` para refletir o fuso horário local.  

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

