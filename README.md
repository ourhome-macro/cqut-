
```markdown
# 车牌识别系统 (License Plate Recognition System)
一个基于Python和hyperlpr3的车牌识别系统，支持实时摄像头捕获和中文车牌显示，适用于树莓派等嵌入式设备。
## 功能特性
- 实时摄像头车牌识别（支持中文/英文/数字）  
- 中文车牌文字渲染（通过PIL库实现）  
- 跨平台支持（Windows、Linux、树莓派）  
- 简单易用的命令行界面  
## 快速开始
### 1. 克隆项目
```bash
git clone https://github.com/your-username/cqut-.git
cd cqut-
```
### 2. 安装依赖
```bash
# 使用requirements.txt安装所有依赖
pip install -r requirements.txt
```
### 3. 运行程序
```bash
python main.py
```
### 4. 退出程序
按 `q` 键退出。
## 项目结构
```
license-plate-recognition/
├── main.py          # 主程序文件
├── requirements.txt # 依赖列表
└── README.md        # 项目说明
```
## 依赖列表
项目依赖可通过`requirements.txt`一键安装：
```txt
Pillow>=9.0.0
hyperlpr3>=0.1.3
opencv-python>=4.5.0
numpy>=1.21.0
```
## 使用说明
1. **摄像头要求**：系统默认使用摄像头（`cv2.VideoCapture(0)`），确保摄像头已连接并正常工作。  
2. **中文显示**：系统通过PIL库渲染中文，需确保系统安装了中文字体（如文泉驿正黑）。  
3. **识别结果**：识别结果会显示在摄像头画面中，包括车牌号和置信度。  
## 部署到树莓派
1. **安装依赖**：  
   ```bash
   sudo apt update
   sudo apt install python3-pip ttf-wqy-zenhei
   pip install -r requirements.txt
   ```
2. **运行程序**：  
   ```bash
   python main.py
   ```
### **说明**  
- **项目名称**：可根据你的项目修改（如`License Plate Recognition`）。  
- **依赖版本**：根据实际使用的库版本调整（如`hyperlpr3`的版本）。  
- **部署步骤**：树莓派部署部分已包含字体安装和依赖安装命令，确保跨平台兼容性。  
