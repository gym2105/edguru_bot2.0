from tg_bot.sample_config import Config


class Development(Config):
    OWNER_ID = 881769564  # my telegram ID
    OWNER_USERNAME = "Gym2105"  # my telegram username
    API_KEY = "1070691487:AAGralX1p4P2lU1tMVSp1VrWc4vIB92H30g"  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = 'postgres://loikpzuqppyhys:27976126133aef1aad1376f0d43a2195831479b5f82ae452bcbd6539cc7abaec@ec2-3-228-114-251.compute-1.amazonaws.com:5432/d59029bsbkh2vk'  # sample db credentials
    MESSAGE_DUMP = '1001221946970' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    SUDO_USERS = [1261080659]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']
