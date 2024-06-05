# The 'Config' class is the base configuration class, which includes common settings
class Config(object):
    DEBUG = True  # Debug mode is enabled
    TESTING = False  # Testing mode is disabled

# The 'DevelopmentConfig' class inherits from 'Config' and overrides the SECRET_KEY setting
class DevelopmentConfig(Config):
    SECRET_KEY = "this-is-a-super-secret-key"  # The secret key for development environment

# The 'config' dictionary maps the environment names to their respective configuration classes
config = {
    'development': DevelopmentConfig,  # Configuration for development environment
    'testing': DevelopmentConfig,  # Configuration for testing environment
    'production': DevelopmentConfig  # Configuration for production environment
}

## Enter your Open API Key here
# This is a comment to remind users to input their Open AI API key in this variable
OPENAI_API_KEY = ''  # User-defined Open AI API key
