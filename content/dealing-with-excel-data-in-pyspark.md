Title:  Dealing With Excel Data in PySpark
Date: 2017-10-05 13:30
Author: bstempi
Category: General Work Stuff
Tags: Python, Spark, tools
Slug: dealing-with-excel-data-in-pyspark

Have you ever asked yourself, "how do I read in 10,000 Excel files and process them using Spark?"  I hope not...it sounds like a terrible task...but in case you have, it just so happens I might have an approach your interested in.

General Approach
----------------

PySpark does not support Excel directly, but it does support reading in binary data.  So, here's the thought pattern:

1.  Read a bunch of Excel files in as an RDD, one record per file
2.  Using some sort of `map` function, feed each binary blob to Pandas to read, creating an RDD of (file name, tab name, Pandas DF) tuples
3.  (optional) if the Pandas data frames are all the same shape, then we can convert them all into Spark data frames

Reading in Excel Files as Binary Blobs
--------------------------------------

This one is pretty easy:  [SparkContext.binaryFiles()](http://spark.apache.org/docs/2.1.1/api/python/pyspark.html#pyspark.SparkContext.binaryFiles) is your friend here.  If you give it a directory, it'll read each file in the directory as a binary blob and place it into an RDD.  If you have 10 files, you'll get back an RDD with 10 entries, each one containing the file name and it's contents.

Making Sense of the Binary Content
---------------------------------

The is the part where we need to take that binary data and turn it into something sensible.  My thought was that Pandas has built-in support for Excel files, so perhaps that'd be a good tool to do a transformation.  Because we're using Spark, we can use a `map` function to work on several of these files in parallel.  Here's a simple example:

```python
import functools
import io


def pd_dfs_from_excel_rdd(rdd_record, pandas_opts):
    file_path = rdd_record[0]
    file_contents = rdd_record[1]

    file_like_obj = io.BytesIO(file_contents)
    df_dict = pd.read_excel(file_like_obj, **pandas_opts)

    dfs = list()

    for sheet_name, sheet_df in df_dict.items():
        entry = (file_path, sheet_name, sheet_df)
        dfs.append(entry)

    return dfs
    
    
spark_context = None # Start your context here
excel_files_rdd = spark_context.binaryFiles(some_path)

pandas_opts = {
        'sheetname': None,
        'header': 1,
    }
    
parsing_func = functools.partial(pd_dfs_from_excel_rdd, pandas_opts=pandas_opts)

parsed_excel_sheets = excel_files_rdd.flatMap(parsing_func)
```

Presto!  If we give Pandas Excel files, we get back an RDD that contains (file path, sheet name, sheet df) tuples.  The other magic that happens here is with the `partial`.  Our map function takes an RDD record and some Pandas options, but Spark will only pass in the former.  So, we create some Pandas options, create a partial that only takes RDD entries, and we're off.  You can change the `pandas_opts` to your liking and things will still work.

Going From Pandas DFs to Spark DFs
----------------------------------

Most people probably aren't going to want to stop with a collection of Pandas DFs.  Far more interesting and performant things can be done with Spark DFs.  PySpark contains the [SQLContext.createDataFrame](http://spark.apache.org/docs/2.1.1/api/python/pyspark.sql.html#pyspark.sql.SQLContext.createDataFrame), which has the folling snippet:

> When schema is None, it will try to infer the schema (column names and types) from data, which should be an RDD of Row, or namedtuple, or dict.

Ok, that's simple enough.  We can take our Pandas DFs, convert them to Spark `Row` objects, and as long as they're homogenous, Spark will recognize it as a data frame.  Here's how I accomplished that in a project:

```python
def flatten_pd_df(pd_df):
    """
    Given a Pandas DF that has appropriately named columns, this function will iterate the rows and generate Spark Row
    objects.  It's recommended that this method be invoked via Spark's `flatMap`.
    :param pd_df: 
    :return: 
    """
    rows = list()
    for index, series in pd_df.iterrows():
        # Takes a row of a df, exports it as a dict, and then passes an unpacked-dict into the Row constructor
        row_dict = {str(k): v for k, v in series.to_dict().items()}
        rows.append(Row(**row_dict))
    return rows
    
rdd_of_rows = rdd_of_pandas_dfs.flatMap(flatten_pd_df)
spark_df = some_sql_context.createDataFrame(rdd_of_rows)
```

This function will get each Pandas data frame, iterate through it's rows as a dictionary, and use this dictionary to instantiate a Spark `Row` object.  At the end of this, we have an RDD of `Row`s.  Happy days!

Closing
-------

Not that I hope that anyone has to deal with tons and tons of Excel data, but if you do, hopefully this is of use.  If it was, drop me a line!  I'd love to hear from you