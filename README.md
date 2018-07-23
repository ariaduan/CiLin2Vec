# Creating-Sememe-and-Word-Embeddings-as-for-CiLin
Models and Codes

This repository provides the codes and the best models for the tasks mentioned in Creating-Sememe-and-Word-Embeddings-as-for-CiLin. To use this repository, just clone it to your own computer. There are six files in this repository. You can train your own models using the codes in "Train" file. To get different models, you can either adjust the parameters for training models or create your own pseudo-corpora using the Cilin knowledge base in "data" file. A prototype of pseudo-corporus is provided in "files" file, named "cilin_hier_perword". The models trained by yourself will show in "results" files. We also provide some best models for evaluation tasks in the "models" file that you can directly use.

We provide codes for three NLP tasks in "tasks" file. They are: semantic compositionality, analogical reasoning and word similarity measurement. To evaluate the pretrained models with these tasks, just open your terminal or python IDE and run the codes. There are a few things to specify here: 1) some tasks' .py files have a "sem-" or "resem-" prefix as for the names. This means they are used to perform the task with sememe-composed word vectors. "Sem-" types will calculate the weight of each sememe according to formula (1) while "resem-" will use formula (2). The specification of these formulas is in the paper. The performance score will directly show on your terminal or IDE while the specific statistics will show in the "results" file.
      
      αi+1 = αi * 0.5     (1)
      αi+1 = αi * 2       (2)
