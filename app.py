import configparser as envParser

envParser = envParser.ConfigParser()
envParser.read('.env')

def env(key_name:str):
    print(envParser.get('MAIN',key_name))


env('key_1')