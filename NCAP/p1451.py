import requests
import csv

class NCAP():
    def __init__(self, ep, usr, pwd):
        self.sigfox_endpoint = ep                           # Sigfox API endpoint (default=V2)
        self.usr = usr                                      # api user
        self.pwd = pwd                                      # api password

    def read_stored_teds(self, path):
        try:
            with open(path, mode='r') as infile:
                reader = csv.reader(infile)
                stored_teds_dict = {rows[1]: rows[4] for rows in reader}

            self.stored_teds = stored_teds_dict
        except:
            print("Error occured while reading TEDS")

        print('Stored ID read')

    def get_device(self, id):
        x = requests.get(self.sigfox_endpoint + 'devices/' + id,
                         auth=(self.usr, self.pwd))
        raw_info = x.json()

        self.dev_teds = {}
        self.dev_teds['id'] = raw_info['id']
        self.dev_teds['pac'] = raw_info['pac']
        devtype_id = raw_info['deviceType']['id']
        self.get_devtype(devtype_id)
        ##self.get_enc(id)


    def get_devtype(self, dtid):
        x = requests.get(self.sigfox_endpoint + 'device-types/' + dtid,
                         auth=(self.usr, self.pwd))
        raw_info = x.json()
        self.dev_teds['keepalive'] = raw_info['keepAlive']
        self.dev_teds['downlink'] = raw_info['downlinkMode']
        self.dev_teds['payloadtype'] = raw_info['payloadType']

    def verify(self, id, path):
        ##Reading TEDS
        print("Verifying device "+id+ " to TEDS "+path)

        try:
            self.read_stored_teds(path)
            print("Stored TEDS read: "+ str(self.stored_teds))
        except:
            print("ERROR occurred reading TEDS")
            return 0

        ##Retrieving Device
        try:
            self.get_device(id)
            print("Device "+ id+ " retrieved." + str(self.dev_teds))
        except:
            print("Devive "+id + " cannot be retrieved from Sigfox Cloud")
            print("---")
            return 0

        ##Verification
        verified = True
        checklist = [ 'id','pac','downlink','keepalive', 'payloadtype']         #The list of verification
        for item in checklist:
            try:
                if (str(self.dev_teds[item]) == str(self.stored_teds[item])):
                    print("Field [" + item + "] V")
                else:
                    print("Field [" + item + "] X")
                    verified = False
                    break
            except:
                print("ERROR occurred verifying the field: "+ item)
                return 0

        if verified:
            print("Device "+ id + " verified")
        else:
            print("Device "+ id + " not verified")

        print("---")

'''
    def get_enc(self, id, pac):
        x = requests.get(self.sigfox_endpoint + 'device/' + id + "/product-certificate",
                         auth=(self.usr, self.pwd),
                         params={'pac':pac})
        raw_info = x.json()
        print(raw_info)
        if raw_info['encryptionPayload']:
            self.dev_teds.encryption = '1'
        else:
            self.dev_teds.encryption = '0'
'''




