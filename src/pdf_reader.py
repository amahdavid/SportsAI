import os
from llama_index.readers.file import PDFReader
from utils.functions import get_index

pdf_path_nba = os.path.join("..", "data", "nba_data", "nba.pdf")
nba_pdf = PDFReader().load_data(file=pdf_path_nba)
nba_index = get_index(nba_pdf, "nba")

pdf_path_fifa = os.path.join("..", "data", "fifa_data", "FIFA.pdf")
fifa_pdf = PDFReader().load_data(file=pdf_path_fifa)
fifa_index = get_index(fifa_pdf, "fifa")

nba_engine = nba_index.as_query_engine()
fifa_engine = fifa_index.as_query_engine()
