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
import logging
import os

import jinja2
from github import Github
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

# from google.appengine.ext.webapp import template
import webapp2

jinja_environment = jinja2.Environment(autoescape=True, loader=jinja2.FileSystemLoader(
        os.path.join(os.path.dirname(__file__), 'bundle/template')))


class MainHandler(webapp2.RequestHandler):
    def get(self, *ar, **kw):
        path = str(ar[0]).split('/')
        gitUserName = path[0]
        repoName = path[1]
        stepSize = int(path[2])
        labPath = ""
        for index in range(3, len(path)):
            if len(str(path[index]).strip()) != 0:
                labPath += path[index] + "/"
        g = Github()
        user = g.get_user(gitUserName)
        repo = user.get_repo(repoName)
        variables = {}
        data = list()
        file = repo.get_file_contents(labPath + "manifest.json")
        decoded_content = file.decoded_content
        manifest = json.loads(decoded_content)
        variables['title'] = manifest['title']
        variables['feedback_link'] = manifest['feedback_link']
        for index in range(1, stepSize + 1):
            dataEntry = {}
            file = repo.get_file_contents(labPath + "step" + str(index) + ".md")
            decoded_content = file.decoded_content
            dataEntry['label'] = manifest["step"+str(index)]['label']
            dataEntry['data'] = decoded_content
            data.append(dataEntry)

        variables['data'] = data

        logging.info(decoded_content)
        template = jinja_environment.get_template('codelab.html')
        self.response.out.write(template.render(variables))


run_wsgi_app(webapp.WSGIApplication(
        [
            (r'/posts/(.*)', MainHandler),

        ]
        ,
        debug=True))
