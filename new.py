{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "data = pd.read_csv(\"data/data/AAPL.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
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
       "      <th>Date</th>\n",
       "      <th>Open</th>\n",
       "      <th>High</th>\n",
       "      <th>Low</th>\n",
       "      <th>Close</th>\n",
       "      <th>Volume</th>\n",
       "      <th>Ex-Dividend</th>\n",
       "      <th>Split Ratio</th>\n",
       "      <th>Adj. Open</th>\n",
       "      <th>Adj. High</th>\n",
       "      <th>Adj. Low</th>\n",
       "      <th>Adj. Close</th>\n",
       "      <th>Adj. Volume</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2007-12-03</td>\n",
       "      <td>181.86</td>\n",
       "      <td>184.14</td>\n",
       "      <td>177.70</td>\n",
       "      <td>178.8600</td>\n",
       "      <td>34338200.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>23.371545</td>\n",
       "      <td>23.664556</td>\n",
       "      <td>22.836927</td>\n",
       "      <td>22.986003</td>\n",
       "      <td>240367400.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2007-12-04</td>\n",
       "      <td>177.15</td>\n",
       "      <td>180.90</td>\n",
       "      <td>176.99</td>\n",
       "      <td>179.8100</td>\n",
       "      <td>27635700.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>22.766244</td>\n",
       "      <td>23.248171</td>\n",
       "      <td>22.745682</td>\n",
       "      <td>23.108091</td>\n",
       "      <td>193449900.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2007-12-05</td>\n",
       "      <td>182.89</td>\n",
       "      <td>186.00</td>\n",
       "      <td>182.41</td>\n",
       "      <td>185.5000</td>\n",
       "      <td>31871500.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>23.503914</td>\n",
       "      <td>23.903592</td>\n",
       "      <td>23.442227</td>\n",
       "      <td>23.839335</td>\n",
       "      <td>223100500.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2007-12-06</td>\n",
       "      <td>186.19</td>\n",
       "      <td>190.10</td>\n",
       "      <td>186.12</td>\n",
       "      <td>189.9528</td>\n",
       "      <td>32136100.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>23.928010</td>\n",
       "      <td>24.430500</td>\n",
       "      <td>23.919014</td>\n",
       "      <td>24.411582</td>\n",
       "      <td>224952700.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2007-12-07</td>\n",
       "      <td>190.54</td>\n",
       "      <td>194.99</td>\n",
       "      <td>188.04</td>\n",
       "      <td>194.3000</td>\n",
       "      <td>38073800.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>24.487046</td>\n",
       "      <td>25.058933</td>\n",
       "      <td>24.165761</td>\n",
       "      <td>24.970258</td>\n",
       "      <td>266516600.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>2007-12-10</td>\n",
       "      <td>193.59</td>\n",
       "      <td>195.66</td>\n",
       "      <td>192.69</td>\n",
       "      <td>194.2100</td>\n",
       "      <td>25799200.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>24.879013</td>\n",
       "      <td>25.145037</td>\n",
       "      <td>24.763351</td>\n",
       "      <td>24.958692</td>\n",
       "      <td>180594400.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>2007-12-11</td>\n",
       "      <td>194.75</td>\n",
       "      <td>196.83</td>\n",
       "      <td>187.39</td>\n",
       "      <td>188.5404</td>\n",
       "      <td>39675900.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>25.028089</td>\n",
       "      <td>25.295398</td>\n",
       "      <td>24.082227</td>\n",
       "      <td>24.230069</td>\n",
       "      <td>277731300.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>2007-12-12</td>\n",
       "      <td>193.44</td>\n",
       "      <td>194.48</td>\n",
       "      <td>185.76</td>\n",
       "      <td>190.8600</td>\n",
       "      <td>43773600.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>24.859736</td>\n",
       "      <td>24.993391</td>\n",
       "      <td>23.872749</td>\n",
       "      <td>24.528170</td>\n",
       "      <td>306415200.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>2007-12-13</td>\n",
       "      <td>190.19</td>\n",
       "      <td>192.12</td>\n",
       "      <td>187.82</td>\n",
       "      <td>191.8300</td>\n",
       "      <td>30879200.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>24.442066</td>\n",
       "      <td>24.690098</td>\n",
       "      <td>24.137488</td>\n",
       "      <td>24.652829</td>\n",
       "      <td>216154400.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>2007-12-14</td>\n",
       "      <td>190.37</td>\n",
       "      <td>200.00</td>\n",
       "      <td>189.54</td>\n",
       "      <td>190.3900</td>\n",
       "      <td>24082600.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>24.465198</td>\n",
       "      <td>25.702788</td>\n",
       "      <td>24.358532</td>\n",
       "      <td>24.467769</td>\n",
       "      <td>168578200.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Date    Open    High     Low     Close      Volume  Ex-Dividend  \\\n",
       "0  2007-12-03  181.86  184.14  177.70  178.8600  34338200.0          0.0   \n",
       "1  2007-12-04  177.15  180.90  176.99  179.8100  27635700.0          0.0   \n",
       "2  2007-12-05  182.89  186.00  182.41  185.5000  31871500.0          0.0   \n",
       "3  2007-12-06  186.19  190.10  186.12  189.9528  32136100.0          0.0   \n",
       "4  2007-12-07  190.54  194.99  188.04  194.3000  38073800.0          0.0   \n",
       "5  2007-12-10  193.59  195.66  192.69  194.2100  25799200.0          0.0   \n",
       "6  2007-12-11  194.75  196.83  187.39  188.5404  39675900.0          0.0   \n",
       "7  2007-12-12  193.44  194.48  185.76  190.8600  43773600.0          0.0   \n",
       "8  2007-12-13  190.19  192.12  187.82  191.8300  30879200.0          0.0   \n",
       "9  2007-12-14  190.37  200.00  189.54  190.3900  24082600.0          0.0   \n",
       "\n",
       "   Split Ratio  Adj. Open  Adj. High   Adj. Low  Adj. Close  Adj. Volume  \n",
       "0          1.0  23.371545  23.664556  22.836927   22.986003  240367400.0  \n",
       "1          1.0  22.766244  23.248171  22.745682   23.108091  193449900.0  \n",
       "2          1.0  23.503914  23.903592  23.442227   23.839335  223100500.0  \n",
       "3          1.0  23.928010  24.430500  23.919014   24.411582  224952700.0  \n",
       "4          1.0  24.487046  25.058933  24.165761   24.970258  266516600.0  \n",
       "5          1.0  24.879013  25.145037  24.763351   24.958692  180594400.0  \n",
       "6          1.0  25.028089  25.295398  24.082227   24.230069  277731300.0  \n",
       "7          1.0  24.859736  24.993391  23.872749   24.528170  306415200.0  \n",
       "8          1.0  24.442066  24.690098  24.137488   24.652829  216154400.0  \n",
       "9          1.0  24.465198  25.702788  24.358532   24.467769  168578200.0  "
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "data.plot()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "data[['Adj. Close']].plot()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
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
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
