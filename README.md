# Replication package of "Does Refactoring Break Tests and to What Extent?"

This repository includes the replication package and results of an IST paper.
If you are using this tool in your research, please cite the following papers:


```
@article{Kashiwa:IST:2022:SATD_Review,
author    = {Yutaro Kashiwa and
               Ryoma Nishikawa and
               Yasutaka Kamei and
               Masanari Kondo and
               Emad Shihab and
               Ryosuke Sato and
               Naoyasu Ubayashi},
title     = {An empirical study on self-admitted technical debt in modern code
               review},
journal   = {Information and Software Technology},
volume    = {146},
pages     = {106855},
year      = {2022},
url       = {https://doi.org/10.1016/j.infsof.2022.106855},
doi       = {10.1016/j.infsof.2022.106855}
}
```


## Source code
Our source code is located in "src" directory. 

## Require
- Docker (> 20.10.13)

## RUN (for Mac or Linux)
This program is designed to run on docker.
```
bash build.sh
```
This script performs docker-compose commands and run python programs on docker.
All the results will be generated in the "outputs" directory after running this script.
Specifically, the program runs on docker, and the output directory in docker is linked to your local machine (i.e., outputs directory in the "ReviewSATD_RP").
