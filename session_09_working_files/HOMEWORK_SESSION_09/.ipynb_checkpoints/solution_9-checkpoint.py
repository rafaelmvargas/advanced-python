{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# COVID-19 Statistical Worksheet"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<U>Notes if you are using Jupyter Notebook</U>:  to call <B>exit()</B> from a notebook, please use <B>sys.exit()</B> (requires <B>import sys</B>); if a strange error occurs, it may be because Jupyter retains variables from all executed cells.  To reset the notebook's variables, click 'Restart Kernel' (the circular arrow) -- this will not undo any text changes.  "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<B>Please do as many of these tasks as you can.</B>  I don't know whether these tasks will be overly time consuming, so please spend a minimum of 2-3 hours and if you have not completed all credit questions after that time and are unable to continue due to time constraints, simply let me know you were not able to finish and any notes you have about the problems.  Thank you!  "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<B>please note</B> the usual caveats:\n",
    "<UL>\n",
    "    <LI>Hints and discussion are in the <B>Discussion Document</B> for this session.</LI>\n",
    "    <LI>Some tasks may require the use of <B>new features</B>.  These will be mentioned in the question and discussed in more depth in the Discussion.</LI>\n",
    "    <LI><B>My answers</B> and results <B>may not always be the best</B>, or even correct!  I am also a student of this library, so there may be better or possibly even more accurate answers than the ones I supply.  <U>If you find a discrepancy between your answer and mine, but yours looks correct</U>, the proper response is to investigate by cross-checking, not to try to fit your answer to my results!  Let me know if you see differences and we'll have a look.  </LI>\n",
    "</UL>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 1: import the data\n",
    "<UL>\n",
    "    <LI>Import the data file <B>covid_event.csv</B> from this week's files.</LI>\n",
    "    <LI>Set the date column as the index, as some of the charting and grouping will be done with the date as a reference.</LI>\n",
    "    <LI>Once it has been set to the index, set the type of the index to <B>datetime64[ns]</B></LI>\n",
    "(It is also possible for the index and data type to be set in the <B>.read_csv()</B> function when you first ingest the data.)\n",
    "    <LI>Check the index's <B>dtype</B> to confirm that it has changed.</LI>\n",
    "</UL>\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
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
       "      <th>county</th>\n",
       "      <th>state</th>\n",
       "      <th>fips</th>\n",
       "      <th>cases</th>\n",
       "      <th>deaths</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>date</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2020-01-21</th>\n",
       "      <td>Snohomish</td>\n",
       "      <td>Washington</td>\n",
       "      <td>53061.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-01-22</th>\n",
       "      <td>Snohomish</td>\n",
       "      <td>Washington</td>\n",
       "      <td>53061.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-01-23</th>\n",
       "      <td>Snohomish</td>\n",
       "      <td>Washington</td>\n",
       "      <td>53061.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-01-24</th>\n",
       "      <td>Cook</td>\n",
       "      <td>Illinois</td>\n",
       "      <td>17031.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-01-24</th>\n",
       "      <td>Snohomish</td>\n",
       "      <td>Washington</td>\n",
       "      <td>53061.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-08-11</th>\n",
       "      <td>Sweetwater</td>\n",
       "      <td>Wyoming</td>\n",
       "      <td>56037.0</td>\n",
       "      <td>7</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-08-11</th>\n",
       "      <td>Teton</td>\n",
       "      <td>Wyoming</td>\n",
       "      <td>56039.0</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-08-11</th>\n",
       "      <td>Uinta</td>\n",
       "      <td>Wyoming</td>\n",
       "      <td>56041.0</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-08-11</th>\n",
       "      <td>Washakie</td>\n",
       "      <td>Wyoming</td>\n",
       "      <td>56043.0</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020-08-11</th>\n",
       "      <td>Weston</td>\n",
       "      <td>Wyoming</td>\n",
       "      <td>56045.0</td>\n",
       "      <td>-1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>424611 rows × 5 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                county       state     fips  cases  deaths\n",
       "date                                                      \n",
       "2020-01-21   Snohomish  Washington  53061.0      1       0\n",
       "2020-01-22   Snohomish  Washington  53061.0      0       0\n",
       "2020-01-23   Snohomish  Washington  53061.0      0       0\n",
       "2020-01-24        Cook    Illinois  17031.0      1       0\n",
       "2020-01-24   Snohomish  Washington  53061.0      0       0\n",
       "...                ...         ...      ...    ...     ...\n",
       "2020-08-11  Sweetwater     Wyoming  56037.0      7       0\n",
       "2020-08-11       Teton     Wyoming  56039.0      2       0\n",
       "2020-08-11       Uinta     Wyoming  56041.0      2       1\n",
       "2020-08-11    Washakie     Wyoming  56043.0      2       0\n",
       "2020-08-11      Weston     Wyoming  56045.0     -1       0\n",
       "\n",
       "[424611 rows x 5 columns]"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "\n",
    "cases = pd.read_csv('./covid_event.csv',index_col='date')\n",
    "cases.index = cases.index.astype(\"datetime64[ns]\")\n",
    "cases"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 2: explore the DataFrame\n",
    "\n",
    "Once imported, make sure to check on the import by reviewing your DataFrame's first few rows, its structure and size, with all of the following tools (these are not required for your solution, but try each one of them to get a sense of it):\n",
    "<B><UL>\n",
    "    <LI>len()</LI>\n",
    "    <LI>.head() and .tail()</LI>\n",
    "    <LI>.columns</LI>\n",
    "    <LI>.dtypes</LI>\n",
    "    <LI>.describe()</LI>\n",
    "    </UL></B></LI>\n",
    "    <LI><U>You may also need</U> to see more of the DataFrame than Notebook displays (default maximum of 10 rows).  You can modify the pandas defaults thusly:\n",
    "\n",
    "<PRE>\n",
    "pd.set_option('display.max_rows', 500)\n",
    "pd.set_option('display.max_columns', 20)\n",
    "        </PRE></LI>\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "424611  rows\n",
      "\n",
      "               county       state     fips  cases  deaths\n",
      "date                                                     \n",
      "2020-01-21  Snohomish  Washington  53061.0      1       0\n",
      "2020-01-22  Snohomish  Washington  53061.0      0       0\n",
      "2020-01-23  Snohomish  Washington  53061.0      0       0\n",
      "2020-01-24       Cook    Illinois  17031.0      1       0\n",
      "2020-01-24  Snohomish  Washington  53061.0      0       0 \n",
      "\n",
      "                county    state     fips  cases  deaths\n",
      "date                                                   \n",
      "2020-08-11  Sweetwater  Wyoming  56037.0      7       0\n",
      "2020-08-11       Teton  Wyoming  56039.0      2       0\n",
      "2020-08-11       Uinta  Wyoming  56041.0      2       1\n",
      "2020-08-11    Washakie  Wyoming  56043.0      2       0\n",
      "2020-08-11      Weston  Wyoming  56045.0     -1       0 \n",
      "\n",
      "Index(['county', 'state', 'fips', 'cases', 'deaths'], dtype='object') \n",
      "\n",
      "county     object\n",
      "state      object\n",
      "fips      float64\n",
      "cases       int64\n",
      "deaths      int64\n",
      "dtype: object\n"
     ]
    }
   ],
   "source": [
    "print(len(cases), ' rows\\n');\n",
    "print(cases.head(), '\\n');\n",
    "print(cases.tail(), '\\n');\n",
    "print(cases.columns, '\\n');\n",
    "print(cases.dtypes);\n",
    "cases.describe();\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<U>Expected Output</U>:<br>\n",
    "<PRE>424611 rows\n",
    "\n",
    "first 5 lines:\n",
    "               county       state     fips  cases  deaths                  new\n",
    "date                                                                          \n",
    "2020-01-21  Snohomish  Washington  53061.0      1       0  SnohomishWashington\n",
    "2020-01-22  Snohomish  Washington  53061.0      0       0  SnohomishWashington\n",
    "2020-01-23  Snohomish  Washington  53061.0      0       0  SnohomishWashington\n",
    "2020-01-24       Cook    Illinois  17031.0      1       0         CookIllinois\n",
    "2020-01-24  Snohomish  Washington  53061.0      0       0  SnohomishWashington\n",
    "\n",
    "last 5 lines:\n",
    "                county    state     fips  cases  deaths                new\n",
    "date                                                                      \n",
    "2020-08-11  Sweetwater  Wyoming  56037.0      7       0  SweetwaterWyoming\n",
    "2020-08-11       Teton  Wyoming  56039.0      2       0       TetonWyoming\n",
    "2020-08-11       Uinta  Wyoming  56041.0      2       1       UintaWyoming\n",
    "2020-08-11    Washakie  Wyoming  56043.0      2       0    WashakieWyoming\n",
    "2020-08-11      Weston  Wyoming  56045.0     -1       0      WestonWyoming\n",
    "\n",
    "columns:\n",
    "Index(['county', 'state', 'fips', 'cases', 'deaths', 'new'], dtype='object')\n",
    "\n",
    "column dtypes:\n",
    "county     object\n",
    "state      object\n",
    "fips      float64\n",
    "cases       int64\n",
    "deaths      int64\n",
    "new        object\n",
    "dtype: object\n",
    "\n",
    "cases.describe:\n",
    "                fips          cases         deaths\n",
    "count  420389.000000  424611.000000  424611.000000\n",
    "mean    31024.987469      12.142074       0.389493\n",
    "std     16212.075849      83.494348       6.264726\n",
    "min      1001.000000   -1742.000000    -512.000000\n",
    "25%     18147.000000       0.000000       0.000000\n",
    "50%     29165.000000       1.000000       0.000000\n",
    "75%     46073.000000       5.000000       0.000000\n",
    "max     78030.000000    8021.000000    1221.000000"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 3: count of unique states represented in the data\n",
    "Please show a count of unique states in the data.  I found <B>55</B> unique areas in the 'state' column.\n",
    "\n",
    "(<U>Hint</U>:  the <B>.unique()</B> method discards duplicates.)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "55"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df1 = cases.state.unique();\n",
    "# len(df1);\n",
    "df1.size"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<U>Expected Output</U>:<br>\n",
    "<PRE>55</PRE>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 4. Show those 'states' not in a 50-state list.\n",
    "If there are <B>55</B> unique names in the <B>state</B> column, what are the 5 non-state names?  \n",
    "<UL>\n",
    "    <LI>Read into a DataFrame the reference file <B>state_name_abbrev.csv</B> to <I>programmatically</I> identify those names that are not part of the 50 state list.</LI>\n",
    "    <LI>Use the column of state names to identify which statements in your file are not found in the 50 state list.</LI>\n",
    "    <LI>This should be possible in one or two statements; there is no need to loop.  (<U>Hint</U>:  consider <B>set.difference()</B>, although there may be a more pandas-centric way.)</LI>\n",
    "</UL>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'Guam', 'Virgin Islands', 'Northern Mariana Islands', 'Puerto Rico', 'District of Columbia'}\n"
     ]
    }
   ],
   "source": [
    "states = pd.read_csv('./state_name_abbrev.csv').rename(columns = { 'name': 'state' });\n",
    "\n",
    "df_diff = set(cases.state.unique()).difference(set(states.state));\n",
    "\n",
    "print(df_diff);\n",
    "\n",
    "# states\n",
    "\n",
    "\n",
    "# states['state'].isin(cases.state.unique())\n",
    "\n",
    "# cases.state.isin(states['state'])\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<U>Expected Output</U>:<br>\n",
    "<PRE>{'Puerto Rico', 'District of Columbia', 'Virgin Islands', 'Northern Mariana Islands', 'Guam'}\n",
    "\n",
    "28        District of Columbia\n",
    "50                 Puerto Rico\n",
    "51              Virgin Islands\n",
    "52                        Guam\n",
    "54    Northern Mariana Islands\n",
    "dtype: object</PRE>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 5:  count of unique counties represented in the data\n",
    "Find a unique count of counties in the data set.  Since some county names are not unique among states, a unique count of counties will look for <B>state</B> and <B>county</B> in combination.  I found <B>3250</B> unique state + county combinations.  \n",
    "\n",
    "<U>Hint</U>:  a groupby object has an <B>.ngroups</B> attribute which returns the number of groups.  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3250\n"
     ]
    }
   ],
   "source": [
    "grouping = cases.groupby(['county', 'state']).ngroups;\n",
    "print(grouping);\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<U>Expected Output</U>:<br>\n",
    "<PRE>3250</PRE>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 6: cases by state, sorted\n",
    "Please sum the number of cases grouped by state.  Then, use <B>.sort_values()</B> with the parameter argument <B>ascending=False</B> to sort the states by cases, from highest to lowest."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
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
       "      <th>cases</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>state</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>California</th>\n",
       "      <td>586078</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Florida</th>\n",
       "      <td>542784</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Texas</th>\n",
       "      <td>522626</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>New York</th>\n",
       "      <td>426713</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Georgia</th>\n",
       "      <td>205920</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Illinois</th>\n",
       "      <td>198975</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Arizona</th>\n",
       "      <td>188780</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>New Jersey</th>\n",
       "      <td>187328</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>North Carolina</th>\n",
       "      <td>138124</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Louisiana</th>\n",
       "      <td>133243</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Pennsylvania</th>\n",
       "      <td>125079</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Tennessee</th>\n",
       "      <td>122089</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Massachusetts</th>\n",
       "      <td>121707</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Alabama</th>\n",
       "      <td>103851</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Ohio</th>\n",
       "      <td>102827</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>South Carolina</th>\n",
       "      <td>102130</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Virginia</th>\n",
       "      <td>101924</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Michigan</th>\n",
       "      <td>98361</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Maryland</th>\n",
       "      <td>97403</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Indiana</th>\n",
       "      <td>77627</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Mississippi</th>\n",
       "      <td>68479</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Washington</th>\n",
       "      <td>66620</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Wisconsin</th>\n",
       "      <td>66146</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Missouri</th>\n",
       "      <td>61932</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Minnesota</th>\n",
       "      <td>61880</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Nevada</th>\n",
       "      <td>57608</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Colorado</th>\n",
       "      <td>51578</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Connecticut</th>\n",
       "      <td>50684</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Arkansas</th>\n",
       "      <td>50411</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Iowa</th>\n",
       "      <td>49521</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Utah</th>\n",
       "      <td>44836</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Oklahoma</th>\n",
       "      <td>44726</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Kentucky</th>\n",
       "      <td>37503</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Kansas</th>\n",
       "      <td>32174</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Nebraska</th>\n",
       "      <td>29030</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Idaho</th>\n",
       "      <td>25961</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Puerto Rico</th>\n",
       "      <td>23403</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>New Mexico</th>\n",
       "      <td>22650</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Oregon</th>\n",
       "      <td>21782</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Rhode Island</th>\n",
       "      <td>20053</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Delaware</th>\n",
       "      <td>15699</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>District of Columbia</th>\n",
       "      <td>12896</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>South Dakota</th>\n",
       "      <td>9713</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>North Dakota</th>\n",
       "      <td>7889</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>West Virginia</th>\n",
       "      <td>7877</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>New Hampshire</th>\n",
       "      <td>6863</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Montana</th>\n",
       "      <td>5125</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Alaska</th>\n",
       "      <td>4595</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Maine</th>\n",
       "      <td>4052</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Hawaii</th>\n",
       "      <td>3733</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Wyoming</th>\n",
       "      <td>3074</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Vermont</th>\n",
       "      <td>1472</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Guam</th>\n",
       "      <td>1403</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Virgin Islands</th>\n",
       "      <td>639</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Northern Mariana Islands</th>\n",
       "      <td>82</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                           cases\n",
       "state                           \n",
       "California                586078\n",
       "Florida                   542784\n",
       "Texas                     522626\n",
       "New York                  426713\n",
       "Georgia                   205920\n",
       "Illinois                  198975\n",
       "Arizona                   188780\n",
       "New Jersey                187328\n",
       "North Carolina            138124\n",
       "Louisiana                 133243\n",
       "Pennsylvania              125079\n",
       "Tennessee                 122089\n",
       "Massachusetts             121707\n",
       "Alabama                   103851\n",
       "Ohio                      102827\n",
       "South Carolina            102130\n",
       "Virginia                  101924\n",
       "Michigan                   98361\n",
       "Maryland                   97403\n",
       "Indiana                    77627\n",
       "Mississippi                68479\n",
       "Washington                 66620\n",
       "Wisconsin                  66146\n",
       "Missouri                   61932\n",
       "Minnesota                  61880\n",
       "Nevada                     57608\n",
       "Colorado                   51578\n",
       "Connecticut                50684\n",
       "Arkansas                   50411\n",
       "Iowa                       49521\n",
       "Utah                       44836\n",
       "Oklahoma                   44726\n",
       "Kentucky                   37503\n",
       "Kansas                     32174\n",
       "Nebraska                   29030\n",
       "Idaho                      25961\n",
       "Puerto Rico                23403\n",
       "New Mexico                 22650\n",
       "Oregon                     21782\n",
       "Rhode Island               20053\n",
       "Delaware                   15699\n",
       "District of Columbia       12896\n",
       "South Dakota                9713\n",
       "North Dakota                7889\n",
       "West Virginia               7877\n",
       "New Hampshire               6863\n",
       "Montana                     5125\n",
       "Alaska                      4595\n",
       "Maine                       4052\n",
       "Hawaii                      3733\n",
       "Wyoming                     3074\n",
       "Vermont                     1472\n",
       "Guam                        1403\n",
       "Virgin Islands               639\n",
       "Northern Mariana Islands      82"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cases_by_state_sorted = cases.groupby(['state']).sum().sort_values('cases', ascending=False).drop(columns=['fips','deaths'])\n",
    "cases_by_state_sorted"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<U>Expected Output</U>:<br>\n",
    "<PRE>state\n",
    "California                  586078\n",
    "Florida                     542784\n",
    "Texas                       522626\n",
    "New York                    426713\n",
    "Georgia                     205920\n",
    "Illinois                    198975\n",
    "Arizona                     188780\n",
    "New Jersey                  187328\n",
    "North Carolina              138124\n",
    "Louisiana                   133243\n",
    "Pennsylvania                125079\n",
    "Tennessee                   122089\n",
    "Massachusetts               121707\n",
    "Alabama                     103851\n",
    "Ohio                        102827\n",
    "South Carolina              102130\n",
    "Virginia                    101924\n",
    "Michigan                     98361\n",
    "Maryland                     97403\n",
    "Indiana                      77627\n",
    "Mississippi                  68479\n",
    "Washington                   66620\n",
    "Wisconsin                    66146\n",
    "Missouri                     61932\n",
    "Minnesota                    61880\n",
    "Nevada                       57608\n",
    "Colorado                     51578\n",
    "Connecticut                  50684\n",
    "Arkansas                     50411\n",
    "Iowa                         49521\n",
    "Utah                         44836\n",
    "Oklahoma                     44726\n",
    "Kentucky                     37503\n",
    "Kansas                       32174\n",
    "Nebraska                     29030\n",
    "Idaho                        25961\n",
    "Puerto Rico                  23403\n",
    "New Mexico                   22650\n",
    "Oregon                       21782\n",
    "Rhode Island                 20053\n",
    "Delaware                     15699\n",
    "District of Columbia         12896\n",
    "South Dakota                  9713\n",
    "North Dakota                  7889\n",
    "West Virginia                 7877\n",
    "New Hampshire                 6863\n",
    "Montana                       5125\n",
    "Alaska                        4595\n",
    "Maine                         4052\n",
    "Hawaii                        3733\n",
    "Wyoming                       3074\n",
    "Vermont                       1472\n",
    "Guam                          1403\n",
    "Virgin Islands                 639\n",
    "Northern Mariana Islands        82\n",
    "Name: cases, dtype: int64</PRE>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 7: bar chart:  cases by state, 10 highest\n",
    "Working from the data built above, show the first 10 states and number of cases in a bar chart. \n",
    "\n",
    "<U>Note</U> that a semicolon placed at the end of any <B>.plot()</B> statements will hide the <B>&lt;AxesSubplot&gt;</B> object from display."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
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
    "cases_by_state_sorted.head(n=10).plot(kind='bar', legend=False, rot=45);"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<U>Expected Output</U>:<br>\n",
    "<IMG SRC=\"images/hw7.png\" align=\"left\">"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 8: show cases by county for a given state.\n",
    "Take user input for a state name (or you can hard-code the state name).  Show the cases by county within the state, sorted from highest to lowest."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Please enter a state name: Florida\n",
      "               cases\n",
      "county              \n",
      "Miami-Dade    135129\n",
      "Broward        63605\n",
      "Palm Beach     37639\n",
      "Hillsborough   32996\n",
      "Orange         32041\n",
      "...              ...\n",
      "Franklin         433\n",
      "Liberty          407\n",
      "Glades           406\n",
      "Gilchrist        369\n",
      "Lafayette        189\n",
      "\n",
      "[68 rows x 1 columns]\n"
     ]
    }
   ],
   "source": [
    "s_input = input('Please enter a state name: ')\n",
    "z= cases[cases['state']==s_input].groupby(['county']).sum().sort_values('cases', ascending=False).drop(columns=['fips','deaths'])\n",
    "print(z)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<U>Expected Output</U>:<BR>\n",
    "<PRE>please enter a state name: Florida\n",
    "total 68\n",
    "county\n",
    "Miami-Dade      135129\n",
    "Broward          63605\n",
    "Palm Beach       37639\n",
    "Hillsborough     32996\n",
    "Orange           32041\n",
    "Duval            23741\n",
    "Pinellas         18103\n",
    "Lee              16717\n",
    "Polk             14645\n",
    "Collier          10487\n",
    "Osceola           9858\n",
    "Escambia          9807\n",
    "Manatee           9395\n",
    "Volusia           8040\n",
    "Seminole          7219\n",
    "Pasco             7172\n",
    "Marion            6668\n",
    "Sarasota          6314\n",
    "Brevard           6190\n",
    "St. Lucie         5920\n",
    "Lake              5229\n",
    "Leon              5115\n",
    "Bay               4523\n",
    "Alachua           4246\n",
    "Santa Rosa        4013\n",
    "Martin            3852\n",
    "St. Johns         3738\n",
    "Okaloosa          3586\n",
    "Clay              3327\n",
    "Columbia          2917\n",
    "Indian River      2555\n",
    "Charlotte         2281\n",
    "Hernando          2069\n",
    "Jackson           1936\n",
    "Gadsden           1927\n",
    "Hendry            1805\n",
    "Citrus            1594\n",
    "Monroe            1548\n",
    "Putnam            1539\n",
    "Suwannee          1507\n",
    "Highlands         1474\n",
    "Walton            1428\n",
    "DeSoto            1377\n",
    "Sumter            1344\n",
    "Nassau            1253\n",
    "Flagler           1095\n",
    "Okeechobee        1077\n",
    "Hardee             986\n",
    "Taylor             981\n",
    "Baker              964\n",
    "Washington         877\n",
    "Wakulla            726\n",
    "Unknown            721\n",
    "Madison            710\n",
    "Levy               698\n",
    "Gulf               685\n",
    "Hamilton           623\n",
    "Dixie              562\n",
    "Bradford           519\n",
    "Holmes             509\n",
    "Calhoun            481\n",
    "Jefferson          462\n",
    "Union              435\n",
    "Franklin           433\n",
    "Liberty            407\n",
    "Glades             406\n",
    "Gilchrist          369\n",
    "Lafayette          189\n",
    "Name: cases, dtype: int64</PRE>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 9: bar chart:  cases by county for a given state, 10 highest\n",
    "Working from the above data, show the first 10 counties in a bar chart."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "vscode": {
     "languageId": "javascript"
    }
   },
   "outputs": [
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
    "z[0: 10].plot(kind = 'bar', rot = 45, legend=False);"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<U>Expected Output</U> (image may be cut off at bottom):<BR>\n",
    "<PRE>please enter a state name: New York\n",
    "total 59</PRE>\n",
    "<IMG SRC=\"images/hw9.png\" align=\"left\">"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 10: pie chart showing all 50 states and share of cases\n",
    "Show the number of cases by state in a pie chart.\n",
    "<UL>\n",
    "    <LI>The plot() arguments I used were <B>kind='pie'</B>, <B>figsize=(5,5)</B>,  <B>labels=None</B> </LI>\n",
    "<LI>I set a legend by using the <B>plt.legend()</B> method with <B>loc=(.95,.35)</B> (for positioning) and <B>labels=</B> equal to the first 10 names in the index.</LI>\n",
    "    </UL>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "\n",
    "top_states = cases_by_state_sorted.head(n=10)\n",
    "top_states = top_states.reset_index()\n",
    "labels_pie = top_states.state\n",
    "\n",
    "plt.pie(cases_by_state_sorted.cases)\n",
    "plt.legend(labels=labels_pie, loc=(.95,.35))\n",
    "plt.show()\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<U>Expected Output</U>:<BR>\n",
    "<IMG SRC=\"images/hw10.png\" align=\"left\">"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 11: pie chart showing top 10 states and share of cases among them\n",
    "perform the same aggregation and charting as above, but chart a slice of just the first 10 states"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "vscode": {
     "languageId": "javascript"
    }
   },
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAUkAAADzCAYAAAALrOQPAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8qNh9FAAAACXBIWXMAAAsTAAALEwEAmpwYAABJV0lEQVR4nO3deXhTVfoH8O9N0qb7XrrQlpS2aZM2LaVYKFB2BIWibKKggI4OII6juNAZZzBuCDODIoKKoFhExm10FIobg5Sl7IWuSVsKXaD7vqdJ7vn90ZZfge5NcpP0fJ4nj9ok57yR8ubce855D0MIAUVRFNU9HtcBUBRFGTOaJCmKonpBkyRFUVQvaJKkKIrqBU2SFEVRvaBJkqIoqhcCrgOgKHN06dKlEQKBYC+AMNDBiDFjAWRoNJono6Kiyrt7AU2SFKUHAoFgr6enp8Td3b2Gx+PRxchGimVZpqKiQlpaWroXwILuXkO/4ShKP8Lc3d3raYI0bjwej7i7u9ehfcTf/WsMGA9FDSc8miBNQ8efU4+5kCZJijJThYWFgvnz54/29fUNCw0NlUydOjUwLS1N2NPrbWxsIgEgPz/fYu7cuaM7fx4XF+cvFoulr7322oihxnTixAmb1atX+w61HUOi9yQpygBE8YlRumwvf8u8S709z7IsFixYELh8+fKqw4cPXwOAM2fOWBcXF1uEh4ereo1VJFL//PPP14D2RJuammpbWFiY0d/Y1Go1LCwsun1uypQpzVOmTGnub1vGgI4kKcoMHT582F4gEJCXX365ovNnMTExLTExMc0xMTFiqVQqEYvF0gMHDjjd+d7s7GzLoKCgUACYNWuWuLy83DIkJET6888/2yUnJ1tHRESEiMVi6ezZswMqKir4ABAdHR38xBNP+IaFhUnefPNNj+jo6OB169aNlMlkEpFIFPbzzz/bdcY1ffr0QAD4/fffbcaMGRMikUikkZGRIampqT2OcrlEkyRFmaG0tDTriIiIu0ZsNjY2bGJi4tWsrCxFUlJSzl//+lcflmV7bOfQoUNXfX19VUqlMmvu3LmNq1ev9t+8efONnJycrNDQ0JaNGzd6d762ra2NycjIULz22mtlAKDRaJj09HTF1q1bi15//XXvO9uOiIhovXDhglKhUGS9+uqrN19++WUfHX18naKX2xQ1jLAsyzz33HM+Z8+etePxeCgvL7e8ceOGwM/PT9PXe6uqqvgNDQ38efPmNQLAU089VbV06dJb9y4feeSR6q6vX7p0aQ0ATJw4semll16yvLO96upq/rJly/zz8/OtGIYharWaGfon1D06kqQoMySTyVpSU1Nt7vz57t27XaqqqgTp6ekKpVKZ5erqqm5padFJHrC3t79tSGplZUUAQCAQQKvV3pUAN27cOHLq1KkNubm5mYcOHbra1tZmlPnIKIOiKGpo4uLiGtra2ph//etfbp0/O3funHVBQYGlm5ubWigUkkOHDtkXFxffNcLriaurq9bBwUHbeX/xk08+cY2JiWkcbIz19fV8Hx+fNgDYvXu3W1+v5wpNkhRlhng8Hn788ce8Y8eOOfj6+oYFBgaGbty4ceSCBQvqUlNTbcVisTQhIcHV39+/dSDt7tu37/rGjRt9xGKxNC0tzXrLli3Fg41x48aNpXK53EcikUg1mj6v9jnD0OMbKEr3UlNT8yMiIiq5joPqn9TUVLeIiAhRd8/RkSRFUVQvaJKkKIrqBU2SFEVRvaBJkqIoqhc0SVIURfWCJkmKoqhe0CRJUWaKz+dHhYSESDsf2dnZll0LTPRXb+XNRo4cKSspKTHr7c1m/eEoymjIHXVaKg3yul5LpQGAUChklUplVtef5ebmDqjSjlqtNsnyZrpER5IUNUyVlZXxZ82aFSAWi6UREREh586dswaADRs2eD/44IP+Y8eODVm0aJF/19FnaWkpf9KkSUGBgYGhy5YtG9V1M8qsWbMCQkNDJYGBgaFdt0OaOpokKcpMqVQqXuel9uzZswPufP7ll1/2joiIaM7Jycl64403bq5atcq/87nc3FyrEydOZB86dOh61/fEx8d7x8TENF69ejVz4cKFtSUlJbf2fn/xxRf5mZmZiitXrmTt3r3bo7S0lK/fT2gYNElSlJnqvNxWKpVZv/32W96dz58/f97+D3/4QxUALFiwoKG2tlZQXV3NA4C5c+fW2tnZ3bVn+ezZs/ZPPPFEFQA8/PDDdQ4ODtrO57Zu3eoRHBwsjYqKkpSWllpkZmZa6e/TGQ69J0lR1F1sbW17rsTbjcOHD9snJSXZX7x4UWlvb89GR0cH66oEG9fM4kNQFDVw48ePb9i3b58r0J7knJ2dNS4uLr0mxwkTJjR89tlnrgDw9ddfO9TX1/MBoLa2lu/o6Ki1t7dnL1++bJWammqr/09gGHQkSVHD1NatW4tXrFghEovFUmtra/azzz673td7tmzZUrx48eLRgYGBoePGjWv08vJqA4DFixfXffzxx+6jR48OHT16dGtEREST/j+BYdBSaRSlB7RUmmmhpdIoiqIGiSZJiqKoXtAkSVEU1QuaJCmKonpBkyRFUVQv6BIgYyZ3FAAQAQgAMBKAGwD3Lg83ADYA+Gj/sxR0/DsPQAuA+i6PBgA1AG4AKOh45AMog7yOLnGgqB7QJGks5I6+ACYAGAtACkACwB/6/zNqhdzxOoBUAJc7HimQ11XpuV9Kj0pLS/nTpk0LBoDKykoLHo9HXFxcNABw5coVhZWVFf1i7CeaJLnQPkK8B0BMl8dIjqKxQntClgB4+NZP5Y5FAM4BOAbgKOR1uZxEZyZkCTKdlkpLX5Xea6k0T09PbWeZtA0bNnjb2dlpX3/99TJdxjBc0CRpKHJHNwD3AZgP4F4ATpzG0zffjscSAIDcsRDA/wAcBfAz5HXV3IVGDcbJkydtNmzY4Nvc3MxzdnbWfPHFF/l2dnZsVFSU5IcffsiNiIhQxcXF+U+bNq3hhRdeqFyxYoVfamqqbWtrKy8uLq7m3XffLQaAp59+euQvv/zixOfzybRp0+o//vjjG1x/Nn2iSVKf2i+hlwN4AMB4mPZEmR+AxzseasgdjwL4GsD3kNfVcRoZ1SdCCJ599lm/xMTEq97e3po9e/Y4v/jiiyO/+eab/Hfffbdw1apV/k8//XRZbW2t4IUXXqgEgHfeeeemh4eHVqPRYOLEicHnzp2zHjVqVNuRI0ecr127lsHj8VBZWWkW5dB6Q5OkrskdbQEsBrAKwDSYdmLsiQXaR8X3AdgNueOvAP4N4DvI61o5jYzqlkql4uXm5lrPmDFDDAAsy8Ld3V0NAAsXLqz/+uuvnV9++eVRly5dyux8T0JCgstnn33mptFomIqKCovU1FSrsWPHtgiFQnbZsmWi+fPn1y5btszsvyBpktQVueMEAGvRniDtOI7GkCzRfgthPoBqyB33f6WZ9sGyN3+g9zCNCCEEgYGBLVeuXFHe+ZxWq0VOTo6VlZUVW1VVJQgICFArlUrLnTt3ely6dEnh7u6uXbx4sai1tZVnYWGBK1euKH788UeHb7/91vnDDz8ccfbs2RwuPpOhmOMox3DkjjzIHRdB7ngawBm0jx6HU4K8kwshWPcPzbLTovjEn0XxifeL4hMZroOi2gvwVldXC44ePWoLACqVirl48aIVALz++useYrG49bPPPrv2xBNPiFQqFVNTU8O3trZmXVxctEVFRYLjx487AkBdXR2vurqav2zZsrqPPvqoSKlU2nD5uQyBjiQHo/2S+nEAz6F9DSPVIYf4XKyC4yQAczoeWaL4xNcAfJO/ZR5ddsIRHo+HL7/8Mu/ZZ5/1a2ho4Gu1WmbdunVlFhYW5PPPP3e7dOmSwtnZmf32228b4uPjvd59993isLCw5oCAgDAvL6+2qKioRqC9buT8+fMDVSoVAwBvvPFGEbefTP9oqbSBkDtaAlgH4BW0L+am7rCi7a+Zp9mw0G6eSgfwGoDvhkOypKXSTAstlTZU7ZfVKwFkA9gOmiC71USEih4SJADIAHwL4LIoPvFBw0VFUUNDk2Rf5I73A7gCIAHtWwSpHuzV3t+fXToRAL4XxScmieITw/QdE0UNFb0n2RO5ow+AnWhf40j1gSWo/VCzYCC7SqagfVS5E8Cm/C3zGvQUGkUNCR1J3knuyIfc8TkACtAE2W9n2NDUVgitB/g2Adonv7JF8YkrdB8VRQ0dTZJdyR3Hon2/8rsY3kt5BoQQkE2a1aIhNOEF4IAoPvGoKD7RR0dhUZRO0CQJdE7MvIL2BKnTQgTDQQWcLuWRkaN00NRMAGmi+MSHdNAWRekETZJyx5FoL9zwJug92kH5l2bpgA6y74MzgK9E8YkJovhEex22O+wwDBP11FNP3RqZb9q0yWPDhg3eumi7ubmZ8ff3Dz1//vytWyx///vfPZYvX96vL8sNGzZ4b9q0yUMXsejb8E4KcscHAHwCwJXrUEyVhvBufKOdOk4PTa8EECuKT3w0f8u8ZD20b1CKEIlOr1AkSkWvpdIAwNLSkhw5csS5pKSk1MvLS6PL/m1sbMg///nPonXr1vlduHAhu6CgwOKzzz5zT0lJUfT1XrVarctQ9G54jiTljgLIHd8D8F/QBDkkP7CT8gh4+vo98geQJIpPXK+n9s0an88nK1eurNi8efNdI7bi4mLBnDlzAsLCwiRhYWGSX3/91RYAxGKxtLKyks+yLJycnMbs3LnTFQAWLlwo+v777x26trFkyZJ6Dw8P9a5du1zXr1/vGx8fX1xdXc2fMGGCWCwWS2NiYsS5ubmWALB48WLR8uXL/cLDw0PWrVt3233nbdu2uU2ZMiWosbHRKLewDr8k2V7X8TcAz3IdiqkjBKrN6uU9LR7XFQGAnaL4xI9E8YkWeu7L7Lz00kvl3333nUtVVdVtJc3WrFnju2HDhrKMjAzF999/n7d27VoRAIwbN67x6NGjdpcuXbLy8fFRnTp1yg4AUlJS7GbOnNl4Z/sffPBB0ZtvvjmyqqpKsH79+up169b5rVixoionJydr2bJlVevWrfPtfG1JSYllSkqKcu/evbfqT27evNn9yJEjjr/88stVOzs7o9yJNawut2UJstAnnB3ffL6mbhrXsZiDLvu0DWENgBBRfOKS/C3z6Ha/fnJxcWGXLl1atWXLlhHW1ta37h2fPn3aITc399b9xMbGRn5dXR0vNja2MSkpyS4/P9/yySefLN+3b5/79evXLRwcHLQODg533XsWiUTqiRMn1s+bN68OAC5fvmz7008/5QHAunXrql977bVbo8ZFixbVCAT/n3K+/PJLV29v77ZffvklTygUGmWCBIbRSFKWILsXwOlPHR3m/2xr0+f9HKpvb2geczRwl1MBnBfFJ8oM3K9J+8tf/lJ28OBBt6amplt/3wkhSElJUSiVyiylUplVXl6e5ujoyM6ePbvh7Nmz9qdPn7a79957G1xdXTUHDhxwnjBhQo+L/Xk8Hvj8vmvv2tnZ3ZZkQ0JCWm7cuCG8fv26UV8hDIskKUuQrQCQCMARDCN4yd01MMfC4jrXcZmyZiJUnmJlXGwr9AdwShSfaKgRrMnz8PDQxsXF1Rw8eNCt82eTJ0+uf/vtt0d0/ndycrI1AAQGBqpramoE169ft5JKpW0xMTGNu3bt8pw6depdl9rdiYyMbNq7d68zAOzevdtl3LhxPb5vzJgxzbt27SpYsGBBYH5+vtEmSrNPkrIE2R8B7EfXWwsM4/jwSE+mjser5SouU7dXex+Xl7wOAH4RxSfO5DAGk/LKK6+U1tbW3vo78PHHHxelpKTYisViaUBAQOjOnTtvFW0ZM2ZMk7+/fysATJs2raG8vNxi1qxZ/do2+tFHHxV+/vnnbmKxWPrvf//b9YMPPui1lNqcOXMa33777Rv33XdfUElJiVHe/jPrUmmyBNkGANt6et5Fq035X+HNcMEwuzc7VISgTqraZ9ECIdcFV1UAluRvmXeY4zjuQkulmZZhWSpNliB7Fb0kSACo5vPHrvbyMPk1eIaWzIZeMYIECQBCAN/RHTqUPpllkpQlyF4BIO/Pa1OthFP+4eJ0Qr8RmQ9CQOSaVbrYgqgrFgAOiuITH+E6EMo8mV2SlCXI/oD2LYb99rmD/SQ6490/FXBMySU+Iq7juAMfQIIoPnE214FQ5seskqQsQTYfwO4Bv5Fh+HTGu3+2aZZquY6hBxZov/TWxxZJahgzmyQpS5DFAPga7aOKgaMz3n3SEN7Nb7TTjLlKkh2AI6L4xCCuA6HMh1kkSVmCLATAYQADLfp6GzXDiBb4eF3TADotBmAufmQnXmXBG9yXkOG4o315kCfXgVDmweSTpCxBNhLALwBcdNFeNZ8/dhWd8b4LIWjbrF4u5TqOfvIHcEgUnyjkOhAuFRUVCeLi4vx9fHxkoaGhkjFjxoTs37/fSZ99Llu2bNSlS5es9NmHoZn0+kBZgswawBEAfrpsN81KOGWri1PSxuraqbps15TlkpEXKuFkSrtcxgF4H8AfuQ4EAHatPabT2xTrP5rR60Qjy7KIi4sLXL58edWhQ4euA0BOTo7lN9984zSUftVqNSwset4c89VXXxUMpX1jZOojyX8ACNdHwwcc7CfTGe//x8E+bV14ShSf+ATXQXDh0KFD9hYWFuTll1+u6PyZWCxue+WVV8o1Gg3WrFnjExYWJhGLxdJ//vOfbkB7Yl2zZo1PUFBQqFgslu7Zs8cZAA4fPmwfFRUVPGPGjMCgoKAwrVaLRx991M/f3z904sSJQVOnTg3ct2+fMwBER0cHnzhxwgYAVqxY4RcWFiYJDAwMff7553VS7JcLJjuSlCXI7gPwjN466JjxHt2mvi5Wq/311o8JaCbC7JNsuKke/7pLFJ94JX/LvBSuAzGk9PR06/Dw8Obuntu+fbubo6OjNiMjQ9HS0sLcc889IXFxcfVnz561SU9Pt1YoFJklJSWC6Ohoyb333tsIAFlZWTaXL1/ODAkJadu3b59zUVGR5dWrVzNv3rwpCAsLC1u9evVdxwm/8847Nz08PLQajQYTJ04MPnfunPX48eNb9P3Zdc0kR5KyBJkbgE/13hGd8QYAfKqdW851DENgBeBbUXyiTu5Zm6rHHnvMLzg4WBoWFiY5evSow9dff+0aEhIijYyMlNTU1AiysrKsTp48af/QQw9VCwQC+Pr6asaPH9946tQpGwAIDw9vCgkJaQOAkydP2i1atKiGz+fDz89P01OFoISEBBepVCqRSqXS3Nxcq9TUVJO8V2mSSRLAXgAGmb1UM4wozsfr+nCd8SYEdbs0Dxrzsp/+8IchvlSNiEwma0lLS7u1dfTzzz8vPH78eE5NTY2AEMJs27atsLNM2s2bN9MXLVpU31t7NjY2AzrHSKlUWu7cudMjKSkpJycnJ2vGjBl1ra2tJplvTC5oWYLsKRj4POwaPj9yuM54n2GlxrJPe6geEMUnruI6CEOJi4trUKlUzNatW29V92lsbOQBwOzZs+s+/PBDd5VKxQBAWlqasL6+njdlypSGb7/91kWj0aC4uFhw/vx5u9jY2KY72548eXLjf//7X2etVouioiLBuXPn7jqwraamhm9tbc26uLhoi4qKBMePHzfFe9oATOyepCxBFoj2M7ENrmPG+8TG6topXPTPhY592jpdOcCx90Txicfyt8zrtXyXOeDxeDh06FDe+vXrfXfs2OHp4uKisbGx0crl8htPPPFETX5+vlAmk0kIIYyLi4v6yJEjeY899lhtcnKynUQiCWUYhrz22ms3/Pz8NGlpabe1vWrVqpqjR4/aBwYGhnp5ebWFhoY2Ozk53bYTKyYmpiUsLKw5ICAgzMvLqy0qKqpf9SiNkcmUSpMlyAQATgOI5iwIQrT/qKi6cl9Ts6lffvZLBXG8dI/qQ3P7rD/nb5l3n747MfdSaXV1dTxHR0e2tLSUf88990hOnz6t9PPzM9lbUuZSKm0TuEyQAMAw/JeH0R7vdzRLjHWf9lDMFcUnruQ6CFM3e/bsoJCQEOmkSZNCXnrppRJTTpB9MYmRpCxBNh7to0ij2BInIKTg98KbDk4s68x1LPqiIbxisWq/hwlsQxyMagDB+jxQzNxHkubGHEaS78FIEiQAaBhm1AIfr3xznvE+xMbkmmmCBNq3sL7GdRCUaTD6JClLkC0GMJ7rOO5Uw+dHrjTTGW9C0PaWeoWp7NMerDWi+ERz/4yUDhh1kuyYrNnMdRw9SbcSTtni4pTEdRy6dpV4X6iEk3vfrzRpfPRxvAdFAUaeJAH8AYCY6yB684WD/eSfzGyP9xuaxxy4jsFA5oriE+dwHQRl3Iw2ScoSZDYAXuU6jj51zHhnW1hc4zoUXWgmltkn2AgZ13EY0DZRfKJZ3nu1sbGJBIDs7GzLoKCgUKC9WMX06dMDAeCLL75w/Otf/zqonWv5+fkWc+fOHa27aI2XMS8mfw6AF9dB9Ev7Hu/a3wtv1pj6jPc+7X3lAIK5jsOAQgE8CiBBn51sWzZfp+tNX/jq8JCvXlasWFEHoG4w7xWJROqff/7ZLAYGfTHKkaQsQeYK4GWu4xiIzhlvNaDmOpbBat+n/cBYruPgwEZRfCLDdRCGtmPHDteVK1f6AcDixYtFq1ev9o2MjAzx8fGRdZY+66l8WtfR6cWLF61kMpkkJCREKhaLpenp6WZV7NgokySAFwCY3F7Pjj3eZ7iOY7DOspIrzbCy5ToODkhg4HoAxqisrMzi4sWLyh9++CH31VdfHQkA+/fvd+osn/a///0vZ9OmTT4FBQW3Vd19//333Z9++ukypVKZlZaWpvD392/j5hPoh9ElSVmCzBbAWq7jGCxTnfEmBORVzWpz2qc9UH/hOgCuLViwoJbP5yMqKqq1qqrKAgB6K5/WKSYmpmnbtm1er7zyimdubq6lnZ2d8e9QGQCjS5IAVgEw6ft6XzjYTz5ia3OR6zgGogoOl3OI73AuLhwtik+cwXUQXLKysrqV3AayE2/t2rXVP/zww1Vra2t2/vz5QT/++ONdVYFMmVElSVmCjAHwZ67jGDKG4W90dw0ypRnvdzRLTPZeqg7Fcx2AselP+bSsrCxLiUSi+tvf/lY+Z86c2itXrgzp1FJjY1RJEsB8GPm6yH5rn/Hm1/J4NVyH0hcN4RV/qZ0xjus4jMBsUXyiefz+6chjjz1WGxoa2iKRSEKnTZsm7iyf1vU1Bw4ccBGLxaEhISFShUJhvWbNmruOcjBlRlXgQpYg+w3ALK7j0CVnrfby/wpvhlkAPR8xx7H/aicmPad+hp4M2W5r/pZ5Qx5R0gIXpsUkClzIEmQiADO5jkPXjH3Gu/08bbPfpz0QK811cTk1OEaTJNE+YWOWa9XSrYRT3nZxPsF1HN3JI94Xy+Fs7vu0B8ILwP1cB0EZD2NKkmZdCPWgg90kY5zxfkPzqFnNROrIH7gOgDIeRpEkZQmyGADmvQ/UCGe8W4hlThI7Zjjt0+6veaL4RA+ug6CMg1EkSQDLuQ7AIIxsxnufdm4Z1zEYKQGAB7kOgjIOxpIkH+Q6AEMxlj3ehKBup+bB4bhPu7/iuA6AMg6cJ0lZgiwCgA/XcRhSDZ8fudLb4yyXMZwjw3afdn/NFMUnmvx5459//rkTwzBRly9fturpNZGRkSGGjMnUGEOptHlcB8CFDKEw9m0X56S/VNdwsj7xVbVZnaetD1YAZgP4QReN3Yg/qdNSaT5bYvtVKu3LL790GTt2bOP+/ftdIiMji7s+p1arYWFhgcuXLyt1GZu54XwkiWGaJAHgoIMdJ3u8K4lDSjbxG877tPtrAdcBDEVdXR3vwoULdvv27cv//vvvXYD2ortRUVHBM2bMCAwKCgoD/r8473PPPecdEhIiDQkJkY4YMSJ8yZIlIgCQy+UeQUFBoUFBQaGvv/76CKC9VNro0aNDH3744VGBgYGhkyZNCmpsbGQAYNu2bW5hYWGS4OBg6Zw5cwIaGhqMIc8MGqfBd9SNnMBlDJziaMb7XbpPu7/mmXKdyYMHDzpNmzatLjw8XOXs7Kw5efKkDQBkZWXZfPDBB4X5+fkZXV+/ffv2YqVSmXXq1KlsJycnzZ///OfykydP2hw8eND10qVLiosXLyr279/vfvr0aWsAKCwstHr22WfLr169muno6Kjdv3+/MwCsWLGiJiMjQ5GdnZ0VHBzcsmPHDjfDf3rd4TrDzzSCGLhl4BlvDeGV/Jvu0+4vD7RXLjdJX3/9tcsjjzxSAwCLFy+u/vzzz10AIDw8vCkkJKTbmo8sy2Lp0qX+69evL4uNjW0+fvy43f3331/r4ODAOjo6svPmzav5/fff7QFg5MiRqokTJ7YAQGRkZHN+fr4QAC5dumQdFRUVLBaLpf/5z39cMzMze7wfagq4vic5fEeRXWgYZlScj9eVY4U37fS9xzuRHZ/Dgmcax2IYh4kAMvp8lZEpKyvjnz171j47O9v6mWeegVarZRiGIXFxcXU2NjZsT+974YUXvL28vNr+/Oc/91mkwtLS8lbhBz6fT1paWngA8Mc//tH/22+/vRoTE9OyY8cO16SkJJPesMD1KM7oztPmSi2fP0bfM96EQL1ZvUKizz7MUAzXAQzG559/7rxw4cLq4uLi9Js3b6aXlpam+fj4tCUlJdn19J6DBw86JiUlOXz66adFnT+bPn1645EjR5waGhp49fX1vCNHjjhPnz69obe+m5ubeX5+fmqVSsV8+eWXLrr8XFzgLEl2nKkdyVX/xihDKIzdrMc93teI14UyuIzQV/tmaiLXAQzGN99847Jo0aLbbuE88MADNd99912PSeu9997zKCsrsxgzZowkJCRE+txzz3lPnjy5efny5VVjx46VREVFSR577LGKSZMmtfTWd3x8fHF0dLRk3LhxIUFBQa26+kxc4axUmixBFgkghZPOjRkh2i0VVZfnNTXr/L7h420vpf3ORobrut1hwC1/y7wB1UikpdJMi7GWSqOX2t1hGH68Hma8W4hlLk2Qg2aSl9yUbnCZJKM57Nu46WHG+zPtnFJdtTUM0e2bwxhNkkaqY8a7QBd7vAlB/U7Ng/T+7+AFcx0AxR1OkmTHsbF0lrUPuprxPk9CLjfBusdZTapP9NybYYyrkaQPh32blAyhMHazq/OQzvF+Vb3aV1fxDFNBXAdAcYerREULmg7Av+3tJicOco93FbG/rCR+5l3QWP8caRHe4YsmSVPQMeOttLTIG+hbt2uWqPQR0jBkcpfcDMNEPfXUU7fKEG7atMljw4YN3rpqPzs72zIoKMhkt232F1fbEmmSHCiGcXzE27P2WOHNameW7dcuBi3hlRyk+7R1JQDAycG+WS6X67RUmlwu77NUmqWlJTly5IhzSUlJqZeXl6av1+tbZ2k2U0NHkiako6p5YX9nvBPZ8Tla8Lnen28uTK6SDZ/PJytXrqzYvHnzXX/fiouLBXPmzAkICwuThIWFSX799VdbABCLxdLKyko+y7JwcnIas3PnTlcAWLhwoej777936KkvjUaDNWvW+ISFhUnEYrH0n//8pxtwd2m2+vp63rRp0wKDg4OlQUFBoXv27HEGgJMnT9rcc889waGhoZLJkycHFRQUWGRmZgqlUumtCd709PTb/ttQaJI0MbV8/pjH+jHjTQjUb9F92rrkynUAg/HSSy+Vf/fddy5VVVW3nSW+Zs0a3w0bNpRlZGQovv/++7y1a9eKAGDcuHGNR48etbt06ZKVj4+P6tSpU3YAkJKSYjdz5szGnvrZvn27m6OjozYjI0ORmpqqSEhIcFcqlZbA7aXZvvvuOwdPT091dnZ2Vm5ubuaiRYvqVSoV8+yzz/r98MMPeZmZmYpVq1ZVvvjiiyNDQ0NV9vb22uTkZGsA2L17t9uKFSsGtPNJF+jltgnK7Jjx/mtVz1XNr7fv0zbJfcdGyiSTpIuLC7t06dKqLVu2jLC2tr5V/ef06dMOubm51p3/3djYyK+rq+PFxsY2JiUl2eXn51s++eST5fv27XO/fv26hYODg9bBwaHH6kFHjx51UCqVNj/++KMzADQ0NPCzsrKsLC0tSdfSbGPHjm155ZVXfNetWzfygQceqJs7d27jhQsXrHJzc61nzJghBtrLtbm7u6sBYPXq1ZV79uxxi46OLvrhhx+cL1y4oNDX/6ue0CRpov5tbzc5olV1sac93m9qVtB1kbplkkkSAP7yl7+UjR07Vvrwww/f2ktOCEFKSorCxsbmtuINs2fPbvj4449H3LhxQ7V169abP/74o/OBAwecJ0yY0GvlH0IIs23btsLFixfXd/354cOH7buWZgsPD1elpKRk/ec//3H8+9//PvLo0aP1Dz30UG1gYGDLlStX7jpGYtWqVTVbt271/vLLLxtkMlmzp6endvD/JwaHXm6bqvYZb3F3M96txCL3GDuW7tPWLZNNkh4eHtq4uLiagwcP3rqvOnny5Pq33377VkWozkvawMBAdU1NjeD69etWUqm0LSYmpnHXrl2eU6dO7fFSGwBmz55d9+GHH7qrVCoGANLS0oT19fV35Zf8/HwLe3t79umnn67esGFD6ZUrV2zCw8Nbq6urBUePHrUFAJVKxVy8eNEKAGxsbMjUqVPrNmzY4Ld69WpOCoZwlSRpuS5dYBiHR7w9BTU8XnXXHyfQfdr6YLJJEgBeeeWV0tra2ltXjh9//HFRSkqKrVgslgYEBITu3LnTvfO5MWPGNPn7+7cCwLRp0xrKy8stZs2adddIUq1WM5aWliwAPP/885UhISGtMplMEhQUFPrUU0+NUqvVdx19cenSJevOUmxvvfWW96ZNm0qsrKzIl19+mRcfH+8THBwsDQ0NlXate7ly5cpqhmGwaNGi+jvbMwSDl0qTJcjsAPQ6dKcGxlGrvfJ74c1QC8CCENSHqT7h0W2IOpeXv2VeYH9fPBxKpR04cMDp4MGDLkeOHNHrGU2bNm3yqKur47/33nvFfb96cHorlcbFPUmTPu/CGNW1z3if/LK4LPYCCb7cBGtOjqk1c/y+XzJ8PPfcc94//fST06effnpdn/3Mnj07oKCgQJiUlJSjz356w0WSpDtA9CBTKIx9y9U56VTxap++X00NAk2SXWzfvr14+/btehvZdfrtt98GvMtM17hIkiZfzt0YMISwIytRIC0kZaGFpHV0KbGqdoxqbFtcnWIjUuem8ce4NDAO/qB/uXWDgJP7YRT3DJ4k01elq2UJMi3oX95+c60npcE3yM3QAtIoLiZ8jxq4CtUQMYA/2h/Q8iybMsSTL9yf7WltXXnZe5UsoYrYagWnEZt9EtPUBfAfzTL8kRx/FNPF0PvowxVX6yRVAGw46ttoWbeS+qBiUhBWQGqCbxD4VMHBrgWjGMAT7Y8epYc+eVHD1PLrm27wY4UTWn+7aDPBxbUofZbkV7c5/J8CAaCI+F0/jplF5zHBqhquoWAYW4N8MPNg8PV5lHHgKkm2YhgnSYGWtI0qQ4G0kJRLC4laVE5snRrhzScYCUA20PYabb2vVbtIJ5KmH05fa6gOnOc0wSeQ9Tx+tRrTziQ/rA4IPJfk6Xk1ypcp9H8M+/wfwz5oIGhLJZGpv2NmrQJhI1phFQKGuWvJBnVLM9cBUNzgMkmaP0KIZw1uSIpISWgBaQkoIRbu9RhhocEopr2Qq06KuV6OeLYWDDOaaGstG9laHy3RXJ+qlk4t5tVcaIbqnqu5MVOLCmUlsvCj6dbWDTEAIIDGMgoXIqJwAQBQD4eqU2RKzilM0xbBL4Bl+F66iM2M6Oy8IUNhGCbqySefLNuzZ88NoH0pTWNjI/+dd97p94TL4cOH7YVCITt79uwmAFi8eLFo/vz5dY8//niv/z8KCwsFTz/9tF9qaqqNg4OD1s3NTf3+++8XhYeHD2niNjs723L+/PlBubm5mSdOnLD59NNPXT/77LOivt85eFxebpsVhyZSFXyDFIYVkHrxTcLzqoaLdRtGMYAv2h96UeQz/Yza0j4GAAhpdACAqtaSwhHWvv6LVNGBXwhP3SQMGalS2XldvPCgl5t7/qXg4NOuPB4rui1+1Lvej8Mx9+MwAOA68c87jlk3LiLathbOUjDMsB35dxhSkvzfsQCdlkqbOSNP76XS1Go1jh07Zm9nZ6ftTJL9wbIsFixYELh8+fKqw4cPXwOAM2fOWBcXF1v0J0myLAtCCPj83qctpkyZ0jxlyhS9j/C5SpL9/h9ubCzVpDmwGPmhhWx1SBG0vhXE3qEFvjwCdxh4V4aGL2zMDVgkuvUDovYAgOuNaTYjrH1hBUvnueoxN3+yuDwCDCwAoLJCFFVV6asSBycfd3fPH88wsO6ubX9cD/DHnoDHsQdqCFSXybjLxzGzTgGpdxuEQcPw0tzkRpJdS6W9//77N7s+l52dbblq1SpRdXW1wNXVVbN///78oKCgtsWLF4uEQiGbkZFh4+npqU5JSbHj8Xjk66+/dt2+fXshACQlJdnt2LHDo6KiwuKNN964ceeo8vDhw/YCgYC8/PLLFZ0/i4mJaQGAuro63ty5cwPr6ur4Go2G2bRpU/Gjjz5am52dbTlnzhxxZGRkY3p6uu2RI0dyt23bNuLYsWOODMOQl156qeSpp566q59t27Z5/P7771c3bNjgXVRUZFlQUCAsLi62XLt2bdnf/va3cgCYNWtWQElJiaVKpeKtXbu27MUXXxzQIn+ukmQpgDCO+u4XHku0Pp1LbAqIyr+MWLs0wJPPwpcBpFzHBwAZoU9eAsObCgCEqJsB4g4ARU3Z0mi3+1UMwwhHsi5hUq1PUpbgxq0F5oTwhdnK2GkF+RE3ZOG/FVtZNfd6cqUFNMJonI2MRnuFtho4VZwk03JPYwq5Cd8gwvCGwzZTk0uSQHupNJlMFiqXy2/bqrpu3Tq/FStWVP3pT3+q2r59u+u6det8jx49mgcAJSUllikpKUqBQIANGzZ429nZaV9//fUyANizZ49bWVmZxcWLF5VXrlyxWrhwYeCdSTItLc06IiKi2xGejY0Nm5iYeNXFxYUtKSkRjB8/PmT58uW1AFBYWCj85JNPrs+cOTP/s88+c0pPT7dWKBSZJSUlgujoaMm9997b6/7xq1evWiUnJ2fX1tbyJRJJ2EsvvVQhFArJF198ke/h4aFtbGxkIiMjpY8++mjNQAplcJUkb3DUb7fc6khJSBG5GVpIGoOKicWIWrh1LLEZjfaH0Wmw88mrdpbcKoVGtDUlaK+eDS1R26rY5hQrvu1YAJioCZ5axKs628BrmdC1jdZWB58L5xf7eHhcPR8YdNabxyP9WojujFr3Bfiv+wL8FwCQRwJzf8es4ku4x74ejlIwjDnuqjLJJNlTqbTLly/b/vTTT3kAsG7duurXXnvt1p/9okWLagSCnlPDggULavl8PqKiolqrqqoGVGqcZVnmueee8zl79qwdj8dDeXm55Y0bNwQA4OXl1TZz5swmADh58qT9Qw89VC0QCODr66sZP35846lTp2zGjRvX0lPb9957b621tTWxtrbWuLi4qG/cuCEICAhQb9261SMxMdEJAEpLSy0yMzOtPD09+301y1WSvNn3S3TPtoXUdSyxqQ2+QeBdBUe7VoxiAC+0P0zGlfBn6sEwt35BibaiGh1JEgCKm6/Wj7aPuPX6hW3R0gPCEwUsQ0bd2VZZWWB0RYWoJTjk1HFX16KJDAPLgcQSgKtBAbga9CQ+ggqWLZdI9KUkzGjMRoi3mhGay0mDnPzO6kJ3pdJ6Y2dn12PdSACwsrK6VfChu9oPMpms5b///a9zd+/dvXu3S1VVlSA9PV0hFArJyJEjZS0tLTygfZTZn/h6IhQKbwXD5/Oh0WiYw4cP2yclJdlfvHhRaW9vz0ZHRwd39tdfZjmSFGiIyr99iU2FtJCoR5UTO8cmjOQTeAEw+RJihT4zktWW9rcV1GW1Fbdd3uTVp3p3TZKWEDjMb4sq+dHyYiuYu/fPs6zAWpE1bZqNTW2+LPy3KkvL1kFNNAjRZj0Rp6Im4hQAoIq4lp7A9LxkxDIl8BYThmdyxyB0yOc6gMHqWirtkUceqQKAyMjIpr179zqvX7++evfu3S7jxo3r9lLW3t5eW19fP6CNH3FxcQ1///vfmX/9619unff/zp07Z11TU8Ovq6vju7m5qYVCITl06JB9cXFxt1/IU6ZMadizZ4/7M888U1VeXi44f/683Y4dO4oGmuBqa2v5jo6OWnt7e/by5ctWqampA14bbNpJkhDiXY1CSSEpDS0kraNLiKVbPUZYaDGKaT/dzuROuOuLhi9suBqw8K5bAER7+yChuq1ETAhbxjC8W7U7RxDH4DFa0ckrgvzYntpvbnYSnTu7VOTtrTw7OuDiKIYhQxphu6LKcyG+9VyIb0EAkkNClMcxs+wyohwb4CAFwwxo1MqhfK4DGIpXXnmlNCEh4VY5tI8++qhw5cqVovfee8+zc+Kmu/ctXry4dsmSJQE//fSTU+fETV94PB5+/PHHvKefftr3vffe8xQKhcTHx0f1/vvvF0VERFTfd999gWKxWBoeHt7cWZLtTo899lhtcnKynUQiCWUYhrz22ms3/Pz8NNnZ2QP6fVm8eHHdxx9/7D569OjQ0aNHt0ZERAx40tjgpdIAQJYgCwOQPpD3ODWSyuAbpDC0gDSIbxKeZw1cO5bYDKtdI5fDn0mqcZHcVeVHVbf3LGHrb7vnOMf78VNOwhGT73ztfyzPnq7hNU3qqy8+X90okSRdcnIumcQwuv9CbYWw6QImZCVhRksuxD4axtIo7/8C0ACwLp0+pt/LaIZDqTRzYmyl0gAgB+3bvO4axgvbSFNQMckPLSA1ITeg9akkDvbN8OW1n1ZnqpdqOtFg53u1xjmk2+RG2Oa77gHlN2bwxghn3PXaBW33RB4QnriqZdhe6yNqtRZ2GRmzptraVV2Vyf7XaGGhGjPY2LtjBZVtLJLuiUUSAKCCuBcnYca1M5jML4VXCBim2/taHLg+kARJmRdOkmT6qvS2MZ+GZftWQNhRxaZNVEZsnBtvLbEx+wPPB+NK+DONYJge/sw0d+3tvt6YERLhMp1lGOa2+zgW4NssaBvH+97yfBOYvkfiTY2ugWfPPAQf34zTItFlMcPAva/3DIY7KryX4CvvJfgKLBhWSaRZv2NWRSoinZtgJ+k6UWVg2Rz1SxkBzs5kPvgPbSYDLEWXGVmqZwW+M5PVlnbdnn5I2NY6AI53/ryNbXHRkLYsC0Z417pOV2I/OloTePq8xdU+L7s73SgKm1RSLK4LDf09ycGxfDLD6K+SEw+EJ0WmVIpMAEALrBvOkZjLSZjReg2BfhrGQqSvvruRYsC+KCPDWZJkgFS0J0mqDxq+sCFv9IM9fpkQtroE3SRJAChrKSj3sRV3u/g9XDtqUj6//EQ5r35Kf2PRai0d09LmTLV3KFeGhR3TCARqg2wKsEaL/TQci56GYwCAEuJVlIQZ+ecw0aIcHhIwTLefX0cu6rFtyshxdRAYQL+d+y097I8p6DJLfSdWW1Hb03N5DakuvbU9ry1qvIDwB3yWcUP9iJAzyctCCwtkJwlBdd/v0C0vlPg+jC9i38X6CZ/jIbt48lrGeHI6yYY0pYMQXZc1o0lyGONsJAmaJPul3s43t8YpuNdLYqIp77FoQFnLdSkhpI7pYaTFB0/4YNs9tt9anq0D0/1otGcMU1AwJvbmzZDqMNmxk3Z2VZMZBgbf080Dy5chLUyGNABAE2zqzpDJyhOY3paP0SItIxhKgZHi0uljSnQTKWWKOBtJSpSKMpjwLgZDuRLxp+aeJ2vasdqqHhMTARE0aep6HSk6EVu/yZqQuw6G7y+NxsrlyuX7Y9PTZ2VptYIBj0p1zRbNjrPw6/jX8ZfY/Vjm+w/ybOH95IcTbqT8HAgZaIVxkx1F2tjYRA61jRMnTtisXr26xy+Z/Px8i7lz5xrr0i2d4HIkCQBHAaziOAajVeA7O1ljYdvtZE1XhK3vtpJPp8ImhVrqFNNrGyHakeOv8cqSivk1gz5psa7WKzT59MOs/+hLJ0aOVEQwAx6Z6sdI3PRbgf1+K7AfWvA0aWRM2nHMqsmEzK0F1hLcMft/h7O6iMHz9ys6LZVWOn1Mn6XSdKGvcmQikUj9888/6/VIWa5xeU8SAI5w3L/R0vCt6vNGL+jfOc+kpdf7jtca0vz708xc9ZhJlkQwoEX+d2N416+Nm3Lu7JK2pkanU0NrS/f4YAWRSAl/Hv+YuhePhX6Ex+tWkr1n/cnVkzyi7e7K5n8GD1KPkpOTrSMiIkLEYrF09uzZARUVFXwAiI6ODj5x4oQNAJSUlAhGjhwpA9rLkU2fPj0QABITE+1CQkKkISEhUolEIq2pqeFlZ2dbBgUFhQLt5deioqKCpVKpRCqVSn777Tfbzjaio6OD586dO9rf3z90wYIF/izbvk37xRdf9AoLC5MEBQWFPvLII6M6f25MuE6Sv4KeHdKttLA1V9DvEmRa796ebdK0VyvvqxUeeIKFqmg3EFT1r9+eqdXW7ikpcZMzMqanarX83KG2py/2aHCeg58mvImNsZ/joZFvkw3X55DEEy6k8gIIKQZgkBGboaxevdp/8+bNN3JycrJCQ0NbNm7c2OvvTlfbtm3z3LFjR4FSqcw6e/as8s5CGN7e3pqTJ0/mZGVlKb766qtrzz//vF/ncwqFwnrXrl1FV69ezSwsLBT+9ttvdkB7KbeMjAxFbm5uZktLC+/LL780iquPrjhNkhKlohbAGS5jMEb19qNyap2C+rV+kbCN5UD3hXO7qmot7leJe3tYe01Xh14HgU6+0muqfSKSTz/sX1IclEQIeq0HaAz8UOC/Ep9OeR9r7jmApcml08eYzZd4VVUVv6GhgT9v3rxGAHjqqaeqzp49a9ff90+YMKHxxRdf9H3zzTdHVFZW8i0sbl/b39bWxixfvlwkFoulS5cuDcjLy7tVSEUmkzUFBASo+Xw+QkNDm/Py8iwB4KeffrIPDw8PEYvF0uTkZPuMjIw+f5cNjeuRJEAvue9yJXx9KximXwu1WW1VWX9ed60htd/HLwSwnuNErPuJ/r6+bzzB1asTpl44v6ihudkhWXft6hcD8gvXMRiKQCAgWm3790Fzc3O3E4GbN28u3bt3b0FLSwsvNjY25PLly7dVk3rrrbc8RowYoVYoFFnp6elZarX6Vn7proxZc3Mz88ILL4z67rvv8nJycrIeffTRytbWVmPISbcxhoBokuwi32/OaY2Fbb/LuRFteX1/XnejOUdKCOn32UIz1bIpVsRCp8u0VCpbr0sXH5ioyJqSwrK8Pi//jcBPXAegS66urloHBwftzz//bAcAn3zyiWtMTEwjAPj6+qrOnz9vCwBffPFFt3vmMzMzhdHR0S1vvfVWaXh4eFNGRsZtSbKuro7v5eWl5vP5+OCDD1w7k25PmpubeQDg6empqaur4x06dMhY9urfhvMkKVEqUgH0+/Q2c6bmW9dd858/oPJurLZC3Z/XaYnGRsU2Z/a3XQYMb5FqvC9D0K+R6kBUVo4am3z64ZFlZf7HCTHao1rPzZyRZ9JL1FpbW3keHh7hnQ+5XO6xb9++6xs3bvQRi8XStLQ06y1bthQDQHx8fNknn3ziLpFIpJWVld2uevnHP/4xIigoKFQsFkstLCzIkiVL6ro+/9xzz5X/+9//dg0ODpYqlUqrrpXQu+Pm5qZdsWJFhUQiCZ0+fbp4MGXMDIGTUml3UoRI9gL4A9dxcC1lzJ9P1DqJ+71FEABU9QdOEm15j/UhuxrnOicpwGHMgJb4FPIqU3+1SA2DnvZpW1k13JCF/3bTyqppvD7aH4LnZs7Ie2+wb6al0kxLb6XSOB9JdjjEdQBcq7cflVPr2L/Jmq4I29DvG+95Dan9nsns5Me6RQRpvU4O9H391dpq73Ph/KLx2cqJF1iW0ev5yQOgBfAV10FQxsFYkuQRtJ+gOCwRgAxksub2N6v6XWOzpq00iCXsgLfYTdFIptoS4fmBvm8gyssD7klOfti9ssLvOCGcn8t+fOaMvGH7+0jdziiSpESpUAP4hOs4uFLgNzd5IJM1nQhhtQA7oOMV6toq8gbaDwOGWaiKDmIIo9eziQgrsFIopk67dHFBqUplzeV2wIMc9k0ZGaNIkh0+BnSzNs+UtE/WzBvUWTyErSvBALeW5jdmDOrP3AqWzve3RdaDoG0w7x+IlhbHUefPLRl3NTf6LCGMoSf1WgF8p4N2WJZlDV7sgxq4jj+nHnOP0SRJiVJRiGG4HChNtjYVDG9Qlb6JtqpioO/Jb8yQEEIG9WXkRZyloVpfnexl7o+SkuAJyaeXOVZXjTxOCPo1i68DX82ckVerg3YyKioqHGmiNG4syzIVFRWOADJ6eg3XBS7u9BGA+VwHYSh1Dv7ZdY4BA56s6cRqywe8g6WNbXXWkLZMC0Y4qCMyYjTiKUW8yjP1vJbeK2boCMta2GZmzphma1udJws/2qDrc3a68YEuGtFoNE+WlpbuLS0tDYMRDUaou7AAMjQazZM9vcAolgB1UoRIeACuARjFdSz6RgByctI/MzQWNrLBttHW+ONxVn112kDfN3HEg8d9bYMH/L5b/ULTcEB4opJlSL8KZ+jSSJ/M0/7+KUEMg37uax+QCzNn5EXroV3KhBnVN5xEqWDRfm/S7OWPuu/0UBIkABBt9aAOxspruOI6lH4tIbCf3xalBkHLUNoZjJs3QiedSV5mVVvrkUSIzoujvKvj9igzYFRJssMngMHuP3FCLbCuuy66P2So7RDS5DCY95W3FEgJIXV9v7JnI4ijOFLrz8kMtFZr6ZCedu/U1Ctzr2o0FkMs7XZLEYBvdNQWZUaMLkl2VCw/wHUc+pQmW5cKhjf0M8RJ26AuOQkIv0lTO+QK4lGa0bEurB1nNSMbGtyDzyQvCyvIDz9Fhl7e7Z2ZM/Lo2drUXYwuSXZ4Fe1LMcxOrcNoRZ3D6MlDbYcQTStABn1frrBJoZPR+oK2cVF8wuOwXiTDFBZGTD57Zimvvt7tJBlcibebAD7UdWSUeTDKJClRKooA7OI6Dl0jAEkNf1rbx3EB/WtLW1MMDP7QrbyGNJ2cdy4A3/qBtnsEIBjo2TE6pdFYOadeuS82PW22UqMRZA3w7W/NnJHH9S4fykgZZZLssBlALddB6NJ10f2ntQJrnZxTTbSVQzrGtVlT561lNQPefdMdF2LnP0ETpKt7g0NSV+cpPZP8cMiNIulJQvr1+5MPYK9+o6JMmdEmSYlSUQ1gK9dx6IpaYFObP+q+IU/WdGK15UMuMVapuqmzbYZhWr+JHqyjDgv1DgXDu349Kvbc2SWaxkbnU4Sgt3Vur8+ckWfWE4XU0BhtkuzwHszk2NlU2bo0nUzWdCDayiEvcL3WkGari1g63d82doIF4Q/0Uldv1Gprt8sp8ydnZsxI12r5Od28JBvAfkPHRZkWo06SEqWiBYCc6ziGqtZhtKLewX/IkzVdEbZWONQ2bjbnhBJCdDZBxgfP8sG2aAf07zLXYGpqRoYnn354dHGxOIncfu/0zzNn5JnNGTaUfhh1kuywDwDnB94PVsdkDauLyZrb2mWbnYbahpZorFu1Tf2uVt4fjsTGJ1YjyUHvl7gc4Anyro6fev7c4uaOc3Z+mDkjb9icYUMNntEnSYlSoQXwItdxDNZ10fzTWoH1oPZJ907toYtWbjbn6vwEw2Ctd7QP62Ik9ydv19Zm43Hp4gNjLl2Me5brWCjTYPRJEgAkSsURmOACc7XAtiZ/1ByJrtslRFUPQCeHJl1rSB2pi3budK86YpKQCFL10bYOyF9+eXsh10FQpsEkkmSHP8PEqpenhq/LAMMb0j7p7hBt9YCri/ekpq0scDDVyvvCA0+wUDXeAwQDLuemZ6mge7SpATCZJNmxJOhpruPorxrHwKx6e9Ggy6D1htVW1Oqyvdq2cp2sl7yTHaw8Z6jDijC4XTD6oAHwR7lcTrcfUv1mMkkSACRKxfcwgdL6BAybJlsHXU/W3GpfW6HTLZv5jel6OQkRAEazHmP92RHGcn9yk1wu1+tZPZT5Makk2eFptO+SMFrX/ONOawVWUn21z2p1e1JpQWOWhBCit6UwM9RhU6yJ5SV9td9PvwLYwnEMlAkyuSQpUSrqADwG6LyWoE60WdhWF/jdq4fZ7P9HtHXWumyvjW11UhOV3pZZMWB4i1TjRzEEOr/32U8lAB6Ty+VGtiyJMgUmlyQBQKJUnEL73m6jkyp7OhMM46LXTkiLztsva8nX7fD0DtawdLtXPaYCBIa+H8gCWCGXy8sN3C9lJkwySXZ4DYBRLQaucQzKarAfpZfJmttpB3SMbH/k1afqbMtkT3xZ1/BgrfdpffdzhzflcvnvBu6TMiMmmyQ7Fpk/hF5OOTOk9smatXqbrLnVD9tUAUCne64BoLy1QEIIqdV1u3eK1Uim2hIrQ02eHEf7lylFDZrJJkkAkCgV9QDmwQjWT+p7sqYTq63Sy2UjAeE3amoMsv1zkSo6mCFMkZ67KQDwiFwuN5blR5SJMukkCdw6rzsOwJBLhw1Wx2SNTupE9oVoK4Z0Nk1vChsVBrlfKISF47y2sY0g0Feh21oA98vlcs6/PCnTZ/JJEgAkSsVFAI8C3CxaTpWtzwTD6GSbYF9YbUWbvtq+1pgWqK+27+RJnCQyrd85PTTdBmCRXC43mpJtlGkziyQJ3FpovtHQ/VY7iTMb7P10WgatN0RbpbeF382aei9dVSvvj/GaoCmOrE2yDpskAB6nEzWULplNkgQAiVLxLwC7DdUfAcOmh63hgWEGfdbMgPtkG3Q+adNVheqGzqqV98eDbfeE8whzTUfN/Ukulxv9jizKtJhVkuzwDAy0dTFv9AOntQIrnVf56RVp1XnBjK6uNaTa6bP9O1lAYBfXNk4LMuR7yq/K5XKzOzyO4p7ZJUmJUqFB+44cvY4o2yzsqgp9Z8n02cedCCEswHrrs4+bzbmhhJAWffZxJ3fiEBSlGZ0yhCbeksvlr+ssIIrqwuySJABIlApWolSsBfAPffVxJXy9AgzjpK/2u0PY+hIAFvrsgyVaK11XK++PSK3/ZFfW/uQA30YAbJDL5X/TR0wUBZhpkuwkUSo2AnhF1+1WOwVnNNr5GmBnze2IttIgtRlvNuc0GaKfO8W1Rd0jILzsfr5cA2CVXC6ntSEpvTLrJAkAEqViM4A/Abo5c6V9Z80agSEna271rS3X+VEL3clrSPUxRD93EoBv9UDbPUIQ1Pfx0hYAC+Vy+eeGiIsa3sw+SQKARKnYCeBx6KBy0NWAhadYvlBn52cPBKutNMhi79q28gCWsMWG6OtOzsROFKMR93a5XwdgjlwuP2yomKjhbVgkSQCQKBUJAJYAGPRorM3CvrLIZ0aE7qIaGKKt1uv9yK5q28oMtl7yTqFa3xhP1qm7Qr2lAKbK5fKB3rukqEEbNkkSACRKxX8BjMMgi2JcCV+vBMM46jSoASCk0d5QfV1vyBAYqq/u3NcWOcGC8LuOKJMBRMnlcmM9XIwyU8MqSQKARKnIBhAN4LOBvK/aOSS90c7H4JM1tyFt7obqqqApU6rPauV94YNnubBtvBMIagDsBDBNLpdzcguAGt44HS1wRaJUtAB4XBEiOQFgF4BeK30TMNq0sD9acDFZcysGolEBxNNQ/alZlaOaVWVY8q0MUrijOw7E2vFedcTjEzcv/JarGChq2I0ku5IoFfsAjAfQ67KTqwGLTnM1WdOJsLXFAAyapEtbruu1WnkfLgMYSxMkxbVhnSQBQKJUpKP9PuW/u3teZWFfUeQznbPJmk5EW1ll6D7zGq4Y7PK+CwLgPQATfLbE5nLQP0XdZlhebt9JolQ0AliuCJEcAfAOgFvJITXimRwwDLf3IgGwmnKD18ssby2UEEJqGAOVgQOQDmCNz5bYMwbqj6L6NOxHkl1JlIoDACQA9gFAlbMkrdF25ERuo2pHtJVc1MrkNWpqlAbopxnAywDG0gRJGRuaJO8gUSqqJErFEwCmZUlWFXM5WdMVYWuFXPRb0Jil7xnuwwCkPlti/+mzJdbQJylSVJ9okuyBRKlIUlvaxwH4M4AaruMhbBMn6zOvN6QF6KnpmwAW+2yJjfPZElugpz4oashokuzF+o9maNZ/NGMHgCAAHwIGPzO6C7UHF702axu8NKxalxMotQD+DiDEZ0vsdzpsl6L0giFEJ3UfhoVda4+NAvAigD+gj7WVukRIW6OqdqdBi+F2NdXzoSRPa/+pQ2ymEe2z1v/y2RJbO/SoKMowaJIchF1rj7kDeBbAegB6n/llNaW5bQ0Hg/TdT098bUMuTRzxQNQg314D4H0AO3y2xBp8GRNFDRVNkkOwa+0xOwBrADwPYKS++tGo0s9rmn+L1lf7feGBr1oiekHLMIzNAN52E+0jx498tsQ26Ck0itI7miR1YNfaY5ZoP9L2WQA6X3iubj6WpFVdGerl7pDE+T590UZgP66Pl7UB+BHApwB+8dkSy8kRvxSlSzRJ6tiutcciAKwEsByATvZatzV8ncRqbnCaJMe6zkoKcojqKYY0tCfGA/SSmjI3NEnqya61x/gAZgJYCuBBAG6Dbau1bs95sA2cXW4DgKOF+7W5Pk+M7vKjEgDfAdjnsyX2EkdhUZTe0SRpAB0JcxqARQCmo31XT7+11uzIBTScTdx0YBeP2vCbgGdxBu0LwFN8tsTSXx7K7NEkyYFda4+5AZgEYDKAWABj0cspiK017zQC4GIJkBLAMQD/A3D8ha8OV3MQA0VxiiZJI7Br7TFrtJdsmwxgAoBgACIAAsI2V6nqPnLVcwhVaK/Wnt7xzwwAGS98dbhOz/1SlNGjSdJI7Vp7zAKAP6sp9W9rOBgIwBeAT8c/3QEIu3lY3tGMGkB9x6MaQBmA8o5/FgNQAEh/4avDpXr/QBRlomiSNCPbls1n8P8JU/XCV4dbOQ6JokweTZIURVG9oAUuKIqiekGTJEVRVC9okqQoiuoFTZIURVG9oEmSoiiqFzRJUhRF9YImSYqiqF7QJElRFNULmiQpiqJ6QZMkRVFUL2iSpCiK6gVNkhRFUb2gSZKiKKoXNElSFEX1giZJiqKoXtAkSVEU1QuaJCmKonpBkyRFUVQvaJKkKIrqBU2SFEVRvaBJkqIoqhc0SVIURfWCJkmKoqhe0CRJURTVC5okKYqiekGTJEVRVC9okqQoiurF/wEMiBR3Fo+mEgAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "top_states = cases_by_state_sorted.head(n = 10);\n",
    "top_states = top_states.reset_index();\n",
    "labels_pie = top_states.state;\n",
    "\n",
    "plt.pie(top_states.cases);\n",
    "plt.legend(labels = labels_pie,loc = (0.95, 0.35));\n",
    "plt.show();\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<U>Expected Output</U>:<BR>\n",
    "<IMG SRC=\"images/hw11.png\" align=\"left\">"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 12: cases over time for a selected state\n",
    "Take <B>input()</B> for a state name (or hard code a state name if you prefer), then build a line chart showing the increase in number of cases over time for that state.  \n",
    "\n",
    "The data shows new cases for each day, so a line chart of just new cases will not show the increase.  In order to calculate the increase, after grouping cases by date in one state, use <B>.cumsum()</B> to calculate the cumulative sum.  Here is an example of <B>.cumsum()</B>:\n",
    "<PRE>\n",
    "df = pd.DataFrame({'a': [1, 2, 3], 'b': [9, 30, 200]})\n",
    "df['c'] = df.b.cumsum()\n",
    "print(df)\n",
    "   a    b    c        # 'c' column adds up 'b' column values\n",
    "0  1    9    9        #   9 =  0 +   9\n",
    "1  2   30   39        #  39 =  9 +  30\n",
    "2  3  200  239        # 239 = 39 + 200\n",
    "</PRE>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a state name to graph a line chart of the cases: New York\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:title={'center':'New York'}, xlabel='date'>"
      ]
     },
     "execution_count": 12,
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
    "s_input = input('Enter a state name to graph a line chart of the cases: ');\n",
    "cases['cum_sum'] = cases.groupby(['state'])['cases'].cumsum()\n",
    "\n",
    "\n",
    "cases[cases['state']==s_input].cum_sum.plot(kind='line', title=s_input)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<U>Expected Output</U>:<BR>\n",
    "<PRE>please enter a state name: New York</PRE>\n",
    "<IMG SRC=\"images/hw12.png\" align=\"left\">"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 13: (extra credit) cases over time:  selected states comparison\n",
    "Repeat the above exercise, but this time allow the user to input any number of states; build a line chart comparing the rates of new cases.  You can plot multiple lines from a DataFrame by calling <B>.plot()</B> on a DataFrame that has the columns you want to plot.  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "vscode": {
     "languageId": "javascript"
    }
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<U>Expected Output</U>:<BR>\n",
    "<PRE>please enter states separated by commas: New York, Florida</PRE>\n",
    "<IMG SRC=\"images/hw13.png\" align=\"left\">    "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 14: (extra credit) scatter plot showing cases by state population\n",
    "This chart shows the correlation of two factors:  the <B>y</B> (vertical) axis will show state population, and the <B>x</B> axis will show number of cases.  The placement of the dot within the 2D area correlates the two numers, which can visually indicate cases per capita  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "scrolled": true,
    "vscode": {
     "languageId": "javascript"
    }
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<U>Expected Output</U>:<BR>\n",
    "<IMG SRC=\"images/hw14.png\" align=\"left\">"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 15: (extra credit) bar chart showing daily increase in cases for a state\n",
    "Use <B>input()</B> for a state name.  You can use the <B>.shift()</B> method to compare count of a day's cases to the prior days, calculating the increase.  See discussion for more details.  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "vscode": {
     "languageId": "javascript"
    }
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<U>Expected Output</U>:<BR>\n",
    "<PRE>please enter a state name: New York</PRE>\n",
    "<IMG SRC=\"images/hw16.png\" align=\"left\">"
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
   "version": "3.10.4"
  },
  "vscode": {
   "interpreter": {
    "hash": "9a03ea288498a3924b1c5dece16cdd88a4ab45a06f5032936c269b006d60be0d"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
