from hashlib import sha3_256
import re

class Funcoes(object):

    @staticmethod
    def cifraSenha(senha):
        return sha3_256(senha.encode('utf-8')).hexdigest()
    
    @staticmethod
    def removerCaracteresEspeciais(s):
        return re.sub(r'[^0-9]', '', s)