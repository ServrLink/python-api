import urllib.request
import json

class ServrLink:

    def __init__(self, baseUrl):
        self.baseUrl = baseUrl
        if not baseUrl.endswith('/'):
            self.baseUrl += '/'

    def isRegisteredDiscord(self, id: str):
        '''
        :param id: Discord user ID
        :return:
          - Whether the query to the Registry was successful
          - Whether the registry contains the Discord user ID
        '''

        url = self.baseUrl + 'api/discord/isregistered?id=' + id
        with urllib.request.urlopen(url) as res:
            raw = res.read()
            parsed = json.loads(raw)

        return parsed['success'], parsed['registered']

    def isRegisteredMinecraft(self, uuid: str):
        '''
        :param uuid: Minecraft UUID
        :return:
          - Whether the query to the Registry was successful
          - Whether the registry contains the Minecraft UUID
        '''

        url = self.baseUrl + 'api/minecraft/isregistered?uuid=' + id
        with urllib.request.urlopen(url) as res:
            raw = res.read()
            parsed = json.loads(raw)

        return parsed['success'], parsed['registered']

    def getDiscordId(self, uuid: str):
        '''
        :param uuid: Minecraft UUID
        :return:
          - Whether the query to the Registry was successful
          - The Discord user ID
        '''

        url = self.baseUrl + 'api/minecraft/getid?uuid=' + uuid
        with urllib.request.urlopen(url) as res:
            raw = res.read()
            parsed = json.loads(raw)

        return parsed['success'], parsed['id']

    def getMinecraftUUID(self, id: str):
        '''
        :param id: The Discord user ID
        :return:
          - Whether the query to the Registry was successful
          - The Minecraft UUID
        '''

        url = self.baseUrl + 'api/discord/getuuid?id=' + id
        with urllib.request.urlopen(url) as res:
            raw = res.read()
            parsed = json.loads(raw)

        return parsed['success'], parsed['uuid']
