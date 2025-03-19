import subprocess

def get_wifi_passwords():  # Fixed function name (removed extra underscore)
    try:
        # Get list of Wi-Fi profiles
        data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'], text=True, encoding='utf-8')
        profiles = [line.split(":")[1].strip() for line in data.split("\n") if "All User Profile" in line]

        if not profiles:
            print("No Wi-Fi profiles found.")
            return

        print("\n{:<30} | {:<}".format("Wi-Fi Name", "Password"))
        print("-" * 50)

        for profile in profiles:
            try:
                # Get the password for each profile
                results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear'], text=True, encoding='utf-8')
                password_lines = [line.split(":")[1].strip() for line in results.split("\n") if "Key Content" in line]

                password = password_lines[0] if password_lines else "No Password Found"
                print("{:<30} | {:<}".format(profile, password))

            except subprocess.CalledProcessError:
                print("{:<30} | {:<}".format(profile, "ERROR: Unable to retrieve password"))

    except Exception as e:
        print(f"Error: {e}")

    input("\nPress Enter to exit...")

# Run the function
get_wifi_passwords()  # Fixed function name
