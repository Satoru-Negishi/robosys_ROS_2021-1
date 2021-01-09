# robosys_ROS_2021-1
ロボットシステム学の課題2で作成したROSのパッケージと使用しているデバイスドライバのコードです。

## 目次
- 概要
- 用意・環境構築
- 回路
- 実行コマンド
- ライセンス

## 概要
大学の講義の課題として作成したROSのパッケージで、下記の動作を行います。
- [Publisher]10進数の0~15までのキーボード入力を受け付ける
- [Subscriber]入力された数字を2進数に変換し表示＆1/0に対応してLEDを点灯・消灯させる

## 用意
- Raspberry Pi 4
- ブレッドボード
- LED
- 抵抗 220Ω
- ジャンパー線

## 回路
LEDを光らせるための電子回路は以下のように作成しました。  
[写真]  
  
[回路図]
  
  
## 環境構築
下記の資料を参考にROSの環境構築とワークスペースを作成しています。
- ROS:https://github.com/ryuichiueda/ros_setup_scripts_Ubuntu20.04_desktop
- ワークスペース:https://github.com/ryuichiueda/robosys2020/blob/master/md/ros.md
  
実際に動作させるために、このパッケージをクローンしてください。
```
$ git clone https://github.com/Satoru-Negishi/robosys_ROS_2021-1.git
```
  
デバイスドライバは以前課題として作成したものを改良して使用しています。  
セットアップや動作確認は[こちら](https://github.com/SatoruNegishi/robosys_devicedriver_2020-12)を参考にしてください。  
  
クローンしたROSのパッケージはビルドします。
```
$ cd ~/catkin_ws
$ catkin_make
$ source ~/.bashrc
```

## 実行
