import ssl
import socket
import datetime

def check_ssl_cert(hostname, port=443):
    context = ssl.create_default_context()
    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert()
            # Check certificate expiration
            expiration_date = datetime.datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z")
            days_left = (expiration_date - datetime.datetime.utcnow()).days
            if days_left <= 0:
                print(f"The certificate for {hostname} has expired.")
            else:
                print(f"The certificate for {hostname} is valid for {days_left} days.")

            # Check for weak or insecure cipher suites
            cipher_suite = ssock.cipher()
            if cipher_suite[0] in ['AES128-GCM-SHA256', 'AES256-GCM-SHA384']:
                print(f"The cipher suite {cipher_suite[0]} is secure.")
            else:
                print(f"The cipher suite {cipher_suite[0]} is not secure.")

            # You can add more checks for certificate details here
            # ...

if __name__ == "__main__":
    hostname = input("Enter the hostname of the target web server: ")
    check_ssl_cert(hostname)
