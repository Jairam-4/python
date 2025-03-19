import subprocess

def get_nearby_wifi_passwords():
    try:
        # Get list of nearby Wi-Fi networks
        scan_results = subprocess.check_output(['netsh', 'wlan', 'show', 'network'], text=True, encoding='utf-8')
        networks = [line.split(":")[1].strip() for line in scan_results.split("\n") if "SSID" in line]

        if not networks:
            print("No nearby Wi-Fi networks found.")
            return

        print("\n{:<30} | {:<}".format("Wi-Fi Name", "Password"))
        print("-" * 50)

        for network in networks:
            try:
                # Get the password if stored on the system
                results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', network, 'key=clear'], text=True, encoding='utf-8')
                password_lines = [line.split(":")[1].strip() for line in results.split("\n") if "Key Content" in line]

                password = password_lines[0] if password_lines else "Not Stored"
                print("{:<30} | {:<}".format(network, password))

            except subprocess.CalledProcessError:
                print("{:<30} | {:<}".format(network, "Not Stored"))

    except Exception as e:
        print(f"Error: {e}")

    input("\nPress Enter to exit...")

# Run the function
get_nearby_wifi_passwords()
