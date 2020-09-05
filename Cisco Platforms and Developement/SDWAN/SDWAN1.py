# https://{{vmanage}}:{{port}}/dataservice/device/counters
# /dataservice/statistics/interface


def login(vmanage_ip, username, password):
    """Login to vmanage"""
    base_url_str = 'https://%s:8443/' % vmanage_ip

    login_action = '/j_security_check'

    # Format data for loginForm
    login_data = {'j_username': username, 'j_password': password}

    # Url for posting login data
    login_url = base_url_str + login_action

    sess = requests.session()
    # If the vmanage has a certificate signed by a trusted authority change verify to True
    login_response = sess.post(url=login_url, data=login_data, verify=False)

    if b'<html>' in login_response.content:
        print("Login Failed")
        sys.exit(0)


url = "https://%s:8443/dataservice/%s" % (vmanage_ip, mount_point)


def get_request(vmanage_ip, mount_point):
    """GET request"""
    url = "https://%s:8443/dataservice/%s" % (vmanage_ip, mount_point)

    response = requests.request("GET", url, verify=False)
    data = response.content
    return data


def post_request(vmanage_ip, mount_point, payload, headers={'Content-Type': 'application/json'}):
    """POST request"""
    url = "https://%s:8443/dataservice/%s" % (vmanage_ip, mount_point)
    payload = json.dumps(payload)

    response = requests.request(
        "POST", url, data=payload, headers=headers, verify=False)
    data = response.json()
    return data
