import subprocess
import time
import threading
import argparse
from config_parser.rist_config_parser import RistConfigParser
from rist_in.rist_in import RistInApp
from rist_out.rist_out import RistOutApp
import utils.run_shell as run_shell
from grpc_app.grpc_app import GRPCServer

class RistApp:
    def __init__(self):
        self.configs = None
        self.rist_in = None
        self.rist_out = None
        self.shell_command_thread = None

    def start_rist_in(self):
        self.rist_in = RistInApp(self.configs)
        command = self.rist_in.get_rist_in_command()
        print("RIST In command:", command)
        self.shell_command_thread = run_shell.run_shell_command(command)

    def start_rist_out(self):
        self.rist_out = RistOutApp(self.configs)
        command = self.rist_out.get_rist_out_command()
        print("RIST Out command:", command)
        self.shell_command_thread = run_shell.run_shell_command(command)

    def stop_rist(self):
        if self.shell_command_thread:
            self.shell_command_thread.stop()
            self.shell_command_thread = None

    def is_rist_running(self):
        if self.shell_command_thread and not self.shell_command_thread.stopped():
            return True
        return False
    
    def update_grpc_rist_app(self, configs):
        self.configs = self.rist_config_parser.get_grpc_rist_application_configs(configs)
        self.stop_rist()
        if self.configs["rist_configs"]["input_type"] == "rist":
            self.start_rist_in()
        elif self.configs["rist_configs"]["input_type"] == "udp" or self.configs["rist_configs"]["input_type"] == "rtp":
            self.start_rist_out() 

    
    def start_grpc_rist_app(self, configs):
        self.configs = self.rist_config_parser.get_grpc_rist_application_configs(configs)
        if self.configs["rist_configs"]["input_type"] == "rist":
            self.start_rist_in()
        elif self.configs["rist_configs"]["input_type"] == "udp" or self.configs["rist_configs"]["input_type"] == "rtp":
            self.start_rist_out() 
    
    def start_rist_app(self):
        if self.configs["rist_configs"]["input_type"] == "rist":
            self.start_rist_in()
        elif self.configs["rist_configs"]["input_type"] == "udp" or self.configs["rist_configs"]["input_type"] == "rtp":
            self.start_rist_out() 


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='RIST Application')
    parser.add_argument('--config', type=str, help='Config file path')
    args = parser.parse_args()
    RistApp = RistApp()
    RistApp.rist_config_parser = RistConfigParser()

    if args.config is not None: 
        RistApp.configs = RistApp.rist_config_parser.get_rist_application_config()
        RistApp.start_rist_app()

    GRPCServer = GRPCServer(RistApp)
    GRPCServer.serve()


    # rist_app = RistApp(args.config)

    # if rist_app.configs["input_type"] == "rist":
    #     rist_app.start_rist_in()
    # else:
    #     rist_app.start_rist_out()

    # try:
    #     while True:
    #         time.sleep(1)
    # except KeyboardInterrupt:
    #     rist_app.stop_rist()
