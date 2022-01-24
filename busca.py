dicidevs = {'php':'joao', 'java':'maria', 'python':'jairo'}

def busca():
    bus = input('Que dev vc busca: ')
    for ch, vl in dicidevs.items():
        if bus == ch:
            print(vl)
busca()


