
from urllib import request
from project import Project
import tomli

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)
        toml_data = tomli.loads(content)
        name = toml_data["tool"]["poetry"]["name"]
        description = toml_data["tool"]["poetry"]["description"]
        license = toml_data["tool"]["poetry"]["license"]
        authors = toml_data["tool"]["poetry"]["authors"]
        dependencies = toml_data["tool"]["poetry"]["dependencies"]
        dev_dependencies = toml_data["tool"]["poetry"]["group"]["dev"][
            "dependencies"
        ]

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        #return Project("Test name", "Test description", [], [])
        return Project(name, authors, description, license, dependencies, dev_dependencies)
