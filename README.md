# DeepL Translation CL

A simple DeepL Translation command line program written in Python that does not require key.

一个使用 `Python` 编写、无需 auth_key 的 DeepL 翻译命令行工具。

## Usage

![image-20221018202931345](https://raw.githubusercontent.com/tisfeng/ImageBed/main/uPic/image-20221018202931345-1666096171.png)

## Examples

### Translate word to Chinese

**Default is to translate text to `Chinese`. If no source language is specified, it will autodetect the source language.**

```python
python3 deepL.py good
```

![iShot_2022-10-18_18.26.15-1666089417](https://raw.githubusercontent.com/tisfeng/ImageBed/main/uPic/iShot_2022-10-18_18.26.15-1666089417.png)

### Translate word to designated language

```python
python3 deepL.py 优雅 -t en
```

![iShot_2022-10-18_18.26.48](https://raw.githubusercontent.com/tisfeng/ImageBed/main/uPic/iShot_2022-10-18_18.26.48-1666089479.png)

### Auto detect source language

```python
python3 deepL.py heel
```

![iShot_2022-10-18_18.27.28](https://raw.githubusercontent.com/tisfeng/ImageBed/main/uPic/iShot_2022-10-18_18.27.28-1666095985.png)

### Translate word from designated language to designated language

```python
python3 deepL.py heel -s en -t zh
```

![iShot_2022-10-18_18.27.59](https://raw.githubusercontent.com/tisfeng/ImageBed/main/uPic/iShot_2022-10-18_18.27.59-1666096054.png)

### Translate Text

```python
python3 deepL.py My heart is slightly larger than the whole universe.
```

![image-20220722001625538](https://raw.githubusercontent.com/tisfeng/ImageBed/main/uPic/image-20220722001625538-1658420185.png)

> Note ⚠️: _Sometimes the request fails because the same IP is requested too many times...😓_

![image-20220722001638112](https://raw.githubusercontent.com/tisfeng/ImageBed/main/uPic/image-20220722001638112-1658420198.png)
