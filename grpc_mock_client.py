import grpc
import grpc_app.rist_app_pb2 as rist_app_pb2
import grpc_app.rist_app_pb2_grpc as rist_app_pb2_grpc
import time

def run_client():
    # Establish a connection to the gRPC server
    channel = grpc.insecure_channel('127.0.0.1:50051')
    
    # Create a stub (client) for the RistApp service
    stub = rist_app_pb2_grpc.RistAppStub(channel)
    
    # Example: calling the StartRistApp RPC
    start_request = rist_app_pb2.RistAppconfig(InputType='rist', InputUrl='127.0.0.1', InputPort= "5678", Mode="server", OutputType = "udp", OutputUrl = "127.0.0.1", OutputPort = "8888" )
    start_response = stub.StartRistApp(start_request)
    print("StartRistApp Response:", start_response)

    time.sleep(5)
    status_request = rist_app_pb2.Empty()
    status_response = stub.StatusRistApp(status_request)
    print("StatusRistApp Response:", status_response)

    time.sleep(1)
    stop_request = rist_app_pb2.Empty()
    stop_response = stub.StopRistApp(stop_request)
    print("StopRistApp Response:", stop_response)

    time.sleep(5)
    status_request = rist_app_pb2.Empty()
    status_response = stub.StatusRistApp(status_request)
    print("StatusRistApp Response:", status_response)

    time.sleep(10)
    update_request = rist_app_pb2.RistAppconfig(InputType='udp', InputUrl='127.0.0.1', InputPort= "1234", Mode="client", OutputType = "rist", OutputUrl = "127.0.0.1", OutputPort = "5678" )
    update_response = stub.UpdateRistApp(update_request)
    print("UpdateRistApp Response:", update_response)

    time.sleep(5)
    status_request = rist_app_pb2.Empty()
    status_response = stub.StatusRistApp(status_request)
    print("StatusRistApp Response:", status_response)

if __name__ == "__main__":
    run_client()