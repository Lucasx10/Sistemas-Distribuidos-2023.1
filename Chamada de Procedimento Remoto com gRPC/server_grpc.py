import subprocess
import grpc
import my_service_pb2
import my_service_pb2_grpc
from concurrent import futures
import logging

# Configurações do logger
logging.basicConfig(filename='server.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

class RemoteControlServicer(my_service_pb2_grpc.RemoteControlServicer):
    def ExecuteCommand(self, request, context):
        command = request.command
        logging.info(f'Command received: {command}')
        output = subprocess.check_output(request.command, shell=True)
        return my_service_pb2.CommandResponse(output=output.decode('utf-8'))

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    my_service_pb2_grpc.add_RemoteControlServicer_to_server(RemoteControlServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
