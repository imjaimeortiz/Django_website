# Django_website
This is my personal website developed with Django, after done some previous projects following tutorials

Important when deploying to Apache:
    - https://www.youtube.com/watch?v=91CVGywuEEY&t=265s
    - apache.conf
    - directives from website --> The directive is set to website.settings, so the 2 options for not getting 500 internal error are moving everything into a website new folder inside website OR in the directive WSGIPythonPath non-writing website, just until website-project.