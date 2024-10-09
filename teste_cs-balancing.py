def validando_nivel_cs(niveis_cs):
    for id_cs, nivel_cs in niveis_cs:
        if not (0 < id_cs < 1000) or not (0 < nivel_cs < 10000):
            raise ValueError("Os IDs de níveis e CS precisam estar entre 1 e 999 e entre 1 e 9999, respectivamente.")

def validando_nivel_cliente(niveis_cliente):
    for clientes in niveis_cliente:
        id_cliente, tamanho_cliente = clientes

        if not (0 < id_cliente < 1000000):
            raise ValueError("O ID do Cliente precisa estar entre 1 e 999999")
        
        if not (0 < tamanho_cliente < 100000):
            raise ValueError("O tamanho inserido é inválido") 

def validando_cs_indisponivel(ids_cs_indisponivel, maximo_indisponivel):
    if len(ids_cs_indisponivel) > maximo_indisponivel:
        raise ValueError(f"O número de CSs indisponíveis é maior que {maximo_indisponivel}.")

def clientes_distribuidos(niveis_cs, niveis_cliente, ids_cs_indisponivel):
    n = len(niveis_cs)
    m = len(niveis_cliente)
    
    if not (0 < n < 1000):
        raise ValueError("O número de CSs deve estar entre 1 e 999.")
    if not (0 < m < 1000000):
        raise ValueError("O número de clientes deve estar entre 1 e 999999.")

    validando_nivel_cs(niveis_cs)
    validando_nivel_cliente(niveis_cliente)
    validando_cs_indisponivel(ids_cs_indisponivel, n // 2)

    cs_disponiveis = [cs for cs in niveis_cs if cs[0] not in ids_cs_indisponivel]
    cs_disponiveis.sort(key=lambda cs: cs[1]) 
    contagem_clientes_cs = {cs_id: 0 for cs_id, _ in cs_disponiveis}
    
    for id_cliente, tamanho_cliente in niveis_cliente:
        for id_cs, nivel_cs in cs_disponiveis:
            if tamanho_cliente <= nivel_cs:
                contagem_clientes_cs[id_cs] += 1
                break  

    max_clientes = max(contagem_clientes_cs.values())
    cs_top_ids = [cs_id for cs_id, contagem in contagem_clientes_cs.items() if contagem == max_clientes]

    return cs_top_ids[0] if len(cs_top_ids) == 1 else 0

def customerSuccessBalancing(cs_levels, client_levels, unavailable_cs_ids):
    return clientes_distribuidos(cs_levels, client_levels, unavailable_cs_ids)

# Teste - customerSuccessBalancing
niveis_cs = [(1, 65), (2, 40)]
niveis_cliente = [(102, 30), (101, 20)]
ids_cs_indisponivel = [3]

resultado = customerSuccessBalancing(niveis_cs, niveis_cliente, ids_cs_indisponivel)
print(f"O CS que atende mais clientes é: {resultado}")
