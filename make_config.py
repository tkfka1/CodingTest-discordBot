import configparser

def config_generator():
    # 설정파일 만들기
    config = configparser.ConfigParser()

    # 설정파일 오브젝트 만들기
    config['system'] = {}
    config['system']['title'] = 'CodeTeacher'
    config['system']['version'] = '1.0.01'

    config['setting'] = {}
    config['setting']['application_id'] = 'LoremIpsum'
    config['setting']['public_key'] = 'LoremIpsum'
    config['setting']['server_id'] = 'LoremIpsum'
    config['setting']['cannel_id_1'] = 'LoremIpsum'
    config['setting']['prefix'] = '!'

    # 설정파일 저장
    with open('config.ini', 'w', encoding='utf-8') as configfile:
        config.write(configfile)

def config_read():
    
    # 설정파일 읽기
    config = configparser.ConfigParser()    
    config.read('config.ini', encoding='utf-8') 

    # 설정파일의 섹션 확인
    # config.sections())
    version_read(config)

## EX) 버전 타이틀 불러오기
def version_read(config):

    ver = config['system']['version']
    title = config['system']['title']
    print(title,ver)


config_generator()

