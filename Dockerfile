From python:3.7

EXPOSE 8501

ADD driver.py .

RUN pip install streamlit pandas requests

CMD streamlit run ./driver.py [ "python" ]