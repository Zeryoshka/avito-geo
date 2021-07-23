from time import sleep

from serdis_client import Serdis

client = Serdis()

print(client.set('key1', 'val'))
print(client.get('key1'))
print(client.get('key2'))
print(client.lset('key1', ['1', '2', '3']))
print(client.lset('key2', ['1', '2', '3']))
print(client.set('key1', "string", ttl=4))
print(client.get('key1'))
sleep(5)
print(client.get('key1'))
