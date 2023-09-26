from pathlib import Path

class Generator:
    def __init__(self):
        self.project_name = ""
        self.repo_url = ""
        self.license = ""
        self.folder_location = ""
        self.documentation_link = ""
        self.contributing_guidelines = ""
        self.maintainer_email = ""
        self.about_paragraph = ""
        self.file_path = ""
        self.layout_path = ""

    def instruction_gen(self) -> str:
        with open(self.layout_path, "r") as file:
            instructions = file.read()
        instructions = instructions.replace("{project_name}", self.project_name)
        instructions = instructions.replace("{repo_url}", self.repo_url)
        instructions = instructions.replace("{license}", self.license)
        instructions = instructions.replace("{documentation}", f"[Documentation]({self.documentation_link})")
        instructions = instructions.replace("{contributing}", f"[Contribution Guidelines]({self.contributing_guidelines})")
        instructions = instructions.replace("{maintainer_email}", self.maintainer_email)
        instructions = instructions.replace("{about}", self.about_paragraph)
        return instructions

    def file_write(self, instructions):
        with open(self.file_path, "w") as file:
            file.write(instructions)

def main():

    generator = Generator()

    print("[?] Enter project details:")
    generator.project_name = input("[?] Project Name: ")
    generator.repo_url = input("[?] Repository URL: ")
    generator.license = input("[?] License (e.g., MIT, GNU 3): ")
    generator.folder_location = input("[?] Folder Location for README generation: ")
    generator.file_path = Path(generator.folder_location) / "README.md"
    generator.layout_path = Path.cwd() / 'data' / 'layout.md'

    print("\nEnter links and contact info:")
    generator.documentation_link = input("[?] Documentation Link: ")
    generator.contributing_guidelines = input("[?] Contribution Guidelines Link: ")
    generator.maintainer_email = input("[?] Maintainer's Email: ")

    print("\nEnter 'About' paragraph (Markdown formatting supported):")
    generator.about_paragraph = input()

    instructions = generator.instruction_gen()
    generator.file_write(instructions)

    print("\n[+] README.md generated successfully at", generator.file_path)

if __name__ == "__main__":
    main()

