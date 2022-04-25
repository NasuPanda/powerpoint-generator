# パワポ画像貼り付けツール

PowerPointで作成したフォーマット位置に画像を出力するGUIツールです。

## 概要

PowerPointで作成したフォーマットを使用して画像貼り付け・テキスト置換を行います。

- 1データ(及び1グループ)に画像が複数存在する場合、指定したラベル位置に画像を貼り付ける事ができます。
- 連番になっているデータの場合、順番に画像を貼り付ける事ができます。

**主な機能**

- 四角形 → 画像 への置換
  - 四角形の配置 = 画像の配置
  - 四角形のテキスト = 画像のラベル
  - 画像はデータ名とラベルを「 _ 」で区切る
- テキストの置換
  - @1 (@ + 数字) = データ名/グループ名への置換
  - #1 (# + 数字) = ラベルへの置換

## 使用方法

### ラベル位置への貼付けの場合

1データ(及び1グループ)に画像が複数存在する場合、指定したラベル位置に画像を配置する事が出来ます。

**入力フォーマット**

ラベル名を指定します。

1枚のスライドに複数グループが存在する場合、「 _ 」で「連番」と「ラベル名」を区切って指定します。

1枚のスライドに1グループの場合は「ラベル名」のみ指定します。

例ではグループが2つなので、「1_右」, 「2_右」のように「 _ 」で「連番」と「ラベル名」を区切ります。
![ラベリング_フォーマット](https://user-images.githubusercontent.com/85564407/165007818-aa214818-b1c2-4a6d-a8a8-8195f7458766.png)

**入力画像**

ねずみ_右の場合: 「ねずみ」がデータ名/グループ名 「右」がラベルとして扱われます。
![image](https://user-images.githubusercontent.com/85564407/165009884-babf36f4-3558-493b-ad4e-54f3cec36d40.png)

**出力されるPowerPoint**

1枚目
![ラベリング 出力_1](https://user-images.githubusercontent.com/85564407/165007834-7e7db6df-e4a0-432d-ab74-d615ac6f2e33.png)
2枚目
![ラベリング 出力 2](https://user-images.githubusercontent.com/85564407/165009914-4737f8af-1c0d-4c4a-a169-a5156a229505.png)

### 連番貼り付けの場合

連番になっているデータの場合、順番に画像を貼り付ける事ができます。

**入力フォーマット**

四角形の中に数字を指定します。
![順に貼り付け_フォーマット](https://user-images.githubusercontent.com/85564407/165007744-6061d6e1-22b3-46e7-9d18-9f0f1b865cd8.png)

**入力画像**

fruits_1の場合: 「fruits」がデータ名/グループ名 「1」がラベル(連番)として扱われます。
![image](https://user-images.githubusercontent.com/85564407/165010477-72faaf06-943e-4dda-9170-b9bcca155da9.png)

**出力されるPowerPoint**

1枚目
![順に貼り付け_出力 1](https://user-images.githubusercontent.com/85564407/165007794-211c05cf-76d9-4563-9d48-42d91bb12728.png)
2枚目
![順に貼り付け_出力 2](https://user-images.githubusercontent.com/85564407/165010628-b2cc1a2c-2767-4cdc-ac12-31311f456887.png)


## 動作環境

アプリケーションを動作させるために以下の環境が必要です。

- Python 3.10.2
- python-pptx 0.6.21
- PySimpleGUI 4.59.0

## 詳細

TODO 編集

### フォーマットの作成

画像を配置したい位置に四角形を配置したPowerPointを作成してください。
以下はイメージです。

2グループ/1スライド & 4枚の画像/1グループ

![image_2グループ](https://user-images.githubusercontent.com/85564407/165007671-73ed03f0-e2bf-4bf4-9327-0478dc17cff6.png)

1グループ/1スライド & 8枚の画像/1グループ

![image_1グループ](https://user-images.githubusercontent.com/85564407/165007711-6dc27749-4be0-4cc4-84d3-084a16ddfe50.png)

「group」はグループ名を指します。画像のデータ名とも言えます。
「label」はラベルを指します。ラベルの指定については後述します。

#### 特定レイアウトの場合

![特定レイアウト_フォーマット](https://user-images.githubusercontent.com/85564407/165007818-aa214818-b1c2-4a6d-a8a8-8195f7458766.png)

※ 注意点

ラベルの順番が揃っていないように見えるのは気のせいではありません。

特定レイアウトへの出力の場合、ラベルが何になるか予想が付かないため順番を揃えていないことが原因です。

![特定レイアウト_出力](https://user-images.githubusercontent.com/85564407/165007834-7e7db6df-e4a0-432d-ab74-d615ac6f2e33.png)

![特定レイアウト_フォーマット_1グループ](https://user-images.githubusercontent.com/85564407/165007993-7de5363b-a96b-441b-8eb4-5fed989105b3.png)

#### 連番出力の場合

連番になっているデータを順番に貼り付ける場合、以下のように四角形の中に数字を指定します。

![順に貼り付け_フォーマット](https://user-images.githubusercontent.com/85564407/165007744-6061d6e1-22b3-46e7-9d18-9f0f1b865cd8.png)

![順に貼り付け_出力](https://user-images.githubusercontent.com/85564407/165007794-211c05cf-76d9-4563-9d48-42d91bb12728.png)


## 動作サンプルに使用した画像

- [【フリーアイコン】 フルーツ](https://sozai.cman.jp/icon/food/fruits/)
- [【フリーアイコン】 矢印（上下左右）](https://sozai.cman.jp/icon/arrow/base1/)
