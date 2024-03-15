import psutil

def info_bateria():
    # Verifica se a bateria está presente
    if not psutil.sensors_battery():
        return "Bateria não encontrada"

    # Obtém informações sobre a bateria
    bateria = psutil.sensors_battery()

    # Calcula o tempo restante estimado
    tempo_restante = "Desconhecido" if bateria.power_plugged else f"{int(bateria.secsleft/60)} minutos"

    # Retorna a carga da bateria e o tempo restante estimado
    return f"Carga da bateria: {bateria.percent}%\nTempo restante estimado: {tempo_restante}"

# Exemplo de uso
print(info_bateria())
