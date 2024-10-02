convidados = ['Darth Vader', 'Stanford Pinnes', 'Doctor Who']
print(f'{convidados[0]}, você está convidado para jantar comigo')
print(f'{convidados[1]}, você está convidado para jantar comigo')
print(f'{convidados[2]}, você está convidado para jantar comigo')

print(f'\nInfelizmente, {convidados[1]} não poderá comparecer')
convidados[1] = 'Rex'
print(f'\n{convidados[1]}, você está convidado para jantar comigo')

print(f'\n{convidados[0]}, {convidados[1]} e {convidados[2]} encontrei uma mesa maior, vou convidar mais pessoas')
convidados.insert(0, 'Aslan')
convidados.insert(2, 'Finn')
convidados.append('Jake')
print(f'{convidados[0]}, você está convidado para jantar comigo')
print(f'{convidados[2]}, você está convidado para jantar comigo')
print(f'{convidados[5]}, você está convidado para jantar comigo')