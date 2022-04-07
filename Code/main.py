from configurator import Configurator

if __name__ == '__main__':
    conf = Configurator()

    # Read config (values from file or hard coded values if file doesn't exist)
    conf.read_config_file()

    # Using values from config
    a = conf.alpha

    # Changing values in config
    conf.bravo += 1

    # Save changed config to file
    conf.save_config_file()
