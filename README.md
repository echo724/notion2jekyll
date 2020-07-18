# Notion2Jekyll
[![PyPI version](https://badge.fury.io/py/notion2jekyll.svg)](https://badge.fury.io/py/notion2jekyll)

Jekyll Exporter makes your notion page to [Jekyll Post Markdown](https://jekyllrb-ko.github.io/docs/posts/) file. This is using [notion-py](https://github.com/jamalex/notion-py) to export notion page to markdown.  

Notion2Jekyll provides these features.  

1. Export a markdown file formatted as the jekyll-post format (`yyyy-m-dd-<your page's title>`) from your notion page.

2. Makes [front matter](https://jekyllrb.com/docs/step-by-step/03-front-matter/)s to the markdown file.

  - `tags` 

  - `layout: post`

3. Download images in your notion page, and automatically set the image path in the md file( `You need to rename the path when you upload in your blog` ).

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install notion2jekyll.  

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
from notion2jekyll.jekyll_exporter import export_out
from notion.client import NotionClient
token_v2 = #<your notion token_v2>
url = #<your notion page url>

export_out(url,token_v2)
```

## Additional Info

- Exporter will make the md file and images in `./jekyllpost_output/` and `./jekyllpost_output/<your block title>/`

- The url should be the page that you want to export.

- The front matter in the markdown will be different based on your jekyll blog variables. So, change the front matters when you finish the export, or change the code in this project.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.  

Please make sure to update tests as appropriate.  

## License

[MIT](https://choosealicense.com/licenses/mit/)  
