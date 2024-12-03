from cryptography.fernet import Fernet

class EncryptionManager:
    KEY = b'5ZauLf3IZJI0W1lMBIPylwjfeckxqtmBSwenqyd_vao='

    @staticmethod
    def encrypt(data):
        f = Fernet(EncryptionManager.KEY)
        return f.encrypt(data.encode()).decode()

    @staticmethod
    def decrypt(data):
        f = Fernet(EncryptionManager.KEY)
        return f.decrypt(data.encode()).decode()
