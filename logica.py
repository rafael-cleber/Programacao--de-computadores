from datetime import datetime

despesas = []

def adicionar_despesa(valor, data, status):
    try:
        valor = float(valor)
        data = datetime.strptime(data, '%d/%m/%Y').date()
    except ValueError:
        raise ValueError("Valor ou data inválidos.")

    despesas.append({
        'valor': valor,
        'data': data,
        'status': status
    })


def listar_despesas():
    return despesas


def totais_por_status():
    total_pagas = sum(d['valor'] for d in despesas if d['status'] == "Paga")
    total_pendentes = sum(d['valor'] for d in despesas if d['status'] == "Pendente")
    return total_pagas, total_pendentes

