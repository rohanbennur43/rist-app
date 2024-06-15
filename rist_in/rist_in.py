class RistInApp:
    def __init__(self,rist_in_configs):
        self.configs = rist_in_configs
    
    def get_rist_in_command(self):
        """
        Runs a RIST sender command to send data from an input URL to an output URL.

        :param input_url: The input URL (e.g., "udp://localhost:1234").
        :param output_url: The output URL (e.g., "rist://remote.server.com:5678").
        :return: Output of the command execution or error message.
        """
        # Construct the command
        if self.configs["rist_configs"]["mode"] == "client":
            rist_in_url = self.configs["rist_configs"]["input_url"]
        else:
            rist_in_url = "@"
        
        rist_in_endpoint = "rist://{}:{}".format(rist_in_url,self.configs["rist_configs"]["input_port"])

        output_endpoint = "{}://{}:{}".format(self.configs["rist_configs"]["output_type"],self.configs["rist_configs"]["output_url"],self.configs["rist_configs"]["output_port"])
        command = ['ristreceiver', '-i', rist_in_endpoint, '-o', output_endpoint,'-p', self.configs["rist_configs"]["profile"]]
        if self.configs["rist_configs"]["encryption"] != "" and self.configs["rist_configs"]["secret"] != "":
            command.extend(['-e', self.configs["rist_configs"]["encryption"], '-s', self.configs["rist_configs"]["secret"]])

        return command