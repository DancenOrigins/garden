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
# make some sprutes
# make the main skelebone
import jinja2
import webapp2
import json
import random
import urllib

#def compcalc1(x):
    #x = int(x) - 4
    #return x
#def compcalc2(x2):
    #x = int(x2) - 4
    #return x
#def compcalc3(x3):
    #x = int(x) - 4
    #return x

env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        main_template = env.get_template('main.html')
        self.response.out.write(main_template.render())

class WaterGameHandler(webapp2.RequestHandler):
    def get(self):
        water_template = env.get_template('water.html')
        self.response.out.write(water_template.render())

class Game1Handler(webapp2.RequestHandler):
    def get(self):
        rules_template = env.get_template('rules.html')
        self.response.out.write(rules_template.render())
    def post(self): ## here's the new POST method in the MainHandler
        turn_num = self.request.get("turnNum")
        if turn_num == "0":
            main_template = env.get_template('gameturn1.html')
        elif turn_num == "1":
            main_template = env.get_template('gameturn2.html')
        elif turn_num == "2":
            main_template = env.get_template('gameturn3.html')
        else:
            main_template = env.get_template('results.html')

        temp_vars = {
           "start": self.request.get("start"),
           "turn1": self.request.get("turn1"),
           "turn2": self.request.get("turn2"),
           "turn3": self.request.get("turn3"),
           "compTurn1": 1,
           "compTurn2": 2,
           "compTurn3": 3,
           "total_marbles": 12,
           "total_marbles2": 8,
           "total_marbles3": 4,
        }
        self.response.out.write(main_template.render(temp_vars))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/water' , WaterGameHandler),
    ('/game1' , Game1Handler),
], debug=True)
