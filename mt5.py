import MetaTrader5 as mt5
import schedule
import time

# Conexão com o MetaTrader 5
if not mt5.initialize():
    print("Erro ao inicializar MetaTrader 5:", mt5.last_error())
    quit()

print("Conectado ao MetaTrader 5")

# Constantes de tipo de ordem
ORDER_BUY = 0
ORDER_SELL = 1

# Configurações dos ativos e horários
ativos = [
    {"ativo": "GBPUSDxx", "volume": 0.01, "tipo_ordem": "venda", "horario_abrir": "05:30", "horario_fechar": "10:00"},  # Forex: venda durante a sessão europeia.
    {"ativo": "USDJPYxx", "volume": 0.01, "tipo_ordem": "compra", "horario_abrir": "00:00", "horario_fechar": "03:00"},  # Forex: compra na abertura da sessão asiática.
    {"ativo": "AUDUSDxx", "volume": 0.01, "tipo_ordem": "venda", "horario_abrir": "22:00", "horario_fechar": "02:00"},  # Forex: venda na sessão asiática.
    {"ativo": "DAX40xx", "volume": 0.01, "tipo_ordem": "venda", "horario_abrir": "07:00", "horario_fechar": "10:30"},  # Índice alemão: venda durante a sessão europeia.
    {"ativo": "FTSE100xx", "volume": 0.01, "tipo_ordem": "venda", "horario_abrir": "07:00", "horario_fechar": "10:30"},  # Índice britânico: venda durante a sessão europeia.
    {"ativo": "SP500xx", "volume": 0.01, "tipo_ordem": "compra", "horario_abrir": "13:30", "horario_fechar": "16:00"},  # Índice dos EUA: compra no início da sessão americana.
    {"ativo": "NASDAQxx", "volume": 0.01, "tipo_ordem": "compra", "horario_abrir": "14:00", "horario_fechar": "17:00"},  # Índice tecnológico dos EUA: compra durante a tarde na sessão americana.
    {"ativo": "XAUUSDxx", "volume": 0.01, "tipo_ordem": "compra", "horario_abrir": "12:30", "horario_fechar": "16:00"},  # Ouro: compra na transição da sessão europeia para americana.
    {"ativo": "USOILxx", "volume": 0.01, "tipo_ordem": "venda", "horario_abrir": "13:00", "horario_fechar": "16:00"},  # Petróleo: venda durante o início da sessão americana.
    {"ativo": "XAGUSDxx", "volume": 0.01, "tipo_ordem": "compra", "horario_abrir": "11:00", "horario_fechar": "15:00"},  # Prata: compra durante a transição para a sessão americana.
    {"ativo": "BTCUSDxx", "volume": 0.01, "tipo_ordem": "compra", "horario_abrir": "00:00", "horario_fechar": "05:00"},  # Bitcoin: compra na madrugada (alta volatilidade).
    {"ativo": "ETHUSDxx", "volume": 0.01, "tipo_ordem": "compra", "horario_abrir": "00:00", "horario_fechar": "05:00"},  # Ethereum: compra na madrugada (alta volatilidade).
    {"ativo": "EURUSDxx", "volume": 0.01, "tipo_ordem": "compra", "horario_abrir": "05:00", "horario_fechar": "10:00"},  # Forex: compra durante a abertura da sessão europeia.
    {"ativo": "LTCUSDxx", "volume": 0.01, "tipo_ordem": "compra", "horario_abrir": "00:00", "horario_fechar": "05:00"},  # Litecoin: compra na madrugada (alta volatilidade).
    
    # Novos ativos sugeridos para análise:
    {"ativo": "NZDUSDxx", "volume": 0.01, "tipo_ordem": "venda", "horario_abrir": "21:00", "horario_fechar": "01:00"},  # Forex: venda na sessão asiática.
    {"ativo": "EURGBPxx", "volume": 0.01, "tipo_ordem": "compra", "horario_abrir": "06:00", "horario_fechar": "09:00"},  # Forex: compra na sessão europeia.
    {"ativo": "USDCHFxx", "volume": 0.01, "tipo_ordem": "compra", "horario_abrir": "12:00", "horario_fechar": "15:00"},  # Forex: compra durante a transição para a sessão americana.
    {"ativo": "GER40xx", "volume": 0.01, "tipo_ordem": "venda", "horario_abrir": "08:00", "horario_fechar": "11:00"},  # Índice alemão: venda durante a manhã europeia.
    {"ativo": "WTIxx", "volume": 0.01, "tipo_ordem": "compra", "horario_abrir": "14:00", "horario_fechar": "17:00"},  # Petróleo (WTI): compra no pico da sessão americana.
    {"ativo": "SILVERxx", "volume": 0.01, "tipo_ordem": "compra", "horario_abrir": "09:00", "horario_fechar": "12:00"},  # Prata: compra na manhã europeia.
    {"ativo": "DOGEUSDxx", "volume": 0.01, "tipo_ordem": "compra", "horario_abrir": "02:00", "horario_fechar": "06:00"},  # Dogecoin: compra em horários de baixa volatilidade.
]


