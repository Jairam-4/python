import subprocess

def find_wifi_passwords():
    command = ["netsh", "wlan", "show", "profiles"]
    networks = subprocess.check_output(command).decode("utf-8").split("\n")
    wifi_names = [line.split(":")[1][1:-1] for line in networks if "All User Profile" in line]

    for wifi_name in wifi_names:
        command = ["netsh", "wlan", "show", "profile", wifi_name, "key=clear"]
        result = subprocess.check_output(command).decode("utf-8").split("\n")
        passwords = [line.split(":")[1][1:-1] for line in result if "Key Content" in line]
        print(f"WiFi Network: {wifi_name}, Password: {passwords[0] if passwords else 'No Password Found'}")

if __name__ == "__main__":
    find_wifi_passwords()
