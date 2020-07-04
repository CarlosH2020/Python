#  (IP, MASK, REDE, BROADCAST)

ip = input('Endereço IP:').split('.')
mask = input('Entre com a mascara de rede:').split('.')

broadcast, ip_rede = [], []


for i in range(len(ip)):
    ip_rede.append(int(ip[i]) & int(mask[i]))
    broadcast.append((~int(mask[i]) & 0xff) | int(ip_rede[i]))


print('_'*10, 'INFORMAÇÕES', '_'*10)
print('IP: %s.%s.%s.%s' % (ip[0], ip[1], ip[2], ip[3]))
print('Mascara: %s.%s.%s.%s' % (mask[0], mask[1], mask[2], mask[3]))
print('Rede: %d.%d.%d.%d' % (ip_rede[0], ip_rede[1], ip_rede[2], ip_rede[3]))
print('Broadcast: %d.%d.%d.%d' % (broadcast[0], broadcast[1], broadcast[2], broadcast[3]))
print('_'*33)
