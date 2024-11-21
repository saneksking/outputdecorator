# Output Decorator <sup>v0.0.3</sup>

[![GitHub release (latest by date)](https://img.shields.io/github/v/release/saneksking/outputdecorator)](https://github.com/saneksking/outputdecorator/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/outputdecorator?label=pypi%20downloads)](https://pypi.org/project/outputdecorator/)
![GitHub top language](https://img.shields.io/github/languages/top/saneksking/outputdecorator)
[![PyPI](https://img.shields.io/pypi/v/outputdecorator)](https://pypi.org/project/outputdecorator)
[![GitHub](https://img.shields.io/github/license/saneksking/outputdecorator)](https://github.com/saneksking/outputdecorator/blob/master/LICENSE)
[![PyPI - Format](https://img.shields.io/pypi/format/outputdecorator)](https://pypi.org/project/outputdecorator)
***
### Output Decorator - Library for decorating strings in CLI apps 
***

## Help:

`pip install outputdecorator`

```python
from output_decorator import StringDecorator

text = StringDecorator.string_decorate(text='Python', symbol='*', print_flag=False)
print(text) # ************************************ Python ***********************************

StringDecorator.string_decorate(text='Python', symbol='*', print_flag=True) 

StringDecorator.framed_decorate(text='Python', top_symbol='*', bottom_symbol='-')
"""
******
Python
------
"""
# Output: ************************************ Python ***********************************

```

***

## Disclaimer of liability:
    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
    FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
    DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
    SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
    CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
    OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
