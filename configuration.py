import yaml


def get_config(parameter_type, parameter_name):
    with open("config.yml", 'r') as ymlfile:
        cfg = yaml.load(ymlfile)
    if parameter_type == 'db-params':
        return cfg['db-params'][parameter_name]
