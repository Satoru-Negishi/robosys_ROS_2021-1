# robosys_ROS_2021-1
ロボットシステム学の課題2で作成したROSのパッケージと使用しているデバイスドライバのコードです。

## 目次
- 概要
- 使用
- 回路
- 環境構築
- 実行
- 動画
- ライセンス

## 概要
大学の講義の課題として作成したROSのパッケージで、下記の動作を行います。
- [Publisher]10進数の0~15までのキーボード入力を受け付ける
- [Subscriber]入力された数字を2進数に変換し表示＆1/0に対応してLEDを点灯・消灯させる

## 使用
- Raspberry Pi 4
- ブレッドボード
- LED
- 抵抗 220Ω
- ジャンパー線

## 回路
LEDを光らせるための電子回路は以下のように作成しました。  
LEDは、左からGPIO[23,24,25,26]に接続しています。
### 写真  
![ROS回路](https://user-images.githubusercontent.com/73330874/104090771-5054dc00-52bc-11eb-8d72-87d31e208fb4.jpg)
  
### 回路図
![ROS回路図](https://user-images.githubusercontent.com/73330874/104091203-4b455c00-52bf-11eb-99ff-27c504c9142f.png)  
  
## 環境構築
### 事前準備
下記の資料を参考にROSの環境構築とワークスペースを作成しています。
- ROS：https://github.com/ryuichiueda/ros_setup_scripts_Ubuntu20.04_desktop
- ワークスペース：https://github.com/ryuichiueda/robosys2020/blob/master/md/ros.md
### クローン
デバイスドライバとパッケージを使用するためにこのリポジトリをクローンしてください。
```
$ git clone https://github.com/Satoru-Negishi/robosys_ROS_2021-1.git
```
### デバイスドライバ
デバイスドライバは以前課題として作成したものを改良して使用しています。  
セットアップや動作確認は[こちら](https://github.com/Satoru-Negishi/robosys_devicedriver_2020-12)を参考にしてください。  
### パッケージのビルド
クローンしたROSのパッケージはビルドします。
```
$ cd ~/catkin_ws
$ catkin_make
$ source ~/.bashrc
```

## 実行
以下のコードを実行することでパブリッシャとサブスクライバのノードが同時に起動します。
```
$roslaunch robosys_ROS_2021-1 flash_led.launch
```
起動後、キーボード入力の待機状態になるため、0～15まで数字を入力してください。  
入力した数字の2進数表記が画面上に表示され、 1 - ON / 0 - OFF のように対応したLEDが点灯・消灯します。  
    
### 補足
パブリッシャとサブスクライバを別々の端末で起動したい場合は以下の様に行ってください。
- 端末1：roscoreを起動します
```
$roscore
```
- 端末2：パブリッシャを起動します
```
$rosrun robosys_ROS_2021-1 input_num.py
```
- 端末3：パブリッシャの起動後にサブスクライバを起動します
```
$rosrun robosys_ROS_2021-1 flash_led.py
```
この状態でパブリッシャを起動している端末上で数字を入力することで上記と同様の動作が行われます。  
  
## 動画
動作の様子が分かる動画をYouTubeに投稿しています。  
(動画内で使用しているパッケージは最新のものではないため、コマンドが一部上記のものと異なります。)  
- [動画リンク](https://youtu.be/wJdgtzbcISE)
## ライセンス
[GNU GENERAL PUBLIC LICENSE v3.0](https://github.com/Satoru-Negishi/robosys_ROS_2021-1/blob/main/COPYING)
