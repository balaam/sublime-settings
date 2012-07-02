import sublime
import sublime_plugin
import urllib
import httplib
import sys

print('plugin loaded')


class Reload(sublime_plugin.TextCommand):
	def run(self, edit):
		try:
			msg = "reload"
			host = "127.0.0.1:8080"
			http = httplib.HTTPConnection(host)
			# additional path goes below like /reload/
			http.putrequest("POST", "/")
			http.putheader("content-length", str(len(msg)))
			http.endheaders()

			http.send(msg)
			response = http.getresponse()
			print self.view.file_name(), "Reload command sent."
		except:
			print self.view.file_name(), "Reload failed. %s" % sys.exc_info()[0]
