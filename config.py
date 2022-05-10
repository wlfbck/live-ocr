import configparser

# https://docs.python.org/3/library/configparser.html


config = configparser.ConfigParser()
config.read('config.ini')
upper_left_x = int(config['DEFAULT']['upperLeftX'])
upper_left_y = int(config['DEFAULT']['upperLeftY'])
lower_right_x = int(config['DEFAULT']['lowerRightX'])
lower_right_y = int(config['DEFAULT']['lowerRightY'])
host = config['DEFAULT']['host']
port = int(config['DEFAULT']['port'])
