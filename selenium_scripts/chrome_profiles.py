import json
import os

def get_active_chrome_profile(config_file=None):
    if config_file is None:
        return None
    try:
        with open(config_file) as f:
            config = json.load(f)
        
        for computer in config["computers"]:
            profile_path = config["chromeProfilePath"].replace("{userName}", computer["userName"])
            if os.path.exists(profile_path):
                return {
                    "computerName": computer["computerName"],
                    "userName": computer["userName"],
                    "chromeProfilePath": profile_path,
                    "profileDirectory": computer["profileDirectory"],
                }
        return None
        
    except Exception as e:
        print(f"Error loading active profile: {str(e)}")
        return None

if __name__ == "__main__":
    if (profile := get_active_chrome_profile()):
        print(f"Active Profile: {profile['chromeProfilePath']}")
    else:
        print("No active Chrome profile found")