import hvac

def update_vault():
    client = hvac.Client(url="http://127.0.0.1:8200", token="root")

    if client.is_authenticated():
        print("Successfully authenticated to Vault.")
        secrets_path = "earthquake"
        client.secrets.kv.v2.create_or_update_secret(path=secrets_path, secret=dict(
            base_url="https://earthquake.usgs.gov/fdsnws/event/1/query", 
            count_url="https://earthquake.usgs.gov/fdsnws/event/1/count"
            ))
        read_response = client.secrets.kv.v2.read_secret_version(path=secrets_path)
        response = read_response['data']['data']
        return response
    else:
        print("Failed to authenticate to Vault.")
        return