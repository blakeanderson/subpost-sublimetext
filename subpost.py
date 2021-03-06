import urllib2, urllib, base64, json, yaml, re
import sublime, sublime_plugin, os, tempfile

class SubpostManager():
    def __init__(self):
        self.settings = {}
        settings = sublime.load_settings(__name__ + '.sublime-settings')
        self.settings['userId'] = settings.get('userId')
        self.settings['apiToken'] = settings.get('apiToken')
        self.settings['hostname'] = settings.get('hostname')

    def load_front_matter(self, content):
        sub_content = re.search( r'(\s*---\s*.*\s*---)', content, re.MULTILINE|re.DOTALL)
        print sub_content
        front_matters = yaml.load_all(sub_content.group())
        front_matter = list(front_matters)
        front_matter = front_matter[0]
        request_data = {}
        if front_matter.has_key('title'):
            request_data['title'] = front_matter['title']
        if front_matter.has_key('tags'):
            request_data['tags'] = front_matter['tags']
        if front_matter.has_key('subtitle'):
            request_data['subtitle'] = front_matter['subtitle']
        if front_matter.has_key('name'):
            request_data['name'] = front_matter['name']
        if front_matter.has_key('page'):
            request_data['page'] = front_matter['page']
        if front_matter.has_key('type'):
            request_data['type'] = front_matter['type']
        else:
            request_data['type'] = 'text'
        print request_data
        return request_data

    def post_to_subpost(self, content, draft):
        request_data = self.load_front_matter(content)
        sub_content = re.sub( re.compile(r'(\s*---\s*.*\s*---)',  re.MULTILINE|re.DOTALL), "", content)
        if request_data['type'] == 'text':
            request_data['body'] = sub_content
        elif request_data['type'] == 'link':
            request_data['description'] = sub_content
        if draft:
            request_data['state'] = "draft"
        encoded_data = urllib.urlencode(request_data)
        request = urllib2.Request('http://subpost.herokuapp.com/v1/' + self.settings["hostname"] + '/post')
        base64string = base64.encodestring('%s:%s' % (self.settings['userId'], self.settings['apiToken'])).replace('\n', '')
        request.add_header("Authorization", "Basic %s" % base64string)
        print request
        print base64string
        res = urllib2.urlopen(request, encoded_data).read()
        print res

class SubpostPostCommand(sublime_plugin.TextCommand):
    def run(self, edit, target='subpost'):
        print target
        region = sublime.Region(0, self.view.size())
        encoding = self.view.encoding()
        if encoding == 'Undefined':
            encoding = 'UTF-8'
        elif encoding == 'Western (Windows 1252)':
            encoding = 'windows-1252'
        view_contents = self.view.substr(region)
        subpost = SubpostManager()
        if target == 'subpost':
            subpost.post_to_subpost(view_contents, False)
        elif target == 'subpost_draft':
            subpost.post_to_subpost(view_contents, True)
