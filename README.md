# gpt-partner

简单拼接了一个语音-文本-语音的demo。调用了chatGPT接口。
在api_key中填入自己的chatGPT即可使用！
- 链接麦克风，通过语音生成wav文件（default chinese）
- 解析wav语音生成文本（default chinese）
- 通过chatGPT接口，远程调用
- 接收返回信息，提取回答内容（仅支持单句回答）
- 调用文本转语音，根据回答生成语音

这只是个简单的调用，默认为中文，当然你也可以修改为其它语言。
