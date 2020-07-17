from notion2md.md_exporter import block2md, recursive_getblocks,get_page
from notion.client import NotionClient
import os

def format_date(block):
    date = block.get_property("created")
    formatted_date = []
    formatted_date.append(str(date.year))
    formatted_date.append(str(date.month))
    formatted_date.append(str(date.day))
    formatted_date = "-".join(formatted_date)
    return formatted_date

def set_filename(block):
    date = format_date(block)
    name = block.title.replace(" ","-")
    fname = date + '-' + name + ".md"
    return fname

def make_file(block):
    directory = './jekyllpost_output/'
    if not(os.path.isdir(directory)):
        os.makedirs(os.path.join(directory))
    fname = set_filename(block)
    fname = os.path.join(directory,fname)
    file = open(fname,'w')
    return file,directory

#page - page type in collection, client = NotionClient
def md_export(page,client,dir):
    blocks = []
    recursive_getblocks(page,blocks,client)
    md = block2md(blocks,dir)
    return md

def remove_overlap(block,md):
    title = "# " + block.title+ "\n\n"
    md = md.replace(title,"")
    return md

def get_tags(block):
    tags = block.get_property('tags')
    return tags

def post_header(block,md):
    header = "---\n"
    header += "tags:\n"
    tags = get_tags(block)
    for tag in tags:
        header += '- ' + tag +'\n'
    header += 'layout: post\n'
    header += '---\n'
    md = header + md
    return md


#url should be collection view page url
def export_cli():
    token_v2, url = get_page()
    export_out(url,token_v2)

def export_in(page,client):
    file,dir = make_file(page)
    md = md_export(page,client,dir)
    md = remove_overlap(page,md)
    md = post_header(page,md)
    file.write(md)
    file.close

def export_out(url,token):
    client = NotionClient(token_v2=token)
    page = client.get_block(url)
    file,dir = make_file(page)
    md = md_export(page,client,dir)
    md = remove_overlap(page,md)
    md = post_header(page,md)
    file.write(md)
    file.close
    print("Notion page is successfully exported to Jekyll post")

if __name__=="__main__":
    export_cli()
