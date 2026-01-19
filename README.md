# onegadget-selector 🚀

[![PyPI version](https://img.shields.io/pypi/v/onegadget-selector.svg)](https://pypi.org/project/onegadget-selector/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)

简单的 onegadget 小工具，建议配合 libcdb 食用

---

## 安装

```
pip install onegadget-selector
```

## 用法

### show_onegadgets

```python
from pwn import *
from onegadget_selector import *

'''
省略...
'''

libc = ELF(libcdb.search_by_symbol_offsets({'__libc_start_main': __libc_start_main_addr % 0x1000}))
show_onegadgets(libc.path)

'''
省略...
'''
```

### select_onegadgets

```python
from pwn import *
from onegadget_selector import *

'''
省略...
'''

libc = ELF(libcdb.search_by_symbol_offsets({'__libc_start_main': __libc_start_main_addr % 0x1000}))
base_addr = __libc_start_main_addr - libc.symbols['__libc_start_main']
one_gadget_offset = select_onegadgets(libc.path)
one_gadget_addr = base_addr + one_gadget_offset

'''
省略...
'''
```