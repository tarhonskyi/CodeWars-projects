def are_coprime(n, m):
    n_facrots = []
    m_factors = []
    same = []
    max_number = max(n, m)
    i = 1
    while i <= max_number:
        if n % i == 0:
            n_facrots.append(i)
        if m % i == 0:
            m_factors.append(i)
        i += 1
        same = list(set(n_facrots) & set(m_factors))
    if same == [1]:
        return True, f'The numbers were {n} and {m}'
    else:
        return False, f'The numbers were {n} and {m}'


print(are_coprime(20, 27))
print(are_coprime(12, 39))
