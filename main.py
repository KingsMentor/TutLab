#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import json
import os

import jinja2
from google.appengine.api import urlfetch

from clientDetails import CLIENT_ID, CLIENT_SECRET
from github import Github
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

import webapp2

urlfetch.set_default_fetch_deadline(60)

jinja_environment = jinja2.Environment(autoescape=True, loader=jinja2.FileSystemLoader(
        os.path.join(os.path.dirname(__file__), 'bundle/template')))


class MainHandler(webapp2.RequestHandler):
    def get(self, *ar, **kw):
        # split the path with '/' to get detail
        path = str(ar[0]).split('/')
        author = str(path[0])
        repoName = str(path[1])
        labPath = ""
        for index in range(2, len(path)):
            if len(str(path[index]).strip()) != 0:
                labPath += path[index] + "/"

        # init git credentials
        g = Github(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
        user = g.get_user(author)
        repo = user.get_repo(repoName)
        variables = {}
        data = list()
        file = repo.get_file_contents(labPath + "manifest.json")
        decoded_content = file.decoded_content
        manifest = json.loads(decoded_content)
        variables['title'] = manifest['title']
        variables['last_updated'] = repo.updated_at
        variables['feedback_link'] = manifest['feedback_link']
        variables['home_link'] = manifest['home']
        steps = list()
        for step in manifest['steps']:
            steps.append(step)
            dataEntry = {}
            dataEntry['label'] = manifest[str(step)]['label']
            dataEntry['id'] = str(step)
            dataEntry['data_link'] = buildRawFileContentPath(author, repoName, labPath, str(step))
            data.append(dataEntry)

        variables['data'] = data
        template = jinja_environment.get_template('codelab.html')
        self.response.write(template.render(variables))


def buildRawFileContentPath(author, repo, path, filename):
    return "https://raw.githubusercontent.com/" + author + "/" + repo + "/master/" + path + filename + ".md"


run_wsgi_app(webapp.WSGIApplication(
        [
            (r'/posts/(.*)', MainHandler),

        ]
        ,
        debug=True))
