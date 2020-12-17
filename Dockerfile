FROM python

WORKDIR /usr/src/app

COPY requirements ./
RUN pip install --no-cache-dir -r requirements

COPY . .

RUN python ./exam_test.py

CMD [ "python3", "./exam_Minyuk.py" ]
