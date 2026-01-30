# 使用Python官方镜像作为基础镜像
FROM python:3.14-slim

# 设置工作目录
WORKDIR /app

# 复制项目文件到工作目录
COPY backend/ .

# 安装uv和项目依赖
RUN pip install --no-cache-dir uv && uv install

# 创建file目录
RUN mkdir -p file

# 暴露端口
EXPOSE 5000

# 运行应用
CMD ["python", "main.py"]