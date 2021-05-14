import configparser as envParser

envParser = envParser.ConfigParser()
envParser.read('.env')

def env(key_name:str,section_name='MAIN'):
    return envParser.get(section_name,key_name,fallback=False)


my_key = env('key_1')
print(my_key)