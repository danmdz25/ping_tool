import os

print("#"* 55)

ip_ou_host= input("Digite o IP ou Host a ser verificado(envio de request): ")

print("-"* 55)

os.system(f'ping -n 5 {ip_ou_host}')

print("-"* 55)