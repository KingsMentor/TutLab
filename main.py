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

from github import Github
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app



import webapp2

urlfetch.set_default_fetch_deadline(60)

jinja_environment = jinja2.Environment(autoescape=True, loader=jinja2.FileSystemLoader(
        os.path.join(os.path.dirname(__file__), 'bundle/template')))


class MainHandler(webapp2.RequestHandler):
    def get(self, *ar, **kw):
        path = str(ar[0]).split('/')
        gitUserName = path[0]
        repoName = path[1]
        labPath = ""
        for index in range(2, len(path)):
            if len(str(path[index]).strip()) != 0:
                labPath += path[index] + "/"
        g = Github(client_id="74a6ead0dcdde0710c40", client_secret="14bbd96eb781620284b5794e657e04bbd4ebf3ff")
        user = g.get_user(gitUserName)
        repo = user.get_repo(repoName)
        variables = {}
        data = list()
        file = repo.get_file_contents(labPath + "manifest.json")
        decoded_content = file.decoded_content
        manifest = json.loads(decoded_content)
        variables['title'] = manifest['title']
        variables['last_updated'] = repo.updated_at
        variables['feedback_link'] = manifest['feedback_link']
        steps = list()
        for step in manifest['steps']:
            steps.append(step)
        for step in steps:
            dataEntry = {}
            file = repo.get_file_contents(labPath + str(step) + ".md")
            decoded_content = file.decoded_content
            dataEntry['label'] = manifest[str(step)]['label']
            dataEntry['data'] = str(decoded_content).decode("utf8")
            dataEntry['id'] = str(step)
            data.append(dataEntry)

        variables['data'] = data

        template = jinja_environment.get_template('codelab.html')
        self.response.write(template.render(variables))


run_wsgi_app(webapp.WSGIApplication(
        [
            (r'/posts/(.*)', MainHandler),

        ]
        ,
        debug=True))
