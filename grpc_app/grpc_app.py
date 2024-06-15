from concurrent import futures
import grpc
import grpc_app.rist_app_pb2 as rist_app_pb2
import grpc_app.rist_app_pb2_grpc as rist_app_pb2_grpc

# Define the service class by inheriting from the generated RistAppServicer
class RistAppServicer(rist_app_pb2_grpc.RistAppServicer):
    def __init__(self, rist_app):
        self.rist_app = rist_app

    def StartRistApp(self, request, context):
        # Implement your logic here
        self.rist_app.stop_rist()
        self.rist_app.start_grpc_rist_app(request)
        ret = self.rist_app.is_rist_running()
        response = rist_app_pb2.AppStatusResponse(app_status=rist_app_pb2.AppResponse.RUNNING)
        if not ret:
           response = rist_app_pb2.AppStatusResponse(app_status=rist_app_pb2.AppResponse.UNKNOWN)
        return response

    def StopRistApp(self, request, context):
        self.rist_app.stop_rist()
        ret = self.rist_app.is_rist_running()
        response = rist_app_pb2.AppStatusResponse(app_status=rist_app_pb2.AppResponse.STOPPED)
        if ret:
           response = rist_app_pb2.AppStatusResponse(app_status=rist_app_pb2.AppResponse.UNKNOWN)
        return response

    def StatusRistApp(self, request, context):
        # Implement your logic here
        ret = self.rist_app.is_rist_running()
        response = rist_app_pb2.AppStatusResponse(app_status=rist_app_pb2.AppResponse.RUNNING)
        if not ret:
            response = rist_app_pb2.AppStatusResponse(app_status=rist_app_pb2.AppResponse.STOPPED)
        return response

    def UpdateRistApp(self, request, context):
        # Implement your logic here
        ret = self.rist_app.update_grpc_rist_app(request)
        ret = self.rist_app.is_rist_running()
        response = rist_app_pb2.AppStatusResponse(app_status=rist_app_pb2.AppResponse.SUCCESSFULL_UPDATE)
        if not ret:
           response = rist_app_pb2.AppStatusResponse(app_status=rist_app_pb2.AppResponse.UNKNOWN)
        return response

# Function to start the server
class GRPCServer():
    def __init__(self, RistApp):
        self.RistApp = RistApp


    def serve(self):
        rist_app_servicer = RistAppServicer(self.RistApp)
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        rist_app_pb2_grpc.add_RistAppServicer_to_server(rist_app_servicer, server)
        server.add_insecure_port('127.0.0.1:50051')
        print("started server")
        server.start()
        server.wait_for_termination()

if __name__ == '__main__':
    serve()
