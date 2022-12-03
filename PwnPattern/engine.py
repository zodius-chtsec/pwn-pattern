import string
from itertools import combinations_with_replacement

class PatternEngine:
    def __init__(self, bad=None):
        self.payload = string.ascii_letters + string.digits + string.punctuation
        if bad:
            self.payload = self.payload.translate({
                ord(k): None for k in bad
            })
    
    def create_pattern(self, length):
        payload = ""
        for i, chunk in zip(range(length), combinations_with_replacement(self.payload, 3)):
            payload += "".join(chunk)
            if len(payload) >= length:
                return payload[:length]
