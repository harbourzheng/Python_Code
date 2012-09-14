'''
Created on Sep 14, 2012

@author: Bo
'''
import json
search_results = []
print json.dumps(search_results, sort_keys=True, indent=1)
[
{
"completed_in": 0.088122000000000006,
"max_id": 11966285265,
"next_page": "?page=2&max_id=11966285265&rpp=100&q=SNL",
"page": 1,
"query": "SNL",
"refresh_url": "?since_id=11966285265&q=SNL",
"results": [
{
"created_at": "Sun, 11 Apr 2010 01:34:52 +0000",
"from_user": "bieber_luv2",
"from_user_id": 106998169,
"id": 11966285265,
"iso_language_code": "en",
"metadata": {
"result_type": "recent"
},
"profile_image_url": "http://a1.twimg.com/profile_images/809471978/DSC00522...",
"source": "&lt;a href=&quot;http://twitter.com/&quot;&gt;web&lt;/a&gt;",
"text": " ...truncated... im nt gonna go to sleep happy unless i see @justin...",
}
],
"results_per_page": 100,
"since_id": 0
},

]