# 百度Paddle AI智能问答比赛 --- 评审环节

欢迎参加[科赛网](https://www.kesci.com)和百度联合举办的Paddle AI智能问答比赛。请按照如下步骤完成模型validation的内容。
* 首先，在K-Lab内打开创建的**比赛项目**
* 在Code Cell内执行下面的指令：
    ```
    %%bash
    cd /home/kesci/work
    git clone https://github.com/Kesci/Baidu_EvaluationScript.git
    ```
* 完成仓库的clone之后，请在Code Cell内执行下面的命令，完成validation。
    ```
    %%bash
    python /path/to/Baidu_EvaluationScript/1st_evaluation.py /path/to/your/model /path/to/validation/file
    ```
* 你将会看到如下结果，其中的value便是对应算法评测的分数
    ```python
    [{'name': 'Bleu-4', 'value': xxxx, 'type': 'zhidao'}, {'name': 'Rouge-L', 'value': xxxx, 'type': 'zhidao'}]
    ```