# 百度Paddle AI智能问答比赛 --- 评审环节

欢迎参加[科赛网](https://www.kesci.com)和百度联合举办的[Paddle AI智能问答比赛](https://www.kesci.com/apps/home/competition/5ad56e667238515d80b53704)。我们提供此次比赛的评审脚本，供选手在K-Lab内对个人的模型进行验证(validation)和测试(testing)。

## 代码介绍

### 测评函数

**初赛**将会使用目录下的[1st_evaluation.py](./1st_evaluation.py)完成测评,返回 `Bleu-4` 和 `Rouge-L` 这两个算法分别对模型的跑分。

### Bleu-4

算法详细内容请移步至 [bleu_scorer.py](./bleu_metric/bleu_scorer.py) 和 [bleu.py](./bleu_metric/bleu.py)
### Rouge-L

算法详细内容请移步至 [rouge.py](./rouge_metric/rouge.py)

## 代码使用

请按照如下步骤完成模型验证和测试。
* 在K-Lab内打开创建的**比赛项目**
* 在Code Cell内执行下面的指令：
    ```
    %%bash
    cd /home/kesci/work
    git clone https://github.com/Kesci/Baidu_EvaluationScript.git
    ```
* 完成仓库的clone之后，请在Code Cell内执行下面的命令，完成validation。
    ```
    %%bash
    cd /home/Kesci/work/Baidu_EvaluationScript/
    python3 1st_evaluation.py /path/to/submit/file /path/to/validation/file
    ```
* 你将会看到如下结果，其中的value便是对应算法评测的分数
    ```python
    [{'name': 'Bleu-4', 'value': xxxx, 'type': 'zhidao'},
     {'name': 'Rouge-L', 'value': xxxx, 'type': 'zhidao'}]

    ```