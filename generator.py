from jinja2 import Environment, FileSystemLoader
from livereload import Server
import json
import markdown
import os


def read_config(file_name):
    with open(file_name, 'r', encoding="utf8") as json_file:
        return json.load(json_file)


def load_template(file_path, file_name):
    env = Environment(loader=FileSystemLoader(file_path))
    return env.get_template(file_name)


def create_folders_for_pages(config_data):
    for article_data in config_data.get('articles'):
        folder = os.path.dirname(article_data['source'])
        path = os.path.join('./site/', folder)
        if not os.path.exists(path):
            os.makedirs(path, mode=0o777)


def convert_markdown_to_html(file_path):
    with open(file_path, 'r', encoding="utf-8") as article:
        markdown_markup = article.read()
        return markdown.markdown(markdown_markup)


def make_index_html(config_data):
    template = load_template(
        './template/',
        'index_template.html'
    )
    with open('site/index.html', "w", encoding="utf8") as file:
        file.write(template.render(config_data))


def make_article_page(markup, file_path_to_html, title):
    template = load_template(
        './template/',
        'markdown_template.html'
    )
    with open(file_path_to_html, "w", encoding="utf8") as file:
        file.write(template.render({
            'article': markup,
            'article_title': title
        }))


def make_site(config_data):
    create_folders_for_pages(config_data)
    make_index_html(config_data)
    for article in config_data['articles']:
        markdown_path = os.path.join(
            './articles/',
            article['source']
        )
        filepath_without_extension = os.path.splitext(
            article['source']
        )[0].replace(' ', '_').replace('&', '').replace(';', '')
        html_path = os.path.join(
            './site/',
            filepath_without_extension + '.html'
        )
        markdown_markup = convert_markdown_to_html(markdown_path)
        make_article_page(
            markdown_markup,
            html_path,
            article['title']
        )


if __name__ == '__main__':
    config_file_name = 'config.json'
    config = read_config(config_file_name)
    make_site(config)
    server = Server()
    server.watch('articles/../*.md', make_site(config))
    server.serve(root='site/')
