{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1babcf70-466e-4069-9261-21fc6670fc60",
   "metadata": {},
   "outputs": [],
   "source": [
    "from bs4 import BeautifulSoup\n",
    "import requests\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "03a01b11-b425-4203-89b7-0d0cdec5079a",
   "metadata": {},
   "outputs": [],
   "source": [
    "url = BeautifulSoup('https://www.sharesansar.com/live-trading',\"html.parser\")\n",
    "soup = requests.get(url)\n",
    "print(soup)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cfb11e99-9bd4-48b7-9657-aee7020e5f20",
   "metadata": {},
   "outputs": [],
   "source": [
    "codes = soup.text\n",
    "codes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "784e787c-6510-4a61-994c-7d036f01cab6",
   "metadata": {},
   "outputs": [],
   "source": [
    "codes = BeautifulSoup(codes,\"lxml\")\n",
    "codes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "782ae304-5452-4f55-a71c-2535862d6290",
   "metadata": {},
   "outputs": [],
   "source": [
    "div_code = codes.div\n",
    "div_code\n",
    "#any codes can be used instead of div to find it if it exist"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "00de6587-fbb7-4a30-b3c2-4e29be787ce9",
   "metadata": {},
   "outputs": [],
   "source": [
    "table_code = codes.table\n",
    "table_code"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e0145e25-07a9-4074-84eb-d96e202b260b",
   "metadata": {},
   "outputs": [],
   "source": [
    "tags = table_code.find_all('tr')\n",
    "tags"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "176db5a0-3c61-4ab4-b89c-70ac0c8ddd3c",
   "metadata": {},
   "outputs": [],
   "source": [
    "data = []\n",
    "for i in tags:\n",
    "    x = i.text\n",
    "    data.append(x)\n",
    "\n",
    "data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e556e052-59de-4931-bedb-ed350f5b810f",
   "metadata": {},
   "outputs": [],
   "source": [
    "rows = data[1:]\n",
    "for i in rows:\n",
    "    print(i.replace(\"/n/n\",\"\").split(\"                            \"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6098c116-49cd-46de-aebd-19de617f66f8",
   "metadata": {},
   "outputs": [],
   "source": [
    "col = data[0].split(\"\\n\")[2:-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "18f6abf3-28dd-4a1c-96d9-4cf1c198c161",
   "metadata": {},
   "outputs": [],
   "source": [
    "rows_data = []\n",
    "rows = data[1:]\n",
    "for i in rows:\n",
    "    y = i.replace(\"\\n\\n\",\"\").split(\"                                \")\n",
    "    y[1] = y[1].replace(\"\\n\",\"\")\n",
    "    y[-1] = y[-1].replace(\"\\n\",\"\")\n",
    "    rows_data.append(y[1:])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b3c3c25b-139c-4fac-9f15-46a771c12d6d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "df = pd.DataFrame(rows_data,columns = col)\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "414fa855-02fb-41d5-9823-26e53c404856",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "import pandas as pd\n",
    "\n",
    "df = pd.DataFrame({\n",
    "    'LTP': ['1,234.56', '2,345.67'],\n",
    "    'Point Change': ['+10.5', '-5.25']\n",
    "})\n",
    "df['LTP'] = [float(i.replace(\",\",\"\")) for i in df['LTP']]\n",
    "df['Point Change'] = [float(i.replace(\",\",\"\")) for i in df['Point Change']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "eedd9dcc-26c9-4cd5-a1be-41e619e8d01e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>LTP</th>\n",
       "      <th>Point Change</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1234.56</td>\n",
       "      <td>10.50</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2345.67</td>\n",
       "      <td>-5.25</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       LTP  Point Change\n",
       "0  1234.56         10.50\n",
       "1  2345.67         -5.25"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "84e7321d-e9a8-4d5b-abb6-02db9f34277d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
