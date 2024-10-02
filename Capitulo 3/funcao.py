compras = ['Alienware x17', 'Setup completo', 'Casa dos sonhos', 'Aston Martin Valhala', 'Viagens', 'Livros', 'Equipamentos para Hacking']
print(len(compras))
compras.append('A coisa mais cara do mundo')
print(compras)
desnecessario = compras.pop()
print(f'\nNão preciso disso: {desnecessario}\n')
compras.insert(3, 'Diamante')
compras.insert(4, 'Submarino')
print(compras)
del compras[3]
del compras[3] # Necessário ser duas vezes o 3 pois o 4 passa a ser o 3 depois que é removido o primeiro acima
compras.remove('Alienware x17')
print(compras)

print(f'\nEm ordem alfabetica temporaria: {sorted(compras)}')
print(f'Em ordem alfabetica inversa temporaria: {sorted(compras, reverse=True)}')
compras.reverse()
print(compras)
compras.reverse()
print(compras)
compras.sort()
print(f'Em ordem alfabética permanente: {compras}')
compras.sort(reverse=True)
print(f'Em ordem alfabética inversa permanente: {compras}')