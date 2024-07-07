from InfoGet import  InformationExtractor
PAHTS=["E:\curriculums\data\chart_test","E:\curriculums\data\\no_chart_test"]
import pandas as pd
def execute(paths):
    info_extractor=InformationExtractor()
    all_result=[]
    for path in paths:
        result_html=info_extractor.parser_html(path)
        result_pdf=info_extractor.parser_pdf(path)
        all_result.extend(result_html)
        all_result.extend(result_pdf)
    return all_result
if __name__=="__main__":
    all_results=execute(PAHTS)
    data_frame=pd.DataFrame(all_results)