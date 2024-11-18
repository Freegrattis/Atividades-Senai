from abc import ABC, abstractmethod

# Classe base abstrata
class FileSystemComponent(ABC):
    @abstractmethod
    def display(self, indent=0):
        pass

# Folha: Representa um arquivo
class File(FileSystemComponent):
    def __init__(self, name):
        self.name = name

    def display(self, indent=0):
        print(" " * indent + f"File: {self.name}")

# Composite: Representa uma pasta que pode conter outros componentes
class Folder(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def display(self, indent=0):
        print(" " * indent + f"Folder: {self.name}")
        for child in self.children:
            child.display(indent + 2)

# Exemplo de uso
if __name__ == "__main__":
    # Criando arquivos
    file1 = File("file1.txt")
    file2 = File("file2.txt")
    file3 = File("file3.txt")

    # Criando pastas
    folder1 = Folder("Folder1")
    folder2 = Folder("Folder2")
    root = Folder("Root")

    # Construindo a hierarquia
    folder1.add(file1)
    folder1.add(file2)
    folder2.add(file3)
    root.add(folder1)
    root.add(folder2)

    # Exibindo a hierarquia
    root.display()
