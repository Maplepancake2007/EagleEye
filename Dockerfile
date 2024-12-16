FROM ubuntu:20.04

# コンテナ内でパッケージリストの更新とPython関連パッケージのインストール
RUN apt-get update && apt-get install -y \
    python3 \              # Python3のインストール
    python3-pip \          # pipのインストール
    python3-venv \         # 仮想環境作成ツール
    curl \                 # データ取得ツール
    wget \                 # データ取得ツール
    git \                  # バージョン管理ツール
    vim \                  # テキストエディタ
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN python3 -m venv venv && \
    . venv/bin/activate && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

ENV POETRY_VIRTUALENVS_IN_PROJECT=false


WORKDIR /src
