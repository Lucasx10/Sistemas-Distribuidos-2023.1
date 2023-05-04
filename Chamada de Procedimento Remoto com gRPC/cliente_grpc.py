import grpc
import click
import my_service_pb2
import my_service_pb2_grpc

@click.command()
@click.option('--server', default='localhost:50051', help='O endereço do servidor gRPC')
def execute_command(server):
    channel = grpc.insecure_channel(server)
    stub = my_service_pb2_grpc.RemoteControlStub(channel)
    while True:
        command = input('Digite o comando que deseja executar: ')
        response = stub.ExecuteCommand(my_service_pb2.CommandRequest(command=command))
        print(response.output)

if __name__ == '__main__':
    execute_command()
