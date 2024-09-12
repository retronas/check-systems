#!/usr/bin/env python3

import requests
import json
import time
from lib.config import Config
from lib.logger import Logger

class URLHandler():
    def __init__(self):
        self.logger = Logger("url")
        pass


    def get(self, url, headers=None):
        self.logger.log_info("Getting data from %s" % url)

        # pagination in response headers (gitlab)
        pagination = None
        next_page = None


        if headers is not None:
            r = requests.get(url, headers)
        else:
            r = requests.get(url)

        if r.status_code == 200:
            if "Link" in r.headers:
                self.logger.log_info("Response headers container link reference, probable pagination, processing")
                pagination = r.headers['Link'].split('<')
                next_page = pagination[1].split(';')[0]
                last_page = None
                if len(pagination) > 2:
                    last_page = pagination[2].split(';')[0]
                self.logger.log_info("Pages LAST: %s NEXT: %s" % (last_page, next_page))

                if next_page == last_page:
                    self.logger.log_info("This is the last page, returning None")
                    next_page = None
                else:
                    next_page = r.headers['Link'].split('; ')[0].replace('<','').replace('>','')
                
            return [r.content, next_page]
        else:
             self.logger.log_error("Failed to get %s, code was %s" % (url, r.status_code))
             return [None,None]
        return None

    def direct(self, url, headers=None):
        self.logger.log_info("Processing direct download mode")
        return self.get(url, headers)

    def github_tree(self, account, repo, branch="main", headers=None):
        self.logger.log_info("Processing github tree download mode")
        url = f"https://api.github.com/repos/{account}/{repo}/git/trees/{branch}?recursive=1"
        json_data = self.get(url, headers)
        return json.loads(json_data[0])

    def github_raw(self, account, repo, branch="main", path='/', headers=None):
        self.logger.log_info("Processing github raw download mode")
        url = f"https://raw.githubusercontent.com/{account}/{repo}/{branch}/{path}"
        return self.get(url, headers)

    def gitlab_tree(self, projectid, path, headers=None):
        self.logger.log_info("Processing gitlab tree download mode")
        #url = f'https://gitlab.com/api/v4/projects/{projectid}/repository/tree?path={path}&per_page=100&pagination=keyset&page_token=keyset'
        url = f'https://gitlab.com/api/v4/projects/{projectid}/repository/tree?path={path}&per_page=100&pagination=keyset'
        dataset = []

        data = self.get(url, headers)
        dataset.append(data[0])

        while data[1] is not None:
            data = self.get(data[1])
            dataset.append(data[0])
            time.sleep(2)

        data_names = []
        for data_items in dataset:
            if data_items is not None:
                json_data = data_items.decode('utf-8')
                data_names.append(json.loads(json_data))

        return data_names