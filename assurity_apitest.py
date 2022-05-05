import requests

url = "https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false"


class ApiTest(object):

    def verify_name(self) -> None:
        response = requests.get(url)
        out = response.json()
        assert response.status_code == 200, "Unexpected response code: " + str(response.status_code)
        result = "Pass: Name \"Carbon credits\" Matched" if out['Name'] == 'Carbon credits' else "Fail: Name not Matched"
        print(result)

    def verify_canrelist(self) -> None:
        response = requests.get(url)
        out = response.json()
        assert response.status_code == 200, "Unexpected response code: " + str(response.status_code)
        result = "Pass: CanRelist is True" if out['CanRelist'] is True else "Fail: CanRelist is not True"
        print(result)

    def verify_promotions(self) -> None:
        response = requests.get(url)
        out = response.json()
        assert response.status_code == 200, "Unexpected response code: " + str(response.status_code)
        if out['Promotions'][1]['Name'] == 'Gallery':
            print("Pass: " + out['Promotions'][1]['Description'])
        else:
            print("Fail: Promotions Name not matched")


if __name__ == '__main__':
    test = ApiTest()
    test.verify_name()
    test.verify_canrelist()
    test.verify_promotions()
