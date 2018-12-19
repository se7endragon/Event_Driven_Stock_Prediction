# Event Driven Stock Prediction

Deep Learning implementation of Stock Prediction inspired by [Deep Learning for Event-Driven Stock Prediction] (Ding et al.,2015)


#### Data Preparation
#####  News Data
###### News dataset from Bloomberg & Reuters (Oct.20.2006 ~ Nov.26.2013)
  - Extract news titles only (generators/data_generator.py)
  - Extract Relation Triples using OpenIE 5.0 (generators/svo_generator.py)
  - Match Relation Triples with corresponding word embeddings (generators/svo_embedding_generator.py)
  - For detailed description of preprocessing steps, refer to the corresponding .py files

##### S&P 500 Data
- Working on it

[Deep Learning for Event-Driven Stock Prediction]: <https://www.aaai.org/ocs/index.php/IJCAI/IJCAI15/paper/view/11031/10986>
