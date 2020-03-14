import pandas as pd
import os
from paper.models import paper

data = pd.read_csv("/home/pankaj/Documents/Paper-database/paperdatabase/paper/sorted_paper_data.csv")
base_path = "/home/pankaj/allen_Kota_crawl/data"
def create_paper(data,i):
    year = str(data.iloc[i]['year'])
    id_no = str(data.iloc[i]['id'])
    pattern = str(data.iloc[i]['pattern'])
    level = str(data.iloc[i]['level'])
    language = str(data.iloc[i]['language'])
    testtype = str(data.iloc[i]['testtype'])
    testdate = str(data.iloc[i]['testdate'])
    papertype = str(data.iloc[i]['papertype'])
    question_path = str(os.path.join(base_path,year,id_no,"Question.pdf"))
    solution_path = str(os.path.join(base_path,year,id_no,"Question.pdf"))
    p = paper(year=year,id_no=id_no,pattern=pattern,level=level,language=language,testtype=testtype,testdate=testdate,papertype=papertype,question_path=question_path,solution_path=solution_path)
    p.save()



for i in range(0,7090):
    create_paper(data,i)