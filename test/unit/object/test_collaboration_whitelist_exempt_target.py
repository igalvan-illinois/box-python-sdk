
# coding: utf-8
from __future__ import unicode_literals, absolute_import

from boxsdk.config import API


def test_get(mock_box_session, test_collaboration_whitelist_exemption):
    exemption_id = test_collaboration_whitelist_exemption.object_id
    expected_url = '{0}/collaboration_whitelist_exempt_targets/{1}'.format(API.BASE_API_URL, exemption_id)
    mock_exemption = {
        'type': 'collaboration_whitelist_entry',
        'id': '98765',
        'domain': 'example.com',
        'direction': 'inbound'
    }
    mock_box_session.get.return_value.json.return_value = mock_exemption
    exemption = test_collaboration_whitelist_exemption.get()
    mock_box_session.get.assert_called_once_with(expected_url, headers=None, params=None)
    assert exemption.id == mock_exemption['id']
    assert exemption.domain == mock_exemption['domain']
    assert exemption.direction == mock_exemption['direction']


def test_delete(mock_box_session, test_collaboration_whitelist_exemption):
    exemption_id = test_collaboration_whitelist_exemption.object_id
    expected_url = mock_box_session.get_url('collaboration_whitelist_exempt_targets', exemption_id)
    test_collaboration_whitelist_exemption.delete()
    mock_box_session.delete.assert_called_once_with(expected_url, expect_json_response=False, headers=None, params={})
