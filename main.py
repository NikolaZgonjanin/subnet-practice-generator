import ipaddress
import numpy as np
import random

# Generation settings
NUM_PROBLEMS = 300
MIN_DEVICES = 2
MAX_DEVICES = 3000
MIN_SUBNETS = 2
MAX_SUBNETS = 5


def generate_corrected_subnet_problem_sets(num_sets):
    markdown_output = "# Zadaci iz podmrežavanja\n\n"
    for i in range(1, num_sets + 1):
        base_network = f"{random.randint(10, 192)}.{random.randint(0, 255)}.{random.randint(0, 255)}.0/{random.randint(16, 24)}"
        num_subnets = random.randint(MIN_SUBNETS, MAX_SUBNETS)
        devices_per_subnet = np.random.exponential(scale=150, size=num_subnets).astype(int)
        devices_per_subnet = np.clip(devices_per_subnet, MIN_DEVICES, MAX_DEVICES).tolist()

        try:
            network = ipaddress.ip_network(base_network, strict=False)
            subnets = []
            start_address = network.network_address

            for devices in sorted(devices_per_subnet, reverse=True):
                if start_address >= network.broadcast_address:
                    break  # Exit if no space is left in the network
                
                new_prefix_length = 32 - int((devices + 1).bit_length())
                candidate_network = ipaddress.ip_network(f"{start_address}/{new_prefix_length}", strict=False)
                
                if (candidate_network.network_address + (1 << (32 - new_prefix_length))) > network.broadcast_address:
                    continue  # Skip if the subnet cannot fit
                
                subnets.append(candidate_network)
                start_address = candidate_network.broadcast_address + 1

        except ValueError:
            continue

        markdown_output += f"## Zadatak {i}\n"
        markdown_output += "**Mreža:** " + base_network + "\n"
        markdown_output += "**Broj uređaja po mreži:** " + ", ".join(map(str, sorted(devices_per_subnet, reverse=True))) + "\n\n"
        markdown_output += "<details>"
        markdown_output += "<summary>Rešenje</summary>\n"
        markdown_output += "<table><thead><tr><td> Subnet </td><td> Mrežna adresa</td><td>Maska</td><td>Mrežni opseg</td><td>Brodkast</td></tr></thead><tbody>\n"
        # markdown_output += "| --- | --- | --- | --- | --- |\n"
        for subnet in subnets:
            network_address = subnet.network_address
            netmask = subnet.netmask
            usable_range = f"{subnet.network_address + 1} - {subnet.broadcast_address - 1}"
            broadcast_address = subnet.broadcast_address
            markdown_output += f"<tr><td>{subnet}</td><td>{network_address}</td><td>{netmask}</td><td>{usable_range}</td><td>{broadcast_address}</td></tr>\n"

        markdown_output += "</tbody></table></details>\n"

    return markdown_output

# Generate problem sets
problem_sets_md_corrected = generate_corrected_subnet_problem_sets(NUM_PROBLEMS)

# Save to .md file
md_file_path_corrected = 'podmrezavanje.md'
with open(md_file_path_corrected, 'w') as file:
    file.write(problem_sets_md_corrected)
