# SIC/XE Assembler & Loader(分工完成)

## 組譯器架構

### Assembler 模組
1. **Error_Scan.py** - 語法與格式錯誤檢查
2. **Pass1.py** - 建立符號表與中間檔案
3. **Pass2_1.py** - 產生 Object Code，檢查定址模式錯誤
4. **Pass2_2.py** - Expression 驗證與最終 Object File 生成
5. **assembler.py** - 主程式，整合所有模組

### Loader
- **loader.py** - 處理 Object Code，執行位址修改與二進位輸出

## 使用方式

### Assembler
```bash
python assembler.py <input_file.asm>
```

### Loader
```bash
python loader.py <object_file.obj>
```

## 輸出檔案
- `*.obj` - Object Code 檔案
- `*.txt` - 指定格式的輸出結果
- 中間檔案（Intermediate Files）

## 主要特色
- ✅ 完整的錯誤檢測機制
- ✅ 支援 Format 2/3/4 指令
- ✅ PC-Relative 與 Base-Relative 定址
- ✅ Expression 計算與驗證
- ✅ 模組化設計，易於維護擴展

## 系統需求
- Python 3.x (版本一)
- C++ 編譯器 (版本二)

## 參考資料
- [Stack Overflow - String Value in Stack](https://stackoverflow.com/questions/58639287/)
- [YouTube - Assembler Tutorial](https://www.youtube.com/watch?v=rdKX9hzA2lU)
- [Hackaday - Writing an Assembler in Python](https://hackaday.io/project/10576-mucpu-an-8-bit-mcu/log/36010)
