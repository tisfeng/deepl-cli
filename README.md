# DeepL Translation CL

A simple DeepL Translation command line program written in Python that does not require key.

一个使用 `Python` 编写、无需 auth_key 的 DeepL 翻译命令行工具。

## Usage

![image-20220722001822359](https://raw.githubusercontent.com/tisfeng/ImageBed/main/uPic/image-20220722001822359-1658420302.png)

## Examples

**Default is to translate to Chinese. If no source language is specified, it will autodetect the source language.**

```python
python3 deepL.py good
```
![image-20220721232029678](https://raw.githubusercontent.com/tisfeng/ImageBed/main/uPic/image-20220721232029678-1658416830.png)


```pythone
python3 deepL.py 优雅 --target-language EN
```
![image-20220722002541987](https://raw.githubusercontent.com/tisfeng/ImageBed/main/uPic/image-20220722002541987-1658420742.png)

```pythone
python3 deepL.py heel
```
![image-20220722001531505](https://raw.githubusercontent.com/tisfeng/ImageBed/main/uPic/image-20220722001531505-1658420131.png)

```pythone
python3 deepL.py heel --source-language EN --target-language ZH
```
![image-20220722001607452](https://raw.githubusercontent.com/tisfeng/ImageBed/main/uPic/image-20220722001607452-1658420167.png)

```pythone
python3 deepL.py My heart is slightly larger than the whole universe.
```
![image-20220722001625538](https://raw.githubusercontent.com/tisfeng/ImageBed/main/uPic/image-20220722001625538-1658420185.png)



*Sometimes the request fails because the same IP is requested too many times...😓*

![image-20220722001638112](https://raw.githubusercontent.com/tisfeng/ImageBed/main/uPic/image-20220722001638112-1658420198.png)