# Função para abrir uma posição
def abrir_posicao(ativo, volume, tipo_ordem):
    """Abre uma posição de compra ou venda."""
    if not mt5.market_book_add(ativo):
        print(f"Mercado fechado ou símbolo {ativo} indisponível.")
        return

    order_type = ORDER_BUY if tipo_ordem == "compra" else ORDER_SELL
    symbol_info = mt5.symbol_info(ativo)

    if not symbol_info:
        print(f"Erro ao obter informações do ativo {ativo}.")
        return

    # Obter preços de mercado
    symbol_tick = mt5.symbol_info_tick(ativo)
    if not symbol_tick:
        print(f"Erro ao obter os ticks do ativo {ativo}.")
        return

    price = symbol_tick.ask if tipo_ordem == "compra" else symbol_tick.bid

    # Montar a solicitação de ordem
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": ativo,
        "volume": volume,
        "type": order_type,
        "price": price,
        "deviation": 10,
        "magic": 7859,
        "comment": "diego02071988@gmail.com",
    }

    result = mt5.order_send(request)
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print(f"Erro ao enviar ordem para {ativo}: Retcode: {result.retcode}, Detalhes: {result}")
    else:
        print(f"Ordem enviada com sucesso: {ativo}, Tipo: {tipo_ordem}, Volume: {volume}")

# Função para fechar posições
def fechar_posicoes(ativo):
    """Fecha todas as posições abertas para o ativo."""
    positions = mt5.positions_get(symbol=ativo)  # Obtém todas as posições abertas do ativo
    if positions is None or len(positions) == 0:
        print(f"Nenhuma posição aberta para {ativo}")
        return

    for position in positions:
        # Determina o tipo de ordem inversa para fechar a posição
        order_type = ORDER_SELL if position.type == ORDER_BUY else ORDER_BUY
        price = (
            mt5.symbol_info_tick(ativo).bid if order_type == ORDER_SELL else mt5.symbol_info_tick(ativo).ask
        )

        # Monta a solicitação para fechar a posição
        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": position.symbol,
            "volume": position.volume,  # Usa o volume da posição existente
            "type": order_type,
            "price": price,
            "deviation": 10,
            "magic": 123456,
            "comment": "Fechamento automático",
            "position": position.ticket,  # Especifica o ticket da posição a ser fechada
        }

        # Envia a ordem para fechar a posição
        result = mt5.order_send(request)
        if result.retcode != mt5.TRADE_RETCODE_DONE:
            print(f"Erro ao fechar posição para {ativo}: Retcode: {result.retcode}, Detalhes: {result}")
        else:
            print(f"Posição fechada com sucesso: {ativo}, Volume: {position.volume}")

# Agendamento
for ativo in ativos:
    schedule.every().day.at(ativo["horario_abrir"]).do(
        abrir_posicao, ativo=ativo["ativo"], volume=ativo["volume"], tipo_ordem=ativo["tipo_ordem"]
    )
    schedule.every().day.at(ativo["horario_fechar"]).do(
        fechar_posicoes, ativo=ativo["ativo"]
    )

# Loop principal
print("Bot de trading iniciado...")
while True:
    try:
        schedule.run_pending()
        time.sleep(1)
    except Exception as e:
        print(f"Erro inesperado: {e}")
