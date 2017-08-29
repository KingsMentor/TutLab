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
import logging
import os

import jinja2
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

# from google.appengine.ext.webapp import template
import webapp2

jinja_environment = jinja2.Environment(autoescape=True, loader=jinja2.FileSystemLoader(
        os.path.join(os.path.dirname(__file__), 'bundle/template')))


class MainHandler(webapp2.RequestHandler):
    def get(self, *ar, **kw):
        logging.info("here")
        template = jinja_environment.get_template('codelab.html')
        self.response.out.write(template.render())


run_wsgi_app(webapp.WSGIApplication(
        [
            (r'/(.*)', MainHandler),

        ]
        ,
        debug=True))
