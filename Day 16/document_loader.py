from langchain_community.document_loaders import TextLoader

# Load Text File
loader = TextLoader("C:\\Users\\suman\\Desktop\\Ai - Internship\\AI-Internship\\Day 16\\data\\company_info.txt")

documents = loader.load()

#print(documents)