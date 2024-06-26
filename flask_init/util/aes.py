import json

from Crypto.Cipher import AES
import base64


class AES_encryption:
    """
    AES加密
    """
    BLOCK_SIZE = 16  # Bytes

    def __init__(self):
        self.pad = lambda s: s + (self.BLOCK_SIZE - len(s) % self.BLOCK_SIZE) * \
                             chr(self.BLOCK_SIZE - len(s) % self.BLOCK_SIZE)
        self.unpad = lambda s: s[:-ord(s[len(s) - 1:])]

    def aes_encode(self, key, data):
        '''
        AES的ECB模式加密方法
        :param key: 密钥
        :param data:被加密字符串（明文）
        :return:密文
        '''
        key = key.encode('utf8')
        # 字符串补位
        data = self.pad(data)
        cipher = AES.new(key, AES.MODE_ECB)
        # 加密后得到的是bytes类型的数据，使用Base64进行编码,返回byte字符串
        result = cipher.encrypt(data.encode())
        encodestrs = base64.b64encode(result)
        enctext = encodestrs.decode('utf8')
        return enctext

    def aes_decode(self, key, data):
        '''
        AES的ECB模式解密方法
        :param key: 密钥
        :param data: 加密后的数据（密文）
        :return:明文
        '''
        key = key.encode('utf8')
        data = base64.b64decode(data)
        cipher = AES.new(key, AES.MODE_ECB)

        # 去补位
        text_decrypted = self.unpad(cipher.decrypt(data))
        text_decrypted = text_decrypted.decode('utf8')
        return text_decrypted


if __name__ == '__main__':
    key = '12345678123456781234567812345678'  # 32位
    data = {
        'name': 'test'
    }
    aes = AES_encryption()
    result = aes.aes_encode(key, json.dumps(data))
    print(result)
    data = aes.aes_decode(key, result)
    print(data)
