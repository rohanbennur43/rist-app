class RistOutApp:
    def __init__(self,rist_out_configs):
        self.configs = rist_out_configs
    
    def get_rist_out_command(self):
        """
        Runs a RIST sender command to send data from an input URL to an output URL.

        :param input_url: The input URL (e.g., "udp://localhost:1234").
        :param output_url: The output URL (e.g., "rist://remote.server.com:5678").
        :return: Output of the command execution or error message.
        """
        # Construct the command
        if self.configs["rist_configs"]["mode"] == "client":
            rist_out_url = self.configs["rist_configs"]["output_url"]
        else:
            rist_out_url = "@"
        
        rist_out_endpoint = "rist://{}:{}".format(rist_out_url,self.configs["rist_configs"]["output_port"])

        input_endpoint = "{}://{}:{}".format(self.configs["rist_configs"]["input_type"],self.configs["rist_configs"]["input_url"],self.configs["rist_configs"]["input_port"])

        command = ['ristsender', '-i', input_endpoint, '-o', rist_out_endpoint ,'-p', self.configs["rist_configs"["profile"]]]
        if self.configs["rist_configs"]["encryption"] != "" and self.configs["rist_configs"]["encryption"] != "":
            command.extend(['-e', self.configs["rist_configs"]["encryption"], '-s', self.configs["rist_configs"]["secret"]])
        return command