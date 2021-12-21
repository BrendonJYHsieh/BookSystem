# 建置成exe方法
參考: https://www.readfog.com/a/1636267007799300096 \
安裝 Pyinstaller:
```console
pip install pyinstaller
```
安裝anaconda: https://www.anaconda.com/products/individual \
開啟anaconda prompt\
創建虛擬環境:
```console
conda create -n BookSystem python==3.9.6
```
進入虛擬環境
```console
conda activate BookSystem
```
cd至本目錄\
安裝所需模組
```console
pip install -r requirements.txt
```
測試成功與否
```console
python main.py
```
打包成exe
```console
Pyinstaller -F -w -i icon.ico main.py
```
exe會存放於dist資料夾內\
但還不能直接執行，因為缺少Asset與google_calendar資料夾\
將exe放到此目錄下即可執行\
退出虛擬環境
```console
conda deactivate
```