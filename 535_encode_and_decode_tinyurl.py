# -*- coding: utf-8 -*-
import uuid
class Codec:
    _map = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        code = uuid.uuid4().hex
        Codec._map[code] = longUrl
        return "http://tinyurl.com/{}".format(code)

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        code = shortUrl.replace("http://tinyurl.com/", "")
        return Codec._map[code]
