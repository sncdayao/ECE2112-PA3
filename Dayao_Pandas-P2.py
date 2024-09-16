{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "3bc684ac-efda-4b4d-86b7-a71c7b9d8398",
   "metadata": {},
   "source": [
    "Sophia Nicole C. Dayao 2ECE-C\n",
    "<br>\n",
    "**ECE2112 PA3: Experiment 3**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "c835b9bc-3603-41dd-89cd-70ed140d0c7a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5f76e4d8-2d66-45af-a008-fa4be018deaa",
   "metadata": {},
   "source": [
    "**PROBLEM 2**\n",
    "<br> Using the dataframe \"cars\" in problem 1, extract the following information using subsetting, slicing, and indexing operations:\n",
    "<br> a. Display the first five rows with odd-numbered columns of cars.\n",
    "<br> b. Display the row that contains the 'Model' of 'Mazda RX4'.\n",
    "<br> c. How many cylinders ('cyl') does the car model 'Camaro Z28' have?\n",
    "<br> d. Determine how many cylinders ('cyl') and what gear type ('gear') do the car models 'Mazda RX4 Wag', 'Ford Pantera L', and 'Honda Civic' have."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "17f4da9a-8c58-40a7-b0fe-457fc28ef8f1",
   "metadata": {},
   "outputs": [],
   "source": [
    "#load the .csv file into a data frame named \"cars\" using pandas\n",
    "\n",
    "cars = pd.read_csv('cars.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "7ab1a475-0c49-456b-aafe-dc9a846719c7",
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
       "      <th>Model</th>\n",
       "      <th>mpg</th>\n",
       "      <th>cyl</th>\n",
       "      <th>disp</th>\n",
       "      <th>hp</th>\n",
       "      <th>drat</th>\n",
       "      <th>wt</th>\n",
       "      <th>qsec</th>\n",
       "      <th>vs</th>\n",
       "      <th>am</th>\n",
       "      <th>gear</th>\n",
       "      <th>carb</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Mazda RX4 Wag</td>\n",
       "      <td>21.0</td>\n",
       "      <td>6</td>\n",
       "      <td>160.0</td>\n",
       "      <td>110</td>\n",
       "      <td>3.90</td>\n",
       "      <td>2.875</td>\n",
       "      <td>17.02</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Hornet 4 Drive</td>\n",
       "      <td>21.4</td>\n",
       "      <td>6</td>\n",
       "      <td>258.0</td>\n",
       "      <td>110</td>\n",
       "      <td>3.08</td>\n",
       "      <td>3.215</td>\n",
       "      <td>19.44</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Valiant</td>\n",
       "      <td>18.1</td>\n",
       "      <td>6</td>\n",
       "      <td>225.0</td>\n",
       "      <td>105</td>\n",
       "      <td>2.76</td>\n",
       "      <td>3.460</td>\n",
       "      <td>20.22</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Merc 240D</td>\n",
       "      <td>24.4</td>\n",
       "      <td>4</td>\n",
       "      <td>146.7</td>\n",
       "      <td>62</td>\n",
       "      <td>3.69</td>\n",
       "      <td>3.190</td>\n",
       "      <td>20.00</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Merc 280</td>\n",
       "      <td>19.2</td>\n",
       "      <td>6</td>\n",
       "      <td>167.6</td>\n",
       "      <td>123</td>\n",
       "      <td>3.92</td>\n",
       "      <td>3.440</td>\n",
       "      <td>18.30</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            Model   mpg  cyl   disp   hp  drat     wt   qsec  vs  am  gear  \\\n",
       "1   Mazda RX4 Wag  21.0    6  160.0  110  3.90  2.875  17.02   0   1     4   \n",
       "3  Hornet 4 Drive  21.4    6  258.0  110  3.08  3.215  19.44   1   0     3   \n",
       "5         Valiant  18.1    6  225.0  105  2.76  3.460  20.22   1   0     3   \n",
       "7       Merc 240D  24.4    4  146.7   62  3.69  3.190  20.00   1   0     4   \n",
       "9        Merc 280  19.2    6  167.6  123  3.92  3.440  18.30   1   0     4   \n",
       "\n",
       "   carb  \n",
       "1     4  \n",
       "3     1  \n",
       "5     1  \n",
       "7     2  \n",
       "9     4  "
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#display the first five rows with odd-numbered columns of cars\n",
    "\n",
    "odd_numbered_columns = cars.iloc[1::2].head()\n",
    "odd_numbered_columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "ab9d8f3a-9b20-48b9-a4ba-b65b5bd0a026",
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
       "      <th>Model</th>\n",
       "      <th>mpg</th>\n",
       "      <th>cyl</th>\n",
       "      <th>disp</th>\n",
       "      <th>hp</th>\n",
       "      <th>drat</th>\n",
       "      <th>wt</th>\n",
       "      <th>qsec</th>\n",
       "      <th>vs</th>\n",
       "      <th>am</th>\n",
       "      <th>gear</th>\n",
       "      <th>carb</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Mazda RX4</td>\n",
       "      <td>21.0</td>\n",
       "      <td>6</td>\n",
       "      <td>160.0</td>\n",
       "      <td>110</td>\n",
       "      <td>3.9</td>\n",
       "      <td>2.62</td>\n",
       "      <td>16.46</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Model   mpg  cyl   disp   hp  drat    wt   qsec  vs  am  gear  carb\n",
       "0  Mazda RX4  21.0    6  160.0  110   3.9  2.62  16.46   0   1     4     4"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#display the row that contains the 'Model' of 'Mazda RX4'\n",
    "\n",
    "cars.loc[cars['Model']=='Mazda RX4']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "5c89b273-8764-4896-a728-55ae36b86d8c",
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
       "      <th>Model</th>\n",
       "      <th>cyl</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>Camaro Z28</td>\n",
       "      <td>8</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Model  cyl\n",
       "23  Camaro Z28    8"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#identify the number of cylinders in car model 'Camaro Z28'\n",
    "#showing 'Model' for easier verification\n",
    "\n",
    "cars.loc[(cars['Model']=='Camaro Z28'),['Model','cyl']]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "eddc3bf7-aec7-46b7-af45-8a13855fc84c",
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
       "      <th>Model</th>\n",
       "      <th>cyl</th>\n",
       "      <th>gear</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Mazda RX4 Wag</td>\n",
       "      <td>6</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>Honda Civic</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>28</th>\n",
       "      <td>Ford Pantera L</td>\n",
       "      <td>8</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             Model  cyl  gear\n",
       "1    Mazda RX4 Wag    6     4\n",
       "18     Honda Civic    4     4\n",
       "28  Ford Pantera L    8     5"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#identify the number of cylinders and gear type in car models 'Mazda RX4 Wag', 'Ford Pantera L', and 'Honda Civic'\n",
    "#showing 'Model' for easier verification\n",
    "\n",
    "cars.loc[cars['Model'].isin(['Mazda RX4 Wag','Ford Pantera L','Honda Civic']),['Model','cyl','gear']]"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
