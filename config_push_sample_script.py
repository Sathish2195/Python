from concurrent.futures import ThreadPoolExecutor, as_completed
from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoTimeoutException, NetmikoAuthenticationException

# Define the configuration commands to push
CONFIG_COMMANDS = [
    "interface Loopback100",
    "description Automated Loopback by Python",
    "ip address 192.168.100.1 255.255.255.255",
    "no shutdown",
]


def load_devices_from_text(filename="devices.txt"):
    """
    Parses a plain text file and converts line elements into structured 
    Netmiko device dictionaries.
    """
    devices = []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                # Ignore empty lines or comment lines
                if not line or line.startswith("#"):
                    continue

                # Split line by comma
                parts = [item.strip() for item in line.split(",")]

                # Ensure the line has at least the minimum 4 core parameters
                if len(parts) >= 4:
                    device_dict = {
                        "device_type": parts[0],
                        "host": parts[1],
                        "username": parts[2],
                        "password": parts[3]
                    }
                    # If a 5th element exists, treat it as the optional 'secret'
                    if len(parts) == 5 and parts[4]:
                        device_dict["secret"] = parts[4]

                    devices.append(device_dict)
                else:
                    print(f"Skipping malformed line: {line}")
        return devices
    except FileNotFoundError:
        print(f"Error: The inventory file '{filename}' was not found.")
        return []


def push_config(device, config_set):
    host = device.get("host")
    try:
        with ConnectHandler(**device) as net_connect:
            if "secret" in device:
                net_connect.enable()
            output = net_connect.send_config_set(config_set)
            return f"SUCCESS: {host}\nOutput:\n{output}"
    except NetmikoTimeoutException:
        return f"FAILED: {host} (Connection Timeout)"
    except NetmikoAuthenticationException:
        return f"FAILED: {host} (Authentication Failure)"
    except Exception as e:
        return f"FAILED: {host} (Error: {str(e)})"


def main():
    # Load devices dynamically from the text file
    devices = load_devices_from_text("devices.txt")
    if not devices:
        print("No devices loaded. Exiting.")
        return

    MAX_THREADS = 10
    print(f"Loaded {len(devices)} devices. Starting deployment...")

    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        future_to_device = {
            executor.submit(push_config, device, CONFIG_COMMANDS): device.get("host")
            for device in devices
        }

        for future in as_completed(future_to_device):
            host = future_to_device[future]
            try:
                result = future.result()
                print(f"\n{'-'*40}\nResult for {host}:\n{result}\n{'-'*40}")
            except Exception as exc:
                print(f"{host} generated an exception: {exc}")


if __name__ == "__main__":
    main()
