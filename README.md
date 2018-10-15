# Creating-Sememe-and-Word-Embeddings-as-for-CiLin

### Abstract

In natural language processing (NLP), to learn embedded representation is an effective approach to capturing semantics from language resources. However, by now, this has been much limited to using large-scale corpora, with little attention to extracting rational knowledge from knowledge bases. In this paper, based on TongYiCi CiLin, a famous Chinese thesaurus, we present a method for implanting rational knowledge into embedded representation, then evaluate it on different NLP tasks. According to the hierarchical encodings for morphemic and lexical meanings in TongYiCi CiLin, we design multiple templates to create instances as pseudo-sentences from these pieces of knowledge, and apply word2vec to obtain CiLin2Vec, the sememe and word embeddings of new kinds as for TongYiCi CiLin. For evaluation, tasks of semantic compositionality, analogical reasoning and word similarity measurement are taken into consideration. We make progress and breakthrough on the tasks, reaching an accuracy of over 0.9 for both semantic compositionality and analogical reasoning, which proves that the pieces of rational knowledge have been appropriately implanted and shows very promising prospects for adoption of the knowledge bases.


### Models and Codes

This repository provides the codes and the best models for the tasks mentioned in [Creating-Sememe-and-Word-Embeddings-as-for-CiLin](https://github.com/ariaduan/Creating-Sememe-and-Word-Embeddings-as-for-CiLin/blob/master/Creating%20Sememe%20and%20Word%20Embeddings%20as%20for%20CiLin.pdf). To use this repository, just clone it to your own computer. There are five directories in this repository. You can train your own models using the codes in *"train"* directory. To get different models, you can either adjust the parameters for training models or create your own pseudo-corpora using the [Cilin knowledge base](http://www.ltp-cloud.com/download). A prototype of pseudo-corporus is provided in *"files"* directory, named *"cilin_hier_perword"*. The models trained by yourself will show in "results" directory. We also provide some best models for evaluation tasks in the *"models"* directory that you can directly use, but some other files are too large to upload and need to be downloaded from [google drive](https://drive.google.com/drive/folders/13K9M364vcQN30wgLnvlHUWHAOFdkdRFS?usp=sharing) and save into the same directory.

We provide codes for three NLP tasks in "tasks" directory. They are: semantic compositionality, analogical reasoning and word similarity measurement. To evaluate the pretrained models with these tasks, just open your terminal and run the codes. There are a few things to specify here: 1) some tasks' .py files have a "sem-" or "resem-" prefix as for the names. This means they are used to perform the task with sememe-composed word vectors. "Sem-" types will calculate the weight of each sememe according to formula (1) while "resem-" will use formula (2). The specification of these formulas is in the paper. The performance score will directly show on your terminal while the specific statistics will show in the "results" directory.
      
      αi+1 = αi * 0.5     (1)
      αi+1 = αi * 2       (2)
      
For *composition* task, run the following commends under *"tasks"* directory. Add all the models you want to evaluate by appending "--models [model name]"at the end of the commend. The evaluation score will be shown in order on the command window and the details will be documented in *"sem/resem_comp_(model)"* in *"results"* directory.
```
      python3 sem_comp.py --path [path to the master directory] --models cb_cilin_def_palin_3 --models sg_cilin_def_palin_2010_5
      python3 resem_comp.py --path [path to the master directory] --models cb_cilin_def_palin_3 --models sg_cilin_def_palin_2010_5
```
For *analogy* task, run the following commends under *"tasks"* directory. Add all the models you want to evaluate by appending "--models [model name]"at the end of the commend. The evaluation score will be shown in order on the command window and the details will be documented in *"(sem/resem_)anal_(model)"* in *"results"* directory.
```
      python3 anal.py --path [path to the master directory] --models cb_cilin_def_palin_3 --models sg_cilin_def_palin_2010_5
      python3 sem_anal.py --path [path to the master directory] --models cb_cilin_def_palin_3 --models sg_cilin_def_palin_2010_5
      python3 resem_anal.py --path [path to the master directory] --models cb_cilin_def_palin_3 --models sg_cilin_def_palin_2010_5
```
For *similarity* task, run the following commends under *"tasks"* directory. Add all the models you want to evaluate by appending "--models [model name]"at the end of the commend. The evaluation score will be shown in order on the command window and the details will be documented in *"(sem/resem_)simi_MC/WS_(model)"* in *"results"* directory.
```
      python3 simi_MC.py --path [path to the master directory] --models cb_cilin_def_palin_3 --models sg_cilin_def_palin_2010_5
      python3 sem_simi_MC.py --path [path to the master directory] --models cb_cilin_def_palin_3 --models sg_cilin_def_palin_2010_5
      python3 resem_simi_MC.py --path [path to the master directory] --models cb_cilin_def_palin_3 --models sg_cilin_def_palin_2010_5
      python3 simi_WS.py --path [path to the master directory] --models cb_cilin_def_palin_3 --models sg_cilin_def_palin_2010_5
      python3 sem_simi_WS.py --path [path to the master directory] --models cb_cilin_def_palin_3 --models sg_cilin_def_palin_2010_5
      python3 resem_simi_WS.py --path [path to the master directory] --models cb_cilin_def_palin_3 --models sg_cilin_def_palin_2010_5
```
