# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "28892113"))
    API_HASH = getenv("API_HASH", "dc4cb3e9a4144280688ee20415529b15")
    BOT_TOKEN = getenv("BOT_TOKEN", "8196038845:AAGA8OejoFEq23qrrQZ-Qn7kkmv24Yh4s5M")
    FSUB = getenv("FSUB", "ചെമ്പരത്തി")
    CHID = int(getenv("CHID", "-1002338834649."))
    SUDO = list(map(int, getenv("SUDO", "7600777042").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://amilmuhammed3:cHaUKJYudmXDICa4@cluster0.mbo75.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
