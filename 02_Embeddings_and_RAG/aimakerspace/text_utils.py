import os
from typing import List
from PyPDF2 import PdfReader 

"""
This code contains our 2 main classes for text.
1st class: TextFileLoader, which loads a text file or a folder of text files into
a list of strings
2nd class: CharacterTextSplitter, which creates the chunks that we need to pass 
to our embedding model. It creates chunks of size
1000 characters with 200 characters of overlap. The overlapping chunks help maintain
context between adjacent parts of the string.
Important note: CharacterTextSplitter never creates a chunk that is formed from 
two or more stings! I.e. it preserves the original document boundaries!
"""
class TextFileLoader:
    def __init__(self, path: str, encoding: str = "utf-8"):
        self.documents = []
        self.path = path
        self.encoding = encoding

    def load(self):
        if os.path.isdir(self.path):
            self.load_directory()
        elif os.path.isfile(self.path):
            if self.path.endswith(".txt"):
                self.load_file()
            elif self.path.endswith(".pdf"):
                self.load_pdf()
            else:
                raise ValueError("File type not supported. Please use .txt or .pdf files.")
        else:
            raise ValueError(
                "Provided path is neither a valid directory nor a supported file."
            )

    def load_file(self):
        with open(self.path, "r", encoding=self.encoding) as f:
            self.documents.append(f.read())

    def load_pdf(self, file_path=None): # Accept an optional file_path
        path_to_load = file_path or self.path # Use file_path if provided, else self.path
        reader = PdfReader(path_to_load)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        self.documents.append(text)


    def load_directory(self):
        for root, _, files in os.walk(self.path):
            for file in files:
                if file.endswith((".txt", ".pdf")):
                    file_path = os.path.join(root, file)
                    if file.endswith(".txt"):
                        with open(file_path, "r", encoding=self.encoding) as f:
                            self.documents.append(f.read())
                    elif file.endswith(".pdf"):
                        self.load_pdf(file_path)

    def load_documents(self):
        self.load()
        return self.documents


class CharacterTextSplitter:
    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
    ):
        assert (
            chunk_size > chunk_overlap
        ), "Chunk size must be greater than chunk overlap"

        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def split(self, text: str) -> List[str]:
        chunks = []
        for i in range(0, len(text), self.chunk_size - self.chunk_overlap):
            chunks.append(text[i : i + self.chunk_size])
        return chunks

    def split_texts(self, texts: List[str]) -> List[str]:
        chunks = []
        for text in texts:
            chunks.extend(self.split(text))
        return chunks

""" 
This is a test block showing how to use the classes properly and prints the total
number of chunks, the first 2 chunks, and the last 2 chunks
"""
if __name__ == "__main__":
    loader = TextFileLoader("data/KingLear.txt")
    loader.load()
    splitter = CharacterTextSplitter()
    chunks = splitter.split_texts(loader.documents)
    print(len(chunks))
    print(chunks[0])
    print("--------")
    print(chunks[1])
    print("--------")
    print(chunks[-2])
    print("--------")
    print(chunks[-1])
