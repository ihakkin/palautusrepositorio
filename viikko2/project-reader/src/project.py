class Project:
    def __init__(self, name, authors, description, license, dependencies, dev_dependencies):
        self.name = name
        self.authors = authors
        self.description = description
        self.license = license 
        self.dependencies = list(dependencies.keys())
        self.dev_dependencies = list(dev_dependencies.keys())

    def _stringify_dependencies(self, dependencies):
        #return ", ".join(dependencies) if len(dependencies) > 0 else "-"
        return "\n- ".join([""] + dependencies) if dependencies else "-"

    def __str__(self):
        authors_str = "\n- " + "\n- ".join(self.authors) if self.authors else "-"
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '-'}\n"  # Lisää tyhjä rivi lisenssin jälkeen
            f"\nAuthors:{authors_str}"
            f"\n\nDependencies: {self._stringify_dependencies(self.dependencies)}"
            f"\n\nDevelopment dependencies: {self._stringify_dependencies(self.dev_dependencies)}"
        )
