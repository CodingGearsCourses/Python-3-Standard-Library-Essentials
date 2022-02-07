# --------------------------------
# CodingGears.io
# --------------------------------
# configparser

# TODO: Imports
import configparser

# TODO: Path to config file
config_file = "sample_data/data_config.ini"

# TODO: Create a config parser
parser = configparser.ConfigParser()

# TODO: Read ini file
parser.read(config_file)

# TODO: List sections
# print(parser.sections())

# TODO: Check if a section is present
# print("IBM section : {}".format(parser.has_section("ibm".lower())))
# print("Dev section : {}".format(parser.has_section("DEV".lower())))

# TODO: Accessing values
for section in parser.sections():
    print("Environment : {}".format(section))
    print("-" * 40)
    print("APP_DIR      : ", parser.get(section, "APP_DIR"))
    print("LOGS_DIR     : ", parser.get(section, "LOGS_DIR"))
    print("APP_LOG_FILE : ", parser.get(section, "APP_LOG_FILE"))
    print()
