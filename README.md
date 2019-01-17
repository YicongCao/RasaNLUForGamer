## GameBot NLU

基于 Rasa NLU 的代码，进行了少量修改，后端采用 scikit-learn（意图分类）和 MITIE（实体识别），内置了游戏向的标注文本。

这个工程只包含 NLU 服务，不含可视化的部分。

![使用该NLU的Demo](https://ws3.sinaimg.cn/large/006tNc79gy1fz9m009ll8j30ef0bizm5.jpg)

### 食用方法

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



