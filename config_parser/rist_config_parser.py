import configparser

class RistConfigParser:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config_dict = {}

    def _read_config(self, config_file):
        """
        Reads configuration from a config file.
        """
        self.config.read(config_file)

        # Read rist_sender section
        print(self.config)
        self.config_dict['rist_configs'] = {
            'input_type': self.config.get("rist_configs",'input_type'),
            'input_url': self.config.get("rist_configs",'input_url'),
            'input_port': self.config.getint( "rist_configs",'input_port'),
            'mode': self.config.get("rist_configs", 'mode'),
            'output_type': self.config.get("rist_configs", 'output_type'),
            'output_url': self.config.get("rist_configs", 'output_url'),
            'output_port': self.config.getint("rist_configs", 'output_port')
        }

    def get_rist_application_config(self, config_file):
        """
        Get RIST sender configuration parameters.
        """
        self._read_config(config_file)
        return self.config_dict

    def get_grpc_rist_application_configs(self, configs):
        profile = "0"
        encryption_type = ""
        secret = ""
        if configs.Profile:
            profile = configs.Profile
        if configs.Secret:
            secret = configs.Secret
        if configs.Encryption:
            encryption_type = configs.Encryption
        self.config_dict['rist_configs'] = {
            'input_type': configs.InputType, 
            'input_url': configs.InputUrl,
            'input_port': configs.InputPort,
            'mode': configs.Mode, 
            'output_type': configs.OutputType, 
            'output_url': configs.OutputUrl, 
            'output_port': configs.OutputPort,
            'profile': profile,
            'encryption': encryption_type,
            'secret': secret
        } 
        return self.config_dict

if __name__ == "__main__":
    config_file = "config.ini"
    parser = RistConfigParser(config_file)

    sender_config = parser.get_rist_sender_config()
    print("RIST Configuration:")
    print(f"Input Type: {sender_config['input_type']}")
    print(f"Input URL: {sender_config['input_url']}")
    print(f"Input Port: {sender_config['input_port']}")
    print(f"Mode: {sender_config['mode']}")
    print(f"Output Type: {sender_config['output_type']}")
    print(f"Output URL: {sender_config['output_url']}")
    print(f"Output Port: {sender_config['output_port']}")
    print()

