# AI-video-Replicate

> AI 视频生成与复刻工具，支持 Seedance、Sora2 和 Sora2免费 三种模型，提供文生视频、图生视频和视频复刻功能

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![Gradio](https://img.shields.io/badge/gradio-5.44+-ff7800.svg)

---

## 项目介绍

AI-video-Replicate 是一个专业的 AI 视频生成与复刻工具，集成了多个先进的视频生成模型。通过简洁的 Gradio 界面，用户可以轻松实现：

- **文生视频**: 通过自然语言描述生成高质量视频
- **图生视频**: 基于关键帧图片生成视频
- **视频复刻**: 自动提取视频提示词和关键帧，一键复刻视频效果

项目集成了 Qwen3-VL 视觉语言模型进行智能视频分析，基于 Sora2 五大支柱框架生成专业的视频复刻提示词。

### 核心特性

- **多模型支持**: 集成 Seedance、Sora2、Sora2免费 三种视频生成模型
- **智能提示词生成**: 基于 Sora2 五大支柱框架自动生成专业提示词
- **关键帧自动提取**: 从视频中均匀提取 8 张关键帧用于图生视频
- **实时进度跟踪**: 任务提交后自动轮询，实时显示生成进度
- **样例视频内置**: 提供样例视频，快速体验功能
- **Docker 部署**: 支持 Docker 和 Docker Compose 一键部署

---

## 功能清单

| 功能名称 | 功能说明 | 技术栈 | 状态 |
|---------|---------|--------|------|
| 文生视频 | 通过文本提示词生成视频 | Seedance/Sora2 API | ✅ 稳定 |
| 图生视频 | 通过关键帧图片生成视频 | Seedance/Sora2 API | ✅ 稳定 |
| 视频复刻 | 自动提取提示词和关键帧复刻视频 | Qwen3-VL + FFmpeg | ✅ 稳定 |
| 提示词生成 | 基于 Sora2 框架生成专业提示词 | Qwen3-VL | ✅ 稳定 |
| 关键帧提取 | 自动从视频提取均匀分布的关键帧 | FFmpeg | ✅ 稳定 |
| 进度轮询 | 实时显示视频生成进度 | httpx | ✅ 稳定 |
| Gradio 界面 | 友好的 Web 操作界面 | Gradio 5.44+ | ✅ 稳定 |

---

## 模型对比

| 特性 | Seedance | Sora2 | Sora2免费 |
|------|----------|-------|-----------|
| 模型 | seedance-1-5-pro-251215<br>seedance-1-0-pro-fast | sora-2 | sora2-landscape-10s/15s<br>sora2-portrait-10s/15s |
| 时长 | 4s, 5s, 8s, 12s | 10s, 15s | 10s, 15s |
| 比例 | 21:9, 16:9, 4:3, 1:1, 3:4, 9:16 | portrait, landscape | 横屏/竖屏 |
| 图生视频 | 单张关键帧 | 多张关键帧 | 多张关键帧 |
| 免费额度 | 按需付费 | 按需付费 | 每天 10 次 |

---

## 安装说明

### 环境要求

- Python 3.11+
- FFmpeg（用于视频关键帧提取）
- 8GB+ 内存推荐

### 安装步骤

#### 方式一: 本地运行

1. **克隆项目**
```bash
git clone https://github.com/xiaohuihui202504/AI-video-Replicate.git
cd AI-video-Replicate
```

2. **安装依赖**
```bash
pip install -r requirements.txt
pip install httpx[http2]
```

3. **配置环境变量**
```bash
cp .env.example .env
# 编辑 .env 文件，填入你的 API Key
```

4. **启动应用**
```bash
python app.py
```

5. **访问界面**
打开浏览器访问 `http://localhost:7860`

#### 方式二: Docker 部署

**使用 docker-compose (推荐)**

创建 `.env` 文件:
```bash
SEEDANCE_AUTH_TOKEN=your-seedance-token
SORA2_API_KEY=your-sora2-key
SORA2_ENABLED=true
SORA2FREE_API_KEY=your-free-key
QWEN_API_KEY=your-qwen-key
```

运行:
```bash
docker-compose up -d
```

**使用 Docker 命令**

1. 构建镜像
```bash
docker build -t video-generator:latest .
```

2. 运行容器
```bash
docker run -d \
  --name ai-video-replicate \
  -p 7860:7860 \
  -e SEEDANCE_AUTH_TOKEN=your-seedance-token \
  -e SORA2_API_KEY=your-sora2-key \
  -e SORA2FREE_API_KEY=your-free-key \
  -e QWEN_API_KEY=your-qwen-key \
  video-generator:latest
```

访问 http://localhost:7860 使用 AI-video-Replicate

---

## 使用说明

### 文生视频

1. 选择模型提供者 (seedance / sora2 / sora2free)
2. 输入视频描述提示词
3. 选择模型、时长和比例 (根据模型类型自动显示/隐藏)
4. 点击 "生成视频" 按钮
5. 等待视频生成完成

### 图生视频 (通过视频复刻)

图生视频功能通过「视频复刻」实现，系统会自动从上传的视频中提取关键帧作为参考图：

1. 在「视频复刻」区域上传视频或点击 "加载样例视频"
2. 点击 "提取视频提示词 & 关键帧" 按钮
3. 系统自动提取 **8 张关键帧**（均匀分布在视频时间轴上）
4. 选择模型提供者：
   - **Sora2**: 使用全部 8 张关键帧
   - **Sora2免费**: 使用全部 8 张关键帧
   - **Seedance**: 使用第 1 张关键帧（仅支持单图）
5. 确认或修改提示词
6. 点击 "生成视频" 按钮

> 关键帧会显示在「提取的关键帧」区域，可以预览

### 视频复刻流程

```
上传视频 → 点击"提取视频提示词 & 关键帧"
   ↓
系统分析视频内容
   ↓
生成 SORA2 风格提示词 + 提取 8 张关键帧
   ↓
确认/修改提示词
   ↓
选择模型参数生成新视频
```

---

## 环境变量配置

| 变量名 | 说明 | 默认值 | 必填 |
|--------|------|--------|------|
| `SEEDANCE_API_BASE_URL` | Seedance API 地址 | https://seedanceapi.duckcloud.fun | 否 |
| `SEEDANCE_AUTH_TOKEN` | Seedance API Token | - | 是 |
| `SORA2_API_BASE_URL` | Sora2 API 地址 | https://api.jxincm.cn | 否 |
| `SORA2_API_KEY` | Sora2 API Key | - | 条件必填 |
| `SORA2_ENABLED` | 是否启用 Sora2 | true | 否 |
| `SORA2FREE_API_BASE_URL` | Sora2免费 API 地址 | https://rendersora2api.duckcloud.fun | 否 |
| `SORA2FREE_API_KEY` | Sora2免费 API Key | - | 条件必填 |
| `QWEN_API_BASE_URL` | Qwen3-VL API 地址 | https://api-inference.modelscope.cn/v1 | 否 |
| `QWEN_API_KEY` | Qwen3-VL API Key | - | 是 |
| `QWEN_MODEL_ID` | Qwen 模型 ID | Qwen/Qwen3-VL-8B-Instruct | 否 |
| `GRADIO_PORT` | Gradio 服务端口 | 7860 | 否 |

---

## 项目结构

```
AI-video-Replicate/
├── app.py                    # Gradio 前端主程序
├── qwen3vl.py                # Qwen3-VL 视频分析模块
├── requirements.txt          # Python 依赖
├── Dockerfile                # Docker 镜像
├── docker-compose.yml        # Docker Compose 配置
├── .env                      # 环境变量配置
├── .env.example              # 环境变量示例
├── .gitignore                # Git 忽略配置
├── sample/                   # 样例视频目录
│   └── video.mp4            # 样例视频文件
├── prompt/                   # 提示词缓存目录
├── test/                     # 测试目录
├── 复刻SORA2视频提示词专家.md  # 提示词模板文档
└── README.md                 # 项目文档
```

---

## 技术栈

| 技术 | 版本 | 用途 |
|------|------|------|
| Python | 3.11+ | 主要开发语言 |
| Gradio | 5.44+ | Web 界面框架 |
| FastAPI | 0.115+ | API 框架 |
| httpx | latest | 异步 HTTP 请求 |
| Pillow | 11.0+ | 图片处理 |
| OpenAI SDK | 2.3+ | AI 模型调用 |
| FFmpeg | system | 视频关键帧提取 |
| Qwen3-VL | 8B-Instruct | 视频内容分析 |

---

## 视频复刻提示词专家

本项目集成了专业的视频复刻提示词生成系统，基于 Sora2 五大支柱框架：

### 五大支柱

1. **主体与角色 (Subject & Character)**: 外观、服装、情感状态
2. **动作与运动 (Action & Movement)**: 具体动词描述
3. **环境与背景 (Environment & Setting)**: 位置、时间和氛围
4. **电影构图 (Cinematography)**: 摄像机角度、运动和取景
5. **美学与风格 (Aesthetics & Style)**: 视觉效果和风格

### 提示词结构

生成的提示词采用三段式结构：
- **Style**: 视觉纹理、光照质量、色彩调板、氛围
- **Cinematography**: 摄像机运动、镜头特性、布光方案、情绪基调
- **Scene Breakdown**: 场景分解、动作序列、对话、背景音

---

## 关键帧提取说明

系统使用 Qwen3-VL 模型分析视频，并通过 FFmpeg 提取关键帧：

| 参数 | 值 | 说明 |
|------|-----|------|
| 提取帧数 | 8 张 | 默认从视频中均匀提取 8 张关键帧 |
| 提取方式 | 均匀分布 | 按时间轴均匀分布，间隔 = 视频时长 / 9 |
| 图片格式 | JPG | 自动转换为 base64 发送给 API |

**示例**: 10 秒视频的关键帧提取时间点：
- 第 1 帧: ~1.1s
- 第 2 帧: ~2.2s
- 第 3 帧: ~3.3s
- ...
- 第 8 帧: ~8.8s

---

## 开发指南

### 本地开发

```bash
# 安装开发依赖
pip install -r requirements.txt

# 配置环境变量
cp .env.example .env

# 启动开发服务器
python app.py
```

### 构建部署

```bash
# 构建镜像
docker build -t video-generator:latest .

# 运行容器
docker-compose up -d
```

---

## 常见问题

<details>
<summary>Q: 视频生成需要多长时间？</summary>

A: 通常需要 1-5 分钟，具体取决于视频时长和服务器负载。Sora2 可能需要更长时间（最多 15 分钟），Sora2免费 图生视频超时时间为 10 分钟。
</details>

<details>
<summary>Q: 支持哪些图片格式？</summary>

A: 支持 PNG、JPG、JPEG、GIF、WebP、BMP 格式。关键帧自动提取为 JPG 格式。
</details>

<details>
<summary>Q: 如何获取 API Key？</summary>

A:
- **Seedance**: 联系服务提供商获取
- **Sora2**: 访问 https://api.jxincm.cn/register?aff=SeEB 注册获取
- **Sora2免费**: 默认 API Key 已配置，每天 10 次免费额度
- **Qwen3-VL**: 访问 https://modelscope.cn 注册获取
</details>

<details>
<summary>Q: 视频下载失败怎么办？</summary>

A: 系统会提供视频 URL，可以手动复制链接下载。Seedance 视频会通过代理下载。
</details>

<details>
<summary>Q: Sora2 选项是灰色不可用？</summary>

A: 检查 `.env` 文件中的 `SORA2_ENABLED` 是否设置为 `true`（注意拼写），或通过环境变量设置。
</details>

<details>
<summary>Q: Sora2免费 有什么限制？</summary>

A: Sora2免费 每天限制使用 10 次，支持文生视频和图生视频（通过关键帧）模式。
</details>

<details>
<summary>Q: 图生视频如何使用？</summary>

A: 图生视频通过「视频复刻」功能实现。上传视频后点击「提取视频提示词 & 关键帧」，系统会自动提取 8 张关键帧用于图生视频。
- Sora2 / Sora2免费: 全部 8 张
- Seedance: 仅第 1 张
</details>

<details>
<summary>Q: 为什么没有单独的图片上传功能？</summary>

A: 为了简化操作流程，图生视频功能统一通过视频复刻的关键帧提取实现，这样可以保证提示词和图片的一致性，提升复刻效果。
</details>

---

## 技术交流群

欢迎加入技术交流群，分享你的使用心得和反馈建议：

![技术交流群](https://mypicture-1258720957.cos.ap-nanjing.myqcloud.com/Obsidian/image-20260122235736120.png)

---

## 作者联系

- **微信**: laohaibao2025
- **邮箱**: 75271002@qq.com

![微信二维码](https://mypicture-1258720957.cos.ap-nanjing.myqcloud.com/Screenshot_20260123_095617_com.tencent.mm.jpg)

---

## 打赏

如果这个项目对你有帮助，欢迎请我喝杯咖啡 ☕

**微信支付**

![微信支付](https://mypicture-1258720957.cos.ap-nanjing.myqcloud.com/Obsidian/image-20250914152855543.png)

---

## Star History

如果觉得项目不错，欢迎点个 Star ⭐

[![Star History Chart](https://api.star-history.com/svg?repos=xiaohuihui202504/AI-video-Replicate&type=Date)](https://star-history.com/#xiaohuihui202504/AI-video-Replicate&Date)

---

## License

SPDX-License-Identifier: MIT

Copyright (c) 2025 xiaohuihui202504
