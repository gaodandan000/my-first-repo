# my-first-repo
用来存我的AI项目/脚本/文档

## 设置 Anthropic API

### 环境变量配置

1. 复制 `.env.example` 到 `.env`:
   ```bash
   cp .env.example .env
   ```

2. 编辑 `.env` 文件，填入你的API凭证

3. 加载环境变量:
   ```bash
   source .env
   # 或者
   export $(cat .env | xargs)
   ```

### 使用方法

在你的脚本中可以这样使用:

**Python:**
```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
    base_url=os.environ.get("ANTHROPIC_API_BASE")
)
```

**Node.js:**
```javascript
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env.ANTHROPIC_API_KEY,
  baseURL: process.env.ANTHROPIC_API_BASE
});
```

**注意:** `.env` 文件已被添加到 `.gitignore`，不会被提交到版本控制中。
