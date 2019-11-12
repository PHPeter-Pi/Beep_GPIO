# Beep GPIO

ラズパイ Zero の GPIO につなげたピエゾ・スピーカーからビープ音を出すだけのスクリプトです。

## スピーカー

ピエゾ・スピーカーは 100 円均一などで売っているキッチンタイマーなど、音が鳴る系の小物に入っているものを分解して使います。

## 配線

ピエゾ・スピーカーの「＋」（プラス）極と「ー」（マイナス）極をラズパイ Zero の GPIO につなげます。GPIO のピンは、本体カメラ端子側の一番端の 2 本を使います。外側が本体 40 番ピン、内側が 39 番ピンです。

- スピーカーの「＋」（プラス）極を GPIO の 21 番ピン（本体の 40 番ピン）
- スピーカーの「ー」（マイナス）極を GPIO の GND ピン（本体の 39 番ピン）

- 参考資料：
  - [ハードウェアについて](http://hara.jpn.com/_default/ja/Topics/RaspPiZero.html) | Raspberry Pi Zeroについて @ 原 功のホームページ
  - [Raspberry Pi Zero W Revision 1.1　Schematics](https://www.raspberrypi.org/documentation/hardware/raspberrypi/schematics/rpi_SCH_ZeroW_1p1_reduced.pdf) @ ラズパイ公式

## 使い方

```shellsession
$ # コマンドの clone
$ cd ~/
$ git clone https://github.com/PHPeter-Pi/Beep_GPIO.git
$ cd Beep_GPIO

$ # 音が鳴るかの確認
$ ./beep.sh ok
$ ./beep.sh ng
$ ./beep.sh ready

$ # シンボリック・リンクの作成
$ ln -s $(pwd)/beep.sh /usr/local/bin/beep

$ # 再チェック
$ beep ok

$ # コマンドのアップデート
$ cd ~/Beep_GPIO
$ git pull origin
```

## 仕様

以下で動作確認しています。

- OS: Raspbian OS 10 (Buster) Lite
- Model: Raspberry Pi Zero W Rev 1.1

```shellsession
$ cat /etc/os-release
PRETTY_NAME="Raspbian GNU/Linux 10 (buster)"
NAME="Raspbian GNU/Linux"
VERSION_ID="10"
VERSION="10 (buster)"
VERSION_CODENAME=buster
ID=raspbian
ID_LIKE=debian
HOME_URL="http://www.raspbian.org/"
SUPPORT_URL="http://www.raspbian.org/RaspbianForums"
BUG_REPORT_URL="http://www.raspbian.org/RaspbianBugs"

$ cat /proc/cpuinfo
processor	: 0
model name	: ARMv6-compatible processor rev 7 (v6l)
BogoMIPS	: 697.95
Features	: half thumb fastmult vfp edsp java tls
CPU implementer	: 0x41
CPU architecture: 7
CPU variant	: 0x0
CPU part	: 0xb76
CPU revision	: 7

Hardware	: BCM2835
Revision	: 9000c1
Serial		: 00000000f4e5809a
Model		: Raspberry Pi Zero W Rev 1.1
pi@raspberrypi:~ $ cat /proc/cpuinfo | grep Model
Model		: Raspberry Pi Zero W Rev 1.1
```
