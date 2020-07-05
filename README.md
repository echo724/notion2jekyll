# Notion2Jekyll
[![PyPI version](https://badge.fury.io/py/notion2jekyll.svg)](https://badge.fury.io/py/notion2jekyll)

Jekyll Exporter makes your notion page to [Jekyll Post Markdown](https://jekyllrb-ko.github.io/docs/posts/) file. This is using [notion-py](https://github.com/jamalex/notion-py) to export notion page to markdown.  

Notion2Jekyll provides these features.  

1. Export markdown file from your notion page.

2. Makes [front matter](https://jekyllrb.com/docs/step-by-step/03-front-matter/) to the markdown file.

- `Tags`

- `toc` → `if your Jekyll blog supports`

- `layout` → `article(default)`

1. Download images in your notion page, and automatically set the image path in the md file( `You need to rename the path when you upload in your blog` ).

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.  

```Bash
$pip install notion2jekyll
```

## Usage_Command Line

```Bash
$python -m notion2jekyll
#Markdown file name: <output file name(without .md)>
#Token_v2: <your token_v2 on notion.so>
#Notion Page Url: <your notion page to export>
```

## Usage_Jupyter or Ipython

```Python
from notion2jekyll import export
from notion.client import NotionClient
token_v2 = #<your notion token_v2>
url = #<your notion page url>
page = NotionClient(token_v2 = token_v2)
export(page,client)
```

- Exporter will make the md file and images in `./jekyllpost_output/` and `./jekyllpost_output/<your block title>/`

- The url should be the page that you want to export.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.  

Please make sure to update tests as appropriate.  

## License

[MIT](https://choosealicense.com/licenses/mit/)  
