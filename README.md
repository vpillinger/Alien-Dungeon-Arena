# Alien-Dungeon-Arena
Competitive Multi player Dungeon Crawler Game

Goal: The goal of this game is to create a real-time multi player dungeon crawler with competitive rounds that last no
more than 20 minutes. The server-side of this game is to be written in python, while the front-end is to be written in
<TBD>. Ultimately, the plan is to turn it into a phone-based game.
Multi player rounds will be rouge-like in nature, with randomly generated maps, items, and monsters.


Design Goals:
  1) Create a modular design
    a) Seperate modules and packages that are not game specific into seperate packages to be re-used (eg, maze package).
    b) Avoid interdependence between modules.
  2) Provide appropriate code documentation
    a) Docstrings should be on all public methods. They should include input, output, pre/post conditions, and a
    description of the method.
    b) In-line comments should be used sparingly, where appropriate.
  3) Write clean code
    a) Unit testing is mandatory (100% code coverage only)
    b) Avoid code duplication
    c) Write in a Pythonic manner
    d) Follow PEP-8 standards
  4) Items, Statistics, Characters, and Enemies should be data driven (csv,xml, or alternative) whenever possible.
    Having to change code to introduce or change new enemies, items, or balance changes is not acceptable (within reason).

Copyright 2016 Vincent Pillinger

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.