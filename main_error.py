import sys
clients = [
    {
        'name': 'as',
        'company': "Google",
        "email": "pablo@.com",
        "position": "software engineer"
    },
    {
        'name': 'Ricardo',
        'company': "Facebook",
        "email": "ricardo@.com",
        "position": "Data engineer"
    }
]


def list_clients(cliente_imprimir=None):
    if not cliente_imprimir:
        cliente_imprimir = clients

    for idx, client in enumerate(cliente_imprimir):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid=idx,
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position']
        ))


def search_client(client_name):

    for Client in clients:
        if Client['name'] != client_name:
            continue
        else:

            # _____ERROR_____
            # desde aca quiero enviar el cliente encontra a la funcion
            # list_clients para poder mostrar el cliente encontrado

            # Client= list(Client)
            # print(type(Client))
            print("_________Datos del cliente_____")
            # list_clients(Client)


def _print_welcome():
    print("_______Hola____")
    print("*" * 5)
    print("[B]uscar cliente")
    print("[L]ista de clientes")


if __name__ == "__main__":
    _print_welcome()
    command = input()
    command = command.upper()

    if command == "L":
        list_clients()

    elif command == "B":
        client_name = input('Nombre del cliente ')
        search_client(client_name)
    else:
        print('Invalid command')
