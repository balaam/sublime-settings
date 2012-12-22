import sublime
import sublime_plugin
import urllib
import httplib
import sys

print('plugin loaded')

class Execute(sublime_plugin.TextCommand):
    def run(self, edit):
        print('execute test')
        try:
            if self.view.is_dirty():
                self.view.run_command("save")

            sels = self.view.sel()
            selected_text = self.view.substr(sels[0])

            if not selected_text:
                # print "Returning because no text"
                return

            msg = "gText=\"Hello\""
            host = "127.0.0.1:8080"
            http = httplib.HTTPConnection(host)

            http.putrequest("POST", "/execute/")
            http.putheader("content-length", str(len(selected_text)))

            http.endheaders()
            http.send(selected_text)
            response = http.getresponse()
            print self.view.file_name(), "Reload command sent."
        except httplib.BadStatusLine as e:
            print 'Bad status line error'
            print e, e.line
        except:
            print self.view.file_name(), "Reload failed. %s" % sys.exc_info()[0]

