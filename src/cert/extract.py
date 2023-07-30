import OpenSSL
import ssl
from urllib.parse import urlparse

class Extract:
    @staticmethod
    def extract_host_port(url: str):
        port = 443
        parsed_url = urlparse(url)
        host = parsed_url.hostname
        if parsed_url.port:
            port = parsed_url.port

        return host, port


    @staticmethod
    def pem_to_x509(cert_data: str):
        return OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, str.encode(cert_data))


    def fetch_ssl(self, url: str):
        host, port = self.extract_host_port(url)
        result = {}
        connection = ssl.create_connection((host, port))
        context = ssl.SSLContext()
        sock = context.wrap_socket(connection, server_hostname=url)
        server_certificate = self.pem_to_x509(ssl.DER_cert_to_PEM_cert(sock.getpeercert(True)))

        altnames = ''
        for extension_id in range(0, server_certificate.get_extension_count()):
            extension = server_certificate.get_extension(extension_id)
            if 'subjectAltName' in str(extension.get_short_name()):
                altnames = extension.__str__()
        result['name'] = url.replace("https://","")
        result['subject'] = str(server_certificate.get_subject()).replace("<X509Name object '", "").replace("'>", "")
        result['notBefore'] = server_certificate.get_notBefore().decode()
        result['notAfter'] = server_certificate.get_notAfter().decode()
        result['issuer'] = str(server_certificate.get_issuer()).replace("<X509Name object '", "").replace("'>", "")
        result['extension_count'] = server_certificate.get_extension_count()
        result['subjectAltName'] = altnames

        sock.close()
        return result
