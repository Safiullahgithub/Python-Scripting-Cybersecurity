import subprocess

def find_subdomains(domain):
    command = f"nslookup -type=NS {domain}"
    try:
        output = subprocess.check_output(command, shell=True, universal_newlines=True)
        lines = output.split("\n")
        subdomains = []

        for line in lines:
            if "nameserver" in line:
                subdomain = line.split("nameserver")[1].strip()
                subdomains.append(subdomain)

        return subdomains

    except subprocess.CalledProcessError:
        print("Error: Command execution failed.")
        return []

# Provide the domain for which you want to find subdomains
domain = "uetpeshawar.edu.pk"

# Find subdomains
subdomains = find_subdomains(domain)

# Print the subdomains
print(f"Subdomains for {domain}:")
for subdomain in subdomains:
    print(subdomain)