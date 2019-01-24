## GameBot NLU

以游戏库对话查询 bot 为中心，开发了主机游戏相关的如下四个工程：

- VGTimeSpider
- VGTimeBackend
- RasaNLUForGamer
- GamebotPreVue

前者是爬虫，中间是所爬游戏库的查询后端。其中，爬虫不仅仅爬取 VGTime 游戏时光 网站上的游戏库，还抓取了近两年的游戏新闻，新闻语料用来训练 NLU 服务，也就是第三个工程。

NLU 服务可以用来理解用户提问，游戏库查询后端包括提问中游戏的详细信息，爬虫随时可以补充语料、游戏库。

这个工程基于 Rasa NLU 的代码，进行了少量修改，后端采用 scikit-learn（意图分类）和 MITIE（实体识别），内置了游戏向的标注文本。

这个工程只包含 NLU 服务，不含可视化的部分。

![使用该NLU的Demo](https://ws3.sinaimg.cn/large/006tNc79gy1fz9m009ll8j30ef0bizm5.jpg)

### 食用方法

请注意，运行该项目需要导入预先使用 游戏新闻语料 训练好的 MITIE 的 word embedding 模型。

要把 total_word_feature_extractor_game.dat 放到 `data` 目录下，然后再执行镜像构建的命令。

这个模型，可以通过 `tools` 目录下的 wordrep 程序进行训练得到，该目录下已经包含了用 jieba 分好词的语料，和游戏库中导出的游戏名字典。执行如下命令即可得到 total_word_feature_extractor_game.dat 模型。

```bash
# 训练 word embedding 模型，大概耗时 15min
./wordrep -e ./zh
```

模型超过 100MB，所以无法发布到 Git 上。如果无法运行 wordrep，可以手动拉取 MITIE 的源代码进行编译，我在 tools 目录下放的是 macOS 平台编译的 amd64 版本。或者可以联系我来获取这个模型文件。

```bash
# 构建镜像
docker build -t rasagame:v1 -f docker/Dockerfile_game .

# 启动镜像
docker run -it --rm --name game-nlu -p 5005:5000 rasagame:v1 python -m rasa_nlu.server -c sample_configs/config_jieba_mitie_sklearn.yml --path models
```

### 效果样例

```json
# API for NLU
Request: HTTP GET http://localhost:5005/parse?q=搜索任天堂出的射击游戏
Response:
{
  "intent": {
    "name": "game_recommend",
    "confidence": 0.4798265664356213
  },
  "entities": [
    {
      "entity": "company",
      "value": "任天堂",
      "start": 2,
      "end": 5,
      "confidence": null,
      "extractor": "ner_mitie"
    },
    {
      "entity": "type",
      "value": "射击",
      "start": 7,
      "end": 9,
      "confidence": null,
      "extractor": "ner_mitie"
    }
  ],
  "text": "搜索任天堂出的射击游戏"
}
```



