import os, socket, urllib.request

def getUrl() -> None:
    try:
        result = urllib.request.urlopen("https://ident.me").read().decode("utf8")
    except Exception as x:
        print(type(x),x)
        result = '0.0.0.0'
        pass
    return result

class validatorToolbox:
    easy_version = "1.0.0"
    server_host_name = socket.gethostname()
    user_home_dir = os.path.expanduser("~")
    dotenv_file = f"{user_home_dir}/.easynode.env"
    active_user_name = os.path.split(user_home_dir)[-1]
    findora_root_mainnet = f'/data/findora/mainnet'
    findora_root_testnet = f'/data/findora/testnet'
    toolbox_location = os.path.join(user_home_dir, "validatortoolbox-fra")
    our_external_ip = getUrl()