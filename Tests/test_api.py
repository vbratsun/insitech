import initial_config
from Tests.http_client import HttpClient

class TestAPI:
    def test_manufacturers_request(self):
        category_id=5
        expected_response_body={'page': 1, 'pageSize': 1000, 'totalCount': 7, 'manufacturers': [{'id': 240, 'deviceKindId': 5, 'name': 'Nintendo'}, {'id': 208, 'deviceKindId': 5, 'name': 'GPD'}, {'id': 305, 'deviceKindId': 5, 'name': 'Microsoft'}, {'id': 336, 'deviceKindId': 5, 'name': 'Sony'}, {'id': 341, 'deviceKindId': 5, 'name': 'Nvidia'}, {'id': 399, 'deviceKindId': 5, 'name': 'Valve'}, {'id': 505, 'deviceKindId': 5, 'name': 'PGP'}]}
        client = HttpClient(base_url=initial_config.site_url)
        response = client.get(f"/api/strapi/manufacturers/{category_id}?pageSize=1000&sort=popularity")
        assert response.json()==expected_response_body