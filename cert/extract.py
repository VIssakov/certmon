import OpenSSL
import ssl
#import json

class Extract:
    #@staticmethod
    #def extract_port(url: str): pass

    @staticmethod
    def pem_to_x509(cert_data: str):
        return OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, str.encode(cert_data))

    def fetch_ssl(self, url: str):
        result = {}
        connection = ssl.create_connection((url, 443))
        context = ssl.SSLContext()
        sock = context.wrap_socket(connection, server_hostname=url)
        server_certificate = self.pem_to_x509(ssl.DER_cert_to_PEM_cert(sock.getpeercert(True)))
        ### fullfill dict
        result['subject'] = server_certificate.get_subject()
        result['notBefore'] = server_certificate.get_notBefore().decode()
        result['notAfter'] = server_certificate.get_notAfter().decode()
        result['issuer'] = server_certificate.get_issuer()
        result['extension_count'] = server_certificate.get_extension_count()
        ###
        sock.close()
        #return json.dumps(result)
        return result
