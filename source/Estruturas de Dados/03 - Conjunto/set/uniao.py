conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}
conjunto_uniao = conjunto_a.union(conjunto_b)
print(conjunto_uniao)
print('---' * 10)
conjunto_sep = conjunto_a.intersection(conjunto_b)
print(conjunto_sep)
print('---' * 10)
conjunto_dif = conjunto_a.difference(conjunto_b)
print(conjunto_dif)
print('---' * 10)
conjunto_sim = conjunto_a.symmetric_difference(conjunto_b)
print(conjunto_sim)
print('---' * 10)
