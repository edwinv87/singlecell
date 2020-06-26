# Single Cell

SingleCell is a python class for managing single-cell RNA-seq data. It contains three pandas dataframes; `data` for holding gene expression values (counts/normalized counts), `genedata` for holding more information about the genes e.g., gene names, and `celldata` which contains more information about cells such as cell types, labels etc. It is similar in concept to R package SingleCellExperiment on Bioconductor (<https://bioconductor.org/packages/release/bioc/html/SingleCellExperiment.html).>

## Installation

The singlecell package can be easily installed from Anaconda Cloud using the Anaconda package distribution software. From the anaconda prompt run the following command to install singlecell package in your environment:

`conda install -c edwinvans singlecell`

The user can also checkout the anaconda cloud page for more information <https://anaconda.org/edwinvans/singlecell.> The source code is available here on the GitHub repository.

## Usage

The SingleCell class can be used to create an object which stores single-cell gene expression data and additional data about genes and cells in their respective dataframes. To create a SingleCell object sc, the following python code can be used:

```python
import pandas as pd
from singlecell import SingleCell

dataset = 'biase'

data_path = "data/" + dataset + '/' + dataset + "_data.csv"
celldata_path = "data/" + dataset + '/' + dataset + "_celldata.csv"
genedata_path = "data/" + dataset + '/' + dataset + "_genedata.csv"

# Create pandas dataframes by reading data from files
data = pd.read_csv(data_path, index_col=0)
celldata = pd.read_csv(celldata_path, index_col=0)
genedata = pd.read_csv(genedata_path, index_col = 0)

# Create a single cell object
sc = SingleCell(dataset, data, celldata, genedata)
```

In the above example, a SingleCell object, sc, was ceated by passing the dataset name and the main data, the cell data and gene data as pandas dataframes. Pandas is a powerpul python library for creating data structures from a variety of sources. Pandas can open and read data from numerous differernt file types such as csv files and creating dataframes from it. This enables the user to create SingleCell objects from different data file types. For more information on pandas see <https://pandas.pydata.org/>

## Contact

Contact the author on vans.edw@gmail.com to give feedback/suggestions for further improvements and to report issues.
